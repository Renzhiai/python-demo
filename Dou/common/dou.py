#coding:utf-8
"""Camera library for scripts.
"""

import os
import subprocess
import ConfigParser

from configs import Configs
from configs import AppConfig
from automator.uiautomator import Device

def connect_device(device_name,logger):
    """connect_device(device_id) -> Device
    Connect a device according to device ID.
    """
    environ = os.environ
    device_id = environ.get(device_name)
    if device_id == None:
        device_id = device_name
    backend = Configs("common").get("Info","backend")
    logger.debug("Device ID is " + device_id + " backend is " + backend)
    if backend.upper() == "MONKEY":
        device = globals()["%sUser"%backend](device_id)
    else:
        device = Device(device_id)
    if device is None:
        logger.critical("Cannot connect device.")
        raise RuntimeError("Cannot connect %s device." % device_id)
    return device

class Dou(object):

    def __init__(self,device,logger):
        self.config = ConfigParser.ConfigParser()
        self.logger = logger
        self.m_device = device
        self.appconfig = AppConfig("appinfo")
        if isinstance(device, Device):
            self.device = device
        else:
            self.device = connect_device(device,self.logger)
        self.config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"configure","common.ini"))
        self.phoneNumber = self.config.get("Telephony","phoneNumber")
        self.relayPort = self.config.get("Default","RelayPort")
        self.relaySerial = self.config.get("Default","RelaySerial")

    def closeRelay(self):
        command = "CommandApp_USBRelay  "+self.relaySerial+" close "+self.relayPort
        os.system(command)
        self.logger.info("close the relay")

    def openRelay(self):
        command = "CommandApp_USBRelay  "+self.relaySerial+" open "+self.relayPort
        os.system(command)
        self.logger.info("open the relay")

    def game_test(self,times,testloop):
        self.logger.info("==========Begin to test game (1)==========")
        self.device.press.home()
        self.device.press.home()
        self.device.delay(2)
        self.start_activity(self.appconfig("Game","package"),self.appconfig("Game","activity"))

        battery_start = self.get_battery()
        self.logger.info("battery_start: %s" %battery_start)

        self.logger.info(u'手动点击游戏，进入教学模式，操作时间30秒')
        for i in range(2):
            self.device.delay(20)
            self.device.click(100,100)  #点两下后，正式开始游戏

        self.device.delay(2)
        self.logger.info("==========Paly games "+str(times)+"mins==========")
        self.closeRelay()
        self.device.delay(60*times)
        self.openRelay()
        self.device.delay(2)

        battery_finish = self.get_battery()
        self.logger.info("battery_finish: %s" %battery_finish)
        self.updateResult("game_battery",battery_finish,testloop)
        game_battery = int(battery_start)-int(battery_finish)
        self.logger.info("game_battery: %s" %game_battery)

        self.device.press.home()
        self.logger.info('==========Test game has been completed (1)==========')
        return game_battery

    def play_music(self,times,testloop):
        self.logger.info("==========Begin to play music (2)==========")
        self.device.press.home()
        self.device.press.home()
        self.setDisplay('1 minute')
        battery_start = self.get_battery()
        self.logger.info("battery_start: %s" %battery_start)
        self.start_activity(self.appconfig("Music","package"),self.appconfig("Music","activity"))

        #play music
        if self.device(resourceId=self.appconfig("Music","id_next")).wait.exists(timeout=5000):
            self.device(resourceId=self.appconfig("Music","id_next")).click()
        else:
            self.logger.info(u"没有找到控件，请手动播放音乐，操作时间20秒")
            self.warnByCall()

        self.device.delay(2)
        self.logger.debug("==========Playing Music "+str(times)+"mins==========")
        self.closeRelay()
        self.device.delay(60*times)
        self.openRelay()
        self.device.delay(2)

        #pause music
        if self.device(resourceId=self.appconfig("Music","id_pause")).wait.exists(timeout=5000):
            self.device(resourceId=self.appconfig("Music","id_pause")).click()
        else:
            self.logger.info(u"没有找到控件，请手动停止音乐，操作时间15秒")
            self.warnByCall()

        battery_finish = self.get_battery()
        self.logger.info("battery_finish: %s" %battery_finish)
        self.updateResult("music_battery",battery_finish,testloop)
        music_battery = int(battery_start)-int(battery_finish)
        self.logger.info("music_battery: %s" %music_battery)

        self.device.wakeup()
        self.device.press.home()
        self.setDisplay('Never')
        self.logger.info("==========Test music has been completed (2)==========")
        return music_battery

    def tencent_video_test(self,times,testloop,networktype):
        self.logger.info("==========Begin to play video (3)==========")
        self.openwifi()

        self.start_activity(self.appconfig("Tencent","package"),self.appconfig("Tencent","activity"))
        battery_start = self.get_battery()
        self.logger.info("battery_start: %s" %battery_start)

        #click search box
        if self.device(resourceId=self.appconfig("Tencent","id_search")).wait.exists(timeout = 5000):
            self.device(resourceId=self.appconfig("Tencent","id_search")).click()
        else:
            self.logger.info(u'没有找到搜索框，请点击腾讯视频搜索框，操作时间20秒')
            self.warnByCall()
        #click films history
        if self.device(resourceId=self.appconfig("Tencent","id_search_history")).wait.exists(timeout=5000):
            self.device(resourceId=self.appconfig("Tencent","id_search_history")).click()
        else:
            self.logger.info(u'没有找到历史记录，请点搜索要播放的视频，操作时间30秒')
            self.warnByCall()
        #click episode 1
        if self.device(text="1").wait.exists(timeout=5000):
            self.device(text="1").click()
        else:
            self.logger.info(u'没有找到第1集，请手动选择集数，操作时间20秒')
            self.warnByCall()

        self.device.delay(2)
        self.logger.debug("==========Watching "+str(times)+"mins==========")
        self.closeRelay()
        self.device.delay(60*times)
        self.openRelay()
        self.device.delay(2)

        battery_finish = self.get_battery()
        self.logger.debug("battery_finish: %s" %battery_finish)
        t_video_battery = int(battery_start)-int(battery_finish)
        self.updateResult("tencentvideo_battery",battery_finish,testloop)
        self.logger.info("tencentvideo_battery: %s" %t_video_battery)

        self.device.press.back()
        self.device.press.back()
        self.device.press.back()
        self.device.press.back()
        self.device.press.home()
        self.closewifi()
        self.logger.info("==========Test video has been completed (3)==========")
        return t_video_battery

    def Call_test(self,times,testloop):
        self.logger.info("==========Begin to test call (4)==========")
        self.setDisplay('1 minute')
        battery_start = self.get_battery()
        self.logger.info("battery_start: %s" %battery_start)

        command = "adb -s "+self.m_device +" shell am start -a android.intent.action.CALL -d tel:"+self.phoneNumber
        os.system(command)
        self.logger.info("phoneNumber:%s"%self.phoneNumber)

        self.device.delay(2)
        self.logger.info("==========Call test "+str(times)+"mins==========")
        self.closeRelay()
        self.device.delay(times*60)
        self.openRelay()
        self.device.delay(2)

        command='adb shell input keyevent KEYCODE_ENDCALL'
        os.system(command)

        self.device.delay(2)
        battery_finish = self.get_battery()
        self.logger.info("battery_finish: %s" %battery_finish)
        call_battery = int(battery_start)-int(battery_finish)
        self.updateResult("call_battery",battery_finish,testloop)
        self.logger.info("call_battery: %s" %call_battery)

        self.device.press.home()
        self.setDisplay('Never')
        self.logger.info("==========Test call has been completed (4)==========")
        return call_battery

    def camera_test(self,camera_times,recording_times,testloop):
        self.logger.info("==========Begin to test camera (5)==========")
        self.device.press.home()
        self.device.press.home()
        self.device.delay(2)
        self.start_activity(self.appconfig("Camera","package"),self.appconfig("Camera","activity"))

        battery_start = self.get_battery()
        self.logger.info("battery_start: %s" %battery_start)

        self.device.delay(2)
        if self.device(text='PHOTO').exists:
            self.device(text='PHOTO').click()
        else:
            self.logger.info(u'没有找到PHOTO，请手动点击，操作时间10秒')
            self.warnByCall()

        os.chdir(self.appconfig('Filepath','path'))
        p=subprocess.Popen("camera.bat")

        self.device.delay(2)
        self.logger.info("==========Take photo test "+str(camera_times)+"mins==========")
        self.closeRelay()
        self.device.delay(60*camera_times)
        self.openRelay()
        self.device.delay(2)

        #kill shell pid
        shell_pid = self.get_shell_pid()
        self.logger.info("kill shell pid %s"%shell_pid)
        kill_command="adb -s "+self.m_device+" shell kill "+shell_pid
        if not shell_pid=="":
            os.system(kill_command)
            self.logger.info("kill shell pid success")

        #switch video recording
        if self.device(text='VIDEO').exists:
            self.device(text='VIDEO').click()
        else:
            self.logger.info(u'没有找到VIDEO，无法录制视频，请手动操作，操作时间20秒')
            self.warnByCall()

        self.device.delay(2)
        self.device(resourceId=self.appconfig("Camera","id_shutter")).click()
        self.device.delay(2)
        self.logger.info("==========Recording test "+str(recording_times)+"mins==========")
        self.closeRelay()
        self.device.delay(60*recording_times)
        self.openRelay()
        self.device.delay(2)
        #stop video recording
        if self.device(resourceId=self.appconfig("Camera","id_pause")).wait.exists(timeout=3000):
            self.device(resourceId=self.appconfig("Camera","id_pause")).click()

        battery_finish = self.get_battery()
        self.logger.info("battery_finish: %s" %battery_finish)
        camera_battery = int(battery_start)-int(battery_finish)
        self.updateResult("camera_battery",battery_finish,testloop)
        self.logger.info("camera_battery: %s" %camera_battery)

        self.device.press.back()
        self.device.press.home()
        self.logger.info("==========Test camera has been completed (5)==========")
        return camera_battery

    def browser_test(self,times,testloop):
        self.logger.info("==========Begin to test browser (6)==========")
        self.device.press.home()
        self.device.press.home()
        self.device.delay(2)
        self.start_activity(self.appconfig("Browser","package"),self.appconfig("Browser","activity"))

        battery_start = self.get_battery()
        self.logger.info("battery_start: %s" %battery_start)

        if self.device(resourceId=self.appconfig("Browser","id_url")).wait.exists(timeout=5000):
            self.device(resourceId=self.appconfig("Browser","id_url")).set_text(self.appconfig("Browser","websit"))
            self.device.delay(2)
            self.device.press.enter()
        else:
            self.device.info(u'没有找到输入框，请从历史记录手动进入网站，操作时间20秒')
            self.warnByCall()

        self.device.delay(2)
        self.logger.info("==========Browser test "+str(times)+"mins==========")
        self.closeRelay()
        self.device.delay(60*times)
        self.openRelay()
        self.device.delay(2)

        battery_finish = self.get_battery()
        self.logger.info("battery_finish: %s" %battery_finish)
        browser_battery = int(battery_start)-int(battery_finish)
        self.updateResult("browser_battery",battery_finish,testloop)
        self.logger.info("browser_battery: %s" %browser_battery)

        self.device.press.home()
        self.logger.info("==========Test browser has been completed (6)==========")
        return browser_battery

    def baidumap_test(self,times,testloop):
        self.logger.info("==========Begin to test map (7)==========")
        self.device.press.home()
        self.device.press.home()
        self.openGPS()
        self.device.delay(2)
        self.start_activity(self.appconfig("Map","package"),self.appconfig("Map","activity"))

        battery_start = self.get_battery()
        self.logger.info("battery_start: %s" %battery_start)

        if self.clickByResourceId(self.appconfig('Map','id_searchbox'),u'搜索框'):
            if self.clickByResourceId(self.appconfig('Map','id_history'),u'历史记录'):
                self.device.delay(15)
                self.device.click(600,930)  #点击到这去
                if self.clickByText(u'步行',10000):
                    self.device.delay(15)
                    self.device.click(380,1130) #点击跟我走
        else:
            self.logger.info(u'自行设置地图导航，操作时间30秒')

        if not self.device(text=u'查看全览').wait.exists(timeout=10000):
            self.warnByCall()
        self.device.delay(2)
        self.logger.info("==========Map test "+str(times)+"mins==========")
        self.closeRelay()
        self.device.delay(60*times)
        self.openRelay()
        self.device.delay(2)

        battery_finish = self.get_battery()
        self.logger.info("battery_finish: %s" %battery_finish)
        self.updateResult("baidumap_battery",battery_finish,testloop)
        baidumap_battery = int(battery_start)-int(battery_finish)
        self.logger.info("baidumap_battery: %s" %baidumap_battery)

        self.device.press.back()
        self.device.press.back()
        self.device.press.back()
        self.device.press.home()
        self.closeGPS()
        self.logger.info("==========Test map has been completed (7)==========")
        return baidumap_battery

    def sina_weibo_test(self,times,testloop):
        self.logger.info("==========Begin to test weibo (8)==========")
        self.device.press.home()
        self.device.press.home()
        self.device.delay(2)
        self.start_activity(self.appconfig("Weibo","package"),self.appconfig("Weibo","activity"))

        battery_start = self.get_battery()
        self.logger.info("battery_start: %s" %battery_start)

        os.chdir(self.appconfig('Filepath','path'))
        p=subprocess.Popen("weibo.bat")

        self.device.delay(2)
        self.logger.info("==========Weibo test "+str(times)+"mins==========")
        self.closeRelay()
        self.device.delay(60*times)
        self.openRelay()
        self.device.delay(2)

        #kill shell pid
        shell_pid = self.get_shell_pid()
        self.logger.info("kill shell pid %s"%shell_pid)
        kill_command="adb -s "+self.m_device+" shell kill "+shell_pid
        if not shell_pid=="":
            os.system(kill_command)
            self.logger.info("kill shell pid success")

        battery_finish = self.get_battery()
        self.logger.info("battery_finish: %s" %battery_finish)
        weibo_battery = int(battery_start)-int(battery_finish)
        self.updateResult("weibo_battery",battery_finish,testloop)
        self.logger.info("weibo_battery: %s" %weibo_battery)

        self.device.press.home()
        self.logger.info("==========Test weibo has been completed (8)==========")
        return weibo_battery

    def wechat_test(self,times,testloop):
        self.logger.info("==========Begin to test Wechat (9)==========")
        self.device.press.home()
        self.device.press.home()
        self.device.delay(2)
        self.start_activity(self.appconfig("WeChat","package"),self.appconfig("WeChat","activity"))

        battery_start = self.get_battery()
        self.logger.info("battery_start: %s" %battery_start)

        self.logger.info(u'手动点击微信团队，进入对话，弹出输入法框，操作时间20秒')
        self.warnByCall()
        self.device.delay(40)
        os.chdir(self.appconfig('Filepath','path'))
        subprocess.Popen("wechat.bat")

        self.device.delay(2)
        self.logger.info("==========Wechat test "+str(times)+"mins==========")
        self.closeRelay()
        self.device.delay(60*times+20)
        self.openRelay()
        self.device.delay(2)

        #kill shell pid
        shell_pid = self.get_shell_pid()
        self.logger.info("kill shell pid %s"%shell_pid)
        kill_command="adb -s "+self.m_device+" shell kill "+shell_pid
        if not shell_pid=="":
            os.system(kill_command)
            self.logger.info("kill shell pid success")

        battery_finish = self.get_battery()
        self.logger.info("battery_finish: %s" %battery_finish)
        wechat_battery = int(battery_start)-int(battery_finish)
        self.updateResult("wechat_battery",battery_finish,testloop)
        self.logger.info("wechat_battery: %s" %wechat_battery)

        self.device.press.home()
        self.logger.info("==========Test wechat has been completed (9)==========")
        return wechat_battery

    def start_activity(self,packet,activity):
        data = self.device.server.adb.shell("am start -n %s/%s"%(packet,activity))
        if data.find("Error")>-1:
            self.logger.error("Fail: %s/%s" %(packet,activity))
            return False
        self.logger.info("start_activity %s success."%activity)
        return True

    def get_shell_pid(self):
        sh_pid=""
        findpid_command = 'adb -s '+self.m_device+' shell ps |findstr "sh" '
        self.logger.info(self.m_device)
        p = subprocess.Popen(findpid_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        returnValue= p.communicate()[0]
        self.logger.info("shellpid info:%s"%returnValue)
        pidlist = returnValue.split("\n")
        for loop in range(len(pidlist)):
            if " sh\r" in pidlist[loop]:
                self.logger.info(pidlist[loop])
                self.logger.info("find shell process")
                sh_pidinfo = pidlist[loop]
                self.logger.info("sh_pidinfo:%s"%sh_pidinfo)
                pidinfo_list = sh_pidinfo.split()
                sh_pid=pidinfo_list[1]
                self.logger.info("sh_pid is:%s"%sh_pid)
                break
        else:
            self.logger.info("can not find shell process")
        return sh_pid

    def updateResult(self,battery_type,battery_finish,loop):
        self.config.read(self.appconfig('Filepath','path')+'result.ini')
        section = "loop_"+str(loop+1)
        self.config.set(section, battery_type, battery_finish)
        self.config.write(open(self.appconfig('Filepath','path')+'result.ini', "r+"))
        self.logger.info("update %s success"%battery_type)

    def setDisplay(self,mode):
        self.logger.info("change display to "+mode)
        self.device.press.home()
        self.device.press.home()
        if self.device(text='Settings').wait.exists(timeout=3000):
            self.device(text='Settings').click()
        self.device.delay(2)
        self.device(scrollable=True).scroll.to(text='Display')
        self.device(text="Display").click()
        if self.device(text="Sleep").wait.exists(timeout=3000):
            self.device(text="Sleep").click()
        if self.device(text=mode).wait.exists(timeout=3000):
            self.device(text=mode).click()
            self.logger.info("change display to "+mode+" success")
        self.device.press.back()
        self.device.press.back()

    def openwifi(self):
        self.logger.info("Begin to open wifi.")
        self.device.press.home()
        self.device.press.home()
        if self.device(text='Settings').wait.exists(timeout=5000):
            self.device(text='Settings').click()
        self.device.delay(2)
        self.device(scrollable=True).scroll.to(text='Wi‑Fi')
        self.device(text="Wi‑Fi").click()
        if self.device(text="OFF").wait.exists(timeout=3000):
            self.device(text="OFF").click()
        if self.device(text="ON").wait.exists(timeout=3000):
            self.logger.info(u"Wifi已经打开，请连接AP，操作时间30s")
            self.device.delay(30)
            self.device.press.back()
            self.device.press.back()
            self.device.press.home()

    def closewifi(self):
        self.logger.debug("Begin to close wifi.")
        self.device.press.home()
        self.device.press.home()
        if self.device(text='Settings').wait.exists(timeout=5000):
            self.device(text='Settings').click()
        self.device.delay(2)
        self.device(scrollable=True).scroll.to(text='Wi‑Fi')
        self.device(text="Wi‑Fi").click()
        if self.device(text="ON").wait.exists(timeout=3000):
            self.device(text="ON").click()
        if self.device(text="OFF").wait.exists(timeout=3000):
            self.logger.info("Wifi has been closed.")
            self.device.press.back()
            self.device.press.back()
            self.device.press.home()

    def openGPS(self):
        self.logger.debug("Begin to open gps.")
        self.device.press.home()
        self.device.press.home()
        if self.device(text='Settings').wait.exists(timeout=5000):
            self.device(text='Settings').click()
        self.device.delay(2)
        self.device(scrollable=True).scroll.to(text='Location')
        self.device(text='Location').click()
        if self.device(text='Off').wait.exists(timeout=3000):
            self.device(text='Off').click()
        if self.device(text='On').wait.exists(timeout=3000):
            self.logger.info('GPS has been opened')
            self.device.press.back()
            self.device.press.back()
            self.device.press.home()

    def closeGPS(self):
        self.logger.debug("Begin to close gps")
        self.device.press.home()
        self.device.press.home()
        if self.device(text='Settings').wait.exists(timeout=5000):
            self.device(text='Settings').click()
        self.device.delay(2)
        self.device(scrollable=True).scroll.to(text='Location')
        self.device(text='Location').click()
        if self.device(text='On').wait.exists(timeout=3000):
            self.device(text='On').click()
        if self.device(text='Off').wait.exists(timeout=3000):
            self.logger.info('GPS has been closed')
            self.device.press.back()
            self.device.press.back()
            self.device.press.home()

    def get_battery(self):
        command = "adb -s "+self.m_device+" shell cat sys/class/power_supply/battery/capacity"
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        battery= p.communicate()[0]
        return battery.strip()

    def clickByResourceId(self,id,content,times=5000):
        if self.device(resourceId=id).wait.exists(timeout=times):
            self.device(resourceId=id).click()
            return True
        else:
            self.logger.info(u'没有找到:'+content+u',请手动操作')
            return False

    def clickByText(self,text_,times=5000):
        if self.device(text=text_).wait.exists(timeout=times):
            self.device(text=text_).click()
            return True
        else:
            self.logger.info(u'没有找到:'+text_+u',请手动操作')
            return False

    def warnByCall(self,times=20,phone='18566112639'):
        command = "adb -s "+self.m_device +" shell am start -a android.intent.action.CALL -d tel:"+phone
        os.system(command)
        self.device.delay(times)
        command='adb shell input keyevent KEYCODE_ENDCALL'
        os.system(command)

    def warnBySendSMS(self,item,phone='18566112639'):
        command="adb -s "+self.device+" shell am start -a android.intent.action.SENDTO -d sms:"+phone+" --es sms_body "+item
        os.system(command)

if __name__ == '__main__':
    pass
            