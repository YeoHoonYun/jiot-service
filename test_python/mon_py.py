import datetime, threading, pymongo, json

conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@jiot.jiguem.com:27017/default_db?authSource=jiot_log')
db = conn.get_database('jiot_log')
# collection = db.get_collection('ha_sensors_state')
# mon_list = list(collection.find(
#             {
#                 # "ulPk" : 10000,
#                 "dt": "2019-08-09 12:47:16 KST+0900"
#             }
#         ))
#
# print(mon_list)

collection = db.get_collection('hs_sensor_series_1')
mon_list = list(collection.find(
            {
                # "ulPk" : 10000,
                "kor_time": "2019-08-09 12:47:16 KST+0900"
            }
        ))

print(mon_list)