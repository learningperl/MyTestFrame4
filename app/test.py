# coding=utf-8
import os,threading


def run(cmd):
    os.popen(cmd)
    print('appium已经停止')


res = os.popen('dir').read()
print(res)
cmd = 'node E:\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
# 创建一个线程
th = threading.Thread(target=run,args=(cmd,))
th.start()
print('appium 正在运行')


