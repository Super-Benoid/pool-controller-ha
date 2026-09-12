#!/usr/bin/env bash
# À exécuter depuis Studio Code Server ; aucune dépendance Python.
set -euo pipefail
repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
config_dir="${1:-$(dirname -- "$repo_dir")}"
source_file="$repo_dir/integrations/awtrix_salon.yaml"
target_file="$config_dir/awtrix_salon.yaml"

if [[ ! -f "$config_dir/configuration.yaml" ]]; then
  echo "configuration.yaml absent de $config_dir. Indiquez le dossier HA en argument." >&2
  exit 1
fi
if ! grep -Eq '^[[:space:]]*automation[[:space:]]+awtrix_salon:[[:space:]]*!include[[:space:]]+awtrix_salon.yaml[[:space:]]*(#.*)?$' "$config_dir/configuration.yaml"; then
  echo "Inclusion AWTRIX attendue non trouvée. Aucun fichier modifié ; transmettre la ligne d'inclusion actuelle." >&2
  exit 1
fi
if [[ -L "$target_file" && "$(readlink -f -- "$target_file")" == "$source_file" ]]; then
  echo "AWTRIX est déjà relié au dépôt GitHub."
  exit 0
fi
if [[ ! -f "$target_file" || -L "$target_file" ]]; then
  echo "Fichier AWTRIX existant absent ou lien différent. Aucun fichier modifié." >&2
  exit 1
fi

# Accepter uniquement les deux configurations retrouvées dans le projet.
# Une version personnelle différente doit être intégrée dans GitHub d'abord.
current_hash="$(sha256sum -- "$target_file")"
current_hash="${current_hash%% *}"
case "$current_hash" in
  30f7125f625fe0ca18e5e26b7712384caf8b79f20f1698fe077eacb46d18d377|a4e5da08c656cc734ec0b4b4c09a4e00b95653e90ad262fb899ea08707beaa7a) ;;
  *)
    echo "La configuration AWTRIX diffère des versions connues. Aucun fichier modifié." >&2
    echo "Transmettre awtrix_salon.yaml pour préserver ses dernières personnalisations." >&2
    exit 1
    ;;
esac
backup_file="$target_file.avant-hivernage.$(date +%Y%m%d-%H%M%S).bak"
cp -p -- "$target_file" "$backup_file"
ln -sfn -- "$source_file" "$target_file"
echo "AWTRIX relié au dépôt. Sauvegarde : $backup_file"
echo "Vérifier avec ha core check, puis redémarrer Home Assistant."
