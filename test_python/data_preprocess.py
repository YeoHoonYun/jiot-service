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
        result = {kor_time:{}}
        entity_list = []
        print(kor_time)
 #####################################################################################################################################
        for ulPk in ulPk_list:
            url = "http://%s:8081/api/device/getdevices?ulpk=%s" % ("183.98.179.130", ulPk)
            headers = {
                'Content-Type': 'application/json'
            }

            res = get(
                url=url,
                headers=headers
            )

            entity_list = [x["devnm"] for x in json.loads(res.text)["data"]]
            entity_list.extend(['fan_attribute', 'cover_attribute'])
#####################################################################################################################################
            result[kor_time][ulPk] = {}
            for entity in entity_list:
                result[kor_time][ulPk][str(entity)] = 0

        mon_list = list(collection.find(
            {
                # "ulPk" : 10000,
                "dt": kor_time
            }
        ))

        for entity in entity_list:
            for data in mon_list:
                if data.get("entity_id") == entity:
                    print(data)
                    if("fan.xiaomi_miio_device" in data.get("entity_id")):
                        # result[kor_time][data.get("ulPk")]["temper"] = str(data.get("attributes").get("temperature"))
                        # result[kor_time][data.get("ulPk")]["aqi"] = str(data.get("attributes").get("aqi"))
                        # result[kor_time][data.get("ulPk")]["humidity"] = str(data.get("attributes").get("humidity"))
                        # del result[kor_time][data.get("ulPk")][str(entity)]
                        result[kor_time][data.get("ulPk")]["fan_attribute"] = data.get("attributes")
                    elif ("cover.curtain" in data.get("entity_id")):
                        result[kor_time][data.get("ulPk")]["cover_attribute"] = data.get("attributes")
                    # elif ("binary_sensor.motion_sensor" in data.get("entity_id") or "binary_sensor.door_window_sensor" in data.get("entity_id")):
                    #     result[kor_time][data.get("ulPk")][entity] = data.get("attributes").get("state")
                    else:
                        result[kor_time][data.get("ulPk")][entity] = data.get("state")

        print(result)
        page_sanitized = json.loads(json_util.dumps(result))
        # d2 = json.loads(s1)
        mongoUpdate(page_sanitized, "hs_sensor_series")

if __name__ == '__main__':
    at = AsyncTask()
    at.device_automation()