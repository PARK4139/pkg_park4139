# -*- coding: utf-8 -*-
from BlurWindow.blurWindow import blur
from bs4 import BeautifulSoup as bs
from datetime import datetime
from gtts import gTTS
from mutagen.mp3 import MP3
from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
# from random import randint, random
from screeninfo import get_monitors
from selenium import webdriver
from sys import argv
from urllib.parse import unquote
import clipboard
import googletrans
import json
import os
import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리
import pyautogui
import pyperclip
import pyttsx3
import random
import re
import requests
import shutil
import signal
import subprocess
import sys
import time
import traceback
import win32api
from datetime import timedelta

 
# _________________________________________________________________________________________ mkr: new
class park4139:
    directory_to_work = ''
    log_directory=''
    trouble_yn='n'
    debug_mode_yn ="n"
    string_space_promised = '      '
    time_s = 0.0
    time_e = 0.0

    def __init__(self,directory_to_work,log_directory):
        self.directory_to_work =directory_to_work
        self.log_directory=log_directory
        os.system('chcp 65001 > nul')
        
    def sleep(self, milliseconds):
        seconds =milliseconds/1000
        time.sleep(seconds)

    def bkup(self,bkup_service_host_file ,file_to_bkup): 
        try:
            cmd = fr'start cmd /c call "{bkup_service_host_file}" "{file_to_bkup}"'
            # print(fr"test command >{self.string_space_promised}{cmd}")
            park4139.run_command(self,cmd, intended_working_directory=os.path.dirname(bkup_service_host_file))
        except:
            park4139.trouble_shoot('20231204132424')
    
    
    # 2023-12-03 일요일 13:06 최신화 함수
    def get_python_pkg_global_path(self):
        for path in sys.path:
            print(path)
            if self.is_regex_in_contents(contents=path, regex='site-packages') == True:
                print(rf'echo "{path}"')
                os.system(rf'echo "{path}" | clip.exe ')
                os.system(rf'explorer "{path}"')
                os.exit()

    # 2023-12-03 일요일 13:25 최신화 함수
    @staticmethod
    def pause():
        os.system('pause')


    # 2023-12-03 일요일 13:25 최신화 함수
    def taskkill(self,program_exe):
        for proc in psutil.process_iter():
            try:
                process_im_name = proc.name()
                processID = proc.pid
                # print(process_im_name , '          - ', processID)
                if process_im_name.strip() == program_exe:
                    parent_pid = processID
                    parent = psutil.Process(parent_pid)
                    for child in parent.children(recursive=True):
                        child.kill()
                    parent.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  # 예외처리
                pass

    # # 2023-12-03 일요일 13:25 최신화 변수명 출력함수
    # def print(variable):
    #     def namestr(obj, namespace):
    #         get_name = [name for name in namespace if namespace[name] is obj]
    #         return get_name[0]
        
    #     def Change(variable):
    #         print(namestr(variable, globals()), "=", variable)

    #     print(f'{Change(variable)} : {variable}')
    

    def speak(self,ment):
        helper_py = rf"C:\Users\WIN10PROPC3\Desktop\services\helper-from-text-to-speech\helper.py"
        try:
            os.system(rf'python "{helper_py}" "{ment}"')
        except:
            park4139.trouble_shoot('20231202231750')
        os.chdir(self.directory_to_work)
        print(ment)


    def speaks(self,ments):
        for ment in ments:
            self.speak(ment)


    # 2023-12-03 일요일 13:25 최신화 함수
    def trouble_shoot(self,id: str):
        # for development
        print(f':: _______________________________________________________________________________________ trouble shooting id : {id}  s')
        os.system(f'echo {id}| clip.exe')
        traceback.print_exc(file=sys.stdout)
        self.speak('트러블슈팅 아이디를 클립보드에 붙여넣었습니다')
        print(f':: _______________________________________________________________________________________ trouble shooting id : {id}  e')
        os.system('pause') # 이 코드는 PRODUCTION 환경 에서는 고민이 필요함.
        self.trouble_yn = 'y'

        # for production
        # pass


    # 2023-12-03 일요일 13:25 최신화 함수
    @staticmethod
    def get_time_as_(pattern):
        now = time
        localtime = now.localtime()
        time_styles = {
            'now': str(now.time()),
            'yyyy': str(localtime.tm_year),
            'MM': str(localtime.tm_mon),
            'dd': str(localtime.tm_mday),
            'HH': str(localtime.tm_hour),
            'mm': str(localtime.tm_min),
            'ss': str(localtime.tm_sec),
            'weekday': str(localtime.tm_wday),
            'elapsed_days_from_jan_01': str(localtime.tm_yday),
        }
        for time_style_key, time_style_value in time_styles.items():
            if time_style_key == pattern:
                return time_styles[pattern]
            else:
                return str(now.strftime(pattern))

    
    def download_clip(self,url):
        try:
            # :: 다운로드가 안되면 주석 풀어 시도
            # os.system(rf'yt-dlp -U')

            # :: 다운로드 옵션 ID 확인
            print(':: 다운로드 옵션 ID 목록')
            video_id = ''
            lines = subprocess.check_output(rf'yt-dlp -F {url}', shell=True).decode('utf-8').split("\n")
            video_ids = [
                '315',
                '313',
                '303',
                '308',
                '616',
                '248',
            ]
            audio_ids = [
                '250',
                '251',
            ]
            for line in lines:
                if 'video only' in line or 'audio only' in line:
                    print(line)
                    # video setting
                    for id in video_ids:
                        if id in line:
                            video_id = id
                    # audio setting
                    for id in audio_ids:
                        if id in line:
                            audio_id = id

            # :: 다운로드 가능 옵션 ID 설정
            # if video_id not in video_ids and audio_id not in audio_ids:
            #     video_id = str(input('video option:'))
            #     audio_id = str(input('audio option:'))
            #     speak(rf'다운로드 옵션이 선택되었습니다')
            #     print(rf'video option: {video_id}  audio option: {audio_id}')
            #     speak(rf'video option: {video_id}  audio option: {audio_id}')
            # else:
            #     pass

            # :: 다운로드 디렉토리 생성
            directories = ["storage"]
            for directory in directories:
                if not os.path.isdir(rf'./{directory}'):
                    os.makedirs(rf'mkdir {directory}')

            # :: 다운로드
            print(rf':: 실행대기 명령어')
            print(rf'yt-dlp -f {video_id}+{audio_id} {url}')
            # os.system(rf'yt-dlp -f 313+251 --remux mp4 {url}')
            try:
                os.system(rf'yt-dlp -f {video_id}+{audio_id} {url}')
            except:
                print('20231129110714')



            # :: yotube 에서 고해상도 음성 없는 영상과 음성을 받아 하나의 영상으로 merge.
            print(rf':: 비디오 사운드를 하나의 파일로 만드는 중입니다')


            # :: project tree 생성
            destination = rf'{os.getcwd()}\storage'
            if not os.path.exists(destination):
                os.makedirs(destination)



            # :: 비디오/음성 파일 상대주소 get
            lines = os.listdir()
            files = []
            patterns = ['?v=', '/shorts/','&v='] #https://www.youtube.com/shorts/
            # print(rf'url : {url}')
            for line in lines:
                for pattern in patterns:
                    try:
                        clip_id = url.split(pattern)[1]
                        if park4139.is_regex_in_contents(line, clip_id) is True:
                            files.append(line)
                        else:
                            pass
                    except:
                        # print('20231201180140')
                        # traceback.print_exc(file=sys.stdout)
                        pass
            for file in files:
                print(rf'file : {file}')
            file_v = os.path.relpath(files[1], os.getcwd())
            file_a = os.path.relpath(files[0], os.getcwd())
            paths = [os.path.relpath(destination, os.getcwd()), os.path.basename(files[1])]
            file_va = os.path.join(*paths)
            print(rf'file_v : {file_v}')
            print(rf'file_a : {file_a}')
            print(rf'file_va : {file_va}') # :: 콘솔에 .webmrage 가 자꾸 출력되는 현상 '.webm' 을 sTing 에 +로 더하면 생기는 현상이었다. 디버깅 중 지워서 해결했는데 근본적인 해결방법은 아니라고 생각된다.



            # :: ffmpeg.exe 위치 설정
            ffmpeg_exe = fr"C:\Users\WIN10PROPC3\Desktop\`workspace\tool\LosslessCut-win-x64\resources\ffmpeg.exe"

            # :: 이게 trouble 원인으로 생각하고 작성한건데 잘못 짚은 것 같다.
            # trouble_characters = ['Ä' ]
            # trouble_characters_alternatives = {'Ä': 'A'}
            # for trouble_character in trouble_characters:
            #     file_v = file_v.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            #     file_a = file_a.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            #     file_va = file_va.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            #     try:
            #         if trouble_character in file_va:
            #             os.rename(file_v, file_v.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
            #             os.rename(file_a, file_a.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
            #             print(rf'파일명 변경이 되었습니다')
            #     except:
            #         print('파일명 변경 중 에러가 발생하였습니다')
            try:
                print(fr'echo y | "{ffmpeg_exe}" -i "{file_v}" -i "{file_a}" -c copy "{file_va}"')
                lines = subprocess.check_output(fr'echo y | "{ffmpeg_exe}" -i "{file_v}" -i "{file_a}" -c copy "{file_va}"', shell=True).decode('utf-8').split("\n")
                for line in lines:
                    print(line)
                print("파일머지 완료")
                park4139.log_mid(log_title = f"파일머지 완료, url: {url}")
            except:
                print('파일머지 중 에러가 발생하였습니다')
            try:
                print(rf':: 다운로드 및 merge 결과 확인')
                print(rf'explorer "{file_va}"')
                subprocess.check_output(rf'explorer "{file_va}"', shell=True).decode('utf-8').split("\n")
                print("파일실행 완료")
                park4139.log_mid(log_title = f"파일실행 완료, url: {url}")
            except:
                print('파일실행 중 에러가 발생하였습니다')


            # :: 불필요 리소스 삭제
            # merge 할때 필요했던 리소스 파일들 이제 불필요하니 삭제
            try:
                if os.path.exists(file_va):
                    subprocess.check_output(rf'echo y | del /f "{file_v}"', shell=True).decode('utf-8').split("\n")
                    lines = subprocess.check_output(rf'echo y | del /f "{file_a}"', shell=True).decode('utf-8').split("\n")
                    for line in lines:
                        print(line)
                    print("파일실행 완료")
                    park4139.log_mid(log_title = f"파일실행 완료, url: {url}")
            except:
                print('20231129112939')
        except:
            print(f'20231129112936')
            # traceback.print_exc(file=sys.stdout)
        os.chdir(self.directory_to_work)

    # 디스플레이 정보 가져오기
    @staticmethod
    def get_display_setting():
        for infos in get_monitors():
            for info in str(infos).split(','):
                if 'width=' in info.strip():
                    width = info.split('=')[1]
                elif 'height=' in info.strip():
                    height = info.split('=')[1]
        display_setting = {
            'height': int(height),
            'width': int(width)
        }
        return display_setting



    def debug_s():
        lines = subprocess.check_output("cls", shell=True).decode('utf-8').split('\n')


    def debug_e():
        # lines= subprocess.check_output("cmd /k ", shell=True).decode('utf-8').split('\n')
        lines = subprocess.check_output("pause", shell=True).decode('utf-8').split('\n')




    def print_police_line(police_line_ment):
        police_line = ''
        for i in range(0, 255 // len(police_line_ment)):
            police_line = police_line + f'{police_line_ment} '
        print(f'{police_line.upper()}')


    @staticmethod
    def is_regex_in_contents(contents, regex):
        pattern = re.compile(regex)
        m = pattern.search(context)
        if m:
            return True
        else:
            return False


    # 출력의 결과는 tasklist /svc 와 유사하다.
    def print_python_process_for_killing_zombie_process():
        for process in psutil.process_iter():
            print(process.name(), "\t" + str(process.pid), "\t" + process.status())


    def run_command(self,cmd,intended_working_directory=directory_to_work):
        if intended_working_directory != "":
            os.chdir(intended_working_directory)
        print(rf'test command >{self.string_space_promised}{cmd}')
        try:
            # os.system(cmd)
            # os.Popen 으로 print 가능하도록 할 수 있다는 것 같았는데 다른 방식으로 일단 되니까. 안되면 시도.

            # cmd = 'dir /b'
            # cmd = ['dir', '/b']
            # fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout # 명령어 실행 후 반환되는 결과를 파일에 저장합니다.
            # fd_popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout # shell=True 옵션, cmd를 string 가능하도록 설정
            # data = fd_popen.read().strip()# data에 저장합니다.
            # fd_popen.close()# 파일을 닫습니다.
            # print(data)

            try:
                lines = subprocess.check_output(cmd, shell=True).decode('utf-8').split('\n')
            except UnicodeDecodeError:
                lines = subprocess.check_output(cmd, shell=True).decode('euc-kr').split('\n')
            for line in lines:
                print(line)
        except:
            self.trouble_shoot('20231203144559')
        os.chdir(self.directory_to_work)


    # 시작로깅(json 형태로 넣을 수 있도록 코드 업데이트 할것)
    def log_s(self, log_title = "시작로깅"):
        lines = subprocess.check_output('chcp 65001 >nul', shell=True).decode('utf-8').split('\n')  # 한글 엔코딩 설정 , shell=True).decode('utf-8').split('\n')
        self.time_s = time.time()  # 서버라이프사이클 계산용 변수 설정
        server_time = self.get_time_as_(f'%Y-%m-%d %H:%M:%S')
        lines = subprocess.check_output(rf'echo "server_time  : {server_time} ,  directory_to_work  : {self.directory_to_work},  __file__  : {__file__},  log_title : {log_title} " >> "{self.log_directory}\success.log"', shell=True).decode('utf-8').split('\n')
        for line in lines:
            print(line)

    def log_mid(self,log_title = "중간로깅"):
        server_time = self.get_time_as_(f'%Y-%m-%d %H:%M:%S')
        lines = subprocess.check_output(rf'echo "server_time  : {server_time} ,  directory_to_work  : {self.directory_to_work},  __file__  : {__file__},  log_title : {log_title} " >> "{self.log_directory}\success.log"', shell=True).decode('utf-8').split('\n')
        # os.system('cls')


    def log_e(self,log_title = "종료로깅"):
        self.time_e = time.time()  # 서버라이프사이클 계산용 변수 설정
        server_time = self.get_time_as_(f'%Y-%m-%d %H:%M:%S')
        server_life_cycle = self.time_e - self.time_s
        lines = subprocess.check_output(rf'echo "server_time  : {server_time} ,  directory_to_work  : {self.directory_to_work},  __file__  : {__file__},  log_title : {log_title},  server_life_cycle : {server_life_cycle}  " >> "{self.log_directory}\success.log"', shell=True).decode('utf-8').split('\n')
        # os.system('cls')

    # 프로그램 PID 출력
    def get_current_program_pid():
        pro = subprocess.check_output(fr'powershell (Get-WmiObject Win32_Process -Filter ProcessId=$PID).ParentProcessId', shell=True).decode('utf-8')  # 실험해보니 subprocess.check_output(cmd,shell=True).decode('utf-8') 코드는 프로세스가 알아서 죽는 것 같다. 모르겠는데 " " 가 있어야 동작함
        lines = pro.split('\n')
        pids=[]
        for line in lines:
            if "" != line.strip():
                pid = line
                pids.append(pid)
                print(f'pid: {pid}')
        return pids
    
    
    def commentize(self, title):
        print(f'_________________________________________________________________ {title.replace("_","")}')
        # 아래 코드를 주석 해제하면 귀찮을 정도로 너무 말이 많을 수 있습니다.
        # self.speak(title)

    @staticmethod
    def get_target_bite(start_path = '.'):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size


    @staticmethod
    def get_target_megabite(target_path):
        return park4139.get_target_bite(target_path.strip()) / 1024 ** 2
    
    @staticmethod
    def get_target_gigabite(target_path):
        return park4139.get_target_bite(target_path.strip()) / 1024 ** 3

    @staticmethod
    def toogle_console_color(color_bg, colors_texts):
        to_right_nbsp = ''
        to_right_nbsp_cnt=150
        for i in range(0, to_right_nbsp_cnt):
            to_right_nbsp = to_right_nbsp + ' '
        for color_text in colors_texts:
            if color_bg != color_text:
                for setting_key, setting_value in park4139.get_display_setting().items():
                    pass
                for i in range(0, 32):
                    os.system(f"color {color_bg}{color_text}")

class etc:
    def __init__(self):
        pass

    # 버튼 멘트 셋팅
    button_ments = {
        'yes': '해라',
        'no': '마라',
        'again': '이따 다시물어라',
    }