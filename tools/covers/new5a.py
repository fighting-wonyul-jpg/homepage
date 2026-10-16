# 2026-10-16 추가 표지 (천식, 노인성 가려움)
import os,sys,math; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from covers_lib import *
SKIN=(232,196,170); SKIN2=(206,166,140)
def LF(d): leaf(d,1320,730,160,60,-30,A(G))
def f(im,d):  # asthma: 기관지 나무 모양, 찬 바람 줄, 미세먼지 점
    TR=(214,120,120)
    ln(d,[(800,150),(800,400)],A(TR),46)
    def br(x,y,ang,L,w,n):
        if n==0: circ(d,x,y,w*0.9,fill=A((236,160,160))); return
        x2,y2=x+math.cos(math.radians(ang))*L,y+math.sin(math.radians(ang))*L
        ln(d,[(x,y),(x2,y2)],A(TR),w)
        br(x2,y2,ang-28,L*0.72,w*0.68,n-1); br(x2,y2,ang+28,L*0.72,w*0.68,n-1)
    br(800,400,140,170,36,4); br(800,400,40,170,36,4)
    for y,x0,x1 in [(230,180,470),(300,230,520),(370,160,430)]:
        ln(d,[(x0,y),((x0+x1)/2,y-18),(x1,y)],A(BL,230),12)
    for x,y,r in [(1150,230,12),(1220,300,9),(1290,210,14),(1180,380,8),(1340,330,11),(1260,440,9),(1390,250,7)]:
        circ(d,x,y,r,fill=A((150,150,160),200))
    LF(d)
go('asthma',*SKY,f)
def f(im,d):  # elderly-itch: 갈라진 마른 피부결, 물방울, 보습 크림 통
    rr(d,380,230,1000,690,70,fill=A(SKIN))
    for pts in [[(450,330),(560,380),(640,350),(760,420),(900,380)],[(430,500),(540,470),(660,540),(800,500),(960,560)],
                [(560,380),(600,470)],[(760,420),(720,520)],[(660,540),(690,640)],[(640,350),(620,260)]]:
        ln(d,pts,A(SKIN2),7)
    for x,y,r in [(1100,270,34),(1180,360,26),(1080,420,22)]:
        drop(d,x,y,r,A(BL,235))
    rr(d,1070,520,1270,640,24,fill=A(WH)); rr(d,1055,480,1285,540,20,fill=A(AC))
    LF(d)
go('elderly-itch',*PEACH,f)
print('ok')
