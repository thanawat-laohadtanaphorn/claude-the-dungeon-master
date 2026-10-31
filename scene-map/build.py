"""Build a scene map page from a scene state file.

    python3 build.py scene.json out.html [--portraits DIR] [--party party.json] [--journal journal.json]

Defaults: portraits/, party.json and journal.json next to scene.json or one folder up (each is optional
except portraits). Every token needs a portrait: <portraits>/<img>.jpg, 1020x960.
Needs Pillow (pip install pillow). Publish out.html as an Artifact.
"""
import argparse, base64, io, json, os, sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))

ap = argparse.ArgumentParser()
ap.add_argument('state'); ap.add_argument('out')
ap.add_argument('--portraits'); ap.add_argument('--party'); ap.add_argument('--journal')
ap.add_argument('--template', default=os.path.join(HERE, 'template.html'))
a = ap.parse_args()

here = os.path.dirname(os.path.abspath(a.state))
def find(name):  # next to the scene file, or one folder up (scenes/ inside the campaign folder)
    for d in (here, os.path.dirname(here)):
        if os.path.exists(os.path.join(d, name)):
            return os.path.join(d, name)
    return os.path.join(here, name)
lib = a.portraits or find('portraits')
def load(path, name):
    path = path or find(name)
    return json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}

st = json.load(open(a.state, encoding='utf-8'))
party, journal = load(a.party, 'party.json'), load(a.journal, 'journal.json')

missing = [f"{t['id']} ({t.get('name', '')}): img {t.get('img')!r}" for t in st['tokens']
           if not (t.get('img') and os.path.exists(os.path.join(lib, t['img'] + '.jpg')))]
if missing:
    sys.exit('No portrait for:\n  ' + '\n  '.join(missing) +
             f'\nAdd <img>.jpg (1020x960) to {lib}. Every token needs a portrait.')

def crop(src, box, px):
    """box = (w, h, x, y) on the 1020x960 portrait; returns a JPEG data URL px x px."""
    w, h, x, y = box
    im = Image.open(src).convert('RGB').crop((x, y, x + w, y + h)).resize((px, px), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=86)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()

jpeople = {p for sec in ('main', 'side', 'loose', 'done') for e in journal.get(sec, []) for p in e.get('people', [])}
face, port = {}, {}
for k in {t['img'] for t in st['tokens']} | jpeople:
    src = os.path.join(lib, k + '.jpg')
    if not os.path.exists(src):
        continue
    crowd = any(t.get('img') == k and t.get('count', 0) > 1 for t in st['tokens'])
    face[k] = crop(src, (780, 780, 120, 60) if crowd else (560, 560, 230, 150), 150)  # map token
    port[k] = crop(src, (780, 780, 120, 60), 280)                                        # top cards

h = open(a.template, encoding='utf-8').read()
for key, val in (('__STATE__', st), ('__FACE__', face), ('__PORT__', port), ('__PARTY__', party),
                 ('__JOURNAL__', journal), ('__SCENE__', '')):
    h = h.replace(key, json.dumps(val, ensure_ascii=False))
h = h.replace('__TITLE__', st['title'])
open(a.out, 'w', encoding='utf-8').write(h)
print('wrote', a.out)
