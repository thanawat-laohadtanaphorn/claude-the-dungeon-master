"""Crop any picture to a kit portrait: 1020x960, face near the top middle.

    python3 crop_portrait.py source.jpg portraits/<id>.jpg [--face X Y] [--height H]

--face X Y   where the face centre is in the source picture (pixels). Default: centre, upper third.
--height H   how much of the source (in pixels) the portrait spans top to bottom. Default: as much as fits.
The face lands near (510, 330) in the result, which is where the scene map cuts tokens from.
Needs Pillow (pip install pillow).
"""
import argparse
from PIL import Image

W, H, FX, FY = 1020, 960, 510, 330
ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('out')
ap.add_argument('--face', nargs=2, type=float); ap.add_argument('--height', type=float)
a = ap.parse_args()

im = Image.open(a.src).convert('RGB')
sw, sh = im.size
fx, fy = a.face if a.face else (sw / 2, sh / 3)
ch = a.height or min(sh, sw * H / W)
ch = min(ch, sh, sw * H / W)
cw = ch * W / H
s = ch / H
left = min(max(fx - FX * s, 0), sw - cw)
top = min(max(fy - FY * s, 0), sh - ch)
im.crop((round(left), round(top), round(left + cw), round(top + ch))).resize((W, H), Image.LANCZOS).save(a.out, 'JPEG', quality=90)
print('wrote', a.out)
