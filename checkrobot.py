#!/usr/bin/env python
# coding=utf-8

import os
import threading
import time

import requests
import sys
'''

pip install --upgrade pip

pip freeze >requirements.txt

pip install -r requirements.txt

pip install requests
'''


def getInfo(processname):
    task = os.popen('tasklist')
    if processname in task.read():
        print("-----ok")
    else:
        print("Sorry,the process is not in process list,may be not running......")
        sendSms()
        sys.exit(0)


    print("-----return ---")


# 每隔10秒钟执行
def cycle():
    while 1:
        getInfo("robot.exe")
        time.sleep(10)


def sendSms():
    url = 'http://m.vipss.info:9999/sendsms'
    d = {'content': '机器人挂了', 'phone': '17623217250'}
    r = requests.post(url, data=d)
    print(r)


if __name__ == '__main__':
    t = threading.Thread(target=cycle)
    t.start()
    t.join()
