# Portraits

Every character has **exactly one picture**, `portraits/<id>.jpg`, kept whole. It's shown two ways:

- **Figure:** the whole picture. Every linked name in a story post opens it.
- **Portrait:** a face crop the scene map cuts from the same picture, a close face for the map token and head and shoulders for the cards.

No second file, no separate crop: one picture per character, always.

## Who gets one

Player characters, companions, NPCs, named animals and monsters, the first time they appear. A group (a gang of bandits, a swarm, a herd) gets one crowd picture and a `count` on its token.

## Where they come from

- **From the player:** the player can hand Claude a picture for any character (one they found or made). Claude uses it as that character's one picture and records where the face is.
- **Everyone else:** freely licensed art from the internet. Prefer public-domain paintings on [Wikimedia Commons](https://commons.wikimedia.org); CC-licensed photos work well for animals and monsters.
- Record each one in `portraits/index.md`: character, file, source link, licence.
- For important NPCs, Claude shows 3 to 4 numbered options and the player picks one.

## Format

- JPEG, any shape (full-body, half-length or a head shot all work). Keep the whole picture; don't crop it down to the face. Scale it down if the long side is over about 1600 px.
- Saved as `portraits/<id>.jpg`, where `<id>` is the character's lowercase id (`sim_rook`), the same id the scene map token uses as `img`.
- **Where the face is:** if the face sits near the top middle of the picture, nothing else is needed. Otherwise record it in `portraits/faces.json` with `tools/set_face.py`, and check the preview: `python3 tools/set_face.py portraits/sim_rook.jpg --face 640 410 --preview check.jpg`. `--width` sets how wide the head-and-shoulders crop is (about 2.5 head widths).

## Reuse

A picture is found once and reused every time that character appears again. Never redraw or swap a picture without the player asking. If the player sends a new one, it replaces the old file; there is still only one.

## Linking names

In every story post, every mention of a character's name links to their picture, which opens the whole figure: `[Wren](portraits/wren.jpg)`.
