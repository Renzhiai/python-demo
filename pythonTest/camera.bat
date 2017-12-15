@echo off &color 0a&setlocal enabledelayedexpansion&title %~n0
@mode con lines=60 cols=100


adb shell ls >nul

IF %ERRORLEVEL% ==0 goto 0
IF NOT %ERRORLEVEL% ==0 goto 1



ping -n 1 127.0.0.1>nul

adb  shell < start_camera.txt

::adb shell sh /sdcard/QQ_auto.sh

echo.
echo.







pause