from pathlib import Path

path = Path("dashboard/piscine.yaml")
text = path.read_text(encoding="utf-8")

replacements = [
    (
        "                    <div><span>À atteindre à</span><strong>${targetTime()}</strong></div>",
        "                    <div><span>Fin estimée</span><strong>${targetTime()}</strong></div>",
    ),
    (
        "              const cible=states['sensor.pcha_heure_atteinte_objectif']?.state??'—';",
        "              const cibleState=states['sensor.pcha_heure_cible_objectif']?.state;\n              const cibleDate=cibleState && !['unknown','unavailable','none',''].includes(cibleState) ? new Date(cibleState) : null;\n              const cible=cibleDate && !Number.isNaN(cibleDate.getTime()) ? cibleDate.toLocaleTimeString('fr-FR',{hour:'2-digit',minute:'2-digit'}).replace(':','H') : '—';",
    ),
    (
        "<span>Cible filtration<strong>${cible}</strong></span>",
        "<span>Cible V3<strong>${cible}</strong></span>",
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Dashboard inattendu pour remplacement {old!r}: {count} occurrence(s)")
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
print("dashboard/piscine.yaml mis à jour")
