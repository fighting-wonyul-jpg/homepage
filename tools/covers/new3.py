# 2026-10-16 추가 3편 표지 (백반증, 결절성 양진, 미각장애)
import os,sys,math; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from covers_lib import *
SKIN=(232,196,170); SKIN2=(214,172,146); DARK=(170,80,70)
def LF(d): leaf(d,1320,730,160,60,-30,A(G))
def f(im,d):  # vitiligo: 피부 바탕 위 하얀 반점
    rr(d,460,220,1140,680,80,fill=A(SKIN))
    for x,y,rx,ry in [(640,380,90,64),(700,420,60,70),(900,520,110,70),(960,480,70,60),(1010,330,50,40)]:
        d.ellipse(s(x-rx,y-ry,x+rx,y+ry),fill=A((252,250,246)))
    LF(d)
go('vitiligo',*PEACH,f)
def f(im,d):  # prurigo-nodularis: 피부 바탕 위 작고 둥근 돌기
    rr(d,460,220,1140,680,80,fill=A(SKIN))
    for x,y,r in [(600,360,34),(720,470,40),(860,350,30),(940,540,38),(1040,420,32),(650,580,28),(820,600,26)]:
        circ(d,x,y+6,r,fill=A(SKIN2)); circ(d,x,y,r,fill=A(RED,220)); circ(d,x-r*0.3,y-r*0.3,r*0.28,fill=A((240,170,150),200))
    LF(d)
go('prurigo-nodularis',*ROSE,f)
def f(im,d):  # taste-disorder: 혀 모양과 숟가락
    d.chord(s(520,180,880,820),0,180,fill=A(PINK)); rr(d,520,360,880,560,60,fill=A(PINK))
    ln(d,[(700,400),(700,680)],A((200,120,140)),8)
    for x,y in [(610,520),(790,520),(640,620),(760,620),(700,740)]: circ(d,x,y,14,fill=A((240,190,200)))
    d.ellipse(s(960,200,1100,380),fill=A((205,210,214))); rr(d,1012,370,1048,720,18,fill=A((205,210,214)))
    LF(d)
go('taste-disorder',*SAND,f)
print('ok')
