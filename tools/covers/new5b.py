# 2026-10-16 추가 표지 (척추 수술 후 통증, 인공관절 수술 후 회복, 골절 후 회복)
import os,sys,math; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from covers_lib import *
BONE=(236,224,206); BONE2=(222,206,184); METAL=(176,186,196); METAL2=(140,152,164)
def LF(d): leaf(d,1320,730,160,60,-30,A(G))
def f(im,d):  # post-spine-surgery: 척추뼈 기둥과 고정 나사·막대
    for i in range(5):
        rr(d,680,170+i*115,920,255+i*115,26,fill=A(BONE))
        if i<4: rr(d,700,255+i*115,900,285+i*115,12,fill=A(BONE2))
    for i in (2,3):
        circ(d,660,212+i*115,16,fill=A(METAL2)); circ(d,940,212+i*115,16,fill=A(METAL2))
    ln(d,[(660,442),(660,557)],A(METAL),12); ln(d,[(940,442),(940,557)],A(METAL),12)
    spark(d,1080,330,85,A(AC)); LF(d)
go('post-spine-surgery',*SAND,f)
def f(im,d):  # joint-replacement-rehab: 넙다리뼈·정강이뼈와 금속 인공관절
    rr(d,720,120,880,400,60,fill=A(BONE)); rr(d,730,520,870,800,55,fill=A(BONE))
    d.chord(s(660,320,940,500),0,180,fill=A(METAL)); rr(d,670,468,930,520,18,fill=A(METAL2))
    rr(d,690,430,910,470,14,fill=A((250,250,250)))
    d.arc(s(540,260,1060,780),300,20,fill=A(AC),width=14*S); spark(d,560,380,70,A(AC)); LF(d)
go('joint-replacement-rehab',*MINT,f)
def f(im,d):  # fracture-recovery: 금이 갔다가 붙은 뼈와 깁스 붕대
    a=math.radians(-28); cx,cy=800,450
    def P(x,y): return (cx+x*math.cos(a)-y*math.sin(a),cy+x*math.sin(a)+y*math.cos(a))
    def poly(pts,col): d.polygon([(X*S,Y*S) for X,Y in [P(x,y) for x,y in pts]],fill=col)
    poly([(-330,-45),(330,-45),(330,45),(-330,45)],A(BONE))
    for x in (-330,330):
        X,Y=P(x,-40); circ(d,X,Y,58,fill=A(BONE)); X,Y=P(x,40); circ(d,X,Y,58,fill=A(BONE))
    poly([(-120,-75),(120,-75),(120,75),(-120,75)],A((250,250,250)))
    for k in range(-100,101,40): ln(d,[P(k,-75),P(k+22,75)],A((214,222,228)),6)
    ln(d,[P(-150,-45),P(-135,-10),P(-160,10),P(-140,45)],A(RED,220),8)
    spark(d,560,280,80,A(AC)); LF(d)
go('fracture-recovery',*SKY,f)
print('ok')
