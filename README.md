# Phil-Detector
![phill](https://user-images.githubusercontent.com/75519839/180497994-7c88000d-e89e-443f-bc6c-80237a3e7218.png)<br>
[사진 출처 : Urbanbrush 무료 이미지](https://www.urbanbrush.net/)


수집한 알약 정보를 기반으로 알약의 제형 또는 용도 분류후 검출 모델 제작 및 서비스 구현

***
### Install
<pre><code>pip install -r requirements.txt</code></pre>
해당 파일은 Python 3.8 버젼에서 제작되었습니다. 🧐
***

## Workflow
- 현재 진행중인 부분은 **진한 색**으로 표시

문제 제기(가설 수립) -> 주제 설정 -> 데이터 수집 -> 데이터 적재 -> **데이터 분석** -> 모델링 -> 모델 최적화 -> 가설 검정 및 결과 도출 -> 서비스 구현
    
    *잠정 중단 라벨링 작업 중 예상 최소 소요 기간 1달 이상*


1. 문제 제기 및 가설 수립
    - 문제 제기 : 필자의 경우 시골에서 자라서 약사가 처방해준 약들이 봉지에 설명이 되어있지않아 무슨 종류의 약인지 궁금해도 확인할 방법이 없었음
    - 가설 제기 : 알약 사진으로 내가 받은 약의 종류 또는 용도를 알 수 있을까?

2. 주제 설정
    - 딥러닝을 통한 알약 이미지 분석 서비스

3. 데이터 수집
    - 셀레니움 데이터 크롤링 : [데이터 수집 출처 : 약학정보원](https://www.health.kr/searchIdentity/search.asp)<br>
    - OPEN API : [데이터 수집 출처 : 식품의약품안전처, 공공데이터포털](https://www.data.go.kr/index.do)

4. 데이터 적재
    - mysql
    - csv
    - jpg

5. 데이터 분석
    - *현재 구현중*

6. 모델링
    - *데이터 분석과 동시에 진행 중*
    - *분류 모델을 사용할 예정*
    - *1차 사전학습 모델을 통해 간단한 프로토 타입 모델 구현 후 직접 커스텀하여 전용 모델을 만들 예정*
    

    
### 데이터 수집 조건

- 약학정보원 식별 정보 조건


1. 식별문자 여부
2. 식별마크 여부
3. 회사명 또는 제품명, 성분명
4. 알약의 제형
    - 정제형
    - 경질캡슐형
    - 연질캡슐형
    - 기타

5. 알약의 모양
    - 원형
    - 타원형
    - 장방형
    - 반원형
    - 삼각형
    - 사각형
    - 마름모형
    - 오각형
    - 육각형
    - 팔각형
    - 기타

6. 색상
    - 하양
    - 노랑
    - 주황
    - 분홍
    - 빨강
    - 갈색
    - 연두
    - 초록
    - 청록
    - 파랑
    - 남색
    - 자주
    - 보라
    - 회색
    - 검정
    - 투명
  
7. 분할선
    - 없음
    - (+) 형
    - (-) 형
    - 기타
---

### 셀리니움 데이터 수집 항목

- phill_name
    - 알약 제품명

- phill_ingredient
    - 알약 성분

- identification_mark
    - 식별 문자

- phill_type
    - 알약 제형

- phill_size
    - 알약 크기

- compony
    - 제조사


### OPEN API 데이터 수집 항목

- ITEM_NAME
    - 제품명
- ENTP_NAME
    - 회사명
- ITEM_IMAGE
    - 이미지 정보
- PRINT_FRONT
    - 프린트 내역
- PRINT_BACK
    - 프린트 내역
- DRUG_SHAPE
    - 약의 방향
- COLOR_CLASS1
    - 약 색상
- COLOR_CLASS1
    - 약 색상 2
- CLASS_NAME
    - 약의 종류
- ETC_OTC_NAME
    - 전문의약품인지 여부

### 이미지 수집 현황

- 24589개 항목
- 파일용량 2.31GB
- 약의 형태를 기준으로 이름 지정하여 다운로드

---
### 관련 참고 논문
- [알약 자동 인식을 위한 딥러닝 모델간 비교 및 검증](https://koreascience.kr/article/JAKO201913747257285.pdf)
- [딥러닝을 활용한 알약 분석 어플리케이션](https://manuscriptlink-society-file.s3-ap-northeast-1.amazonaws.com/kips/conference/2020fall/presentation/KIPS_C2020B0152.pdf)

### 관련 참고 코드
- [Simple image Search Engine](https://github.com/matsui528/sis)
