#!/usr/bin/python
import os, sys, time
from optparse import OptionParser

# u

class processManager:
    def __init__(self, base, command, process_list):
        self.base = base
        self.process_list = process_list
        self.command = command

    def manage(self):
        while (1):
            for process in self.process_list:
                oscommend = os.popen("ps aux | grep " + process + " | awk '{print $12}'").readlines()
                check_process = "%s" % (oscommend[0])
                if (self.base+"/"+process+"\n" not in oscommend):
                    os.system("nohup "+self.command+" "+self.base+"/" + process + " 2>/dev/null 1>/dev/null &")

            try:
                time.sleep(3)
            except:
                sys.exit()


if __name__ == "__main__":
    base = "/home/pi/dev"
    command = "/usr/bin/python3"
    process_list = ["chat_main.py", "loof_request.py"]

    parser = OptionParser()
    parser.add_option("-b", "--base", dest="base")
    parser.add_option("-c", "--command", dest="command")

    (options, args) = parser.parse_args()

    if options.base == None:
        print("기본 베이스 파일경로를 넣어주세요. ex) -b ${베이스 경로}")
        sys.exit(0)
    if options.command == None:
        print("실행할 파이썬환경 위치를 넣어주세요.  -c ${커맨드 명령어}")
        sys.exit(0)
    if len(args) < 1:
        print("실행할 스크립트 정보를 넣어주세요.")
        sys.exit(0)

    #print(options.base)
    #print(options.command)
    #print(args)

    processManager = processManager(options.base, options.command, args)
    processManager.manage()
