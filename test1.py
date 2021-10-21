from appium import webdriver
import time
info={
    #1.测的平台  Android ios  不区分大小写
    "platformVersion":"Android",
    #2.测试的版本号  设置-关于平板电脑  版本号
    "platformVersion":"5.1.1",
    #3.设备名  adb devices         127.0.0.1:62001  iOS必须要去写
    "deviceName":"127.0.0.1:62001",
    #测哪个东西 包名 开发定义
    #获取包名：adb shell dumpsys window|findstr mCurrentFocus
    #获取当前窗口
    "appPackage":"",
    #界面名
    "appActivity":"",
    #不重置
    "noRest":False
}
#启动Remote（服务器，配置信息）
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
time.sleep(3)
driver.quit()