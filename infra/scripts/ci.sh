#!/usr/bin/env bash
set -euo pipefail
ROOT="${CI_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"
cd "$ROOT"
"$ROOT/infra/scripts/ci/validate-repo.sh" --root "$ROOT"
"$ROOT/infra/scripts/ci/check-size.sh" --root "$ROOT"
python3 scripts/validate.py --root .
if command -v composer >/dev/null 2>&1 && command -v php >/dev/null 2>&1; then
  composer install --no-interaction --prefer-dist
  vendor/bin/phpunit
else
  echo "php toolchain unavailable; bootstrap validation only"
fi
for f in infra/scripts/*.sh; do bash -n "$f"; done
echo "php checks ok"
