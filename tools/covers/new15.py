# 2026-10-15 추가 15편 표지
import os,sys,math; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from covers_lib import *
RED=(214,110,100); DARK=(170,80,70); BONE=(236,224,206); BONE2=(222,206,184)
def LF(d): leaf(d,1320,730,160,60,-30,A(G))
def f(im,d):  # pregnancy-back-pain
    d.arc(s(560,160,960,760),60,300,fill=A(BONE2),width=40*S); d.chord(s(560,460,1000,760),180,360,fill=A(RED,170)); spark(d,640,420,70,A(AC)); LF(d)
go('pregnancy-back-pain',*PEACH,f)
def f(im,d):  # postpartum-joint-pain
    rr(d,520,360,760,440,40,fill=A(BONE2)); circ(d,780,400,50,fill=A(RED,210)); rr(d,920,200,1000,700,40,fill=A(BONE2)); circ(d,960,450,55,fill=A(RED,210)); LF(d)
go('postpartum-joint-pain',*ROSE,f)
def f(im,d):  # ankylosing-spondylitis
    for i in range(6): rr(d,700,150+i*95,900,225+i*95,24,fill=A(BONE))
    ln(d,[(660,160),(660,740)],A(RED,200),12); ln(d,[(940,160),(940,740)],A(RED,200),12); LF(d)
go('ankylosing-spondylitis',*SAND,f)
def f(im,d):  # thoracic-outlet
    ln(d,[(480,330),(800,380),(1120,330)],A(BONE2),40); d.arc(s(640,380,960,700),200,340,fill=A(BONE2),width=30*S)
    ln(d,[(800,420),(1000,520),(1180,700)],A(RED,220),12); ln(d,[(800,440),(990,560),(1150,740)],A(BL,230),10); LF(d)
go('thoracic-outlet',*SKY,f)
def f(im,d):  # ankle-instability
    rr(d,740,140,860,520,50,fill=A(BONE2)); d.polygon(s(700,520,900,520,1050,690,700,690),fill=A(BONE2))
    for k in range(3): d.arc(s(640-k*20,460-k*20,960+k*20,780+k*20),200,250,fill=A(RED,200-k*50),width=8*S)
    LF(d)
go('ankle-instability',*MINT,f)
def f(im,d):  # baker-cyst
    rr(d,720,140,860,440,60,fill=A(BONE)); rr(d,730,470,850,780,55,fill=A(BONE)); circ(d,900,470,70,fill=A(BL,220)); LF(d)
go('baker-cyst',*SKY,f)
def f(im,d):  # preconception
    d.chord(s(600,460,1000,700),0,180,fill=A((190,150,105))); ln(d,[(800,480),(800,300)],A(DG),10)
    leaf(d,860,310,130,48,-40,A(G)); leaf(d,740,340,110,42,-140,A(G2)); circ(d,1100,260,50,fill=A(AC,220)); LF(d)
go('preconception',*PEACH,f)
def f(im,d):  # postpartum-hair-loss
    rr(d,600,300,1000,380,30,fill=A((190,150,105)))
    for x in range(620,1000,30): ln(d,[(x,380),(x,460)],A((190,150,105)),8)
    for k in range(5): d.arc(s(560+k*90,520,700+k*90,700),200,320,fill=A((120,100,90),180),width=5*S)
    LF(d)
go('postpartum-hair-loss',*ROSE,f)
def f(im,d):  # menstrual-migraine
    circ(d,700,380,120,fill=A(RED,200)); circ(d,760,350,110,fill=ROSE[0]+(255,))
    ln(d,[(600,560),(720,560),(750,500),(790,620),(820,540),(1000,540)],A(DARK),8); LF(d)
go('menstrual-migraine',*ROSE,f)
def f(im,d):  # child-tonic
    d.chord(s(620,400,980,640),0,180,fill=A((170,110,80))); rr(d,620,500,980,530,8,fill=A((170,110,80)))
    ln(d,[(800,420),(800,280)],A(DG),8); leaf(d,850,290,110,40,-40,A(G)); leaf(d,750,310,90,34,-140,A(G2)); LF(d)
go('child-tonic',*MINT,f)
def f(im,d):  # underweight
    rr(d,640,560,960,620,20,fill=A(BONE2)); ln(d,[(800,560),(800,420)],A(BONE2),14); circ(d,800,380,60,outline=A(DARK),width=8*S)
    d.chord(s(1000,420,1200,560),0,180,fill=A((250,250,250))); circ(d,1100,440,40,fill=A((250,250,250))); LF(d)
go('underweight',*SAND,f)
def f(im,d):  # nocturia
    circ(d,640,330,110,fill=A((236,220,170))); circ(d,690,300,100,fill=NIGHT[0]+(255,))
    for x,y,r in [(950,420,46),(1030,560,34)]: drop(d,x,y,r,A(BL,240))
    LF(d)
go('nocturia',*NIGHT,f)
def f(im,d):  # vestibular-neuritis
    d.arc(s(620,280,900,560),0,300,fill=A(RED,220),width=26*S); circ(d,760,420,40,fill=A(RED,220))
    for k in range(3): d.arc(s(900+k*40,260-k*30,1100+k*50,580+k*30),300,60,fill=A(DARK,200-k*50),width=7*S)
    LF(d)
go('vestibular-neuritis',*SKY,f)
def f(im,d):  # dermatographism
    rr(d,520,300,1080,620,60,fill=A((246,226,214)))
    ln(d,[(600,520),(720,400),(840,520),(960,400)],A(RED,200),22); LF(d)
go('dermatographism',*PEACH,f)
def f(im,d):  # lpr
    rr(d,740,140,860,700,50,fill=A(BONE2))
    for k in range(3): ln(d,[(760,620-k*120),(800,580-k*120),(840,620-k*120)],A(RED,210),10)
    spark(d,800,220,70,A(AC)); LF(d)
go('lpr',*SAND,f)
print('ok')
