# 원장님 블로그 공지 두 편(2026-08-24 진료과목 소개, 08-25 만성통증 진료 안내)의 진료 방식을 칼럼에 반영한다. 여러 번 실행해도 한 번만 들어감.
# 1) 모든 칼럼 한약 항목: 원장 직접 탕전 + 10일분 처방
# 2) 근골격계 칼럼(약침·초음파 가이드 약침): 겉(약침·추나)과 속(체질 한약)을 함께 치료
# 3) 디스크·협착증 칼럼: 수술 권유를 받았어도 심한 마비·대소변 장애가 없으면 비수술 치료로 증상 관리
import re
from _common import column_slugs, read, write, touch, touch_sitemap
HERB=' 한약은 원장이 원내 탕전실에서 약재 선별부터 달이는 과정까지 직접 관리하며, 10일분씩 처방해 복용 경과를 보고 약재 구성과 양을 조절합니다.'
GUTSOK=' 아픈 자리는 초음파 가이드 약침과 추나로 다스리고, 통증이 오래가게 만드는 몸속의 기혈 순환과 장부 기능은 체질에 맞춘 한약으로 함께 살피면 통증 완화와 재발 관리를 함께 도모할 수 있습니다.'
SURG=' 디스크나 협착증으로 수술을 권유받았더라도 다리 힘이 크게 빠지는 마비나 대소변 장애가 없다면, 초음파 가이드 약침과 추나 같은 비수술 치료로 증상 완화와 통증 관리를 먼저 해 볼 수 있습니다.'
SURG_SLUGS={'lumbar-disc','spinal-stenosis','neck-disc','sciatica'}
changed=[]
for slug in column_slugs():
    s=read(slug); o=s
    i=s.index('<h2 id="treat"'); j=s.index('<h2',i+5); sec=s[i:j]
    m=re.search(r'(<h3>\d\. [^<]*한약[^<]*</h3>\s*<p>.*?)(</p>)',sec,re.S)
    add=''
    if HERB.strip() not in sec: add+=HERB
    if '초음파 가이드 약침' in sec and GUTSOK.strip() not in sec: add+=GUTSOK
    if add: sec=sec[:m.end(1)]+add+sec[m.end(1):]
    if slug in SURG_SLUGS and SURG.strip() not in sec:
        k=re.search(r'(<h3>\d\. [^<]*약침[^<]*</h3>\s*<p>.*?)(</p>)',sec,re.S)
        sec=sec[:k.end(1)]+SURG+sec[k.end(1):]
    s=s[:i]+sec+s[j:]
    if s!=o: write(slug,touch(s)); changed.append(slug)
touch_sitemap(changed); print(len(changed),'편 수정')
