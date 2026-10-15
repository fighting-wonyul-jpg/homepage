# 2026-10-15 추가 18편 표지
import os,sys,math; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from covers_lib import *
RED=(214,110,100); BRN=(196,150,140); DARK=(170,80,70); BONE=(236,224,206); BONE2=(222,206,184)
def LF(d): leaf(d,1320,730,160,60,-30,A(G))
def petal5(d,x,y,r,col):
    for k in range(5):
        a=math.radians(k*72-90); circ(d,x+math.cos(a)*r,y+math.sin(a)*r,r*0.75,fill=col)
    circ(d,x,y,r*0.5,fill=A(AC))
def eyeball(d,x,y,w,h,col):
    d.ellipse(s(x-w,y-h,x+w,y+h),outline=col,width=10*S); circ(d,x,y,h*0.55,fill=col)
def f(im,d):  # menopause-diet
    d.ellipse(s(560,250,1040,650),outline=A(RED,220),width=26*S)
    for k in range(12):
        a=math.radians(200+k*12); x=800+math.cos(a)*240; y=450+math.sin(a)*200
        ln(d,[(x,y),(800+math.cos(a)*215,450+math.sin(a)*178)],A(DARK),5)
    rr(d,700,600,900,690,20,fill=A(AC,230)); LF(d)
go('menopause-diet',*PEACH,f)
def f(im,d):  # rotator-cuff-tear
    circ(d,700,450,120,fill=A(BONE)); d.arc(s(560,280,1000,720),200,300,fill=A(RED),width=26*S); d.arc(s(560,280,1000,720),320,40,fill=A(RED),width=26*S)
    spark(d,1010,330,90,A(AC)); LF(d)
go('rotator-cuff-tear',*SKY,f)
def f(im,d):  # spondylolisthesis
    for i,dx in enumerate([0,0,70,0,0]):
        rr(d,680+dx,190+i*110,920+dx,270+i*110,26,fill=A(BONE if i!=2 else (232,176,160)))
    spark(d,1060,440,80,A(AC)); LF(d)
go('spondylolisthesis',*SAND,f)
def f(im,d):  # meniscus-tear
    rr(d,640,170,960,400,60,fill=A(BONE)); rr(d,660,500,940,740,50,fill=A(BONE))
    d.chord(s(620,380,800,520),180,360,fill=A(RED,220)); d.chord(s(800,380,980,520),180,360,fill=A(RED,220))
    ln(d,[(860,420),(880,445),(865,470)],A((255,255,255)),6); LF(d)
go('meniscus-tear',*MINT,f)
def f(im,d):  # whiplash
    for k,a in enumerate([-0.35,0,0.35]):
        col=A(RED,90+k*0) if a else A(RED,230)
        x=800+math.sin(a)*260; y=330-math.cos(a)*40
        ln(d,[(800,640),(x,y+90)],col,30); circ(d,x,y,80,fill=col)
    d.arc(s(500,180,1100,780),200,250,fill=A(DARK),width=8*S); d.arc(s(500,180,1100,780),290,340,fill=A(DARK),width=8*S); LF(d)
go('whiplash',*SKY,f)
def f(im,d):  # pes-anserine
    rr(d,720,140,860,440,60,fill=A(BONE)); rr(d,730,470,850,780,55,fill=A(BONE))
    for k in range(3): ln(d,[(640-k*30,220+k*40),(700,430),(735,520)],A(RED,220),12)
    spark(d,700,500,90,A(AC)); LF(d)
go('pes-anserine',*ROSE,f)
def f(im,d):  # finger-arthritis
    for i,x in enumerate([620,760,900]):
        rr(d,x,230-i*30,x+100,700,50,fill=A(BONE2))
        for y in [380-i*30,540-i*20]: circ(d,x+50,y,48,fill=A(RED,200))
    LF(d)
go('finger-arthritis',*PEACH,f)
def f(im,d):  # piriformis
    d.arc(s(500,180,1100,700),200,340,fill=A(BONE2),width=60*S)
    ln(d,[(620,380),(980,520)],A(RED,230),40); ln(d,[(820,450),(830,820)],A(AC),10); LF(d)
go('piriformis',*SAND,f)
def f(im,d):  # child-atopic
    rr(d,700,360,900,640,40,fill=A((250,250,250))); rr(d,690,300,910,370,20,fill=A((140,200,190)))
    for x,y in [(560,300),(600,520),(1030,330),(1060,560),(990,450)]: circ(d,x,y,14,fill=A(RED,160))
    leaf(d,600,420,150,56,-60,A(G2)); LF(d)
go('child-atopic',*MINT,f)
def f(im,d):  # child-snoring
    circ(d,760,400,150,fill=A(AC,230)); circ(d,830,360,140,fill=SKY[0]+(255,))
    for k in range(3): d.arc(s(900+k*60,300-k*40,1000+k*90,400-k*20),200,340,fill=A(DARK),width=8*S)
    LF(d)
go('child-snoring',*SKY,f)
def f(im,d):  # hyperthyroidism
    d.ellipse(s(560,300,800,560),fill=A(RED,220)); d.ellipse(s(800,300,1040,560),fill=A(RED,220)); rr(d,770,380,830,480,20,fill=A(DARK))
    spark(d,800,220,80,A(AC)); LF(d)
go('hyperthyroidism',*ROSE,f)
def f(im,d):  # edema
    rr(d,700,200,840,720,70,fill=A(BONE2)); d.ellipse(s(660,560,880,760),fill=A(BONE2))
    for x,y,r in [(980,300,40),(1040,450,30),(950,560,24)]: drop(d,x,y,r,A(BL,240))
    LF(d)
go('edema',*SKY,f)
def f(im,d):  # tonic-herbs
    d.chord(s(560,380,1040,700),0,180,fill=A((150,90,60)))
    rr(d,560,500,1040,540,10,fill=A((150,90,60)))
    for k in range(3): ln(d,[(700+k*100,470),(680+k*100,400),(710+k*100,330),(690+k*100,260)],A((255,255,255),210),8)
    for x,y in [(1120,620),(480,640)]: d.ellipse(s(x-50,y-25,x+50,y+25),fill=A(BONE2))
    LF(d)
go('tonic-herbs',*SAND,f)
def f(im,d):  # adenomyosis
    d.polygon(s(700,300,900,300,860,560,740,560),fill=A(RED,210)); circ(d,800,330,100,fill=A(RED,210))
    ln(d,[(700,320),(600,280),(560,330)],A(RED,210),18); ln(d,[(900,320),(1000,280),(1040,330)],A(RED,210),18)
    for x,y in [(770,400),(830,430),(790,480),(820,370)]: circ(d,x,y,12,fill=A(DARK))
    LF(d)
go('adenomyosis',*ROSE,f)
def f(im,d):  # accident-headache
    circ(d,800,440,150,fill=A(BONE2))
    for k in range(4): d.arc(s(560-k*30,200-k*30,1040+k*30,680+k*30),200+k*20,300+k*20,fill=A(RED,200-k*30),width=8*S)
    spark(d,900,360,60,A(AC)); LF(d)
go('accident-headache',*PEACH,f)
def f(im,d):  # accident-insomnia
    circ(d,560,300,90,fill=A((236,220,170))); circ(d,600,270,80,fill=NIGHT[0]+(255,))
    eyeball(d,880,470,170,80,A((236,220,170)))
    for x,y in [(300,200),(1300,180),(1200,320),(400,620)]: circ(d,x,y,5,fill=A((255,255,255)))
    LF(d)
go('accident-insomnia',*NIGHT,f)
def f(im,d):  # spring-fatigue
    d.chord(s(950,350,1250,650),180,360,fill=A(AC,220))
    for x,y,r in [(560,330,60),(720,480,46),(600,620,38)]: petal5(d,x,y,r,A((240,170,180)))
    LF(d)
go('spring-fatigue',*MINT,f)
def f(im,d):  # seasonal-cold
    for x,y,a in [(560,300,-20),(700,420,30),(520,560,60)]: leaf(d,x,y,140,52,a,A((214,150,90)))
    ln(d,[(820,380),(960,420),(1080,380),(1200,420)],A(RED,230),40); ln(d,[(1080,400),(1110,560)],A(RED,230),36)
    LF(d)
go('seasonal-cold',*SAND,f)
print('ok')
