:: 메아리 설정
@echo off

:: 콘솔 제목 설정
title %~n0

:: maximized window 설정
if not "%maximized%"=="" goto :maximized
set maximized=true
start /max cmd /C "%~dpnx0"
goto :EOF
:maximized

:: minimized window 설정
@REM if not "%minimized%"=="" goto :minimized
@REM set minimized=true
@REM start /min cmd /C "%~dpnx0"
@REM goto :EOF
@REM :minimized



:: admin mode 설정
@REM >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
@REM if '%errorlevel%' NEQ '0' ( echo Requesting administrative privileges... goto UACPrompt 
@REM ) else ( goto gotAdmin ) 
@REM :UACPrompt 
	@REM echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs" 
	@REM set params = %*:"="" 
	@REM echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" 
	@REM "%temp%\getadmin.vbs" 
	@REM del "%temp%\getadmin.vbs" 
	@REM exit /B 
@REM :gotAdmin
	@REM pushd "%CD%"
	@REM CD /D "%~dp0"
@REM :------------------------------------------ below cript will acted as administrator mode ------------------------------------------ 



:: 콘솔 색 설정
color df

:: korean encoding 설정
chcp 65001 >nul

:: local ENVIRONMENT mode 설정
:: setlocal


:: 콘솔 화면 정리
cls



:: 프로젝트로 이동
:: cd "C:\Users\WIN10PROPC3\Desktop\services\helper-from-nothing-to-controlled-trash-bin"


:: 파이썬 가상환경 실행
cmd /k call ".\.venv\Scripts\activate.bat"


:: debugging 설정
timeout 60