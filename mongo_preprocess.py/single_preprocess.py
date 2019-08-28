import pymongo, json
from datetime import datetime
from pytz import timezone
from datetime import timedelta
from requests import get

import json
from bson import json_util, ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def get_kst():
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    KST = datetime.now(timezone('Asia/Seoul')) - timedelta(days=7)
    return KST.strftime("%Y-%m-%d %H:%M:%S %Z%z")

def mongoUpdate(data, connection):
    conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@jiot.jiguem.com:27017/default_db?authSource=jiot_log')
    db = conn.get_database('jiot_log')
    collection = db.get_collection(connection)
    collection.insert(data,check_keys=False)

conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@jiot.jiguem.com:27017/default_db?authSource=jiot_log')
db = conn.get_database('jiot_log')
collection = db.get_collection('ha_sensors_state')
result = {}

ulPk = 10000
# from_date = (datetime(2019, 8, 12, 00, 00, 00)).strftime("%Y-%m-%d %H:%M:%S")
# to_date = (datetime(2019, 8, 12, 23, 59, 59)).strftime("%Y-%m-%d %H:%M:%S")
from_date = "2019-08-01 00:00:00"
to_date = "2019-08-12 23:59:59"

if __name__ == '__main__':
    mon_list = list(collection.find(
            {
                "ulPk" : ulPk,
                "dt" : {"$gte" : from_date, "$lte" : to_date}
            }
        ))
    url = "http://%s:8081/api/device/getdevices?ulpk=%s" % ("183.98.179.130", ulPk)
    headers = {
        'Content-Type': 'application/json'
    }

    res = get(
        url=url,
        headers=headers
    )

    entity_list = [x["devnm"] for x in json.loads(res.text)["data"]]
    # entity_list.extend(['fan_attribute', 'cover_attribute'])

    for data in mon_list:
        result["kor_time"] = data.get('dt')
        result["ulPk"] = ulPk
        result["data"] = {}
        for entity in entity_list:
            result["data"][str(entity)] = 0
            if ulPk == data.get("ulPk"):
                if data.get("entity_id") == entity:
                    if ("fan.xiaomi_miio_device" in data.get("entity_id")):
                        result["data"]["fan_attribute"] = data.get("attributes")
                    elif ("cover.curtain" in data.get("entity_id")):
                        result["data"]["cover_attribute"] = data.get("attributes")
                    result["data"][entity] = data.get("state")

        # print(result)
        page_sanitized = json.loads(json_util.dumps(result))
        mongoUpdate(page_sanitized, "hs_sensor_series_3")