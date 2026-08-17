#!/usr/bin/env python3
"""Ajoute la vue Paramètres V3 au dashboard PCHA via !include.

Migration stricte et idempotente : le fichier principal n'est modifié que si
la structure attendue est reconnue. La vue elle-même reste dans un fichier
séparé pour simplifier les évolutions futures.
"""

from pathlib import Path

DASHBOARD = Path("dashboard/piscine.yaml")
VIEW = Path("dashboard/views/parametres.yaml")
INCLUDE = "  - !include views/parametres.yaml"


def main() -> None:
    if not DASHBOARD.exists():
        raise SystemExit(f"ERREUR — fichier absent : {DASHBOARD}")
    if not VIEW.exists():
        raise SystemExit(f"ERREUR — vue absente : {VIEW}")

    text = DASHBOARD.read_text(encoding="utf-8")

    if INCLUDE in text:
        print("Dashboard Paramètres V3 déjà intégré — aucune modification.")
        return

    checks = {
        "clé views": "\nviews:\n",
        "vue accueil": "  - title: Validation Concept D\n",
        "vue pilotage": "  - title: Pilotage\n",
        "vue solaire": "  - title: Solaire\n",
    }
    for label, marker in checks.items():
        count = text.count(marker)
        if count != 1:
            raise SystemExit(
                f"ERREUR — structure inattendue ({label}: {count} occurrence(s), 1 attendue). "
                "Aucun fichier écrit."
            )

    # piscine.yaml ne contient qu'un titre racine puis la liste `views:`.
    # Ajouter un élément indenté de deux espaces en fin de fichier crée donc
    # une nouvelle vue sans réécrire ni déplacer les vues existantes.
    updated = text.rstrip() + "\n\n" + INCLUDE + "\n"
    DASHBOARD.write_text(updated, encoding="utf-8")
    print("OK — vue Paramètres V3 ajoutée au dashboard via !include.")


if __name__ == "__main__":
    main()
