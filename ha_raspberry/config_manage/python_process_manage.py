#!/usr/bin/python
import os
import sys
import time

process_list = ["chat_main.py", "loof_request.py"]


def main():
    while (1):
        for process in process_list:
            oscommend = os.popen("ps aux | grep " + process + " | awk '{print $12}'").readlines()
            check_process = "%s" % (oscommend[0])
            if (check_process.find(process) == -1):
                os.system("nohup /usr/bin/python3 /home/jiguem/dev/" + process + " 2>/dev/null 1>/dev/null &")

        try:
            time.sleep(3)
        except:
            sys.exit()


if __name__ == "__main__":
    main()
