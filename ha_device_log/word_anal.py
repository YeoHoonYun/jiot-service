def word_dic():
    word_dic = {
		"binary_sensor.door_window_sensor_158d00026a7012" : {
            "type_device" : "state",
			"on" : {
                "tit": "현관문 열림",
                "content":"현관문이 열렸습니다."
		    },
            "off": {
                "tit": "현관문 닫힘",
                "content": "현관문이 닫혔습니다."
            }
        },
		"binary_sensor.switch_158d000270d356" : {
            "type_device": "last_action",
			"double" : {
                "tit": "초인종 2번 이상",
                "content":"초인종이 여러번 울렸습니다."
		    },
            "single" : {
                "tit": "초인종 1번",
                "content":"초인종이 한번 울렸습니다."
		    }
		}
	}
    return word_dic