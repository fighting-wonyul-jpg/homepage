# 2026-10-16 추가 표지 (근육 파열, 복합부위통증증후군)
import os,sys,math; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from covers_lib import *
MUS=(222,140,128); MUS2=(200,112,102); BONE2=(222,206,184)
def LF(d): leaf(d,1320,730,160,60,-30,A(G))
def f(im,d):  # muscle-strain: 근육 섬유 다발 가운데가 갈라진 모습과 얼음 주머니
    for i in range(7):
        y=300+i*45; w=1-abs(i-3)/5
        ln(d,[(470,450+(y-435)*0.35),(600,y),(745,y+(8 if i%2 else -8))],A(MUS if i%2 else MUS2),30)
        ln(d,[(805,y+(-8 if i%2 else 8)),(950,y),(1080,450+(y-435)*0.35)],A(MUS if i%2 else MUS2),30)
    ln(d,[(775,270),(755,340),(790,410),(760,480),(795,560),(770,620)],A(RED,230),10)
    rr(d,1040,170,1260,330,40,fill=A(BL,235))
    for x,y in [(1090,220),(1160,250),(1210,210)]: rr(d,x-22,y-22,x+22,y+22,8,fill=A(WH,220))
    LF(d)
go('muscle-strain',*PEACH,f)
def f(im,d):  # crps: 한 점에서 번져 나가는 통증 물결과 부드러운 깃털
    cx,cy=720,450
    circ(d,cx,cy,46,fill=A(RED,235))
    for k in range(1,5):
        r=80+k*70; pts=[]
        for t in range(0,361,4):
            a=math.radians(t); rr_=r+10*math.sin(a*8)
            pts.append((cx+math.cos(a)*rr_,cy+math.sin(a)*rr_*0.82))
        ln(d,pts,A(RED if k<3 else AC,220-k*35),9)
    leaf(d,1260,300,280,90,-55,A((248,238,228)),A(BONE2))
    for i in range(6):
        t=i/6-0.4; x=1260+150*t*math.cos(math.radians(-55)); y=300+150*t*math.sin(math.radians(-55))
        ln(d,[(x,y),(x+34,y+24)],A(BONE2),4); ln(d,[(x,y),(x-34,y-24)],A(BONE2),4)
    LF(d)
go('crps',*ROSE,f)
print('ok')
