"""Hivernage regression tests against the repository YAML, without actuating HA."""
from pathlib import Path
import unittest
import yaml
from jinja2 import Environment
from test_liaison_esp32 import read

ROOT = Path(__file__).resolve().parents[1]
MODE = 'input_select.pcha_mode_de_fonctionnement'
WIN = {MODE: 'HIVERNAGE'}
def render(text, values=None, **extra):
    values = values or {}
    env = Environment()
    env.globals.update(states=lambda e: values.get(e, 'unavailable'),
                       is_state=lambda e, s: values.get(e, 'unavailable') == s)
    env.globals.update(extra)
    return env.from_string(str(text)).render().strip()
def bs(path):
    data=read(path)
    if isinstance(data,dict):data=data['template']
    return [s for group in data for s in group.get('binary_sensor',[])]
def by_id(path, uid, kind='sensor'):
    data=read(path)
    return next(s for group in data for s in group.get(kind,[]) if s.get('unique_id')==uid)

class WinterTests(unittest.TestCase):
    def test_persistent_mode_and_state(self):
        data=read('helpers/input_select.yaml')
        self.assertIn('HIVERNAGE',data['pcha_mode_de_fonctionnement']['options'])
        self.assertNotIn('initial',data['pcha_mode_de_fonctionnement'])
        self.assertIn('HIVERNAGE',data['pcha_etat_machine']['options'])

    def test_all_faults_suspend_without_hardware_or_unlock(self):
        diagnostics=bs('diagnostics/diagnostics.yaml')
        self.assertEqual(len(diagnostics),11)
        for sensor in diagnostics:
            with self.subTest(sensor=sensor['unique_id']):
                self.assertEqual(render(sensor['state'],WIN).lower(),'false')
                if 'delay_off' in sensor:
                    self.assertEqual(render(sensor['delay_off'],WIN),'0')
        # Underlying manual latch is neither cleared nor rearmed by winter.
        action_text=(ROOT/'automations/hivernage.yaml').read_text()
        self.assertNotIn('entity_id: input_boolean.pcha_verrou_pro_001',action_text)
        level=next(a for a in read('diagnostics/diagnostics.yaml')['automation']
                   if a['id']=='pcha_diagnostics_recalculer_niveau_global')
        expression=next(a['variables']['niveau_calcule'] for a in level['actions'] if 'variables' in a)
        self.assertEqual(render(expression,WIN),'NORMAL')

    def test_demands_and_objective_do_not_require_sensors(self):
        for path, ids in {
            'templates/systeme.yaml':['pcha_demande_fonctionnement'],
            'templates/calculs.yaml':['pcha_filtration_requise'],
            'templates/planification_v3.yaml':['pcha_filtration_requise_v3'],
            'templates/chauffage.yaml':['pcha_chauffage_solaire_requis','pcha_chauffage_solaire_actif','pcha_protection_serpentin_requise'],
        }.items():
            for uid in ids:
                s=by_id(path,uid,'binary_sensor')
                self.assertEqual(render(s['state'],WIN).lower(),'false',uid)
        for uid in ('pcha_objectif_filtration_quotidien','pcha_temps_filtration_restant','pcha_progression_objectif_quotidien'):
            self.assertEqual(render(by_id('templates/calculs.yaml',uid)['state'],WIN),'0')
        obj=by_id('templates/calculs.yaml','pcha_objectif_filtration_quotidien')
        for attr in ('somme_temperature_jour','echantillons_temperature_jour'):
            self.assertEqual(render(obj['attributes'][attr],WIN),'0')
        self.assertEqual(render(obj['attributes']['temperature_reference'],WIN),'None')

    def test_direct_start_and_transition_out_are_blocked(self):
        guard=read('scripts/pompe.yaml')['pcha_pompe_demarrer']['sequence'][0]['value_template']
        physical_guard=read('templates/actionneurs.yaml')[0]['switch'][0]['turn_on'][0]['value_template']
        for g in (guard,physical_guard):
            self.assertEqual(render(g,WIN),'False')
            self.assertEqual(render(g,{MODE:'AUTO','input_select.pcha_etat_machine':'HIVERNAGE'}),'False')
            self.assertEqual(render(g,{MODE:'AUTO','input_select.pcha_etat_machine':'ATTENTE'}),'True')
            self.assertEqual(render(g,{}),'False')

    def test_unavailable_hardware_does_not_block_winter_machine(self):
        for a in read('automations/machine.yaml'):
            if a.get('conditions'):
                self.assertEqual(render(a['conditions'][0]['value_template'],WIN).lower(),'true')
            for action in a['actions']:
                if 'wait_template' in action:
                    self.assertEqual(render(action['wait_template'],WIN).lower(),'true')
        winter=read('scripts/machine.yaml')['pcha_machine_hivernage']['sequence']
        self.assertTrue(winter[0]['continue_on_error'])
        self.assertEqual(winter[-1]['data']['option'],'HIVERNAGE')

    def test_late_vidange_timer_cannot_change_mode(self):
        a=next(a for a in read('automations/vidange.yaml') if a['id']=='pcha_vidange_terminer')
        self.assertEqual(a['conditions'][0]['state'],'VIDANGE')
        a=next(a for a in read('automations/vidange.yaml') if a['id']=='pcha_vidange_annuler')
        check=next(x['if'][0]['value_template'] for x in a['actions'] if 'if' in x)
        self.assertEqual(render(check,WIN,trigger={'to_state':{'state':'HIVERNAGE'}}),'False')

    def test_awtrix_deletes_pool_and_dismisses_without_periodic_dismiss(self):
        data=read('integrations/awtrix_salon.yaml')
        main=next(a for a in data if a['id']=='awtrix_salon_affichages_principaux')
        branch=main['actions'][-1]
        self.assertEqual(render(branch['if'][0]['value_template'],WIN),'False')
        deletion=branch['else'][0]['data']
        self.assertEqual(deletion['topic'],'awtrix_salon/custom/piscine')
        self.assertEqual(deletion['payload'],'')
        winter=next(a for a in data if a['id']=='awtrix_salon_hivernage_pcha')
        self.assertNotIn('time_pattern',[t['trigger'] for t in winter['triggers']])
        topics=[x['data']['topic'] for x in winter['actions'] if x.get('action')=='mqtt.publish']
        self.assertEqual(topics,['awtrix_salon/custom/piscine','awtrix_salon/notify/dismiss'])
        alert=next(a for a in data if a['id']=='awtrix_salon_alertes_pcha')
        self.assertEqual(render(alert['actions'][0]['value_template'],WIN),'False')
        generic=next(a for a in data if a['id']=='awtrix_salon_notifications_persistantes')
        condition=generic['actions'][0]['value_template']
        for title,nid,allowed in [('PCHA — DEGRADE','pcha_mes_001',False),('Home Assistant','pcha_pro_001',False),('Météo','meteo',True)]:
            self.assertEqual(render(condition,WIN,trigger={'notification':{'title':title,'notification_id':nid}}),str(allowed))

    def test_awtrix_treatment_cannot_republish_during_winter(self):
        data=read('integrations/awtrix_salon.yaml')
        treatment=next(a for a in data if a['id']=='awtrix_salon_traitement_piscine')
        self.assertEqual(treatment['mode'],'restart')
        self.assertEqual(render(treatment['actions'][0]['value_template'],WIN),'False')
        # Every publication rechecks the live mode, including after a delay.
        for branch in treatment['actions'][-1]['choose']:
            for index,action in enumerate(branch['sequence']):
                if action.get('action')=='mqtt.publish':
                    guard=branch['sequence'][index-1]['value_template']
                    self.assertEqual(render(guard,WIN),'False')
                    self.assertEqual(render(guard,{MODE:'TRAITEMENT'}),'True')

    def test_ui_exposes_suspension_and_winter_history(self):
        s=(ROOT/'dashboard/piscine.yaml').read_text()
        self.assertIn('Objectif de filtration suspendu',s)
        self.assertIn('HIVERNAGE:6',s)
        self.assertIn('HIVERNAGE:4',s)
        self.assertIn('SUSPENDU',s)

if __name__=='__main__':unittest.main()
