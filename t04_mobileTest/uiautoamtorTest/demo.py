#coding:utf-8
#from uiautomator import Device
from uiautomator import device as d
#当搜索设备的时候，指定设备序列号
#d=Device("466b1b18")
#d=Device("466b1b18",adb_server_host="192.168.1.68",adb_server_port=5037)
#检索设备信息
#print(d.info)
#亮屏
#d.screen.on()
#d.wakeup()
#熄屏
#d.screen.off()
#d.sleep()
#检查亮屏还是熄屏
#if d.screen=="on":
#	d.sleep()
#if d.screen=="off":
#	d.wake()
#按键
#d.press.home()
#d.press.back()
#d.press("back")
#d.press("menu") #无反应
#d.press("left")
#d.press("right")
#d.press("down")
#d.press("up")
#d.press("center")
#d.press("search")
#d.press("enter")
#d.press("delete")
#d.press("recent") #查看recent app，相当于按menu键了
#d.press("volume_up")
#d.press("volume_down")
#d.press("volume_mute")
#d.press("camera")
#d.press("power")
#点击屏幕
#d.click(100,100)
#d.long_click(297,428)
#滑动
#d.swipe(306,347,306,100)
#连同图标一起拖动
#d.drag(335,484,335,100)
#方向
#print(d.orientation)	#横屏的时候显示left或者right，竖屏的时候显示natural
#d.orientation="l"
#d.orientation="r"
#d.orientation="n"
#禁止旋转
#d.freeze_rotation()
#旋转屏幕
#d.freeze_rotation(False)
#保存图片
#d.screenshot("D:/a.png")
#保存当前页面的布局
#d.dump("D:/hierarchy.xml")
#得到一个dump文本
#xml = d.dump()
#下拉状态栏
#d.open.quick_settings()
#打开通知栏
#d.open.notification()
#如果页面存在
#if d(text="Settings").exists:
	#d.press.home()
#等待当前界面空闲,默认10秒
#d.wait.idle(timeout=10000)
#d.press.home()
	
#Watcher
#创建一个watcher
#d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait").click(text="Force Close")
#d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait").press.back.home()
#d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait").press("back", "home")
#检查是否触发watcher
#d.watcher("watcher_name").triggered
#移除watcher
#d.watcher("watcher_name").remove()
#watcher集合
#d.watchers
#检查是否触发watcher
#d.watchers.triggered
#重置所有触发的watcher
#d.watchers.reset()
#移除watchers
#d.watchers.remove()
#d.watchers.remove("watcher_name")
#强制运行所有的watcher
#d.watchers.run()

#Handler
#def fc_close(d):
#	if d(text="Force Close").exists:
#		d(text="Force Close").click()
#d.handlers.on(fc_close)
#d.handlers.off(fc_close)

#Selector
#d(text="More").click()
#d(resourceId="com.android.settings:id/title").click()
#d(scrollable="false",text="Display").click()
#d(longClickable="false",text="Data usage").click()
#------------------------------------------------
#text, textContains, textMatches, textStartsWith
#className, classNameMatches
#description, descriptionContains, descriptionMatches, descriptionStartsWith
#checkable, checked, clickable, longClickable
#scrollable, enabled,focusable, focused, selected
#packageName, packageNameMatches
#resourceId, resourceIdMatches
#index, instance
#------------------------------------------------
#d.dump("D:/layout.xml")

#Child
#d(className="android.widget.FrameLayout").child(text="Bluetooth").click()

#sibling
#d.dump("D:/layout.xml")
#d(className="android.widget.ImageButton",index="2").click()	#wifi界面
#d(text="Off").sibling(className="android.widget.Switch").click()	#wifi界面
#d(text="Wi-Fi").right(className="android.widget.ImageButton").click()
#d(text="Wi-Fi").down(text="IPV6").click()
#当界面有相同文字的UI对象时，instance=0，就点第一个
#d(text="Google",instance=1).click()

#统计当前页面UI的个数
#print(d(text="Google").count)
#也可以写成下面这样
#print(len(d(text="Google")))
#迭代
#for view in d(text="Google"):
	#......

#检索当前对象的信息
#print(d(text="Settings").info)

#清除文本内容
#d(className="android.widget.EditText").clear_text()
#d(className="android.widget.EditText").set_text("这是")

#d(text="Settings").click.bottomright()
#d(text="Settings").click.topleft()
#d(text="System WebView licenses").click.wait()

#d(text="Call").long_click()
#d(text="Call").long_click.bottomright()
#d(text="Call").long_click.topletf()

#把UI对象拖到某个点
#d(text="Settings").drag.to(200,400,steps=100)
#d(text="Settings").drag.to(text="Drive",steps=100)

#滑动
#d(text="Play Store").swipe.right()
#d(text="Display").swipe.left(steps=100)
#d(text="Settings").swipe.down(steps=10)
#d(text="Settings").swipe.right()
#d(text="Settings").swipe.up()

#缩小图片
#d(resourceId="com.tct.gallery3d:id/drawer_layout").pinch.In(percent=100,steps=10)
#放大图片
#d(resourceId="com.tct.gallery3d:id/drawer_layout").pinch.Out()

#等待某个UI出现
#d(text="Dialing").wait.exists(timeout=10000)
#d.press.home()
#等待某个UI消失
#d(text="Dialing").wait.gone(timeout=10000)
#d.press("recent")

#往下滑
#d(scrollable=True).fling()
#向左滑
#d(scrollable=True).fling.horiz.forward()
#向上滑
#d(scrollable=True).fling.vert.backward()
#向左滑
#d(scrollable=True).fling.horiz.backward()
#滑到最初始位置
#d(scrollable=True).fling.horiz.toBeginning(max_swipes=1000)
#滑到底部
#d(scrollable=True).fling.toEnd()

#向下滚
#d(scrollable=True).scroll(steps=10)
#d(scrollable=True).scroll.horiz.forward(steps=100)
#向上滚
#d(scrollable=True).scroll.vert.backward()
#d(scrollable=True).scroll.horiz.toBeginning(steps=100,max_swipes=1000)
#d(scrollable=True).scroll.toEnd()
#滚到指定地点
#d(scrollable=True).scroll.to(text="Location")
