from device_control import *

class word_class:
    def __init__(self):
        pass

    def word_dic(self, body):
        return {
            ('수면', 'NNG'): {
                ('모드', 'NNG'): {
                    "function": su_mon(body),
                    "content": "챗봇 : 수면 모드를 실행합니다."
                },
            },
            ('종료', 'NNG'): {
                ('수면', 'NNG'): {
                    ('모드', 'NNG'): {
                        "function": su_mon_off(body),
                        "content": "챗봇 : 수면 모드를 종료합니다."
                    },
                },
            },
            ('시작', 'NNG'): {
                ('수면', 'NNG'): {
                    ('모드', 'NNG'): {
                        "function": su_mon(body),
                        "content": "챗봇 : 수면 모드를 실행합니다."
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