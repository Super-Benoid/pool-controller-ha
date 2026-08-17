from pathlib import Path

path = Path("dashboard/piscine.yaml")
text = path.read_text(encoding="utf-8")

replacements = [
    (
        '        "temperature temperature temperature luminosite luminosite luminosite debit debit debit puissance puissance puissance objectif objectif objectif objectif"\n        "reglages-titre',
        '        "temperature temperature temperature luminosite luminosite luminosite debit debit debit puissance puissance puissance objectif objectif objectif objectif"\n        "meteo-j meteo-j meteo-j meteo-j meteo-j meteo-j1 meteo-j1 meteo-j1 meteo-j1 meteo-j1 potentiel potentiel potentiel potentiel potentiel potentiel"\n        "reglages-titre',
    ),
    (
        '            "objectif objectif objectif objectif objectif objectif objectif objectif"\n            "reglages-titre',
        '            "objectif objectif objectif objectif objectif objectif objectif objectif"\n            "meteo-j meteo-j meteo-j meteo-j meteo-j1 meteo-j1 meteo-j1 meteo-j1"\n            "potentiel potentiel potentiel potentiel potentiel potentiel potentiel potentiel"\n            "reglages-titre',
    ),
    (
        '            "objectif"\n            "reglages-titre"',
        '            "objectif"\n            "meteo-j"\n            "meteo-j1"\n            "potentiel"\n            "reglages-titre"',
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Grille dashboard inattendue : {count} occurrence(s)")
    text = text.replace(old, new, 1)

marker = """      ##########################################################################
      # Réglages rapides
      ##########################################################################"""
if text.count(marker) != 1:
    raise SystemExit("Marqueur Réglages rapides introuvable ou ambigu")

cards = r'''      ##########################################################################
      # Météo et potentiel thermique V3
      ##########################################################################
      - type: custom:button-card
        entity: sensor.pcha_meteo_aujourd_hui
        show_icon: false
        show_name: false
        show_state: false
        tap_action:
          action: more-info
        triggers_update:
          - sensor.pcha_meteo_aujourd_hui
        view_layout:
          grid-area: meteo-j
        custom_fields:
          contenu: |
            [[[
              const a = entity?.attributes ?? {};
              const labels = {'clear-night':'Nuit claire',cloudy:'Nuageux',exceptional:'Exceptionnel',fog:'Brouillard',hail:'Grêle',lightning:'Orage','lightning-rainy':'Orage pluvieux',partlycloudy:'Éclaircies',pouring:'Fortes pluies',rainy:'Pluie',snowy:'Neige','snowy-rainy':'Neige / pluie',sunny:'Ensoleillé',windy:'Venteux','windy-variant':'Venteux / nuageux'};
              const icons = {'clear-night':'mdi:weather-night',cloudy:'mdi:weather-cloudy',exceptional:'mdi:alert-circle-outline',fog:'mdi:weather-fog',hail:'mdi:weather-hail',lightning:'mdi:weather-lightning','lightning-rainy':'mdi:weather-lightning-rainy',partlycloudy:'mdi:weather-partly-cloudy',pouring:'mdi:weather-pouring',rainy:'mdi:weather-rainy',snowy:'mdi:weather-snowy','snowy-rainy':'mdi:weather-snowy-rainy',sunny:'mdi:weather-sunny',windy:'mdi:weather-windy','windy-variant':'mdi:weather-windy-variant'};
              const f=(v,d=1)=>{const n=Number(v);return Number.isFinite(n)?n.toLocaleString('fr-FR',{minimumFractionDigits:d,maximumFractionDigits:d}):'—';};
              const condition=labels[entity?.state]??(entity?.state||'Indisponible').replaceAll('_',' ');
              const icon=icons[entity?.state]??'mdi:weather-partly-cloudy';
              return `<div class="pcha-wx"><div class="pcha-wx-head"><ha-icon icon="${icon}"></ha-icon><span>Aujourd’hui</span></div><div class="pcha-wx-main"><strong>${condition}</strong><b>${f(a.temperature_min)}° <span>→</span> ${f(a.temperature_max)}°</b></div><div class="pcha-wx-meta"><span><ha-icon icon="mdi:water-percent"></ha-icon>${f(a.humidity,0)} %</span><span><ha-icon icon="mdi:weather-windy"></ha-icon>${f(a.wind_speed)} km/h</span></div></div>`;
            ]]]
        styles: &meteo_card_styles
          card:
            - background: linear-gradient(145deg, rgba(5,29,45,.98), rgba(15,23,42,.98))
            - border: 1px solid rgba(56,189,248,.30)
            - border-radius: 18px
            - box-shadow: 0 10px 28px rgba(0,0,0,.28), 0 0 22px rgba(56,189,248,.06)
            - padding: 15px 17px
            - min-height: 126px
          grid:
            - grid-template-areas: '"contenu"'
            - grid-template-columns: 1fr
          custom_fields:
            contenu:
              - width: 100%
              - text-align: left
        extra_styles: |
          .pcha-wx { display:grid; gap:10px; width:100%; }
          .pcha-wx-head { display:flex; align-items:center; gap:9px; color:#cbd5e1; font-size:14px; font-weight:700; }
          .pcha-wx-head ha-icon { width:25px; color:#38bdf8; filter:drop-shadow(0 0 7px rgba(56,189,248,.35)); }
          .pcha-wx-main { display:flex; align-items:baseline; justify-content:space-between; gap:12px; }
          .pcha-wx-main strong { color:#f8fafc; font-size:19px; font-weight:800; }
          .pcha-wx-main b { color:#67e8f9; font-size:18px; white-space:nowrap; }
          .pcha-wx-main b span { color:#64748b; font-size:13px; padding:0 3px; }
          .pcha-wx-meta { display:flex; justify-content:space-between; gap:12px; color:#94a3b8; font-size:12px; }
          .pcha-wx-meta span { display:flex; align-items:center; gap:5px; white-space:nowrap; }
          .pcha-wx-meta ha-icon { width:16px; color:#a78bfa; }

      - type: custom:button-card
        entity: sensor.pcha_meteo_demain
        show_icon: false
        show_name: false
        show_state: false
        tap_action:
          action: more-info
        triggers_update:
          - sensor.pcha_meteo_demain
        view_layout:
          grid-area: meteo-j1
        custom_fields:
          contenu: |
            [[[
              const a = entity?.attributes ?? {};
              const labels = {'clear-night':'Nuit claire',cloudy:'Nuageux',exceptional:'Exceptionnel',fog:'Brouillard',hail:'Grêle',lightning:'Orage','lightning-rainy':'Orage pluvieux',partlycloudy:'Éclaircies',pouring:'Fortes pluies',rainy:'Pluie',snowy:'Neige','snowy-rainy':'Neige / pluie',sunny:'Ensoleillé',windy:'Venteux','windy-variant':'Venteux / nuageux'};
              const icons = {'clear-night':'mdi:weather-night',cloudy:'mdi:weather-cloudy',exceptional:'mdi:alert-circle-outline',fog:'mdi:weather-fog',hail:'mdi:weather-hail',lightning:'mdi:weather-lightning','lightning-rainy':'mdi:weather-lightning-rainy',partlycloudy:'mdi:weather-partly-cloudy',pouring:'mdi:weather-pouring',rainy:'mdi:weather-rainy',snowy:'mdi:weather-snowy','snowy-rainy':'mdi:weather-snowy-rainy',sunny:'mdi:weather-sunny',windy:'mdi:weather-windy','windy-variant':'mdi:weather-windy-variant'};
              const f=(v,d=1)=>{const n=Number(v);return Number.isFinite(n)?n.toLocaleString('fr-FR',{minimumFractionDigits:d,maximumFractionDigits:d}):'—';};
              const condition=labels[entity?.state]??(entity?.state||'Indisponible').replaceAll('_',' ');
              const icon=icons[entity?.state]??'mdi:weather-partly-cloudy';
              return `<div class="pcha-wx"><div class="pcha-wx-head"><ha-icon icon="${icon}"></ha-icon><span>Demain</span></div><div class="pcha-wx-main"><strong>${condition}</strong><b>${f(a.temperature_min)}° <span>→</span> ${f(a.temperature_max)}°</b></div><div class="pcha-wx-meta"><span><ha-icon icon="mdi:water-percent"></ha-icon>${f(a.humidity,0)} %</span><span><ha-icon icon="mdi:weather-windy"></ha-icon>${f(a.wind_speed)} km/h</span></div></div>`;
            ]]]
        styles: *meteo_card_styles
        extra_styles: |
          .pcha-wx { display:grid; gap:10px; width:100%; }
          .pcha-wx-head { display:flex; align-items:center; gap:9px; color:#cbd5e1; font-size:14px; font-weight:700; }
          .pcha-wx-head ha-icon { width:25px; color:#a78bfa; filter:drop-shadow(0 0 7px rgba(167,139,250,.35)); }
          .pcha-wx-main { display:flex; align-items:baseline; justify-content:space-between; gap:12px; }
          .pcha-wx-main strong { color:#f8fafc; font-size:19px; font-weight:800; }
          .pcha-wx-main b { color:#c4b5fd; font-size:18px; white-space:nowrap; }
          .pcha-wx-main b span { color:#64748b; font-size:13px; padding:0 3px; }
          .pcha-wx-meta { display:flex; justify-content:space-between; gap:12px; color:#94a3b8; font-size:12px; }
          .pcha-wx-meta span { display:flex; align-items:center; gap:5px; white-space:nowrap; }
          .pcha-wx-meta ha-icon { width:16px; color:#a78bfa; }

      - type: custom:button-card
        entity: sensor.pcha_score_potentiel_thermique_jour
        show_icon: false
        show_name: false
        show_state: false
        tap_action:
          action: more-info
        triggers_update:
          - sensor.pcha_score_potentiel_thermique_jour
          - sensor.pcha_potentiel_thermique_jour
          - sensor.pcha_heure_cible_objectif
          - sensor.pcha_heure_atteinte_objectif
        view_layout:
          grid-area: potentiel
        custom_fields:
          contenu: |
            [[[
              const score=Math.max(0,Math.min(100,Number(entity?.state)||0));
              const niveau=states['sensor.pcha_potentiel_thermique_jour']?.state??'INDISPONIBLE';
              const cible=states['sensor.pcha_heure_atteinte_objectif']?.state??'—';
              const strategie=(states['sensor.pcha_heure_cible_objectif']?.attributes?.strategie??'—').replaceAll('_',' ');
              const favorables=Number(entity?.attributes?.heures_ensoleillees_ou_partiellement_nuageuses);
              const evaluees=Number(entity?.attributes?.heures_evaluees);
              const moyenne=Number(entity?.attributes?.temperature_moyenne_prevue_fenetre);
              const fmt=(n,d=0)=>Number.isFinite(n)?n.toLocaleString('fr-FR',{minimumFractionDigits:d,maximumFractionDigits:d}):'—';
              return `<div class="pcha-pot"><div class="pcha-pot-head"><span><ha-icon icon="mdi:white-balance-sunny"></ha-icon>Potentiel thermique</span><b>${niveau} · ${Math.round(score)}%</b></div><div class="pcha-pot-bar"><i style="width:${score}%"></i></div><div class="pcha-pot-grid"><span>Heures favorables<strong>${fmt(favorables)} / ${fmt(evaluees)} h</strong></span><span>T° moyenne prévue<strong>${fmt(moyenne,1)} °C</strong></span><span>Cible filtration<strong>${cible}</strong></span></div><div class="pcha-pot-strat">${strategie}</div></div>`;
            ]]]
        styles:
          card:
            - background: linear-gradient(145deg, rgba(31,24,50,.98), rgba(8,28,46,.98))
            - border: 1px solid rgba(167,139,250,.34)
            - border-radius: 18px
            - box-shadow: 0 10px 28px rgba(0,0,0,.28), 0 0 24px rgba(167,139,250,.07)
            - padding: 15px 17px
            - min-height: 126px
          grid:
            - grid-template-areas: '"contenu"'
            - grid-template-columns: 1fr
          custom_fields:
            contenu:
              - width: 100%
              - text-align: left
        extra_styles: |
          .pcha-pot { display:grid; gap:9px; width:100%; }
          .pcha-pot-head { display:flex; justify-content:space-between; align-items:center; gap:10px; }
          .pcha-pot-head span { display:flex; align-items:center; gap:8px; color:#cbd5e1; font-size:14px; font-weight:700; }
          .pcha-pot-head ha-icon { width:24px; color:#fbbf24; filter:drop-shadow(0 0 7px rgba(251,191,36,.35)); }
          .pcha-pot-head b { color:#f0abfc; font-size:16px; white-space:nowrap; }
          .pcha-pot-bar { height:7px; overflow:hidden; border-radius:999px; background:rgba(71,85,105,.45); }
          .pcha-pot-bar i { display:block; height:100%; border-radius:999px; background:linear-gradient(90deg,#38bdf8,#8b5cf6 58%,#e879f9); box-shadow:0 0 10px rgba(139,92,246,.30); }
          .pcha-pot-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:8px; }
          .pcha-pot-grid span { color:#94a3b8; font-size:10px; }
          .pcha-pot-grid strong { display:block; color:#e2e8f0; font-size:13px; margin-top:2px; white-space:nowrap; }
          .pcha-pot-strat { color:#67e8f9; font-size:10px; font-weight:750; text-transform:uppercase; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }

'''

text = text.replace(marker, cards + marker, 1)
path.write_text(text, encoding="utf-8")
print("Dashboard météo V3 patché")
