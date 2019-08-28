from device_control import *
import json

device_list = {
    "모든_불" : "group.all_lights",
    "모든_청정기" : "group.all_fans",
    "모든_커튼" : "group.all_covers",

    "안방_천정등" : "light.light_yeelight_ceiling",
    "안방_침실등" : "light.light_yeelight_lamp01",
    "안방_블라인드" : "cover.blind",
    "안방_화장실등" : "light.light_yeelight_bulb02",

    "거실_책상등" : "light.light_yeelight_table",
    "거실_무드등": "light.light_yeelight_lamp02",
    "거실_커튼" : "cover.curtain_158d0002edad4d",
    "부엌등" : "light.light_yeelight_bulb03",
    "로봇청소기" : "vacuum.xiaomi_vacuum_cleaner",
    "공기청정기1" : "fan.xiaomi_miio_device",
    "공기청정기2" : "fan.xiaomi_miio_device_2"
}

color_list = {
    "회색" : [80,80,80],
    "빨강색" : [255,0,0],
    "오렌지색" : [255,165,0]
}

class word_class:
    def __init__(self):
        pass

    def sumon_mode(self):
        command_list = []
        command_list.append(light_off(device_list.get("안방_천정등")))
        command_list.append(time_sleep(20))
        command_list.append(light_brightness(device_list.get("안방_침실등"), 20))
        command_list.append(time_sleep(20))
        command_list.append(cover_off(device_list.get("안방_블라인드")))
        command_list.append(time_sleep(20))
        command_list.append(light_off(device_list.get("안방_화장실등")))
        command_list.append(time_sleep(20))
        command_list.append(light_off(device_list.get("안방_침실등")))
        return command_list

    def meongsang_mode(self):
        command_list = []
        command_list.append(chat_message("무드등의 밝기를 조절합니다.", "b10"))
        command_list.append(light_brightness(device_list.get("거실_무드등"), 100, color_list.get("오렌지색")))
        command_list.append(time_sleep(10))
        command_list.append(cover_off(device_list.get("거실_커튼")))
        command_list.append(time_sleep(10))
        command_list.append(light_off(device_list.get("부엌등")))
        command_list.append(time_sleep(10))
        command_list.append(light_off(device_list.get("거실_책상등")))
        command_list.append(time_sleep(10))
        command_list.append(robot_back(device_list.get("로봇청소기")))
        command_list.append(time_sleep(10))
        command_list.append(fan_start(device_list.get("공기청정기2")))
        return command_list

    def chulguen_mode(self):
        command_list = []
        command_list.append(cover_off(device_list.get("안방_블라인드")))
        command_list.append(time_sleep(20))
        command_list.append(light_on(device_list.get("안방_침실등")))
        command_list.append(time_sleep(1))
        command_list.append(fan_start(device_list.get("공기청정기1")))
        command_list.append(time_sleep(20))
        command_list.append(chat_message("약 드실 시간입니다.","b10"))
        command_list.append(time_sleep(20))
        command_list.append(chat_message("오늘 추천 샤워온도는 36도입니다.","b10"))
        command_list.append(time_sleep(20))
        command_list.append(cover_on(device_list.get("안방_블라인드")))
        command_list.append(cover_on(device_list.get("거실_커튼")))
        command_list.append(time_sleep(20))
        command_list.append(light_on(device_list.get("안방_천정등")))
        command_list.append(time_sleep(1))
        command_list.append(fan_start(device_list.get("공기청정기2")))
        command_list.append(time_sleep(20))
        command_list.append(chat_message("오늘 추천 의상은 티셔츠입니다.","b4","30","27"))
        command_list.append(time_sleep(20))
        command_list.append(chat_message("챙기실 물건은 잊지 않으셨죠? <B>가방, 휴대폰, 지갑</B>","b4","30","27"))
        command_list.append(time_sleep(20))
        command_list.append(fan_stop(device_list.get("모든_청정기")))
        command_list.append(time_sleep(20))
        command_list.append(robot_start(device_list.get("로봇청소기")))
        command_list.append(time_sleep(1))
        command_list.append(cover_off(device_list.get("거실_커튼")))
        command_list.append(time_sleep(30))
        command_list.append(robot_back(device_list.get("로봇청소기")))
        # command_list.append(light_off(device_list.get("모든_불")))
        # command_list.append(time_sleep(1))
        # command_list.append(fan_stop(device_list.get("모든_청정기")))
        # command_list.append(time_sleep(2))
        # command_list.append(cover_off(device_list.get("모든_커튼")))
        return command_list

    def init_mode(self):
        command_list = []
        command_list.append(light_off(device_list.get("모든_불")))
        command_list.append(time_sleep(1))
        command_list.append(fan_stop(device_list.get("모든_청정기")))
        command_list.append(time_sleep(2))
        command_list.append(cover_off(device_list.get("모든_커튼")))
        return command_list

    def test_mode(self):
        command_list = []
        command_list.append(chat_message("오늘 추천 샤워온도는 36도입니다.", "b10"))
        command_list.append(chat_message("챙기실 물건은 잊지 않으셨죠? <B>가방, 휴대폰, 지갑</B>", "b4", "30", "25"))
        command_list.append(chat_message("무드등의 밝기를 조절합니다.", "b10"))
        command_list.append(chat_message("오늘 추천 의상은 티셔츠입니다.","b4","30","25"))
        command_list.append(cover_on(device_list.get("거실_커튼")))
        command_list.append(time_sleep(5))
        command_list.append(cover_off(device_list.get("거실_커튼")))
        return command_list

    def word_dic(self, body):
        return {
            ('자', 'VV'): {
                ('나', 'NP'): {
                    "functions": self.sumon_mode(),
                    "content": "수면 모드가 실행되었습니다."
                },
            },
            ('잔다', 'VV'): {
                ('나', 'NP'): {
                    "functions": self.sumon_mode(),
                    "content": "수면 모드가 실행되었습니다."
                },
            },
            ('꺼', 'VV'): {
                ('모드', 'NNG'): {
                    ('수면', 'NNG'): {
                        "functions": self.init_mode(),
                        "content": "수면 모드가 종료되었습니다."
                    },
                    ('명상', 'NNG'): {
                        "functions": self.init_mode(),
                        "content": "명상 모드가 종료되었습니다."
                    },
                    ('외출', 'NNG'): {
                        "functions": self.init_mode(),
                        "content": "외출 모드가 종료되었습니다."
                    },
                },
            },
            ('끄', 'VV'): {
                ('모드', 'NNG'): {
                    ('수면', 'NNG'): {
                        "functions": self.init_mode(),
                        "content": "수면 모드가 종료되었습니다."
                    },
                    ('명상', 'NNG'): {
                        "functions": self.init_mode(),
                        "content": "명상 모드가 종료되었습니다."
                    },
                    ('외출', 'NNG'): {
                        "functions": self.init_mode(),
                        "content": "외출 모드가 종료되었습니다."
                    },
                },
            },

            ('모드', 'NNG'): {
                ('수면', 'NNG'): {
                    "functions": self.sumon_mode(),
                    "content": "수면 모드가 실행되었습니다."
                },
                ('명상', 'NNG'): {
                    "functions": self.meongsang_mode(),
                    "content": "명상 모드가 실행되었습니다."
                },
                ('외출', 'NNG'): {
                    "functions": self.chulguen_mode(),
                    "content": "외출 모드가 실행되었습니다."
                },
                ('출근', 'NNG'): {
                    "functions": self.chulguen_mode(),
                    "content": "외출 모드가 실행되었습니다."
                },
            },
            ('시작', 'NNG'): {
                ('모드', 'NNG'): {
                    ('수면', 'NNG'): {
                        "functions": self.sumon_mode(),
                        "content": "수면 모드가 실행되었습니다."
                    },
                    ('명상', 'NNG'): {
                        "functions": self.meongsang_mode(),
                        "content": "명상 모드가 실행되었습니다."
                    },
                    ('외출', 'NNG'): {
                        "functions": self.chulguen_mode(),
                        "content": "외출 모드가 실행되었습니다."
                    },
                    ('출근', 'NNG'): {
                        "functions": self.chulguen_mode(),
                        "content": "외출 모드가 실행되었습니다."
                    },
                    ('테스트', 'NNG'): {
                        "functions": self.test_mode(),
                        "content": "테스트 모드가 실행되었습니다."
                    },
                },
            },
            ('종료', 'NNG'): {
                ('모드', 'NNG'): {
                    ('수면', 'NNG'): {
                        "functions": self.init_mode(),
                        "content": "수면 모드가 종료되었습니다."
                    },
                    ('명상', 'NNG'): {
                        "functions": self.init_mode(),
                        "content": "명상 모드가 종료되었습니다."
                    },
                    ('외출', 'NNG'): {
                        "functions": self.init_mode(),
                        "content": "외출 모드가 종료되었습니다."
                    },
                },
            },

        #     ('안방', 'NNG') : {
        #         ('불', 'NNG') : {
        #             ('키', 'VV') : {
        #                 "function" : hue1_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('켜', 'VV'): {
        #                 "function" : hue1_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('켜', 'NNM'): {
        #                 "function" : hue1_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('끄', 'VV') : {
        #                 "function" : hue1_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼', 'VV'): {
        #                 "function" : hue1_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼주', 'VV'): {
        #                 "function" : hue1_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼', 'NNG'): {
        #                 "function" : hue1_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('켜', 'NNG'): {
        #                 "function" : hue1_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             }
        #         },
        #         ('조명', 'NNG') : {
        #             ('키', 'VV') : {
        #                 "function" : hue1_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('켜', 'VV'): {
        #                 "function" : hue1_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('켜', 'NNM'): {
        #                 "function" : hue1_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('끄', 'VV') : {
        #                 "function" : hue1_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼', 'VV'): {
        #                 "function" : hue1_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼주', 'VV'): {
        #                 "function" : hue1_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼', 'NNG'): {
        #                 "function" : hue1_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('켜', 'NNG'): {
        #                 "function" : hue1_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #         },
        #     },
        #     ('거실', 'NNG') : {
        #         ('불', 'NNG') : {
        #             ('키', 'VV') : {
        #                 "function" : hue2_turn_on(),
        #                 "content" : "대답 : 거실 불을 킵니다."
        #             },
        #             ('켜', 'VV'): {
        #                 "function" : hue2_turn_on(),
        #                 "content" : "대답 : 거실 불을 킵니다."
        #             },
        #             ('켜', 'NNM'): {
        #                 "function" : hue2_turn_on(),
        #                 "content" : "대답 : 거실 불을 킵니다."
        #             },
        #             ('끄', 'VV') : {
        #                 "function" : hue2_turn_off(),
        #                 "content" : "대답 : 거실 불을 끕니다."
        #             },
        #             ('꺼', 'VV'): {
        #                 "function" : hue2_turn_off(),
        #                 "content" : "대답 : 거실 불을 끕니다."
        #             },
        #             ('꺼주', 'VV'): {
        #                 "function" : hue2_turn_off(),
        #                 "content" : "대답 : 거실 불을 끕니다."
        #             },
        #             ('꺼', 'NNG'): {
        #                 "function" : hue2_turn_off(),
        #                 "content" : "대답 : 거실 불을 끕니다."
        #             },
        #             ('켜', 'NNG'): {
        #                 "function" : hue2_turn_on(),
        #                 "content" : "대답 : 거실 불을 킵니다."
        #             }
        #         },
        #         ('조명', 'NNG') : {
        #             ('키', 'VV') : {
        #                 "function" : hue2_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('켜', 'VV'): {
        #                 "function" : hue2_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('켜', 'NNM'): {
        #                 "function" : hue2_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('끄', 'VV') : {
        #                 "function" : hue2_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼', 'VV'): {
        #                 "function" : hue2_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼주', 'VV'): {
        #                 "function" : hue2_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼', 'NNG'): {
        #                 "function" : hue2_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('켜', 'NNG'): {
        #                 "function" : hue2_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #         },
        #     },
        #     ('작은방', 'NNG') : {
        #         ('불', 'NNG') : {
        #             ('키', 'VV') : {
        #                 "function" : hue3_turn_on(),
        #                 "content" : "대답 : 작은방 불을 킵니다."
        #             },
        #             ('켜', 'VV'): {
        #                 "function" : hue3_turn_on(),
        #                 "content" : "대답 : 작은방 불을 킵니다."
        #             },
        #             ('켜', 'NNM'): {
        #                 "function" : hue3_turn_on(),
        #                 "content" : "대답 : 작은방 불을 킵니다."
        #             },
        #             ('끄', 'VV') : {
        #                 "function" : hue3_turn_off(),
        #                 "content" : "대답 : 작은방 불을 끕니다."
        #             },
        #             ('꺼', 'VV'): {
        #                 "function" : hue3_turn_off(),
        #                 "content" : "대답 : 작은방 불을 끕니다."
        #             },
        #             ('꺼주', 'VV'): {
        #                 "function" : hue3_turn_off(),
        #                 "content" : "대답 : 작은방 불을 끕니다."
        #             },
        #             ('꺼', 'NNG'): {
        #                 "function" : hue3_turn_off(),
        #                 "content" : "대답 : 작은방 불을 끕니다."
        #             },
        #             ('켜', 'NNG'): {
        #                 "function" : hue3_turn_on(),
        #                 "content" : "대답 : 작은방 불을 킵니다."
        #             },
        #         },
        #         ('조명', 'NNG') : {
        #             ('키', 'VV') : {
        #                 "function" : hue3_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('켜', 'VV'): {
        #                 "function" : hue3_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('켜', 'NNM'): {
        #                 "function" : hue3_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #             ('끄', 'VV') : {
        #                 "function" : hue3_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼', 'VV'): {
        #                 "function" : hue3_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼주', 'VV'): {
        #                 "function" : hue3_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('꺼', 'NNG'): {
        #                 "function" : hue3_turn_off(),
        #                 "content" : "대답 : 안방 불을 끕니다."
        #             },
        #             ('켜', 'NNG'): {
        #                 "function" : hue3_turn_on(),
        #                 "content" : "대답 : 안방 불을 킵니다."
        #             },
        #         },
        #     },
        #     ('작', 'VA') : {
        #         ('방', 'NNG') : {
        #             ('불', 'NNG') : {
        #                 ('키', 'VV') : {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 작은방 불을 킵니다."
        #                 },
        #                 ('켜', 'VV'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 작은방 불을 킵니다."
        #                 },
        #                 ('켜', 'NNM'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 작은방 불을 킵니다."
        #                 },
        #                 ('끄', 'VV') : {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 작은방 불을 끕니다."
        #                 },
        #                 ('꺼', 'VV'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 작은방 불을 끕니다."
        #                 },
        #                 ('꺼주', 'VV'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 작은방 불을 끕니다."
        #                 },
        #                 ('꺼', 'NNG'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 작은방 불을 끕니다."
        #                 },
        #                 ('켜', 'NNG'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 작은방 불을 킵니다."
        #                 }
        #             },
        #             ('조명', 'NNG') : {
        #                 ('키', 'VV') : {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 안방 불을 킵니다."
        #                 },
        #                 ('켜', 'VV'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 안방 불을 킵니다."
        #                 },
        #                 ('켜', 'NNM'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 안방 불을 킵니다."
        #                 },
        #                 ('끄', 'VV') : {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 안방 불을 끕니다."
        #                 },
        #                 ('꺼', 'VV'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 안방 불을 끕니다."
        #                 },
        #                 ('꺼주', 'VV'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 안방 불을 끕니다."
        #                 },
        #                 ('꺼', 'NNG'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 안방 불을 끕니다."
        #                 },
        #                 ('켜', 'NNG'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 안방 불을 킵니다."
        #                 },
        #             },
        #         },
        #     },
        #     ('아이', 'IC') : {
        #         ('방', 'NNG') : {
        #             ('불', 'NNG') : {
        #                 ('키', 'VV') : {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 아이방 불을 킵니다."
        #                 },
        #                 ('켜', 'VV'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 아이방 불을 킵니다."
        #                 },
        #                 ('켜', 'NNM'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 아이방 불을 킵니다."
        #                 },
        #                 ('끄', 'VV') : {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 아이방 불을 끕니다."
        #                 },
        #                 ('꺼', 'VV'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 아이방 불을 끕니다."
        #                 },
        #                 ('꺼주', 'VV'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 아이방 불을 끕니다."
        #                 },
        #                 ('꺼', 'NNG'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 아이방 불을 끕니다."
        #                 },
        #                 ('켜', 'NNG'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 아이방 불을 킵니다."
        #                 }
        #             },
        #             ('조명', 'NNG') : {
        #                 ('키', 'VV') : {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 아이방 불을 킵니다."
        #                 },
        #                 ('켜', 'VV'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 아이방 불을 킵니다."
        #                 },
        #                 ('켜', 'NNM'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 아이방 불을 킵니다."
        #                 },
        #                 ('끄', 'VV') : {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 아이방 불을 끕니다."
        #                 },
        #                 ('꺼', 'VV'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 아이방 불을 끕니다."
        #                 },
        #                 ('꺼주', 'VV'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 아이방 불을 끕니다."
        #                 },
        #                 ('꺼', 'NNG'): {
        #                     "function" : hue3_turn_off(),
        #                     "content" : "대답 : 아이방 불을 끕니다."
        #                 },
        #                 ('켜', 'NNG'): {
        #                     "function" : hue3_turn_on(),
        #                     "content" : "대답 : 아이방 불을 킵니다."
        #                 },
        #             },
        #         },
        #     },
        #     ('커텐', 'NNG') : {
        #         ('치', 'VV') : {
        #             "function" : curtain_open(),
        #             "content" : "대답 : 커튼을 칩니다."
        #         },
        #         ('걷', 'VV') : {
        #             "function" : curtain_close(),
        #             "content" : "대답 : 커튼을 걷습니다."
        #         },
        #         ('열', 'VV') : {
        #             "function" : curtain_close(),
        #             "content" : "대답 : 커튼을 걷습니다."
        #         },
        #         ('닫', 'VV') : {
        #             "function" : curtain_open(),
        #             "content" : "대답 : 커튼을 칩니다."
        #         },
        #     },
        #     ('커튼', 'NNG') : {
        #         ('치', 'VV') : {
        #             "function" : curtain_open(),
        #             "content" : "대답 : 커튼을 칩니다."
        #         },
        #         ('걷', 'VV') : {
        #             "function" : curtain_close(),
        #             "content" : "대답 : 커튼을 걷습니다."
        #         },
        #         ('열', 'VV') : {
        #             "function" : curtain_close(),
        #             "content" : "대답 : 커튼을 걷습니다."
        #         },
        #         ('닫', 'VV') : {
        #             "function" : curtain_open(),
        #             "content" : "대답 : 커튼을 칩니다."
        #         },
        #     },
        #     ('모든', 'MM') : {
        #         ('불', 'NNG'): {
        #             ('키', 'VV'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #             ('켜', 'VV'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #             ('켜', 'NNM'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #             ('끄', 'VV'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('꺼', 'VV'): {
        #                 "function": all_light_off(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('꺼주', 'VV'): {
        #                 "function": all_light_off(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('꺼', 'NNG'): {
        #                 "function": all_light_off(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('켜', 'NNG'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #         },
        #         ('조명', 'NNG'): {
        #             ('키', 'VV'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #             ('켜', 'VV'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #             ('켜', 'NNM'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #             ('끄', 'VV'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('꺼', 'VV'): {
        #                 "function": all_light_off(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('꺼주', 'VV'): {
        #                 "function": all_light_off(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('꺼', 'NNG'): {
        #                 "function": all_light_off(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('켜', 'NNG'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #         },
        #     },
        # ('모든', 'MM') : {
        #         ('불', 'NNG'): {
        #             ('키', 'VV'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #             ('켜', 'VV'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #             ('켜', 'NNM'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #             ('끄', 'VV'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('꺼', 'VV'): {
        #                 "function": all_light_off(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('꺼주', 'VV'): {
        #                 "function": all_light_off(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('꺼', 'NNG'): {
        #                 "function": all_light_off(),
        #                 "content": "대답 : 모든 불을 끕니다."
        #             },
        #             ('켜', 'NNG'): {
        #                 "function": all_light_on(),
        #                 "content": "대답 : 모든 불을 킵니다."
        #             },
        #         },
        #     },
        }