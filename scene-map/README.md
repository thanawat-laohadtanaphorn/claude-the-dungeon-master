# Scene map

One HTML page per fight or scene, built from a scene state file and published as an Artifact. Claude updates the state each post, rebuilds, and republishes to the same link.

```
python3 build.py scenes/cellar-01.json cellar.html --portraits portraits --party party.json --journal journal.json
```

Needs Python 3 and Pillow (`pip install pillow`). The build refuses to run if any token has no portrait.

## Modes

- `"mode": "combat"`: turn-order strip (`order`), round chip (`round`), gold glow and "Now acting" on `active`.
- `"mode": "explore"`: no turn order. The top row is everyone in the scene: tokens with `"focus": true` first (who the party is talking to), then allies, neutrals, foes, and the party last. The chip shows `time`.

## Grid

- `map` is a list of strings, one per row, one character per 5 ft square. Each character is a key in `terrain`.
- Squares are named by column letter and row number: x 2, y 9 is C10 (`colName(x) + (y + 1)`). Tapping a square shows its name, terrain and occupant.
- `terrain[key]`: `name` (shown in the legend, include the rule: "difficult terrain", "half cover"), `fill`, optional `ink`, `mark` (`reeds`, `planks`, `roof`, `stake`, `ladder`, `flame`) and `dot` (a colour). The legend draws each swatch with the same code as the map.
- `labels`: text on the map, `{x, y, text, size, color, anchor}`.

## Tokens

| Field | Meaning |
| --- | --- |
| `id`, `name`, `short_name` | Id, full name, short label for the cards |
| `img` | Portrait id: `portraits/<img>.jpg` (required) |
| `side` | `ally`, `foe`, or anything else for neutral. Party members are allies with an entry in `party.json` |
| `x`, `y` | Square (0-based) |
| `hp` | Allies: `"cur/max"`, shown exactly with a bar |
| `health` | Foes and NPCs: Unhurt, Scratched, Bloodied, Badly hurt, Down (no numbers shown) |
| `ac`, `speed`, `role`, `note` | Shown on cards and panels |
| `conds` | Conditions (red chips), e.g. Poisoned |
| `tags` | Ongoing effects (teal chips), e.g. Mage Armor |
| `res` | Per-fight counts that override `party.json`, e.g. `{"1st": "3/4", "Action Surge": "0/1"}` |
| `size` | 2 for Large, 3 for Huge |
| `count` | Group size for a crowd token (shows ×N; the token shows the whole crowd picture) |
| `down`, `invisible`, `focus` | Flags |

## Character panels (`party.json`)

Tapping a party member opens tabs: Use (slots, resources, then everything usable grouped by action, bonus action, reaction, free, out of combat), Passive, Gear and Bag. See `templates/party.json` for the shape. Things that can't be used right now are greyed out with the reason.

## Journal (`journal.json`)

Shown as a card under the map with Main, Side and Loose ends tabs. Player-facing only. See `templates/journal.json`.
