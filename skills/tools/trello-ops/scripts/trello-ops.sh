#!/usr/bin/env bash
# trello-ops.sh — Trello REST API helper for Antigravity
# Usage: bash trello-ops.sh <command> [args...]
#
# Requires: TRELLO_API_KEY and TRELLO_TOKEN environment variables

set -euo pipefail

BASE_URL="https://api.trello.com/1"
AUTH="key=${TRELLO_API_KEY}&token=${TRELLO_TOKEN}"

# Color output helpers
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

check_auth() {
  if [ -z "${TRELLO_API_KEY:-}" ] || [ -z "${TRELLO_TOKEN:-}" ]; then
    echo -e "${RED}Error: TRELLO_API_KEY and TRELLO_TOKEN must be set.${NC}"
    echo "Get your API key at: https://trello.com/power-ups/admin"
    exit 1
  fi
}

# Wrapper around curl for consistent error handling
trello_request() {
  local method="$1"
  local endpoint="$2"
  shift 2
  local url="${BASE_URL}${endpoint}"

  # Append auth params
  if [[ "$url" == *"?"* ]]; then
    url="${url}&${AUTH}"
  else
    url="${url}?${AUTH}"
  fi

  local response
  response=$(curl -s -w "\n%{http_code}" -X "$method" "$url" "$@")
  local http_code
  http_code=$(echo "$response" | tail -1)
  local body
  body=$(echo "$response" | sed '$d')

  if [[ "$http_code" -ge 400 ]]; then
    echo -e "${RED}Error (HTTP ${http_code}):${NC} ${body}" >&2
    return 1
  fi

  echo "$body"
}

# ─── Commands ────────────────────────────────────────────────────────

cmd_get_boards() {
  echo -e "${GREEN}Fetching your boards...${NC}" >&2
  trello_request GET "/members/me/boards?fields=name,url,closed" | python3 -m json.tool 2>/dev/null || trello_request GET "/members/me/boards?fields=name,url,closed"
}

cmd_get_lists() {
  local board_id="${1:?Usage: get-lists <boardId>}"
  echo -e "${GREEN}Fetching lists for board ${board_id}...${NC}" >&2
  trello_request GET "/boards/${board_id}/lists?fields=name,pos,closed" | python3 -m json.tool 2>/dev/null || trello_request GET "/boards/${board_id}/lists?fields=name,pos,closed"
}

cmd_get_cards() {
  local list_id="${1:?Usage: get-cards <listId>}"
  echo -e "${GREEN}Fetching cards for list ${list_id}...${NC}" >&2
  trello_request GET "/lists/${list_id}/cards?fields=name,desc,labels,due,idMembers,url" | python3 -m json.tool 2>/dev/null || trello_request GET "/lists/${list_id}/cards?fields=name,desc,labels,due,idMembers,url"
}

cmd_get_card() {
  local card_id="${1:?Usage: get-card <cardId>}"
  echo -e "${GREEN}Fetching card ${card_id}...${NC}" >&2
  trello_request GET "/cards/${card_id}?fields=name,desc,labels,due,idMembers,url,idList" | python3 -m json.tool 2>/dev/null || trello_request GET "/cards/${card_id}?fields=name,desc,labels,due,idMembers,url,idList"
}

cmd_create_card() {
  local list_id="${1:?Usage: create-card <listId> <name> [desc]}"
  local name="${2:?Usage: create-card <listId> <name> [desc]}"
  local desc="${3:-}"
  echo -e "${GREEN}Creating card '${name}' in list ${list_id}...${NC}" >&2
  trello_request POST "/cards" \
    -d "idList=${list_id}" \
    -d "name=${name}" \
    -d "desc=${desc}" | python3 -m json.tool 2>/dev/null || echo "Card created."
}

cmd_move_card() {
  local card_id="${1:?Usage: move-card <cardId> <targetListId>}"
  local target_list_id="${2:?Usage: move-card <cardId> <targetListId>}"
  echo -e "${GREEN}Moving card ${card_id} to list ${target_list_id}...${NC}" >&2
  trello_request PUT "/cards/${card_id}" \
    -d "idList=${target_list_id}" | python3 -m json.tool 2>/dev/null || echo "Card moved."
}

cmd_archive_card() {
  local card_id="${1:?Usage: archive-card <cardId>}"
  echo -e "${YELLOW}Archiving card ${card_id}...${NC}" >&2
  trello_request PUT "/cards/${card_id}" \
    -d "closed=true" | python3 -m json.tool 2>/dev/null || echo "Card archived."
}

cmd_add_comment() {
  local card_id="${1:?Usage: add-comment <cardId> <text>}"
  local text="${2:?Usage: add-comment <cardId> <text>}"
  echo -e "${GREEN}Adding comment to card ${card_id}...${NC}" >&2
  trello_request POST "/cards/${card_id}/actions/comments" \
    -d "text=${text}" | python3 -m json.tool 2>/dev/null || echo "Comment added."
}

cmd_add_label() {
  local card_id="${1:?Usage: add-label <cardId> <color>}"
  local color="${2:?Usage: add-label <cardId> <color>}"
  echo -e "${GREEN}Adding ${color} label to card ${card_id}...${NC}" >&2
  trello_request POST "/cards/${card_id}/labels" \
    -d "color=${color}" | python3 -m json.tool 2>/dev/null || echo "Label added."
}

cmd_add_member() {
  local card_id="${1:?Usage: add-member <cardId> <memberId>}"
  local member_id="${2:?Usage: add-member <cardId> <memberId>}"
  echo -e "${GREEN}Adding member ${member_id} to card ${card_id}...${NC}" >&2
  trello_request POST "/cards/${card_id}/idMembers" \
    -d "value=${member_id}" | python3 -m json.tool 2>/dev/null || echo "Member added."
}

cmd_create_list() {
  local board_id="${1:?Usage: create-list <boardId> <name>}"
  local name="${2:?Usage: create-list <boardId> <name>}"
  echo -e "${GREEN}Creating list '${name}' on board ${board_id}...${NC}" >&2
  trello_request POST "/boards/${board_id}/lists" \
    -d "name=${name}" | python3 -m json.tool 2>/dev/null || echo "List created."
}

cmd_create_board() {
  local name="${1:?Usage: create-board <name> [desc]}"
  local desc="${2:-}"
  echo -e "${GREEN}Creating board '${name}'...${NC}" >&2
  trello_request POST "/boards" \
    -d "name=${name}" \
    -d "desc=${desc}" \
    -d "defaultLists=true" | python3 -m json.tool 2>/dev/null || echo "Board created."
}

cmd_search() {
  local query="${1:?Usage: search <query>}"
  echo -e "${GREEN}Searching for '${query}'...${NC}" >&2
  trello_request GET "/search?query=$(python3 -c "import urllib.parse; print(urllib.parse.quote('${query}'))")&modelTypes=cards,boards" | python3 -m json.tool 2>/dev/null || trello_request GET "/search?query=${query}&modelTypes=cards,boards"
}

cmd_help() {
  cat <<EOF
${GREEN}trello-ops.sh${NC} — Trello REST API helper

${YELLOW}Usage:${NC} bash trello-ops.sh <command> [args...]

${YELLOW}Commands:${NC}
  get-boards                          List all your boards
  get-lists <boardId>                 List all lists on a board
  get-cards <listId>                  List all cards on a list
  get-card <cardId>                   Get details of a single card
  create-board <name> [desc]          Create a new board
  create-list <boardId> <name>        Create a new list on a board
  create-card <listId> <name> [desc]  Create a new card
  move-card <cardId> <targetListId>   Move a card to another list
  archive-card <cardId>               Archive a card
  add-comment <cardId> <text>         Add a comment to a card
  add-label <cardId> <color>          Add a label to a card
  add-member <cardId> <memberId>      Assign a member to a card
  search <query>                      Search boards and cards
  help                                Show this help message

${YELLOW}Required env vars:${NC}
  TRELLO_API_KEY    Your Trello API key
  TRELLO_TOKEN      Your Trello authorization token

${YELLOW}Get credentials:${NC}
  https://trello.com/power-ups/admin
EOF
}

# ─── Main ────────────────────────────────────────────────────────────

check_auth

command="${1:-help}"
shift || true

case "$command" in
  get-boards)    cmd_get_boards "$@" ;;
  get-lists)     cmd_get_lists "$@" ;;
  get-cards)     cmd_get_cards "$@" ;;
  get-card)      cmd_get_card "$@" ;;
  create-board)  cmd_create_board "$@" ;;
  create-list)   cmd_create_list "$@" ;;
  create-card)   cmd_create_card "$@" ;;
  move-card)     cmd_move_card "$@" ;;
  archive-card)  cmd_archive_card "$@" ;;
  add-comment)   cmd_add_comment "$@" ;;
  add-label)     cmd_add_label "$@" ;;
  add-member)    cmd_add_member "$@" ;;
  search)        cmd_search "$@" ;;
  help)          cmd_help ;;
  *)
    echo -e "${RED}Unknown command: ${command}${NC}" >&2
    cmd_help
    exit 1
    ;;
esac
