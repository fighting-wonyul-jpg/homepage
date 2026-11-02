# 2026-11-02 장폐색 표지: 구불구불한 장 관과 막힌 자리(조이는 띠), 경고 삼각형
import os,sys,math; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from covers_lib import *
TUBE=(226,150,150); TUBE2=(240,190,186); PALE=(236,206,200)
def path(ctrl,n=60):  # 점들을 부드러운 곡선(Catmull-Rom)으로 촘촘히
    P=[ctrl[0]]+ctrl+[ctrl[-1]]; out=[]
    for k in range(1,len(P)-2):
        p0,p1,p2,p3=P[k-1],P[k],P[k+1],P[k+2]
        for t in [i/n for i in range(n)]:
            out.append(tuple(0.5*((2*p1[c])+(-p0[c]+p2[c])*t+(2*p0[c]-5*p1[c]+4*p2[c]-p3[c])*t*t+(-p0[c]+3*p1[c]-3*p2[c]+p3[c])*t**3) for c in (0,1)))
    return out+[ctrl[-1]]
def tube(d,pts,r,c1,c2):
    for x,y in pts: circ(d,x,y,r,fill=A(c1,255))
    for x,y in pts: circ(d,x-r*0.15,y-r*0.25,r*0.42,fill=A(c2,255))
def f(im,d):
    # 막히기 전: 부풀어 굵은 장 (구불구불)
    a=path([(360,260),(560,200),(760,270),(720,380),(520,420),(480,520),(620,600),(760,610)])
    tube(d,a,48,TUBE,TUBE2)
    # 막힌 뒤: 가늘고 옅은 장
    b=path([(800,612),(930,600),(1030,530),(1120,450)])
    tube(d,b,18,PALE,(246,224,220))
    # 막힌 자리: 조이는 띠
    rr(d,768,552,814,672,14,fill=A(RED,255))
    # 경고 삼각형
    d.polygon(s(1130,150,1240,340,1020,340),fill=A(AC))
    rr(d,1121,205,1139,285,8,fill=A(WH)); circ(d,1130,310,11,fill=A(WH))
    leaf(d,1320,730,160,60,-30,A(G))
go('bowel-obstruction',*PEACH,f)
print('ok')
