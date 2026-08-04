#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageDraw,ImageEnhance,ImageFilter,ImageFont,ImageOps
BASE=Path(__file__).resolve().parent
BG=BASE/'lipsync/v3_real_scene_base.png'
FONT=Path('/System/Library/Fonts/SFNSMono.ttf')
BODY='#EAF2FF';CYAN='#35D9F2';MUTED='#91A4C4';PANEL='#07101F'
CANDIDATES={
 'C':BASE/'identity/candidate_c_young_black_male.png',
 'D':BASE/'identity/candidate_d_young_latino_male.png',
}
def f(n):return ImageFont.truetype(str(FONT),n)
def main():
 for key,path in CANDIDATES.items():
  im=Image.open(BG).convert('RGBA');d=ImageDraw.Draw(im)
  d.rounded_rectangle((1700,250,2485,1245),radius=38,fill=(7,16,31,245))
  x0,y0,x1,y1=1980,610,2420,1170;size=(x1-x0,y1-y0)
  src=Image.open(path).convert('RGB');src=ImageOps.fit(src,size,Image.Resampling.LANCZOS,centering=(.5,.42));src=ImageEnhance.Color(src).enhance(.96).convert('RGBA')
  mask=Image.new('L',size,0);md=ImageDraw.Draw(mask);md.rounded_rectangle((25,10,size[0]-25,size[1]-10),radius=72,fill=248);mask=mask.filter(ImageFilter.GaussianBlur(30))
  px=mask.load();assert px is not None
  for y in range(size[1]):
   fade=max(0,min(1,(size[1]-y)/95))
   for x in range(size[0]):px[x,y]=int(px[x,y]*fade)
  src.putalpha(mask);im.alpha_composite(src,(x0,y0));d=ImageDraw.Draw(im)
  d.text((1760,350),f'YOUNG PRESENTER {key}',font=f(34),fill=BODY)
  d.text((1760,407),'Ash · native PCM · 125.8 WPM',font=f(22),fill=CYAN)
  d.text((1760,455),'Proposed 430 × 560 footprint',font=f(20),fill=MUTED)
  d.text((1760,495),'Character no longer dominates the paper.',font=f(18),fill=MUTED)
  out=BASE/f'identity/YOUNG_PRESENTER_{key}_SMALL_LAYOUT.png';im.convert('RGB').save(out,quality=95);print(out)
if __name__=='__main__':main()
