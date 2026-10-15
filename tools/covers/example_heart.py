# 표지 예시 (서맥·빈맥·흉통 표지를 그린 코드). 새 표지는 이 파일을 복사해 slug와 그림만 바꿔 실행한다.
# 실행하면 images/col-<slug>.jpg가 덮어써지므로 slug를 꼭 바꾸세요.
import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from covers_lib import *
def ecg(segs,x=120,y0=520):
    pts=[(x,y0)]
    for dx,dy in segs: x+=dx; pts.append((x,pts[-1][1]+dy))
    return pts
BEAT=lambda k=1:[(14*k,-30),(14*k,100),(16*k,-130),(14*k,60)]
def bradycardia(im,d):
    heartf(d,800,400,12,A((214,110,100),190))
    ln(d,ecg([(330,0)]+BEAT(1.3)+[(560,0)]+BEAT(1.3)+[(400,0)]),A((170,80,70)),8)
    leaf(d,1320,730,160,60,-30,A(G))
def chest_pain(im,d):
    for k in range(4): d.arc(s(470-k*10,250+k*70,1130+k*10,830+k*70),205,335,fill=A((196,150,140)),width=16*S)
    ln(d,[(800,240),(800,620)],A((196,150,140)),16)
    heartf(d,860,420,7,A((214,110,100),220)); spark(d,860,420,120,A(AC,170))
    leaf(d,1320,730,160,60,-30,A(G))
if __name__=='__main__':
    slug=sys.argv[1] if len(sys.argv)>1 else 'example-test'
    go(slug,*SKY,bradycardia); print('saved images/col-'+slug+'.jpg')
