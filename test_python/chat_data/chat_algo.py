import data_demo, data_server, pprint

if __name__ == '__main__':
    #서버 정보
    usrPk = '3'
    sid = '618DC67618FDE401ED0D74138EB3A59D'
    
    # pprint.pprint(data_demo.data) # 단일 메시지
    # pprint.pprint(data_server.data) # 다중 메시지(나중에 그룹아이디로 가지고 와야됨...)

    data = [data_demo.data, data_server.data]

    for i in data:
        print(i['usrPk']) # 단일 메시지, 전체 메시지
        # 단일 메시지
        if len(i['usrPk']) == 1:
            if i['sid'] == sid:
                print("단일 메시지를 출력합니다.")
            else:
                pass
        
        # 다중 메시지
        else:
            if usrPk in i['usrPk']:
                print("다중 메시지를 출력합니다.")
            else:
                pass