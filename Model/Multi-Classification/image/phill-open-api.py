import requests
import pprint
import json
import pandas as pd
from pandas.io.json import json_normalize
from sqlalchemy import create_engine  # pip install mysqlclient
# import pymysql
import csv

db_id = 'localhost'
ip_address = 'localhost'
db_name = 'phill'

# conn = pymysql.connect(host = db_id, user='root', password= 'password', charset='utf8')
# cursor = conn.cursor()


encoding_key = 'MmmzicJJXJfMkt94kIq6wUWcaWGyCvmw2BErd7dB1nJq53N%2BqOOIkA6lYMY6uiHLnMyJYmvf86t%2BlSwuP3E84w%3D%3D'
file_types = 'json' # xml 원할 시 변경

'''
가지고 올 수 있는 아이템 정보들
item_name : 품목명
entp_name : 업체명
item_seq : 품목일련번호
img_regist_ts : 약학정보원 이미지 생성일
pageNo : 페이지번호
numOfRows : 한 페이지 결과 수
edi_code : 보험코드
serviceKey : 공공데이터포털에서 발급받은 인증기
type : json 또는 xml
'''
# pp = pprint.PrettyPrinter(indent=4) # 깔끔한 상태의 프린트
# print(pp.pprint(response.text))
def phill_info():
    f = open('phill_info.csv', 'w')
    csv_phill = csv.writer(f)
    csv_phill.writerow(['ITEM_NAME','ENTP_NAME','ITEM_IMAGE','PRINT_FRONT','PRINT_BACK','DRUG_SHAPE','COLOR_CLASS1','COLOR_CLASS1','CLASS_NAME','ETC_OTC_NAME'])
    # url = f'https://apis.data.go.kr/1471000/MdcinGrnIdntfcInfoService01/getMdcinGrnIdntfcInfoList01?serviceKey={encoding_key}&pageNo={i}&numOfRows=5&type={file_types}'
    # response = requests.get(url, verify=False)
    # json_ob = json.loads(response.text) # 문자열을 딕셔너리로 변경해준다. 이때 json으로 변경하여 type을 찍어주면 dict라고 나온다.
    # total_count = json_ob['body']['totalCount'] # 필요한 내용만 골라오기

    ''' 
    확인결과 : 해당 api에서 제공하는 알약의 수는 24644개
    그러므로 5개씩 4929번 돌리면 24645개 확인이 가능하다.
    json에 totalCount라는 값에 저장이 되어있는데 해당 값을 불러오려면 api를 사용해야하는데 이렇게 되면 가끔 공공데이터포털에서 같은 주소를 다수 접속해서 트래픽과다로 막히는 경우가 있다.
    '''

    for i in range(1, 4929):
        url = f'https://apis.data.go.kr/1471000/MdcinGrnIdntfcInfoService01/getMdcinGrnIdntfcInfoList01?serviceKey={encoding_key}&pageNo={i}&numOfRows=5&type={file_types}'
        response = requests.get(url, verify=False)
        json_ob = json.loads(response.text) # 문자열을 딕셔너리로 변경해준다. 이때 json으로 변경하여 type을 찍어주면 dict라고 나온다.
        items = json_ob['body']['items'] # 필요한 내용만 골라오기
        df = json_normalize(items)
        for j in range(5):
            try:
                csv_phill.writerow([df['ITEM_NAME'][j], df['ENTP_NAME'][j], df['ITEM_IMAGE'][j], df['PRINT_FRONT'][j], df['PRINT_BACK'][j], df['DRUG_SHAPE'][j],
                df['COLOR_CLASS1'][j], df['COLOR_CLASS2'][j], df['CLASS_NAME'][j], df['ETC_OTC_NAME'][j]])
            except: pass # 25645번째는 존재하지 않으으로 사용하지 않는다.
phill_info()
# 총 소요시간 37분 30.4초