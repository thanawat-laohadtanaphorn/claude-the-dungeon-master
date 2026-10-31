# Portraits

Every character has a portrait. It's used three ways: the linked name in story posts, the card on the scene map, and the map token.

## Who gets one

Player characters, companions, NPCs, named animals and monsters, the first time they appear. A group (a gang of bandits, a swarm, a herd) gets one crowd picture and a `count` on its token.

## Where they come from

- **From the player:** the player can hand Claude a picture for any character (one they found or made). Claude uses it and crops it like any other.
- **Everyone else:** freely licensed art from the internet. Prefer public-domain paintings on [Wikimedia Commons](https://commons.wikimedia.org); CC-licensed photos work well for animals and monsters.
- Record each one in `portraits/index.md`: character, file, source link, licence.
- For important NPCs, Claude shows 3 to 4 numbered options and the player picks one.

## Format

- 1020x960 JPEG, face centred horizontally and about a third of the way down (near x 510, y 330).
- Saved as `portraits/<id>.jpg`, where `<id>` is the character's lowercase id (`sim_rook`), the same id the scene map token uses as `img`.
- `tools/crop_portrait.py` does the crop: `python3 tools/crop_portrait.py source.jpg portraits/sim_rook.jpg --face 640 410`.
- Not too tight: the scene map cuts a close face crop for the token and a wider circle for the card from the same picture, so leave head and shoulders in.

## Reuse

A portrait is made once and reused every time that character appears again. Never redraw or swap a portrait without the player asking.

## Linking names

In every story post, every mention of a character's name links to their portrait file: `[Wren](portraits/wren.jpg)`.
