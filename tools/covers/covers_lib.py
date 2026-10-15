# 칼럼 표지 그림 도우미. 새 표지는 covers/example_heart.py처럼 이 파일을 불러 그린 뒤 go("slug", 배경색1, 배경색2, 그리는함수)를 호출한다.
# 결과: images/col-<slug>.jpg (1600x900). 사람 얼굴·사람 그림은 넣지 않는다. 오른쪽 아래 초록 잎(leaf)이 공통 표식.
import math, random
from PIL import Image, ImageDraw, ImageFilter
W,H,S=1600,900,2
import os; OUT=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),"images")+os.sep
G=(31,122,109); G2=(64,150,130); DG=(21,90,80); AC=(242,165,65); BL=(150,196,214)
def A(c,a=240): return c+(a,)
def base(c1,c2):
    im=Image.new("RGB",(W*S,H*S)); d=ImageDraw.Draw(im)
    for y in range(H*S):
        t=y/(H*S); d.line([(0,y),(W*S,y)],fill=tuple(int(c1[i]+(c2[i]-c1[i])*t) for i in range(3)))
    return im
def L(): 
    l=Image.new("RGBA",(W*S,H*S),(0,0,0,0)); return l,ImageDraw.Draw(l)
def put(im,l,blur=0):
    if blur: l=l.filter(ImageFilter.GaussianBlur(blur*S))
    im.paste(l,(0,0),l)
def s(*v): return [x*S for x in v]
def circ(d,x,y,r,**k): d.ellipse(s(x-r,y-r,x+r,y+r),**k)
def leaf(d,cx,cy,Ln,Wd,ang,fill,vein=None):
    pts=[(Ln*(i/40-0.5),Wd*math.sin(math.pi*i/40)*0.5) for i in range(41)]
    pts+=[(x,-y) for x,y in reversed(pts)]; a=math.radians(ang)
    d.polygon([((cx+x*math.cos(a)-y*math.sin(a))*S,(cy+x*math.sin(a)+y*math.cos(a))*S) for x,y in pts],fill=fill)
    if vein: d.line([((cx-Ln/2*math.cos(a))*S,(cy-Ln/2*math.sin(a))*S),((cx+Ln/2*math.cos(a))*S,(cy+Ln/2*math.sin(a))*S)],fill=vein,width=3*S)
def drop(d,x,y,r,fill):
    circ(d,x,y,r,fill=fill); d.polygon(s(x-r*0.86,y-r*0.5,x+r*0.86,y-r*0.5,x,y-r*2.1),fill=fill)
def save(im,n): im.resize((W,H),Image.LANCZOS).convert("RGB").save(OUT+"col-"+n+".jpg",quality=86,optimize=True,progressive=True)
PINK=(226,150,170); RED=(214,110,100); WH=(255,255,255); BR=(190,150,105)
def ln(d,pts,col,w): d.line([(x*S,y*S) for x,y in pts],fill=col,width=int(w*S),joint="curve")
def rr(d,x0,y0,x1,y1,r,**k): d.rounded_rectangle(s(x0,y0,x1,y1),radius=r*S,**k)
def flake(d,cx,cy,r,col,w=8):
    for k in range(6):
        a=math.radians(k*60); x,y=cx+math.cos(a)*r,cy+math.sin(a)*r
        ln(d,[(cx,cy),(x,y)],col,w)
        for t in (0.55,):
            bx,by=cx+math.cos(a)*r*t,cy+math.sin(a)*r*t
            for da in (-40,40):
                b=a+math.radians(da); ln(d,[(bx,by),(bx+math.cos(b)*r*0.3,by+math.sin(b)*r*0.3)],col,w*0.8)
def spark(d,x,y,r,col):
    for k in range(8):
        a=math.radians(k*45); ln(d,[(x+math.cos(a)*r*0.45,y+math.sin(a)*r*0.45),(x+math.cos(a)*r,y+math.sin(a)*r)],col,6)
def bolt(d,x,y,k,col): d.polygon(s(x,y-90*k,x+30*k,y-10*k,x+5*k,y-10*k,x+40*k,y+90*k,x-20*k,y-5*k,x+5*k,y-5*k),fill=col)
def heartf(d,cx,cy,k,fill):
    d.polygon([((cx+16*math.sin(t)**3*k)*S,(cy-(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))*k)*S) for t in [math.radians(i) for i in range(0,360,3)]],fill=fill)
SAND=((248,244,234),(236,228,212)); MINT=((240,246,242),(222,236,230)); SKY=((236,242,250),(220,230,244)); ROSE=((250,240,242),(240,224,230)); PEACH=((252,242,232),(244,226,212)); NIGHT=((44,62,80),(31,96,104))

def go(n,c1,c2,f):
    """배경(c1→c2 세로 그라데이션)을 깔고 f(im,d)로 그린 뒤 images/col-n.jpg로 저장."""
    im=base(c1,c2); l,d=L(); f(im,d); put(im,l); save(im,n)
