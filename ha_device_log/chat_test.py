import pprint, json
from pytz import timezone
from datetime import datetime
from word_anal import word_dic
def select_user():
	user_list = ["3","4","5"]

	return user_list
def get_kst():
    fmt = "%H:%M:%S"
    KST = datetime.now(timezone('Asia/Seoul'))
    return KST.strftime(fmt)
def word_dict(body):
	message = {
		# "deviceData": '{"entity_id":"light.hue_color_lamp_3","rgb_color": [247,171,81]}',
		# "deviceDomain": "light",
		# "deviceId": "light.hue_color_lamp_3",
		# "deviceService": "turn_on",
		"time": get_kst(),
		# "dcmPk": 94,
		"usrPk": select_user(),
		# "usrCode": 3,
		# "statCode": 1,
		# "outCond": 1,
		"tit": "",
		"message": '',
		# "interv": 32,
		# "inDt": [2019, 5, 10, 15, 1, 58],
		"msgtyp": 103004,
		"isgroupmsg": False,
		"isshowmsg": True,
		# "dt": "2019-05-31 13:36:30 KST+0900"
	}

	dic = word_dic()

	message_ = {
		"type" : "01",
		"content" : ""
	}

	# for key in dic.keys():
	# 	if body["entity_id"] == key:
	# 		for attr in dic[key].keys():
	# 			if body["attributes"][dic[key]["type_device"]] in attr:
	# 				message_["content"] = dic[key][attr]["content"]
	# 				message["tit"] = dic[key][attr]["tit"]
	# 				message["message"] = json.dumps(message_)

	if body["entity_id"] == "binary_sensor.door_window_sensor_158d00026a7012":
		key = "binary_sensor.door_window_sensor_158d00026a7012"
		if body[dic[key]["type_device"]] == "on":
			message_["content"] = dic[key]["on"]["content"]
			message["tit"] = dic[key]["on"]["tit"]

		elif body[dic[key]["type_device"]] == "off":
			message_["content"] = dic[key]["off"]["content"]
			message["tit"] = dic[key]["off"]["tit"]

	elif body["entity_id"] == "binary_sensor.switch_158d000270d356":
		key = "binary_sensor.switch_158d000270d356"
		for attr in dic[key].keys():
			if body["attributes"][dic[key]["type_device"]] in attr:
				message_["content"] = dic[key][attr]["content"]
				message["tit"] = dic[key][attr]["tit"]

	message["message"] = json.dumps(message_)

	return message

if __name__ == '__main__':
	body = {
		"entity_id" : "binary_sensor.door_window_sensor_158d00026a7012",
		"state": "off",
		"attributes":{"device_class" : "opening"}
	}
	#
	# body = {
	# 	"entity_id": "binary_sensor.switch_158d000270d356",
	#
	# 	"attributes": {"last_action": "double"}
	# }

	pprint.pprint(word_dict(body))