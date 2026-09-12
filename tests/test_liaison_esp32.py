"""Regression checks against the actual PCHA YAML (no live HA or pump)."""
from pathlib import Path
import unittest
import yaml
from jinja2 import Environment

ROOT = Path(__file__).resolve().parents[1]
DIAG = 'binary_sensor.pcha_diagnostic_mes_005_liaison_esp32_indisponible'
LINK = 'binary_sensor.pcha_liaison_esp32'
SOURCE = 'binary_sensor.jardin_esp32_jardin_statut_connexion'
START = 'input_boolean.pcha_fenetre_stabilisation_demarrage'
class Loader(yaml.SafeLoader):
    pass
Loader.add_multi_constructor('!', lambda loader, tag, node: loader.construct_scalar(node))
def read(path):
    return yaml.load((ROOT / path).read_text(), Loader=Loader)
def render(template, states=None):
    values = states or {}
    env = Environment()
    env.globals.update(states=lambda e: values.get(e, 'unknown'),
                       is_state=lambda e, v: values.get(e, 'unknown') == v)
    return env.from_string(template).render().strip()

class LiaisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.package = read('diagnostics/diagnostics.yaml')
        cls.diag = next(x for group in cls.package['template']
                        for x in group.get('binary_sensor', [])
                        if x.get('default_entity_id') == DIAG)
        cls.link = next(x for group in read('templates/capteurs.yaml')
                        for x in group.get('binary_sensor', [])
                        if x.get('default_entity_id') == LINK)

    def test_only_connected_status_means_online(self):
        for source in ('on', 'off', 'unknown', 'unavailable', ''):
            with self.subTest(source=source):
                result = render(self.link['state'], {SOURCE: source})
                self.assertEqual(result, str(source == 'on'))
                state = 'on' if result == 'True' else 'off'
                self.assertEqual(render(self.diag['state'], {LINK: state, START:'off'}),
                                 str(source != 'on'))

    def test_startup_suppresses_new_fault_and_delays_are_symmetric(self):
        self.assertEqual(render(self.diag['state'], {LINK:'off', START:'on'}).lower(), 'false')
        self.assertEqual(self.diag['delay_on'], '00:01:00')
        self.assertEqual(render(self.diag['delay_off']), '00:01:00')
        self.assertEqual(self.diag['attributes']['rearmement'], 'TEMPORISE')

    def test_global_level_events_and_independent_faults(self):
        auto = next(a for a in self.package['automation'] if a['id']=='pcha_diagnostics_recalculer_niveau_global')
        expression = next(a['variables']['niveau_calcule'] for a in auto['actions'] if 'variables' in a)
        self.assertEqual(render(expression, {DIAG:'on'}), 'CRITIQUE')
        self.assertEqual(render(expression, {DIAG:'off'}), 'NORMAL')
        self.assertEqual(render(expression, {DIAG:'off', 'binary_sensor.pcha_diagnostic_pro_001_debit_critique':'on'}), 'CRITIQUE')
        self.assertTrue(any(DIAG in t.get('entity_id', []) for t in auto['triggers']))
        events = [a for a in self.package['automation'] if any('event' in action for action in a['actions'])]
        self.assertTrue(any(sum(DIAG in t.get('entity_id', []) for t in a['triggers']) == 2 for a in events))

    def test_vidange_remains_blocked_for_lost_controller(self):
        variables = read('scripts/machine.yaml')['pcha_machine_reevaluer']['sequence'][0]['variables']
        values = {'input_select.pcha_mode_de_fonctionnement':'VIDANGE',
                  'input_select.pcha_niveau_fonctionnement':'CRITIQUE'}
        self.assertEqual(render(variables['critique_bloquant'], {**values, DIAG:'on'}), 'True')
        self.assertEqual(render(variables['critique_bloquant'], values), 'False')

    def test_dashboard_has_card_grids_and_all_history_lanes(self):
        dash = read('dashboard/piscine.yaml')
        view = next(v for v in dash['views'] if v.get('path')=='diagnostics')
        for layout in [view['layout'], *view['layout']['mediaquery'].values()]:
            rows = [row.strip().strip('"').split() for row in layout['grid-template-areas'].strip().splitlines()]
            self.assertEqual(len({len(row) for row in rows}), 1)
            self.assertTrue(any('mes-005' in row for row in rows))
        self.assertTrue(any(c.get('entity')==DIAG for c in view['cards']))
        histories = []
        def visit(node):
            if isinstance(node, dict):
                for key in ('entities', 'series'):
                    if key in node and any(isinstance(e,dict) and e.get('name')=='MES-004' for e in node[key]):
                        histories.append(node[key])
                for value in node.values(): visit(value)
            elif isinstance(node,list):
                for value in node: visit(value)
        visit(dash)
        self.assertGreaterEqual(len(histories), 9)
        for series in histories:
            self.assertEqual(sum(e.get('entity')==DIAG for e in series if isinstance(e,dict)), 1)

    def test_all_yaml_parses(self):
        for path in ROOT.rglob('*.yaml'):
            with self.subTest(path=path):
                yaml.load(path.read_text(), Loader=Loader)

if __name__ == '__main__':
    unittest.main()
