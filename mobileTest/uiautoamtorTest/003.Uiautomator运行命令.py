#coding:utf-8
import os

pcName="com.test.TestDemo";
jarName="Test";
androidSdkID="7";
path="D:/uiauto/Uiautomator";
command1="d:";
command2="cd adt/sdk/tools";
command3="android create uitest-project -n "+jarName+" -t "+androidSdkID+" -p "+path;
command4="cd "+path;
command5="ant build";
command6="adb push "+path+"/bin/"+jarName+".jar"+" data/local/tmp";
command7="adb shell uiautomator runtest "+jarName+".jar"+" -c "+pcName;

os.system(command1+"&"+command2+"&"+command3+"&"+command4+"&"+command5+"&"+command6+"&"+command7)
