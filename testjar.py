# -*- coding: UTF-8 -*-
import os, jpype,time
# pip install JPype1==0.7.0

# 需要导入的jar位置
jarpath = './lib/encrypt.jar'
# 获取java安装路径
jdkpath = os.environ['JAVA_HOME']

# 启动jvm，加载jar
jpype.startJVM(jdkpath + "/jre/bin/server/jvm.dll", "-ea",
               "-Djava.class.path=%s" % jarpath,
               convertStrings=False)
        # 当有依赖的JAR包存在时，一定要使用-Djava.ext.dirs参数进行引入

# 获取jar中的类
JClass = jpype.JClass('com.testingedu.will.Encrypt')
# 初始化类，就是执行构造函数
instance = JClass('.\lib\certificate.jks')
print(time.time())
# 调用加密函数，instance相当于java的对象
result = str(instance.enCrypt('123456'))
print("加密结果：" + result)
print(time.time())
# 调用解密函数
result = str(instance.deCrypt(result))
print("解密结果：" + result)
print(time.time())
# 关闭jvm
jpype.shutdownJVM()