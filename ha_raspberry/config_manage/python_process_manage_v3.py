#!/usr/bin/python
import os, sys, time
import configparser

class processManager:
    def __init__(self, base, command, process_list):
        self.base = base
        self.process_list = process_list
        self.command = command

    def manage(self):
        while (1):
            for process in self.process_list:
                print("ps aux | grep %s | awk '{print $12}'" % (process))
                oscommend = os.popen("ps aux | grep " + process + " | awk '{print $12}'").readlines()
                check_process = "%s" % (oscommend[0])
                print("nohup %s %s/%s 2>/dev/null 1>/dev/null &" % (self.command, self.base, process))
                if (self.base+"/"+process+"\n" not in oscommend):
                    os.system("nohup "+self.command+" "+self.base+"/" + process + " 2>/dev/null 1>/dev/null &")

            try:
                time.sleep(3)
            except:
                sys.exit()


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("process_config")

    process_info = config["PROCESS"]
    base = process_info["base"]
    command = process_info["command"]
    process_list = process_info["process_list"].split(" ")

    processManager = processManager(base, command, process_list)
    processManager.manage()
