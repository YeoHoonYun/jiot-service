import datetime, threading, pymongo, json
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
    KST = datetime.now(timezone('Asia/Seoul')) - timedelta(seconds=5)
    return KST.strftime(fmt)

def mongoUpdate(data, connection):
    conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@jiot.jiguem.com:27017/default_db?authSource=jiot_log')
    db = conn.get_database('jiot_log')
    collection = db.get_collection(connection)
    collection.insert(data,check_keys=False)

# url = "http://%s:8081/api/device/getdevices?ulpk=%s" % ("183.98.179.130", 10000)
# headers = {
#     'Content-Type': 'application/json'
# }
#
# res = get(
#     url = url,
#     headers = headers
# )
#
# entity_list = [x["devnm"] for x in json.loads(res.text)["data"]]

# entity_list = [
#     "binary_sensor.door_window_sensor_158d00028f32a0"
#     ,"binary_sensor.door_window_sensor_158d000357eacf"
#     ,"binary_sensor.door_window_sensor_158d000357eb0d"
#     ,"binary_sensor.door_window_sensor_158d000357eb6d"
#     ,"binary_sensor.door_window_sensor_158d000357ec13"
#     ,"binary_sensor.motion_sensor_158d000290fdaf"
#     ,"binary_sensor.motion_sensor_158d0003041a2c"
#     ,"binary_sensor.motion_sensor_158d00034ffe83"
#     ,"binary_sensor.motion_sensor_158d00034fff25"
#     ,"binary_sensor.motion_sensor_158d00034fff2b"
#     ,"fan.xiaomi_miio_device_2"
#     ,"cover.curtain_158d00031416c2"
#     ,"group.all_fans"
#     ,"group.all_lights"
#     ,"temper"
#     ,"aqi"
#     ,"humidity"
# ]

ulPk_list = [10000, 10001]

conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@jiot.jiguem.com:27017/default_db?authSource=jiot_log')
db = conn.get_database('jiot_log')
collection = db.get_collection('ha_sensors_state')

class AsyncTask:
    def __init__(self):
        pass

    def device_automation(self):
        threading.Timer(1, self.device_automation).start()
        kor_time = get_kst()
        print(kor_time)
 #####################################################################################################################################
        mon_list = list(collection.find(
            {
                # "ulPk" : 10000,
                # 2019-08-12 10:02:58 KST+0900
                "dt": kor_time
                # "dt" : {"$gte" : "2019-08-12 10:23:15 KST+0900", "$lte" : "2019-08-12 10:23:15 KST+0900"}
            }
        ))
        if(len(mon_list) == 0):
            return 0

        for data in mon_list:
            ulPk = data.get("ulPk")
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
            result = {}
            result["kor_time"] = kor_time
            result["ulPk"] = ulPk
            result["data"] = {}

            for entity in entity_list:
                result["data"][str(entity)] = 0
                if data.get("entity_id") == entity:
                    if("fan.xiaomi_miio_device" in data.get("entity_id")):
                        result["data"]["fan_attribute"] = data.get("attributes")

                    elif ("cover.curtain" in data.get("entity_id")):
                        result["data"]["cover_attribute"] = data.get("attributes")

                    result["data"][entity] = data.get("state")

            print(result)
            page_sanitized = json.loads(json_util.dumps(result))
            mongoUpdate(page_sanitized, "hs_sensor_series_1")

if __name__ == '__main__':
    at = AsyncTask()
    at.device_automation()