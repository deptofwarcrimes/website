#!/usr/bin/env bash
# Update one published data page in an isolated clone, then commit and push it.
# Intended for cron. The checked-out website directory may contain human work,
# so this script never operates in it directly.
set -euo pipefail

readonly REPOSITORY="https://github.com/deptofwarcrimes/website.git"
readonly BRANCH="main"
readonly CODEX_BIN="/home/shartlieba/.bun/bin/codex"
readonly STATE_DIR="/home/shartlieba/.local/state/deptofwar-updater"

usage() {
  echo "Usage: $0 {prices|oil}" >&2
  exit 64
}

[[ $# -eq 1 ]] || usage
page="$1"

case "$page" in
  prices)
    target="docs/prices.html"
    prompt="Update docs/prices.html only. Fetch the latest published U.S. Bureau of Labor Statistics Average Price observations from the four existing FRED series already cited in the page: APU000074714, APU0000702111, APU0000708111, and APU0000703112. Preserve the page's existing HTML, visual design, JavaScript schema, historical observations, missing-data handling, and visible source attribution. Add newly published monthly observations only when all applicable values are available; do not synthesize values. Update the page's title, verification metadata, comments, and footer only when supported by the sources. Do not edit any other file. Validate the JavaScript dataset and HTML after editing."
    ;;
  oil)
    target="docs/oil.html"
    prompt="Update docs/oil.html only. Use current primary or clearly attributable published sources. Preserve the page's strict distinction between published period-level Hormuz oil-flow estimates, IMF PortWatch AIS observations, and Lloyd's List verified vessel counts; never infer oil volume from vessel passages and never treat incompatible series as a continuation. Add only complete, source-supported observations or estimates. Preserve the existing HTML, visual design, JavaScript schema, existing history, explicit blanks for unavailable data, and source attribution. Update verification dates, source links, summaries, and metadata only when supported by a source. Do not edit any other file. Validate the JavaScript data blocks and HTML after editing."
    ;;
  *) usage ;;
esac

mkdir -p "$STATE_DIR"
mkdir -p "$STATE_DIR/logs"
exec 9>"$STATE_DIR/${page}.lock"
flock -n 9 || exit 0

timestamp="$(date '+%Y%m%d-%H%M%S')"
log="$STATE_DIR/logs/${page}-${timestamp}.log"
workdir="$(mktemp -d /tmp/deptofwar-${page}-XXXXXX)"
cleanup() { rm -rf "$workdir"; }
trap cleanup EXIT

{
  echo "Run started: $(date '+%F %T %Z')"
  echo "Page: $target"
  git clone --depth 1 --branch "$BRANCH" "$REPOSITORY" "$workdir/repository"
  cd "$workdir/repository"
  "$CODEX_BIN" exec -C "$PWD" -s danger-full-access -a never "$prompt"

  if git diff --quiet; then
    echo "No source-supported update; nothing pushed."
    exit 0
  fi

  changed_files="$(git diff --name-only)"
  if [[ "$changed_files" != "$target" ]]; then
    echo "Refusing to push unexpected changed files:" >&2
    printf '%s\n' "$changed_files" >&2
    exit 1
  fi

  git diff --check
  test -s "$target"
  rg -q '<!DOCTYPE html>' "$target"
  rg -q '</html>' "$target"
  git config user.name "Dept of War Crimes Updates"
  git config user.email "updates@deptofwarcrimes.com"
  git add -- "$target"
  git commit -m "chore: update ${page} data"
  # Other site automations publish to main, so replay this page-only commit on
  # the current remote tip before pushing. A true content conflict is left
  # unpushed for the next reviewed run rather than being resolved blindly.
  git pull --rebase origin "$BRANCH"
  git push origin "HEAD:$BRANCH"
  echo "Run finished: $(date '+%F %T %Z')"
} >>"$log" 2>&1
