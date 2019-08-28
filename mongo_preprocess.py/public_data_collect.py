"""
title: public data collect (weather, air-polution)
author: jason
description:
 -테스트 목적 -> 수집할 세부 항목 정리 필요, 서비스용 토큰 발급 필요

 -날씨는 일 1000회 호출로 제한 -> 날씨는 90초당 1회씩, 미세먼지는 180초 (500회 제한)
 -mongodb: 
   > public_data_weather: 날씨 정보
   > public_data_polution: 미세먼지 (xml) -> 제거 예정
   > public_data_polution2: 미세먼지 (json) -> 상세 내역 포함

2019-05-27
(60*126)
서울특별시	서초구	잠원동	

"""
# -----------------------------------------
# import
import pprint

import requests
import json
# import xml
import xmltodict
import pymongo
# import datetime
import time
from datetime import datetime, timedelta

# -----------------------------------------
# 변수 설정

# 동네예보조회
END_POINT_WEATHER_ForecastSpaceData = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData"
END_POINT_WEATHER_ForecastSpaceData += "?serviceKey={0}&base_date={1}&base_time={2}&nx={3}&ny={4}&numOfRows={5}&_type={6}"

# 초단기예보조회 -가장가까운 미래
END_POINT_WEATHER_ForecastTimeData = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"
END_POINT_WEATHER_ForecastTimeData += "?serviceKey={0}&base_date={1}&base_time={2}&nx={3}&ny={4}&numOfRows={5}&pageNo={6}&_type={7}"

# 초단기실황조회 -현재(10분~30분 이전)
END_POINT_WEATHER_ForecastGrib = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib"
END_POINT_WEATHER_ForecastGrib += "?serviceKey={0}&base_date={1}&base_time={2}&nx={3}&ny={4}&numOfRows={5}&pageNo={6}&_type={7}"

END_POINT_POLUTION = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst"
END_POINT_POLUTION += "?ServiceKey={0}&numOfRows={1}&pageNo={2}&sidoName={3}&searchCondition={4}"

END_POINT_POLUTION2 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst"
END_POINT_POLUTION2 += "?ServiceKey={0}&numOfRows={1}&pageNo={2}&sidoName={3}&searchCondition={4}&_returnType={5}"

SERVICE_KEY = "Jb%2B9qwrwKf6M%2BPNjG%2BtHAB%2B4uIlwXlGYByUeumT%2FLnIqg2ezSvqPWxhv4Dt%2BUZiggpGYKoDp8ZpmcXwNiLGlaQ%3D%3D"
NUMBER_OF_ROWS = 999
PAGE_NO = 1
SEARCH_CONDITION = 'DAILY'
RESULT_TYPE = 'json'

SIDO_NAME = [
    {"sidoName": "서울", "sidoCode": 11}
    # , {"sidoName": "부산", "sidoCode": 21}
    # , {"sidoName": "대구", "sidoCode": 22}
    # , {"sidoName": "인천", "sidoCode": 23}
    # , {"sidoName": "광주", "sidoCode": 24}
    # , {"sidoName": "대전", "sidoCode": 25}
    # , {"sidoName": "울산", "sidoCode": 26}
    # , {"sidoName": "세종특별자치시", "sidoCode": 29}
    # , {"sidoName": "경기도", "sidoCode": 31}
    # , {"sidoName": "강원도", "sidoCode": 32}
    # , {"sidoName": "충청북도", "sidoCode": 33}
    # , {"sidoName": "충청남도", "sidoCode": 34}
    # , {"sidoName": "전라북도", "sidoCode": 35}
    # , {"sidoName": "전라남도", "sidoCode": 36}
    # , {"sidoName": "경상북도", "sidoCode": 37}
    # , {"sidoName": "경상남도", "sidoCode": 38}
    # , {"sidoName": "제주도", "sidoCode": 39}
    ]

# (60*126)
# 서울특별시	서초구	잠원동	
# NXY = {"NX": 60, "NY": 126}
LOCATION_INFO = {'nx':60, 'ny':126, 'sido':'서울특별시', 'sido2':'서초구', 'dong':'잠원동'}
# 날씨 2번 당 1회 가져오기 설정
POLLUTION_CALL_FLAG = False

# ----------------------------------------------------------
# get public data -weather
def getPublicDataWeather_ForecastSpaceData():
    now = datetime.now() + timedelta(minutes=-30)
    # now = datetime.now() + timedelta(minutes=-40)
    # now = datetime.now() + timedelta(hours = -1)
    # dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dt = now.strftime("%Y%m%d")
    # tm = now.strftime("%H00") # 정시 단위, 매시각 40분 이후 호출할 것
    tm = now.strftime("%H%M")

    reqUrl = END_POINT_WEATHER_ForecastSpaceData.format(
        SERVICE_KEY, # service key
        dt, # base_date
        tm, # base_time
        LOCATION_INFO['nx'], # nx
        LOCATION_INFO['ny'], # ny
        NUMBER_OF_ROWS, # numOfRows
        RESULT_TYPE # _type
        )
    print ("request url: %s" % reqUrl)
    r = requests.get(url = reqUrl, params={})
    print ("status: {0}, header: {1}, encoding: {2}".format(r.status_code, r.headers, r.encoding))

    plainData = r.text
    resultData = json.loads(plainData)
    header = resultData["response"]["header"]
    print ("Method=%s^dt=%s^tm=%s^resultCode=%s^resultMessage=%s" % ("getPublicDataWeather", dt, tm, header["resultCode"], header["resultMsg"]))
    print ("resultCode=%s, resultMessage=%s" % (header["resultCode"], header["resultMsg"]))
    if header["resultCode"] == "22":
        return

    bodyData = resultData["response"]["body"]
    items = []
    if not (bodyData["items"] == None or bodyData["items"] == ''):
       items = bodyData["items"]["item"]
    # print ("result: %s items" % str(bodyData["totalCount"]))

    """
    data = {
        "uumOfRows": bodyData["numOfRows"], 
        "totalCount": bodyData["totalCount"],
        "payload": items
        }
    """
    # curDt = datetime.now()
    curDt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("getPublicDataWeather_ForecastSpaceData----------------")
    data = []
    # firstFcstDate = ''
    # firstFcstTime = ''
    for item in items:
        if item['fcstValue'] == '-':
            continue

        item["dt"] = curDt
        item["sido"] = LOCATION_INFO['sido']
        item["sido2"] = LOCATION_INFO['sido2']
        item["dong"] = LOCATION_INFO['dong']

        data.append(item)
        # end if
    if len(data) > 0:
        mongoUpdate("public_data_weather_ForecastSpaceData", data)

# ----------------------------------------------------------
# get public data -weather ForecastTimeData
def getPublicDataWeather_ForecastTimeData():
    now = datetime.now() + timedelta(minutes=-30)
    # now = datetime.now() + timedelta(minutes=-40)
    # now = datetime.now() + timedelta(hours = -1)
    # dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dt = now.strftime("%Y%m%d")
    tm = now.strftime("%H%M") # 정시 단위, 매시각 40분 이후 호출할 것

    reqUrl = END_POINT_WEATHER_ForecastTimeData.format(
        SERVICE_KEY, # service key
        dt, # base_date
        tm, # base_time
        LOCATION_INFO['nx'], # nx
        LOCATION_INFO['ny'], # ny
        NUMBER_OF_ROWS, # numOfRows
        PAGE_NO,
        RESULT_TYPE # _type
        )
    print ("request url: %s" % reqUrl)
    r = requests.get(url = reqUrl, params={})
    print ("status: {0}, header: {1}, encoding: {2}".format(r.status_code, r.headers, r.encoding))

    plainData = r.text
    resultData = json.loads(plainData)
    header = resultData["response"]["header"]
    print ("Method=%s^dt=%s^tm=%s^resultCode=%s^resultMessage=%s" % ("getPublicDataWeather", dt, tm, header["resultCode"], header["resultMsg"]))
    print ("resultCode=%s, resultMessage=%s" % (header["resultCode"], header["resultMsg"]))
    if header["resultCode"] == "22":
        return

    bodyData = resultData["response"]["body"]
    items = []
    if not (bodyData["items"] == None or bodyData["items"] == ''):
       items = bodyData["items"]["item"]
    # print ("result: %s items" % str(bodyData["totalCount"]))

    """
    data = {
        "uumOfRows": bodyData["numOfRows"], 
        "totalCount": bodyData["totalCount"],
        "payload": items
        }
    """
    # curDt = datetime.now()
    curDt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = []
    for item in items:
        if item['fcstValue'] == '-':
            continue

        item["dt"] = curDt
        item["sido"] = LOCATION_INFO['sido']
        item["sido2"] = LOCATION_INFO['sido2']
        item["dong"] = LOCATION_INFO['dong']

        data.append(item)
        # end if
    if len(data) > 0:
        mongoUpdate("public_data_weather_ForecastTimeData", data)


# ----------------------------------------------------------
# get public data -weather ForecastGrib
def getPublicDataWeather_ForecastGrib():
    now = datetime.now() + timedelta(minutes=-30)
    # now = datetime.now() + timedelta(minutes=-40)
    # now = datetime.now() + timedelta(hours = -1)
    # dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dt = now.strftime("%Y%m%d")
    # tm = now.strftime("%H00") # 정시 단위, 매시각 40분 이후 호출할 것
    tm = now.strftime("%H%M") # 정시 단위, 매시각 40분 이후 호출할 것

    reqUrl = END_POINT_WEATHER_ForecastGrib.format(
        SERVICE_KEY, # service key
        dt, # base_date
        tm, # base_time
        LOCATION_INFO['nx'], # nx
        LOCATION_INFO['ny'], # ny
        NUMBER_OF_ROWS, # numOfRows
        PAGE_NO,
        RESULT_TYPE # _type
        )
    print ("request url: %s" % reqUrl)
    r = requests.get(url = reqUrl, params={})
    print ("status: {0}, header: {1}, encoding: {2}".format(r.status_code, r.headers, r.encoding))

    plainData = r.text
    resultData = json.loads(plainData)
    header = resultData["response"]["header"]
    print ("Method=%s^dt=%s^tm=%s^resultCode=%s^resultMessage=%s" % ("getPublicDataWeather", dt, tm, header["resultCode"], header["resultMsg"]))
    print ("resultCode=%s, resultMessage=%s" % (header["resultCode"], header["resultMsg"]))
    if header["resultCode"] == "22":
        return

    bodyData = resultData["response"]["body"]
    items = []
    if not (bodyData["items"] == None or bodyData["items"] == ''):
       items = bodyData["items"]["item"]
    # print ("result: %s items" % str(bodyData["totalCount"]))

    """
    data = {
        "uumOfRows": bodyData["numOfRows"], 
        "totalCount": bodyData["totalCount"],
        "payload": items
        }
    """
    # curDt = datetime.now()
    curDt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = []
    for item in items:
        if item['obsrValue'] == '-':
            continue

        item["dt"] = curDt
        item["sido"] = LOCATION_INFO['sido']
        item["sido2"] = LOCATION_INFO['sido2']
        item["dong"] = LOCATION_INFO['dong']

        data.append(item)
        # end if
    if len(data) > 0:
        mongoUpdate("public_data_weather_ForecastGrib", data)



# ----------------------------------------------------------
# get public data -polution
def getPublicDataPolution(sidoName):
    # sidoName = SIDO_NAME[0]["sidoName"]
    reqUrl = END_POINT_POLUTION.format(
        SERVICE_KEY, # service key
        NUMBER_OF_ROWS, # numOfRows
        PAGE_NO, # pageNo
        sidoName, # sidoName
        SEARCH_CONDITION # searchCondition
        )

    print ("request url: %s" % reqUrl)
    r = requests.get(url = reqUrl, params={})
    print ("status: {0}, header: {1}, encoding: {2}".format(r.status_code, r.headers, r.encoding))

    plainData = r.text
    resultData = xmltodict.parse(plainData)
    header = resultData["response"]["header"]
    print ("Method=%s^sido=%s^resultCode=%s^resultMessage=%s" % ("getPublicDataPolution", sidoName, header["resultCode"], header["resultMsg"]))
    if header["resultCode"] == "22":
        return
    # # resultData = json.loads(plainData)
    # # resultData = json.dumps(xmlData)

    bodyData = resultData["response"]["body"]
    items = []
    if not (bodyData["items"] == None or bodyData["items"] == ''):
       items = bodyData["items"]["item"]
    # print ("result: %s items" % str(bodyData["totalCount"]))

    """
    data = {
        "uumOfRows": bodyData["numOfRows"], 
        "totalCount": bodyData["totalCount"],
        "payload": items
        }
    """
    # curDt = datetime.now()
    print("getPublicDataPolution-------------------------------")
    data = []
    curDt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for item in items:
        if item['cityName'] == LOCATION_INFO['sido2']: #서초구':
            item["dt"] = curDt
            item["sido"] = sidoName
            data.append(item)
        # end if
    # end for
    mongoUpdate("public_data_polution", data)

# ----------------------------------------------------------
# get public data -polution2
def getPublicDataPolution2(sidoName):
    # sidoName = SIDO_NAME[0]["sidoName"]
    reqUrl = END_POINT_POLUTION2.format(
        SERVICE_KEY, # service key
        NUMBER_OF_ROWS, # numOfRows
        PAGE_NO, # pageNo
        sidoName, # sidoName
        SEARCH_CONDITION, # searchCondition
        RESULT_TYPE # data type
        )

    print ("request url: %s" % reqUrl)
    r = requests.get(url = reqUrl, params={})
    print ("status: {0}, header: {1}, encoding: {2}".format(r.status_code, r.headers, r.encoding))
    plainData = r.text
    print("***********************")
    pprint.pprint(plainData)

    if r.headers["content-type"].find("text/xml") > -1:
        resultData = xmltodict.parse(plainData)
        header = resultData["response"]["header"]
        print ("Method=%s^sido=%s^resultCode=%s^resultMessage=%s" % ("getPublicDataPolution2", sidoName, header["resultCode"], header["resultMsg"]))
        return

    # resultData = xmltodict.parse(plainData)
    # # resultData = json.loads(plainData)
    # # resultData = json.dumps(xmlData)
    resultData = json.loads(plainData)
    # if resultData["response"]["header"]["resultCode"] == "22":
    #     return

    items = []
    if not (resultData["list"] == None or resultData["list"] == ''):
        items = resultData["list"]
        
    # bodyData = resultData["response"]["body"]
    # items = []
    # if not (bodyData["items"] == None or bodyData["items"] == ''):
    #    items = bodyData["items"]["item"]
    # # print ("result: %s items" % str(bodyData["totalCount"]))

    """
    data = {
        "uumOfRows": bodyData["numOfRows"], 
        "totalCount": bodyData["totalCount"],
        "payload": items
        }
    """
    # curDt = datetime.now()
    print("getPublicDataPolution2-------------------------------")
    data = []
    curDt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for item in items:
        if item['cityName'] == LOCATION_INFO['sido2']: # '서초구':
            item["dt"] = curDt
            item["sido"] = sidoName
            data.append(item)
        # end if
    # end for
    mongoUpdate("public_data_polution2", data)


# ----------------------------------------------------------
# mongo update
def mongoUpdate(collectionName, data):
    if data == [] or data == None:
        return

    # conn = pymongo.MongoClient('jiot.jiguem.com', 27017)
    conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@jiot.jiguem.com:27017/default_db?authSource=jiot_log')

    db = conn.get_database('jiot_log')
    collection = db.get_collection(collectionName)

    pprint.pprint(data)

    collection.insert(data)
    print("insert ok!")

# ----------------------------------------------------------
if __name__ == "__main__":
    # loop forever
    while True:
        try:
            print ("[%s] get public data -weather" % datetime.now())
            # ----------------------
            getPublicDataWeather_ForecastSpaceData()
            getPublicDataWeather_ForecastTimeData()
            getPublicDataWeather_ForecastGrib()

            if not POLLUTION_CALL_FLAG: #180 sec/ day

                for sido in SIDO_NAME:
                    sidoName = sido["sidoName"]

                    print ("[%s] get public data -polution %s" % (datetime.now(), sidoName))
                    getPublicDataPolution(sidoName)
                    
                    print ("[%s] get public data -polution2 %s" % (datetime.now(), sidoName))
                    getPublicDataPolution2(sidoName)

                    POLLUTION_CALL_FLAG = True

                    break # only index 0 (seoul)
                # for
            # if
            else:
                POLLUTION_CALL_FLAG = False            

            # time.sleep(60*40) #40분 마다
            # time.sleep(90) # 1000 times / 1 day
            time.sleep(600) # 10분마다

        except Exception as ex:
            print ("%s" %ex)
            time.sleep(600)
            # break
