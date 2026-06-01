#!/usr/bin/env bash
# Antigravity installer
# Installs skills, workflows, and rules into the active AI agent configuration directory.
# Usage: ./install.sh --target [gemini|claude|cursor]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET=""

for arg in "$@"; do
  case $arg in
    --target=*)
      TARGET="${arg#*=}"
      ;;
    gemini|claude|cursor)
      TARGET="$arg"
      ;;
    --help|-h)
      echo "Usage: ./install.sh --target [gemini|claude|cursor]"
      echo ""
      echo "Targets:"
      echo "  gemini   Installs into ~/.gemini/antigravity/"
      echo "  claude   Installs AGENT.md as CLAUDE.md in project root + .claude/antigravity/"
      echo "  cursor   Installs into .cursor/rules/ in project root"
      exit 0
      ;;
  esac
done

if [[ -z "$TARGET" ]]; then
  echo "Error: --target is required."
  echo "Run ./install.sh --help for usage."
  exit 1
fi

case "$TARGET" in
  gemini)
    CONFIG_DIR="$HOME/.gemini/antigravity"
    INSTRUCTIONS_DEST="$HOME/.gemini/gemini-instructions.md"
    ;;
  claude)
    CONFIG_DIR="$(pwd)/.claude/antigravity"
    INSTRUCTIONS_DEST="$(pwd)/CLAUDE.md"
    ;;
  cursor)
    CONFIG_DIR="$(pwd)/.cursor/rules"
    INSTRUCTIONS_DEST="$CONFIG_DIR/AGENT.md"
    ;;
  *)
    echo "Error: unknown target target. Valid targets: gemini, claude, cursor."
    exit 1
    ;;
esac

SKILLS_DIR="$CONFIG_DIR/skills"
WORKFLOWS_DIR="$CONFIG_DIR/workflows"
RULES_DIR="$CONFIG_DIR/rules"

echo "Target:     $TARGET"
echo "Config dir: $CONFIG_DIR"
echo ""

echo "[1/5] Creating directories..."
mkdir -p "$SKILLS_DIR" "$WORKFLOWS_DIR" "$RULES_DIR"

echo "[2/5] Installing agent instructions..."
if [[ -f "$INSTRUCTIONS_DEST" ]]; then
  BACKUP="${INSTRUCTIONS_DEST}.backup.$(date +%Y%m%d_%H%M%S)"
  cp "$INSTRUCTIONS_DEST" "$BACKUP"
  echo "  Backed up existing file to $BACKUP"
fi
cp "$SCRIPT_DIR/template/agent-instructions.md" "$INSTRUCTIONS_DEST"

echo "[3/5] Installing rules..."
cp -r "$SCRIPT_DIR/rules/"* "$RULES_DIR/"

echo "[4/5] Installing workflows..."
cp "$SCRIPT_DIR/workflows/"*.md "$WORKFLOWS_DIR/"

echo "[5/5] Installing skills..."
SKILL_COUNT=0

for category_dir in "$SCRIPT_DIR/skills"/*/; do
  [[ -d "$category_dir" ]] || continue
  category_name="$(basename "$category_dir")"
  for skill_dir in "$category_dir"*/; do
    [[ -d "$skill_dir" ]] || continue
    skill_name="$(basename "$skill_dir")"
    dest="$SKILLS_DIR/$category_name/$skill_name"
    mkdir -p "$(dirname "$dest")"
    ln -sfn "$skill_dir" "$dest"
    SKILL_COUNT=$((SKILL_COUNT + 1))
  done
done

echo "  $SKILL_COUNT skills linked"
echo ""

ERRORS=0
[[ -f "$INSTRUCTIONS_DEST" ]] || { echo "ERROR: agent instructions not found at $INSTRUCTIONS_DEST"; ERRORS=$((ERRORS+1)); }
[[ -d "$RULES_DIR" ]]         || { echo "ERROR: rules directory missing"; ERRORS=$((ERRORS+1)); }
[[ -d "$WORKFLOWS_DIR" ]]     || { echo "ERROR: workflows directory missing"; ERRORS=$((ERRORS+1)); }
[[ -d "$SKILLS_DIR" ]]        || { echo "ERROR: skills directory missing"; ERRORS=$((ERRORS+1)); }

if [[ $ERRORS -eq 0 ]]; then
  echo "Installation complete."
  echo "  Instructions -> $INSTRUCTIONS_DEST"
  echo "  Rules        -> $RULES_DIR"
  echo "  Workflows    -> $WORKFLOWS_DIR"
  echo "  Skills ($SKILL_COUNT)  -> $SKILLS_DIR"
  echo "Restart your agent to apply the configuration."
else
  echo "Installation failed with $ERRORS error(s)."
  exit 1
fi
