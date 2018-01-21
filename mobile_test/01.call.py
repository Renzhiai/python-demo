#coding:utf-8
import rza.c.common as common
import time
from uiautomator import device as d
from datetime import datetime
#log保存位置d:/call.log
#截图保存位置d:/img/xxx.png

def enter_call_settings():
	common.press_recent()
	if d(text="Call").wait.exists():
		d(text="Call").click()
		if d(description="More options").wait.exists():
			d(description="More options").click()
			if d(text="Settings").wait.exists():
				d(text="Settings").click()
				if d(text="Call settings").wait.exists():
					d(text="Call settings").click()
					common.log("进入电话设置")
				else:
					common.log("控件未找到，保存截图")
					common.save_fail_img()
			else:
				common.log("控件未找到，保存截图")
				common.save_fail_img()
		else:
			common.log("控件未找到，保存截图")
			common.save_fail_img()
	else:
		common.log("控件未找到，保存截图")
		common.save_fail_img()

def loop_voicemail():
	options=["Voicemail","Fixed Dialing Numbers","Service Dialing Numbers","Call duration",
				"GSM call settings","VoLTE setting","Dual mic noise reduction"]
	if d(text="Voicemail").wait.exists():
		d(text="Voicemail").click()
		options=["Service","Setup","Sound","Vibrate"]
		for i in range(4):
			if d(text=options[i]).wait.exists():
				d(text=options[i]).click()
				time.sleep(1)
				d.press("back")
				time.sleep(1)
			else:
				common.log("text="+options[i]+"未找到，保存截图")
				common.save_fail_img()
	else:
		common.log("text=Voicemail未找到，保存截图")
		common.save_fail_img()
			
def loop_fdn():
	if d(text="Fixed Dialing Numbers").wait.exists():
		d(text="Fixed Dialing Numbers").click()
		if d(text="Enable FDN").wait.exists():
			d(text="Enable FDN").click()
			time.sleep(2)
			if d(text="Cancel").wait.exists():
				d(text="Cancel").click()
				if d(text="Change PIN2").wait.exists():
					d(text="Change PIN2").click()
					time.sleep(2)
					if d(text="Cancel").wait.exists():
						d(text="Cancel").click()
						if d(text="FDN list").wait.exists():
							d(text="FDN list").click()
							if d(description="More options").wait.exists():
								d(description="More options").click()
								if d(text="Add contact").wait.exists():
									d(text="Add contact").click()
									if d(description="More options").wait.exists():
										d(description="More options").click()
										if d(text="Import from contacts").wait.exists():
											d(text="Import from contacts").click()
											if d(text="Contacts").wait.exists():
												d(text="Contacts").click()
												if d(index=2,className="android.view.ViewGroup").wait.exists():
													d(index=2,className="android.view.ViewGroup").click()
													time.sleep(2)
													for i in range(3):
														d.press("back")
														time.sleep(2)
												else:
													common.log("index=2未找到，保存截图")
													common.save_fail_img()
											else:
												common.log("text=Contacts未找到，保存截图")
												common.save_fail_img()
										else:
											common.log("text=Import from contacts未找到，保存截图")
											common.save_fail_img()
									else:
										common.log("description=More options未找到，保存截图")
										common.save_fail_img()
								else:
									common.log("text=Add contact未找到，保存截图")
									common.save_fail_img()
							else:
								common.log("description=More options未找到，保存截图")
								common.save_fail_img()
						else:
							common.log("text=FDN list未找到，保存截图")
							common.save_fail_img()
					else:
						common.log("text=Cancel未找到，保存截图")
						common.save_fail_img()								
				else:
					common.log("text=Change PIN2未找到，保存截图")
					common.save_fail_img()									
			else:
				common.log("text=Cancel未找到，保存截图")
				common.save_fail_img()																						
		else:
			common.log("text=Enable FDN未找到，保存截图")
			common.save_fail_img()
	else:
		common.log("text=Fixed Dialing Numbers未找到，保存截图")
		common.save_fail_img()
			
def loop_sdn():
	if d(text="Service Dialing Numbers").wait.exists():
		d(text="Service Dialing Numbers").click()
		d.press("back")
	else:
		common.log("text=Service Dialing Numbers未找到，保存截图")
		common.save_fail_img()
		
def loop_callduration():
	if d(text="Call duration").wait.exists():
		d(text="Call duration").click()
		for i in range(5):
			if i!=4:
				if d(index=i,className="android.widget.TwoLineListItem").wait.exists():
					#swipe等于长按
					d(index=i,className="android.widget.TwoLineListItem").swipe.right(steps=100)
					
					if d(text="Cancel").wait.exists():
						d(text="Cancel").click()
					else:
						common.log("text=Cancel未找到，保存截图")
						common.save_fail_img()
				else:
					common.log("index="+str(i)+"未找到，保存截图")
					common.save_fail_img()
		d.press("back")
	else:
		common.log("text=Call duration未找到，保存截图")
		common.save_fail_img()
		
def loop_gsmcallsettings():
	if d(text="GSM call settings").wait.exists():
		d(text="GSM call settings").click()
		if d(text="Call forwarding").wait.exists():
			d(text="Call forwarding").click()
			time.sleep(4)
			if d(text="Call forwarding settings").wait.exists(timeout=29000):
				options1=["Always forward","When busy","When unanswered","When unreachable"]
				for i in range(4):
					if d(text=options1[i],resourceId="android:id/title").wait.exists():
						d(text=options1[i],resourceId="android:id/title").click()
						time.sleep(2)
						if d(text="Cancel").wait.exists():
							d(text="Cancel").click()
						else:
							common.log("text=Cancel未找到，保存截图")
							common.save_fail_img()
					else:
						common.log("text="+options1[i]+"未找到，保存截图")
						common.save_fail_img()
				time.sleep(1)		
				d.press("back")
				if d(text="Additional settings").wait.exists(timeout=29000):
					d(text="Additional settings").click()
					time.sleep(4)
					if d(text="Call waiting").wait.exists(timeout=29000):
						d(text="Call waiting").click()
						time.sleep(15)
						d.press("back")
						if d(text="Call barring").wait.exists():
							d(text="Call barring").click()
							if d(text="Outgoing call barring").wait.exists(timeout=29000):
								options2=["Outgoing call barring","Incoming call barring","Cancel all call barring","Change password"]
								for j in range(4):
									if d(text=options2[j]).wait.exists():
										d(text=options2[j]).click()
										if d(text="Cancel").wait.exists():
											d(text="Cancel").click()
										else:
											common.log("text=Cancel未找到，保存截图")
											common.save_fail_img()
									else:
										common.log("text="+options2[j]+"未找到，保存截图")
										common.save_fail_img()
								time.sleep(1)
								d.press("back")
								time.sleep(1)
								d.press("back")
							else:
								common.log("text=Outgoing call barring未找到，保存截图")
								common.save_fail_img()
						else:
							common.log("text=Call barring未找到，保存截图")
							common.save_fail_img()
					else:
						common.log("text=Call waiting未找到，保存截图")
						common.save_fail_img()
				else:
					common.log("text=Additional settings未找到，保存截图")
					common.save_fail_img()
			else:
				common.log("text=Call forwarding settings未找到，保存截图")
				common.save_fail_img()
		else:
			common.log("text=Call forwarding未找到，保存截图")
			common.save_fail_img()
	else:
		common.log("text=GSM call settings未找到，保存截图")
		common.save_fail_img()	
		
def loop_voletsetting():
	if d(text="VoLTE setting").wait.exists():
		d(text="VoLTE setting").click()
		if d(text="VoLTE").wait.exists():
			d(text="VoLTE").click()
			d.press("back")
		else:
			common.log("text=VoLTE未找到，保存截图")
			common.save_fail_img()
	else:
		common.log("text=VoLTE setting未找到，保存截图")
		common.save_fail_img()		

def loop_dmnr():
	if d(text="Dual mic noise reduction").wait.exists():
		d(text="Dual mic noise reduction").click()
	else:
		common.log("text=Dual mic noise reduction未找到，保存截图")
		common.save_fail_img()

if __name__=="__main__":
	enter_call_settings()
	loop_voicemail()
	loop_fdn()
	loop_sdn()
	loop_callduration()
	loop_gsmcallsettings()
	loop_voletsetting()
	loop_dmnr()