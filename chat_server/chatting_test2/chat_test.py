import json
import time
from pytz import timezone
from datetime import datetime

from requests import post
import word_dict

# state = post(url, headers=headers, data=json.dumps(result["function"]))
result = {}
word_dict = word_dict.word_class()
check_list = word_dict.word_dic

def deep_word(dic, word):
    global result
    result = {}
    for anal in dic.keys():
        if anal in word:
            deep_word(dic[anal], word)

    if "functions" in dic.keys():
        result = dic

def get_kst():
    fmt = "%Y-%m-%d %H:%M"
    KST = datetime.now(timezone('Asia/Seoul'))
    return KST.strftime(fmt)


def word_anal(word,body):
    # global word_dict
    words = []
    el_url = "http://demo.jiguem.com:9200/nori_sample/_analyze"
    el_headers = {
        'content-type': "application/json",
    }
    el_data = {
        "analyzer": "nori_analyzer",
        "text": word+".",
        "attributes": ["leftPOS"],
        "explain": True
    }
    response = post(el_url, data=json.dumps(el_data), headers=el_headers)
    anal_word = json.loads(response.text)["detail"]["tokenfilters"][0]["tokens"]

    for i in anal_word:
        i["leftPOS"] = i["leftPOS"].split("(")[0]
        words.append(tuple([i["token"],i["leftPOS"]]))

    print(words)
    deep_word(check_list(body), words)
    print(result)
    try:
        for function in result.get("functions"):
            function = json.loads(function)
            print(function)
            if "timeSleep" in function.keys():
                time.sleep(function.get("timeSleep"))
            elif function.get("msgTyp") == 103001:
                print(103001)
                url = 'https://jiot.iotjiguem.com/api/devicecommand/publishcommand'
                headers = {
                    'Content-Type': 'application/json'
                }
                try:
                    post(url, headers=headers, data=json.dumps(function))
                except:
                    pass
            elif function.get("msgTyp") == 103002 and function.get("isShowMsg"):
                function["message"] = json.dumps({
                    "ID" : function["ID"],
                    "msg" : function["message"],
                    "currTime" : get_kst(),
                    "TMX": function["TMX"],
                    "TMN": function["TMN"]
                })
                print(103002)
                url = 'https://jiot.iotjiguem.com/device1'
                headers = {
                    'Content-Type': 'application/json'
                }
                try:
                    post(url, headers=headers, data=json.dumps(function))
                except:
                    pass
        time.sleep(1)
        return result["content"]
    except:
        return "등록되지 않은 명령입니다. 선택할 명령을 다시 말해주세요.."

if __name__ == '__main__':
    result = {}
    while True:
        word = input("명령어를 입력하세요. \n")
        res = word_anal(word.lower(), "testYun")
        print(res)
        print("###########################")
