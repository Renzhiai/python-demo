#coding:utf-8
import os
import subprocess

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
