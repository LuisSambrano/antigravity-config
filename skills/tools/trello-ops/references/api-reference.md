# Trello REST API Reference

Base URL: `https://api.trello.com/1`
Auth: Append `?key={API_KEY}&token={TOKEN}` to all requests.

## Table of Contents

- [Boards](#boards)
- [Lists](#lists)
- [Cards](#cards)
- [Labels](#labels)
- [Members](#members)
- [Checklists](#checklists)
- [Comments](#comments)
- [Search](#search)
- [Webhooks](#webhooks)

---

## Boards

| Method | Endpoint             | Description                            |
| ------ | -------------------- | -------------------------------------- |
| GET    | `/members/me/boards` | List all boards for authenticated user |
| GET    | `/boards/{id}`       | Get a specific board                   |
| POST   | `/boards`            | Create a new board                     |
| PUT    | `/boards/{id}`       | Update a board                         |
| DELETE | `/boards/{id}`       | Delete a board                         |

### Create Board

```bash
curl -X POST "https://api.trello.com/1/boards?name=My+Board&defaultLists=true&key={key}&token={token}"
```

Fields: `name` (required), `desc`, `defaultLists` (bool), `idOrganization`, `prefs_background`.

---

## Lists

| Method | Endpoint                  | Description              |
| ------ | ------------------------- | ------------------------ |
| GET    | `/boards/{boardId}/lists` | Get lists on a board     |
| GET    | `/lists/{id}`             | Get a specific list      |
| POST   | `/boards/{boardId}/lists` | Create a list on a board |
| PUT    | `/lists/{id}`             | Update a list            |
| PUT    | `/lists/{id}/closed`      | Archive/unarchive a list |

### Create List

```bash
curl -X POST "https://api.trello.com/1/boards/{boardId}/lists?name=My+List&key={key}&token={token}"
```

Fields: `name` (required), `pos` (`top`, `bottom`, or number).

---

## Cards

| Method | Endpoint                | Description         |
| ------ | ----------------------- | ------------------- |
| GET    | `/lists/{listId}/cards` | Get cards in a list |
| GET    | `/cards/{id}`           | Get a specific card |
| POST   | `/cards`                | Create a card       |
| PUT    | `/cards/{id}`           | Update a card       |
| DELETE | `/cards/{id}`           | Delete a card       |

### Create Card

```bash
curl -X POST "https://api.trello.com/1/cards?idList={listId}&name=Card+Title&desc=Description&key={key}&token={token}"
```

Fields: `idList` (required), `name` (required), `desc`, `pos`, `due`, `dueComplete`, `idMembers`, `idLabels`, `urlSource`.

### Move Card

```bash
curl -X PUT "https://api.trello.com/1/cards/{cardId}?idList={targetListId}&key={key}&token={token}"
```

### Archive Card

```bash
curl -X PUT "https://api.trello.com/1/cards/{cardId}?closed=true&key={key}&token={token}"
```

---

## Labels

| Method | Endpoint                             | Description            |
| ------ | ------------------------------------ | ---------------------- |
| GET    | `/boards/{boardId}/labels`           | Get labels on a board  |
| POST   | `/labels`                            | Create a label         |
| POST   | `/cards/{cardId}/idLabels`           | Add label to card      |
| DELETE | `/cards/{cardId}/idLabels/{labelId}` | Remove label from card |

Colors: `green`, `yellow`, `orange`, `red`, `purple`, `blue`, `sky`, `lime`, `pink`, `black`, `null` (no color).

---

## Members

| Method | Endpoint                               | Description              |
| ------ | -------------------------------------- | ------------------------ |
| GET    | `/boards/{boardId}/members`            | Get board members        |
| GET    | `/members/me`                          | Get authenticated member |
| POST   | `/cards/{cardId}/idMembers`            | Add member to card       |
| DELETE | `/cards/{cardId}/idMembers/{memberId}` | Remove member from card  |

---

## Checklists

| Method | Endpoint                                  | Description                          |
| ------ | ----------------------------------------- | ------------------------------------ |
| GET    | `/cards/{cardId}/checklists`              | Get checklists on a card             |
| POST   | `/checklists`                             | Create checklist (`idCard` required) |
| POST   | `/checklists/{id}/checkItems`             | Add item to checklist                |
| PUT    | `/cards/{cardId}/checkItem/{checkItemId}` | Update check item                    |
| DELETE | `/checklists/{id}`                        | Delete a checklist                   |

### Create Checklist with Items

```bash
# Create checklist
curl -X POST "https://api.trello.com/1/checklists?idCard={cardId}&name=Tasks&key={key}&token={token}"

# Add item
curl -X POST "https://api.trello.com/1/checklists/{checklistId}/checkItems?name=Sub-task+1&key={key}&token={token}"
```

---

## Comments

| Method | Endpoint                                     | Description                   |
| ------ | -------------------------------------------- | ----------------------------- |
| GET    | `/cards/{cardId}/actions?filter=commentCard` | Get comments on a card        |
| POST   | `/cards/{cardId}/actions/comments`           | Add comment (`text` required) |
| PUT    | `/actions/{commentId}/text`                  | Update a comment              |
| DELETE | `/actions/{commentId}`                       | Delete a comment              |

---

## Search

```bash
curl "https://api.trello.com/1/search?query=search+term&modelTypes=cards,boards&key={key}&token={token}"
```

Params: `query` (required), `modelTypes` (cards, boards, organizations, members), `board_fields`, `card_fields`, `cards_limit`.

---

## Webhooks

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| POST   | `/webhooks`      | Create a webhook    |
| GET    | `/webhooks/{id}` | Get webhook details |
| DELETE | `/webhooks/{id}` | Delete a webhook    |

### Create Webhook

```bash
curl -X POST "https://api.trello.com/1/webhooks?callbackURL=https://your-server.com/webhook&idModel={boardId}&key={key}&token={token}"
```

---

## Rate Limits

- **100 requests per 10 seconds** per API key per token
- **300 requests per 10 seconds** per API key (across all tokens)
- Responses include `X-Rate-Limit-*` headers

## Error Codes

| Code | Meaning                      |
| ---- | ---------------------------- |
| 400  | Bad request / invalid params |
| 401  | Unauthorized (bad key/token) |
| 404  | Resource not found           |
| 429  | Rate limit exceeded          |
