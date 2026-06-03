#!/bin/bash
# Grimoire hourly heartbeat — runs the full pipeline cycle via Claude Code CLI.
# Designed for unattended execution on an always-on machine (cron).

set -euo pipefail

SKILLS_LAB="/home/xhasan/my-projects/skills-lab"
LOG_DIR="$SKILLS_LAB/logs"
LOG_FILE="$LOG_DIR/heartbeat-$(date +%Y%m%d).log"
CLAUDE="/home/xhasan/.local/bin/claude"
LOCK_FILE="/tmp/grimoire-heartbeat.lock"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"; }

# Prevent overlapping cycles
if [ -f "$LOCK_FILE" ]; then
    log "SKIP — previous cycle still running (lock: $LOCK_FILE)"
    exit 0
fi
touch "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT

mkdir -p "$LOG_DIR"

# Rotate logs older than 30 days
find "$LOG_DIR" -name "heartbeat-*.log" -mtime +30 -delete 2>/dev/null || true

log "=== Grimoire heartbeat cycle starting ==="

# Load env (token for gh CLI)
source "$SKILLS_LAB/.env"
export GITHUB_TOKEN

cd "$SKILLS_LAB"

PROMPT="Run the Grimoire heartbeat cycle as defined in CLAUDE.md.

Steps:
1. Read pipeline/state.json to identify current phase and resume from there
2. Spawn the researcher subagent for Phase 2 (feedback check on Xeebs/grimoire GitHub)
3. Spawn the researcher subagent for Phase 3 (web research — 3-5 new signals to pipeline/queue.md)
4. Spawn the skill-designer subagent for Phase 4 (design skill from top unworked High signal)
5. Spawn the quality-auditor subagent for Phase 5 (test the skill against both scenarios)
6. If tests pass, spawn the publisher subagent for Phase 6 (commit, push, announce, notify)
7. Write final state to pipeline/state.json

Complete at most 1 full skill this cycle. Halt gracefully if rate-limited and write current state."

"$CLAUDE" \
    --dangerously-skip-permissions \
    -p "$PROMPT" \
    2>&1 | tee -a "$LOG_FILE"

log "=== Grimoire heartbeat cycle complete ==="
