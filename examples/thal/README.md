# Sample campaign: Thal, Wren and Holt

Real files from Thanawat's own campaign, mid main quest 2, to show what a running game looks like.

| File | What it shows |
| --- | --- |
| `scenes/combat-millstream.json` → `combat-millstream.html` | Combat mode, round 2 of a river chase: turn order, Holt acting, a mounted foe shown only as "Badly hurt" |
| `scenes/explore-mossend.json` → `explore-mossend.html` | Exploring mode in a village at dawn: everyone in the scene, no turn order |
| `party-state.json` | The live party numbers those maps were built from |
| `party.json` | Character panels: spells, abilities, gear, bag |
| `journal.json` | The player-facing journal: main quests, side quests, loose ends |
| `portraits/` | Portraits used on the maps, with credits in `portraits/index.md` |

Thal is a level 5 wizard (Abjuration), Wren a ranger and Holt a fighter (Champion). This campaign used a few house rules of its own (for example Thal's bonus spell slot), which you'll see mentioned in the sample. They aren't part of the kit.

Rebuild a map: `python3 ../../scene-map/build.py scenes/explore-mossend.json explore-mossend.html`
