"""Tell the scene map where a character's face is in their picture.

    python3 set_face.py portraits/<id>.jpg --face X Y [--width W] [--preview out.jpg]

Each character has exactly one picture, portraits/<id>.jpg, kept whole (the "figure").
The scene map cuts the "portrait" views from it: a close face crop for the map token and a
head-and-shoulders crop for the cards. If the face is near the top middle, nothing is needed.
Otherwise record it here; it's saved in portraits/faces.json next to the picture.

--face X Y   centre of the face in the picture, in pixels.
--width W    width of a head-and-shoulders crop, in pixels (about 2.5 head widths). Default: 80% of the shorter side.
--preview    also write the card and token crops side by side, to check them.
Needs Pillow (pip install pillow).
"""
import argparse, json, os
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('picture'); ap.add_argument('--face', nargs=2, type=float, required=True)
ap.add_argument('--width', type=float); ap.add_argument('--preview')
a = ap.parse_args()

im = Image.open(a.picture).convert('RGB')
W, H = im.size
x, y = a.face
w = a.width or min(W, H) * 0.8
k = os.path.splitext(os.path.basename(a.picture))[0]
path = os.path.join(os.path.dirname(os.path.abspath(a.picture)), 'faces.json')
faces = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
faces[k] = {'x': round(x), 'y': round(y), 'w': round(w)}
json.dump(dict(sorted(faces.items())), open(path, 'w', encoding='utf-8'), indent=1)
print('saved', k, faces[k], 'in', path)

if a.preview:
    def crop(cx, cy, side, px):
        side = min(side, W, H)
        left = min(max(cx - side / 2, 0), W - side); top = min(max(cy - side / 2, 0), H - side)
        return im.crop((round(left), round(top), round(left + side), round(top + side))).resize((px, px), Image.LANCZOS)
    sheet = Image.new('RGB', (440, 280), 'white')
    sheet.paste(crop(x, y + 0.154 * w, w, 280), (0, 0))
    sheet.paste(crop(x, y + 0.128 * w, 0.72 * w, 150), (290, 65))
    sheet.save(a.preview, 'JPEG', quality=88)
    print('preview', a.preview)
