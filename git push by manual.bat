:: TITLE SETTING
title %~n0


:: MINIMIZED WINDOW SETTING
if not "%minimized%"=="" goto :minimized
set minimized=true
start /min cmd /C "%~dpnx0"
goto :EOF
:minimized


:: VARIABLE DEFINATION SETTING
chcp 65001
@echo off
@rem @echo on
setlocal
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyyMMddHHmmss=%%i
cls


:: COMMIT MENT SETTING
::set commit_ment=%yyyyMMddHHmmss%
::set commit_ment=테스트 푸쉬
set commit_ment=작업 이력은 README.md 의 DONE 참조요함(%yyyyMMddHHmmss%)



:: GIT PUSH
git add *  
git commit -m "%commit_ment%" 
git push -u origin main  
git status | find "working tree clean" 



:: GET PROJECT_DIRECTORY
set DIRECTORY_THAT_CONTAINING_GIT_FILE=%cd%
CD ..
set USELESS_PART=%cd%
echo %DIRECTORY_THAT_CONTAINING_GIT_FILE%
echo %USELESS_PART%
SET PROJECT_DIRECTORY=%DIRECTORY_THAT_CONTAINING_GIT_FILE%
SET PROJECT_DIRECTORY=%PROJECT_DIRECTORY:*\=FOO%
SET PROJECT_DIRECTORY=%PROJECT_DIRECTORY:*\=FOO%
SET PROJECT_DIRECTORY=%PROJECT_DIRECTORY:*\=FOO%
SET PROJECT_DIRECTORY=%PROJECT_DIRECTORY:*\=FOO%
SET PROJECT_DIRECTORY=%PROJECT_DIRECTORY:*\=FOO%
SET PROJECT_DIRECTORY=%PROJECT_DIRECTORY:*\=FOO%
SET PROJECT_DIRECTORY=%PROJECT_DIRECTORY:*\=FOO%
SET PROJECT_DIRECTORY=%PROJECT_DIRECTORY:*\=FOO%
SET PROJECT_DIRECTORY=%PROJECT_DIRECTORY:*FOO=%
ECHO %PROJECT_DIRECTORY%


:: CHECK GIT HUB PUSH DONE (Now)
explorer https://github.com/PARK4139/%PROJECT_DIRECTORY%



:: debug
timeout 600