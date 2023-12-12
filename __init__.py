# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'Park4139 : Jung Hoon Park'

import openpyxl  # xls 파일 내용 가져오기, xls 파일에 내용 저장하기
import pandas  # csv, xls 파일 데이터 가져와서 핸들링하는 용도로 써보자
import linecache
# import cv2     # image recognition lib #  기본 PyAutoGUI 이미지 인식의 한계를 극복하기 위함.
# numpy
from PIL import Image, ImageFilter  # PIL : Py img lib
import random
import sys
import time
import clipboard
import keyboard
import pyautogui
import toml
import logging
import os
import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리
import pyglet
import re
import shutil
import subprocess
import traceback
import urllib.parse as parser
from datetime import datetime
from datetime import timedelta
import win32api
from mutagen.mp3 import MP3
from pytube import Playlist
# from random import randint, random
from screeninfo import get_monitors
from moviepy.editor import *
import os
import sys
import subprocess

# import cv2

logger = logging.getLogger('park4193_test_logger')
hdlr = logging.FileHandler('park4193_logger.log')
hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

'''
파일변경감지 아이디어
(이것 git으로 할 수 있잖아!)감지이벤트를 걸어 
파일변경감지 시 비동기 백업처리

'''
# 버튼 멘트 셋팅
button_ments = {
    'yes': '해라',
    'no': '마라',
    'again': '이따 다시물어라',
}


class Park4139:
    USERPROFILE = os.environ.get('USERPROFILE')
    yt_dlp_cmd = fr"{USERPROFILE}\Desktop\services\archive_py\pkg_yt_dlp\yt-dlp.cmd"
    ffmpeg_exe = fr"{USERPROFILE}\Desktop\services\archive_py\$cache_tools\dev_tools_exe\LosslessCut-win-x64\resources\ffmpeg.exe"
    db_abspath = rf"{os.getcwd()}\$cache_database\db.toml"
    db_template = {
        # 'parks2park_archive_log_line_cnt': 0,
    }
    working_directory = fr'{os.getcwd()}'
    log_directory = fr'{os.getcwd()}'
    trouble_yn = 'n'
    debug_mode_yn = "n"
    indent_space_promised = ''
    line_length_promised = '________________________________________________________________'
    time_s = 0.0
    time_e = 0.0
    # biggest_targets(300 MB 이상 빽업대상)
    biggest_targets = []
    smallest_targets = []
    keyboards = {
        "backspace": 0,
        "tab": 1,
        "enter": 2,
        "shift": 3,
        "ctrl": 4,
        "alt": 5,
        "pause": 6,
        "capslock": 7,
        "escape": 8,
        "space": 9,
        "pageup": 10,
        "pagedown": 11,
        "end": 12,
        "home": 13,
        "leftarrow": 14,
        "uparrow": 15,
        "rightarrow": 16,
        "downarrow": 17,
        "insert": 18,
        "delete": 19,
        "0": 20,
        "1": 21,
        "2": 22,
        "3": 23,
        "4": 24,
        "5": 25,
        "6": 26,
        "7": 27,
        "8": 28,
        "9": 29,
        "a": 30,
        "b": 31,
        "c": 32,
        "d": 33,
        "e": 34,
        "f": 35,
        "g": 36,
        "h": 37,
        "i": 38,
        "j": 39,
        "k": 40,
        "l": 41,
        "m": 42,
        "n": 43,
        "o": 44,
        "p": 45,
        "q": 46,
        "r": 47,
        "s": 48,
        "t": 49,
        "u": 50,
        "v": 51,
        "w": 52,
        "x": 53,
        "y": 54,
        "z": 55,
        "leftwindows": 56,
        "rightwindows": 57,
        "application": 58,
        "sleep": 59,
        "numlock": 60,
        "scrolllock": 61,
        "f1": 62,
        "f2": 63,
        "f3": 64,
        "f4": 65,
        "f5": 66,
        "f6": 67,
        "f7": 68,
        "f8": 69,
        "f9": 70,
        "f10": 71,
        "f11": 72,
        "f12": 73,
        "printscreen": 74,
        "insert": 75,
        "delete": 76,
        "home": 77,
        "end": 78,
        "pageup": 79,
        "pagedown": 80,
    }

    def __init__(self):
        os.system('chcp 65001 >nul')

    @staticmethod
    def sleep(milliseconds):
        seconds = milliseconds / 1000
        time.sleep(seconds)

    @staticmethod
    def get_os_sys_environment_variable(environment_variable_name: str):
        Park4139.commentize("모든 시스템 환경변수 출력")
        for i in os.environ:
            print(i)
        return os.environ.get(environment_variable_name)

    @staticmethod
    def update_os_sys_environment_variable(environment_variable_name: str, new_path: str):
        """시스템 환경변수 path 업데이트"""
        Park4139.commentize("테스트가 필요한 함수를 적용하였습니다")
        Park4139.commentize("기대한 결과가 나오지 않을 수 있습니다")
        Park4139.commentize("업데이트 전 시스템 환경변수")
        for i in sys.path:
            print(i)
        sys.path.insert(0, new_path)
        sys.path.append(new_path)
        Park4139.commentize("업데이트 전 시스템 환경변수")
        for i in sys.path:
            print(i)

    @staticmethod
    def get_name_space():
        Park4139.commentize("네입스페이스 출력")
        dir()
        return dir()

    @staticmethod
    def bkup(target_to_bkup):
        try:
            target_abspath = os.path.abspath(target_to_bkup)
            target_dirname = os.path.dirname(target_to_bkup)
            target_dirname_dirname = os.path.dirname(target_dirname)
            target_basename = os.path.basename(target_abspath).split(".")[0]

            # try:
            #     # 파일인 인경우 확장자 처리
            #     target_ext = os.path.basename(target_abspath).split(".")[1]
            # except Exception as e:
            #     # 디렉토리 인경우 확장자 처리
            #     target_ext = ""

            target_zip = rf'$zip_{target_basename}.zip'
            target_yyyy_mm_dd_HH_MM_SS_zip = fr'{target_basename} - {Park4139.get_time_as_("%Y %m %d %H %M %S")}.zip'

            # 파일이 위치한 드라이브로 이동
            drives = [
                "C",
                "D",
                "E",
                "F",
                "G",
            ]
            drive_where_target_is_located = target_abspath.split(":")[0].upper()
            for drive in drives:
                if (drive_where_target_is_located == drive):
                    os.system(rf"cd {drive}:")

            # Park4139.commentize(rf'빽업할 디렉토리의 부모디렉토리로 이동')
            Park4139.commentize(rf'# target_dirname_dirname 로 이동')
            os.chdir(target_dirname_dirname)

            Park4139.commentize(rf'부모디렉토리로 빽업')
            # 하위 명령어 사용 시 빽업할 디렉토리의 부모 디렉토리에서 명령어를 수행해야 해야 에러가 없다.
            # bz.exe 는 반디집에서 제공하는 CLI 기반 명령어 이다 bandizip.exe 의 줄임 명령어이다.
            cmd = f'bz.exe c "{target_zip}" "{target_abspath}"'
            Park4139.get_cmd_output(cmd)

            Park4139.commentize(rf'이름변경')
            cmd = f'ren "{target_zip}" "{target_yyyy_mm_dd_HH_MM_SS_zip}"'
            Park4139.get_cmd_output(cmd)

            Park4139.commentize(rf'부모디렉토리에서 빽업될 디렉토리로 이동')
            cmd = f'move "{target_yyyy_mm_dd_HH_MM_SS_zip}" "{target_dirname}"'
            Park4139.get_cmd_output(cmd)

            Park4139.commentize(rf'빽업될 디렉토리로 이동')
            os.chdir(target_dirname)

            # Park4139.commentize('중간로깅')
            # server_time = Park4139.get_time_as_('%Y-%m-%d %H:%M:%S')

            # Park4139.commentize('현재 프로그램 pid 출력')
            # # os.system(fr'powershell (Get-WmiObject Win32_Process -Filter ProcessId=$PID).ParentProcessId')

            Park4139.commentize(rf'현재 디렉토리에서 zip 확장자 파일만 문자열 리스트로 출력')
            lines = Park4139.get_cmd_output('dir /b /a-d *.zip')
            for line in lines:
                if line != "":
                    if os.getcwd() != line:
                        # 2023-12-04 월 12:14 trouble shooting 완료
                        # SyntaxWarning: invalid escape sequence '\d'
                        # r 을 사용 Raw String(원시 문자열),  \를 모두 제거
                        # 정규식은 r 쓰면 안된다. \ 써야한다.
                        # regex = r'd{4} d{2} d{2} d{2} d{2} d{2}'
                        regex = '\d{4} \d{2} \d{2} \d{2} \d{2} \d{2}'
                        if Park4139.is_regex_in_contents(line, regex):
                            Park4139.commentize("타임스탬프 정규식 테스트를 통과했습니다")
                            print(line)
                            # 2023-12-03 일 20:03 trouble shooting 완료
                            # 빽업 시 타임스탬프에 언더바 넣도록 변경했는데 regex 는 변경 하지 않아서 난 실수 있었음.
                            time_to_backed_up = re.findall(regex, line)
                            time_to_backed_up_ = time_to_backed_up[0][0:10].replace(" ", "-") + " " + time_to_backed_up[0][11:16].replace(" ", ":") + ".00"
                            time_to_backed_up__ = datetime.strptime(str(time_to_backed_up_), '%Y-%m-%d %H:%M.%S')
                            time_current = datetime.now()

                            Park4139.commentize(rf'project tree 생성')
                            target_dirname_old = rf'{target_dirname}\$cache_zip'
                            try:
                                if not os.path.exists(target_dirname_old):
                                    os.makedirs(target_dirname_old)
                            except Exception as e:
                                Park4139.trouble_shoot("1?")
                                traceback.print_exc(file=sys.stdout)
                                Park4139.pause()

                            # 지금부터 7일 이전의 파일만
                            # diff = time_to_backed_up__ - time_current
                            # if diff.days <-7:
                            # print(f"line : {line}")

                            Park4139.commentize(f"1분(60 seconds) 이전의 파일자동정리 시도...")
                            change_min = time_current - timedelta(seconds=60)
                            diff = time_to_backed_up__ - change_min
                            if 60 < diff.seconds:
                                try:
                                    file_with_time_stamp_zip = os.path.abspath(line.strip())
                                    file_dirname_old_abspath = os.path.abspath(target_dirname_old)
                                    print(rf'{Park4139.indent_space_promised}move "{file_with_time_stamp_zip}" "{file_dirname_old_abspath}"')
                                    shutil.move(file_with_time_stamp_zip, file_dirname_old_abspath)

                                except Exception as e:
                                    Park4139.trouble_shoot("%%%FOO%%%")
                                    traceback.print_exc(file=sys.stdout)
                                    Park4139.pause()

            Park4139.commentize("os.getcwd()")
            print(os.getcwd())

        except:
            Park4139.trouble_shoot("202312030000")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()
        finally:
            Park4139.commentize(rf'프로젝트 디렉토리로 이동')
            os.chdir(Park4139.working_directory)

    @staticmethod
    def monitor_target_edited_and_bkup(target_abspath: str, key: str):
        global line_cnt_from_db
        Park4139.commentize(f'{os.path.basename(target_abspath)} 타겟 편집 모니터링 시도')
        db_abspath = Park4139.db_abspath
        # 조건문을 반복 작성해서 기능을 분리할 수가 있었다.
        # 여기서 알게된 사실은 조건문의 구조를 반복해서 특정 기능들의 로직들을 분리할 수 있었다.

        try:
            line_cnt_from_db = Park4139.read_db_toml(db_abspath=db_abspath)[key]
        except KeyError:
            Park4139.update_db_toml(key=key, value=Park4139.get_line_cnt_of_file(target_abspath), db_abspath=db_abspath)
        line_cnt_measured = Park4139.get_line_cnt_of_file(target_abspath)
        print(f"line_cnt_from_db : {line_cnt_from_db}")
        print(f"line_cnt_measured : {line_cnt_measured}")

        # commentize() 관련된 로직 분리
        if Park4139.verify_target_edited(target_abspath, key):
            Park4139.commentize("타겟의 편집을 감지 했습니다")
            Park4139.commentize("타겟빽업을 시도합니다")
            Park4139.commentize("타겟을 데이터 베이스에 업데이트합니다")
        elif Park4139.verify_target_edited(target_abspath, key) is None:
            Park4139.commentize("데이터베이스 타겟에 대한 key가 없어 key를 생성합니다")

        # bkup() 관련된 로직 분리
        if Park4139.verify_target_edited(target_abspath, key):
            Park4139.bkup(target_abspath)

        # db crud 관련된 로직 분리
        if Park4139.verify_target_edited(target_abspath, key):
            Park4139.update_db_toml(key=key, value=Park4139.get_line_cnt_of_file(target_abspath), db_abspath=db_abspath)
        elif Park4139.verify_target_edited(target_abspath, key) is None:
            Park4139.insert_db_toml(key=key, value=Park4139.get_line_cnt_of_file(target_abspath), db_abspath=db_abspath)

    # 2023-12-03 일요일 13:06 최신화 함수
    @staticmethod
    def print_and_open_py_pkg_global_path():
        for path in sys.path:
            print(path)
            if Park4139.is_regex_in_contents(contents=path, regex='site-packages') == True:
                print(rf'echo "{path}"')
                os.system(rf'echo "{path}" | clip.exe ')
                os.system(rf'explorer "{path}"')

    # 2023-12-03 일요일 13:25 최신화 함수
    @staticmethod
    # 이런식의 void 함수의 형태는 @staticmethod, @classmethod 둘 중 아무거나 써도 문제가 없다,
    # 하지만 부모 class 로 만든 인스턴스에 영향이 없도록(값의 공유가 되지 않도록) 하기위해 기본적으로
    # @classmethod를 사용하는 것이 나은 방법인 것 같다.
    # 그래서 pycharm 에서 @classmethod를 생성이 되도록 가이드 해주는 것 같았다.
    # 앞으로는 instance 간에 값의 공유가 필요없는 상황이라면 classmethod 를 쓰자.
    # 심도있게 예측해야할 상황은 field 가 공유되도록 해야 될때 이다. Account
    # 이해한 게 문제가 있는지 상속에 대한 실험은 꼭 진행해보도록 하자.
    # Parent().name    parent.name   Child().name   child.name
    def pause():
        os.system('pause')

    # 2023-12-03 일요일 13:25 최신화 함수
    @staticmethod
    def taskkill(program_exe):
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

    @staticmethod
    def get_length_of_mp3(target):
        try:
            audio = MP3(target)
            return audio.info.length
        except Exception as e:
            Park4139.trouble_shoot("202312030001")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()

    @staticmethod
    def speak(ment):
        """Google TTS 적용"""
        from gtts import gTTS
        import time

        try:
            Park4139.commentize(rf'speak() os.getcwd()')
            print(os.getcwd())

            # Park4139.commentize(rf'한글 설정')
            os.system('chcp 65001 >nul')

            # Park4139.commentize(rf'storage 디렉토리 생성')
            cache_mp3 = rf'{os.getcwd()}\$cache_mp3'
            if not os.path.exists(cache_mp3):
                os.makedirs(cache_mp3)

            # Park4139.commentize(rf'파일 없으면 생성')
            ment__mp3 = rf'{cache_mp3}\{ment}_.mp3'
            ment_mp3 = rf'{cache_mp3}\{ment}.mp3'
            if not os.path.exists(ment_mp3):
                if not os.path.exists(ment__mp3):
                    gtts = gTTS(text=ment, lang='ko')
                    gtts.save(ment__mp3)

            Park4139.commentize(rf'앞부분 소리가 들리지 않는 현상 해결 시도 설정')
            silent_mp3 = rf"{cache_mp3}\silent.mp3"
            # print(f"ment_mp3: {ment_mp3}")
            # print(f"silent_mp3: {silent_mp3}")
            try:
                if os.path.exists(silent_mp3):
                    if not os.path.exists(ment_mp3):
                        try:
                            # silent_mp3를 타겟파일의 앞쪽에 한번 넣는다 무음 시간을 앞에 추가한다
                            cmd = rf'echo y | "ffmpeg" -i "concat:{os.path.abspath(silent_mp3)}|{os.path.abspath(ment__mp3)}" -acodec copy -metadata "title=Some Song" "{os.path.abspath(ment_mp3)}" -map_metadata 0:-1  >nul 2>&1'
                            # print(fr"{Park4139.indent_space_promised}{cmd}")
                            # print('')
                            # os.system(cmd)
                            Park4139.get_cmd_output(cmd)
                        except Exception as e:
                            Park4139.trouble_shoot("202312030002")
                            traceback.print_exc(file=sys.stdout)
                            Park4139.pause()
            except Exception as e:
                Park4139.trouble_shoot("202312030003")
                traceback.print_exc(file=sys.stdout)
                Park4139.pause()
            try:
                # Park4139.commentize(rf'mp3재생, 자꾸 프로세스 세션을 빼앗기 때문에 불편한 문제있는 코드')
                # os.system(rf'start /b cmd /c call "{ment_mp3}" >nul 2>&1')

                # Park4139.commentize(rf'프로세스 세션을 빼앗지 않고 mp3재생')
                # playsound.playsound(os.path.abspath(ment_mp3))

                Park4139.commentize(rf'프로세스 세션을 빼앗지 않고 mp3재생')
                print(rf'{Park4139.indent_space_promised}{ment_mp3}')
                file_mp3 = pyglet.media.load(os.path.abspath(ment_mp3))
                file_mp3.play()

                # Park4139.commentize(rf'mp3 재생길이 만큼 대기')
                # length_of_mp3 = round(float(Park4139.get_length_of_mp3(os.path.abspath(ment_mp3))), 1)
                # time.sleep(length_of_mp3 * 0.95)
                # time.sleep(length_of_mp3 * 1.00)
                # time.sleep(length_of_mp3 * 1.05)


            except Exception as e:
                Park4139.trouble_shoot("202312030004")
                traceback.print_exc(file=sys.stdout)
                Park4139.pause()

            # Park4139.commentize(rf'불필요 파일 삭제')
            os.system(f'echo y | del /f "{ment__mp3}" >nul 2>&1')

            # Park4139.commentize(rf'중간로깅')
            Park4139.log_mid(log_title=f"TTS 재생시도")

        except Exception as e:
            Park4139.trouble_shoot("202312030005")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()

    def speaks(self, ments):
        for ment in ments:
            self.speak(ment)

    # 2023-12-07 목요일 16:51 최신화 함수
    @staticmethod
    def trouble_shoot_decorator(trouble_shoot):
        def wrapper(*args, **kwargs):
            # os.system(f'echo {trouble_shoot(*args, **kwargs)} | clip.exe') # 클립보드로 붙여넣는 기능 소거.
            trouble_shoot(*args, **kwargs)
            pass

        return wrapper

    @trouble_shoot_decorator
    @staticmethod
    def trouble_shoot(trouble_id: str, e=None):
        Park4139.commentize(f'{Park4139.line_length_promised} trouble_id : {trouble_id} s')
        if e != None:
            print(str(e))
        return trouble_id

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

    @staticmethod
    def parse_youtube_video_id(url):
        """
        - code written by stack overflow (none regex way)
        - 파이썬에 내장 기능
        - 이게 내가 선정한 url 구문 분석 방법
        this method return String or None
        Strng 을 리턴했다면 유튜브 비디오 아이디로 기대할 수 있다
        """
        query = parser.urlparse(url=url)
        if query.hostname == 'youtu.be':
            print(f"query.path[1:] : {query.path[1:]}")
            return query.path[1:]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            # print(query.scheme)
            # print(query.netloc)
            # print(query.hostname)
            # print(query.port)
            # print(query._replace(fragment="").geturl())
            # print(query)
            # print(query["v"][0])
            if query.path == '/watch':
                p = parser.parse_qs(query.query)
                print(f"p['v'][0] : {p['v'][0]}")
                return p['v'][0]
            if query.path[:7] == '/embed/':
                print(f"query.path.split('/')[2] : {query.path.split('/')[2]}")
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                print(f"query.path.split('/')[2] : {query.path.split('/')[2]}")
                return query.path.split('/')[2]
        # fail?
        return None

    @staticmethod
    def download_clip(url: str):
        while True:
            if url.strip() == "":
                print(rf"다운로드할 url이 아닙니다 {url}")
                break
            # 다운로드가 안되면 주석 풀어 시도
            # os.system(rf'{Park4139.yt_dlp_cmd} -U')

            # Park4139.raise_error('의도적으로 에러를 발생 중...')
            # if
            #     Park4139.commentize(rf'다운로드가 된 url 입니다 {url}')
            #

            Park4139.commentize('다운로드 옵션 파싱 중...')
            video_id = ''
            # lines = subprocess.check_output(rf'{Park4139.yt_dlp_cmd} -F {url}', shell=True).decode('utf-8').split("\n")

            cmd = rf'{Park4139.yt_dlp_cmd} -F {url}'
            lines = Park4139.get_cmd_output(cmd=cmd)
            # 순서는 우선순위에 입각해 설정되었다. 순서를 바꾸어서는 안된다.
            video_ids_allowed = [
                '315',
                '313',
                '303',
                '308',
                '616',
                '248',
                '247',
                '244',
                '137',
                '136',
            ]
            audio_ids_allowed = [
                '250',
                '251',
            ]
            audio_id = ""
            for line in lines:
                if 'video only' in line or 'audio only' in line:
                    print(line)
                    # video_id 설정
                    for id in video_ids_allowed:
                        if id in line:
                            video_id = id
                            if video_id.strip() == "":
                                print(rf"다운로드 할 수 있는 video_id가 아닙니다 {video_id.strip()}")
                                break
                    # audio_id 설정
                    for id in audio_ids_allowed:
                        if id in line:
                            audio_id = id
                            if audio_id.strip() == "":
                                print(rf"다운로드 할 수 있는 audio_id가 아닙니다 {audio_id.strip()}")
                                break

            # 다운로드 가능 옵션 ID 설정
            # if video_id not in video_ids and audio_id not in audio_ids:
            #     video_id = str(input('video option:'))
            #     audio_id = str(input('audio option:'))
            #     speak(rf'다운로드 옵션이 선택되었습니다')
            #     print(rf'video option: {video_id}  audio option: {audio_id}')
            #     speak(rf'video option: {video_id}  audio option: {audio_id}')
            # else:
            #     pass

            # directories = ["storage"]
            # for directory in directories:
            #     if not os.path.isdir(rf'{os.getcwd()}\{directory}'):
            #         Park4139.commentize(rf'storage 디렉토리 생성 중...')
            #         os.makedirs(rf'{directory}')

            cmd = rf'{Park4139.yt_dlp_cmd} -f {video_id}+{audio_id} {url}'
            if video_id == "" or audio_id == "" == 1:
                text = "다운로드를 진행할 수 없습니다\n다운로드용 video_id 와 audio_id를 설정 후\nurl을 다시 붙여넣어 다운로드를 다시 시도하세요\n{url}"
                pyautogui.prompt(text=text, default=url)
                Park4139.commentize("불완전한 명령어 감지됨...")
                print("다운로드 가능한 video_id 와 audio_id 를 가용목록에 추가해주세요")
                print(cmd)
                Park4139.pause()
                break
            Park4139.commentize(rf'명령어 실행 중...')
            lines = Park4139.get_cmd_output(cmd=cmd)

            Park4139.commentize(rf'storage 생성 중...')
            storage = rf'{os.getcwd()}\storage'
            try:
                if not os.path.exists(storage):
                    os.makedirs(storage)


            except Exception as e:
                Park4139.trouble_shoot("202312030007")
                traceback.print_exc(file=sys.stdout)
                Park4139.pause()

            Park4139.commentize("다운로드 파일 이동 시도 중...")
            file = ""
            try:
                clip_id = Park4139.parse_youtube_video_id(url)
                if clip_id == None:
                    clip_id = url

                lines = os.listdir()
                for line in lines:
                    if Park4139.is_regex_in_contents(str(line), str(clip_id)):
                        file = line

                src = os.path.abspath(file)
                src_renamed = rf"{storage}\{os.path.basename(file)}"
                Park4139.commentize("print(f'src : {src}')")
                print(f'src : {src}')
                print(f'storage : {storage}')
                print(f'src_renamed : {src_renamed}')

                # shutil.move(src, storage)
                if src != os.getcwd():
                    Park4139.move_with_overwrite(src, src_renamed)

            except:
                Park4139.trouble_shoot("202312030009")
                traceback.print_exc(file=sys.stdout)
                Park4139.pause()

            Park4139.commentize(rf'다운로드 결과 확인 중...')
            try:
                src_moved = rf'{storage}\{file}'
                cmd = rf'explorer "{src_moved}"'
                Park4139.get_cmd_output(cmd=cmd)
            except Exception:
                Park4139.trouble_shoot("202312030013")
                traceback.print_exc(file=sys.stdout)
                Park4139.pause()

            Park4139.commentize(rf'다운로드 결과 로깅 중...')
            cmd = f'echo "{url}" >> success_yt_dlp.log'
            Park4139.get_cmd_output(cmd=cmd)
            break

    @staticmethod
    def download_from_youtube_to_webm():
        while True:
            urls = [
                # allowed download url pattern example
                # 'https://www.youtube.com/watch?v=ilAgjIOb6e8',  !!!!!!check comma being !!!!!!!!
                # 'https://www.youtube.com/watch?v=AX7BcBD8-BA&list=PLuHgQVnccGMBjEtHz-BmkIm5OR4sgPH75',
                # 'https://www.youtube.com/watch?v=cDp5WmdUn5I&list=FLvc8kv-i5fvFTJBFAk6n1SA&index=2',
                # 'ilAgjIOb6e8',
                # SBS 고래와 나
            ]
            # 프롬프트 중앙 정렬 설정
            text = '#유튜브URL #유튜브_CLIP_ID #유튜브PlayLists'
            urls_from_prompt = str(pyautogui.prompt(text=text)).strip()
            # print(f"len(urls_from_prompt) : {len(urls_from_prompt)}")

            try:
                # print(f"type(urls_from_prompt) :{type(urls_from_prompt) }")
                urls_from_prompt_as_list = urls_from_prompt.split("\n")
            except AttributeError:
                traceback.print_exc(file=sys.stdout)
                urls_from_prompt_as_list = urls_from_prompt
            if len(urls_from_prompt_as_list) != 0:
                for i in urls_from_prompt_as_list:
                    if i != "":
                        urls.append(str(i).strip())

            Park4139.commentize('________________________________________________________________ 프롬프트로 입력된 Urls')
            print(f"len(urls_from_prompt_as_list) : {len(urls_from_prompt_as_list)}")
            print(urls_from_prompt_as_list)
            for i in urls_from_prompt_as_list:
                print(i)
            try:
                urls.append(sys.argv[1])
            except IndexError:
                pass
            except Exception:
                Park4139.trouble_shoot("202312071455")
                traceback.print_exc(file=sys.stdout)
                Park4139.pause()
                pass

            # park4139.commentize('________________________________________________________________ urls 중복제거(orderless way)')
            # urls_orderless = list(set(urls))
            # urls = urls_orderless

            Park4139.commentize('________________________________________________________________ urls 중복제거(ordered way)')
            urls_not_duplicatated_as_ordered = []
            for url in urls:
                if url not in urls_not_duplicatated_as_ordered:
                    if url is not None:
                        # if url is not "None":
                        urls_not_duplicatated_as_ordered.append(url)
            urls = urls_not_duplicatated_as_ordered
            print(f"len(urls) : {len(urls)}")
            for i in urls:
                print(i)

            # Park4139.commentize('다운로드 할게 없으면 LOOP break')
            if len(urls) == 0:
                print("다운로드할 게 없습니다")
                break

            Park4139.update_db_toml(key="yt_dlp_tried_urls", value=urls, db_abspath=Park4139.db_abspath)
            # park4139.commentize(' 유튜브 다운로드 루틴 진입 시도      ')
            for url in urls:
                # park4139.commentize('url에 공백이 있어도 다운로드가 가능하도록 SETTING')
                url = url.strip()

                if '&list=' in url:
                    Park4139.commentize(' clips mode')
                    clips = Playlist(url)  # 이걸로도 parsing 기능 수행할 수 있을 것 같은데
                    print(f"predicted clips cnt : {len(clips.video_urls)}")
                    for clip in clips.video_urls:
                        os.system(f'echo "여기서부터 비디오 리스트 시작 {url}" >> success_yt_dlp.log')
                        try:
                            Park4139.download_clip(clip)
                        except Exception:
                            Park4139.trouble_shoot("202312071513")
                            traceback.print_exc(file=sys.stdout)
                            Park4139.pause()
                            continue
                        os.system(f'echo "여기서부터 비디오 리스트 시작 {url}" >> success_yt_dlp.log')
                else:
                    if Park4139.parse_youtube_video_id(url) != None:
                        Park4139.commentize('________________________________________________________________ youtube video id parsing mode')
                        try:
                            Park4139.download_clip(f'https://www.youtube.com/watch?v={Park4139.parse_youtube_video_id(url)}')
                        except Exception:
                            Park4139.trouble_shoot("202312071526")
                            traceback.print_exc(file=sys.stdout)
                            Park4139.pause()
                            continue
                    else:
                        Park4139.commentize('________________________________________________________________ experimental mode')
                        try:
                            Park4139.download_clip(url)
                        except Exception:
                            Park4139.trouble_shoot("202312071432")
                            traceback.print_exc(file=sys.stdout)
                            Park4139.pause()
                            continue

    @staticmethod
    def get_display_setting():
        height = ''
        width = ''
        for monitor_info in get_monitors():
            for info in str(monitor_info).split(','):
                if 'width=' in info.strip():
                    width = info.split('=')[1]
                elif 'height=' in info.strip():
                    height = info.split('=')[1]
        display_setting = {
            'height': int(height),
            'width': int(width)
        }
        return display_setting

    # deprecated method by Park4139
    # def print_police_line(police_line_ment):
    #     police_line = ''
    #     for i in range(0, 255 // len(police_line_ment)):
    #         police_line = police_line + f'{police_line_ment} '
    #     print(f'{police_line.upper()}')
    @staticmethod
    def is_regex_in_contents(contents, regex):

        pattern = re.compile(regex)
        m = pattern.search(contents)
        if m:
            Park4139.commentize("def is_regex_in_contents(contents, regex):")
            print(rf"contents: {contents}")
            print(rf"regex: {regex}")
            print(rf"True")
            return True
        else:
            # print(rf"contents: {contents}")
            # print(rf"regex: {regex}")
            # print(rf"False")
            return False

    @staticmethod
    # 출력의 결과는 tasklist /svc 와 유사하다.
    def print_python_process_for_killing_zombie_process():
        for process in psutil.process_iter():
            print(process.name(), "\t" + str(process.pid), "\t" + process.status())

    @staticmethod
    # def get_cmd_output(self, cmd, working_directory=working_directory):
    def get_cmd_output(cmd):
        try:
            # print('')
            print(rf'{Park4139.indent_space_promised}{cmd}')

            # os.system(cmd)
            # os.Popen 으로 print 가능하도록 할 수 있다는 것 같았는데 다른 방식으로 일단 되니까. 안되면 시도.

            # cmd = ['dir', '/b']
            # fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout # 명령어 실행 후 반환되는 결과를 파일에 저장합니다.
            # fd_popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout # shell=True 옵션, cmd를 string 으로 설정
            # lines = fd_popen.read().strip().split('\n')# lines에 저장합니다.
            # fd_popen.close()# 파일을 닫습니다.

            lines = ''
            try:
                lines = subprocess.check_output(cmd, shell=True).decode('utf-8').split('\n')
            except UnicodeDecodeError:
                lines = subprocess.check_output(cmd, shell=True).decode('euc-kr').split('\n')
            except subprocess.CalledProcessError:
                # traceback.print_exc(file=sys.stdout)
                pass
            # for line in lines:
            #     print(line)

            return lines
        except UnboundLocalError and Exception as e:
            Park4139.trouble_shoot("202312030015")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()
            return None

    @staticmethod
    def get_cmd_output_v2(cmd):
        try:
            print(rf'{Park4139.indent_space_promised}{cmd}')
            lines = 'not_'
            try:
                lines = subprocess.check_output(cmd, shell=True).decode('utf-8')
            except UnicodeDecodeError:
                lines = subprocess.check_output(cmd, shell=True).decode('euc-kr')
            except subprocess.CalledProcessError:
                pass
            return lines
        except UnboundLocalError and Exception as e:
            Park4139.trouble_shoot("202312030015")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()
            return None

    @staticmethod
    # 시작로깅(json 형태로 넣을 수 있도록 코드 업데이트 할것)
    def log_s(log_title="시작로깅"):
        Park4139.get_cmd_output('chcp 65001 >nul')  # 한글 엔코딩 설정
        Park4139.time_s = time.time()  # 서버라이프사이클 계산용 변수 설정
        server_time = Park4139.get_time_as_(f'%Y-%m-%d %H:%M:%S')
        cmd = rf'echo "server_time  : {server_time} ,  working_directory  : {Park4139.working_directory},  __file__  : {__file__},  log_title : {log_title} " >> "{Park4139.log_directory}\success.log"'
        Park4139.get_cmd_output(cmd)

    @staticmethod
    def log_mid(log_title="중간로깅"):
        server_time = Park4139.get_time_as_(f'%Y-%m-%d %H:%M:%S')
        cmd = rf'echo "server_time  : {server_time} ,  working_directory  : {Park4139.working_directory},  __file__  : {__file__},  log_title : {log_title} " >> "{Park4139.log_directory}\success.log"'
        Park4139.get_cmd_output(cmd)

    @staticmethod
    def log_e(log_title="종료로깅"):
        Park4139.time_e = time.time()  # 서버라이프사이클 계산용 변수 설정
        server_time = Park4139.get_time_as_(f'%Y-%m-%d %H:%M:%S')
        server_life_cycle = Park4139.time_e - Park4139.time_s
        lines = subprocess.check_output(
            rf'echo "server_time  : {server_time} ,  working_directory  : {Park4139.working_directory},  __file__  : {__file__},  log_title : {log_title},  server_life_cycle : {server_life_cycle}  " >> "{Park4139.log_directory}\success.log"',
            shell=True).decode('utf-8').split(
            '\n')
        # os.system('cls')

    @staticmethod
    # 프로그램 PID 출력
    def get_current_program_pid():
        pro = subprocess.check_output(
            fr'powershell (Get-WmiObject Win32_Process -Filter ProcessId=$PID).ParentProcessId', shell=True).decode(
            'utf-8')  # 실험해보니 subprocess.check_output(cmd,shell=True).decode('utf-8') 코드는 프로세스가 알아서 죽는 것 같다. 모르겠는데 " " 가 있어야 동작함
        lines = pro.split('\n')
        pids = []
        for line in lines:
            if "" != line.strip():
                pid = line
                pids.append(pid)
                print(f'pid: {pid}')
        return pids

    @staticmethod
    def commentize(title):
        print(f'{Park4139.line_length_promised} {title.replace("__", "")}')

        # 아래 코드를 주석 해제하면 귀찮을 정도로 너무 말이 많을 수 있습니다.
        # self.speak(title)

    @staticmethod
    def get_target_bite(start_path='.'):
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
        return Park4139.get_target_bite(target_path.strip()) / 1024 ** 2

    @staticmethod
    def get_target_gigabite(target_path):
        return Park4139.get_target_bite(target_path.strip()) / 1024 ** 3

    @staticmethod
    def toogle_console_color(color_bg, colors_texts):
        to_right_nbsp = ''
        to_right_nbsp_cnt = 150
        for i in range(0, to_right_nbsp_cnt):
            to_right_nbsp = to_right_nbsp + ' '
        for color_text in colors_texts:
            if color_bg != color_text:
                os.system(f"color {color_bg}{color_text}")

    @staticmethod
    def recommand_console_color():
        colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        while True:
            try:
                for color_bg in colors:
                    for color_text in colors:
                        if color_bg != color_text:
                            os.system('cls')
                            for setting_key, setting_value in Park4139.get_display_setting().items():
                                pass
                                # print(f'setting_key: {setting_key}  ,setting_value: {setting_value}  ')
                            # print(f"color {color_bg}{color_text}")
                            for i in range(0, 32):
                                print('')
                            to_right_nbsp = ''
                            for i in range(0, 150):
                                to_right_nbsp = to_right_nbsp + ' '
                            print(f"{to_right_nbsp}color {color_bg}{color_text}")
                            for i in range(0, 32):
                                print('')
                            os.system(f"color {color_bg}{color_text}")
                            import clipboard
                            clipboard.copy(f'color {color_bg}{color_text}')
                            os.system('pause')
            except Exception as e:
                Park4139.trouble_shoot("202312071431")
                traceback.print_exc(file=sys.stdout)
                Park4139.pause()
                # ctrl c 가 입력이 제대로 되지 않는 현상이 있어 ctrl c 로 콘솔을 종료하는데 불편...이는 어떻게 해결하지? 일단 코드 반응속도는 마음에 드는데...

    @staticmethod
    def make_matrix_console():
        os.system('color 0A')
        os.system('color 02')
        while True:
            lines = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8').split("\n")
            for line in lines:
                if "" != line:
                    if os.getcwd() != line:
                        print(lines)
            time.sleep(60)

    @staticmethod
    def make_party_console():
        commands = [
            'color 03',
            'color 09',
            'color 4F',
            'color cF',
            'color bf',
            'color 10',
            'color 1f',
            'color 08',
            'color f0',
            'color f8',
            'color 4c',
            'color c4',
            'color 09',
            'color 0a',
            'color d4',
            'color a4',
            'color 4a',
            'color 51',
            'color 48',
            'color 4c',
            'color 5d',
            'color 3b',
            'color e6',
            'color 07',
            'color 3F',
            'color 13',
            'color a2',
            'color 2a',
            'color 01',
            'color 02',
            'color 03',
            'color 04',
            'color 05',
            'color 06',
            'color 8f',
            'color 9b',
            'color 4a',
            'color da',
            'color ad',
            'color a4',
            'color b2',
            'color 0c',
            'color 0d',
            'color e3',
            'color eb',
            'color e7',
            'color 0f',
        ]
        while (True):
            for command in commands:
                os.system(f'{command}')
                # os.system('echo "202312031429" && pause')

    @staticmethod
    def convert_mp4_to_webm(target_abspath):
        '''테스트 필요'''
        print(f'from : {target_abspath}')
        file_edited = f'{os.path.splitext(os.path.basename(target_abspath))[0]}.webm'
        print(f'to   : {file_edited}')

        path_started = os.getcwd()
        os.system("chcp 65001 >nul")
        os.system('mkdir storage >nul')
        os.chdir('storage')
        os.system(f'"{Park4139.ffmpeg_exe}" -i "{target_abspath}" -f webm -c:v libvpx -b:v 1M -acodec libvorbis "{file_edited}" -hide_banner')
        os.chdir(path_started)

    @staticmethod
    def convert_wav_to_flac(target_abspath):
        '''테스트 필요'''

        # :: 한글 인코딩 setting
        os.system("chcp 65001 >nul")

        print(f'from : {target_abspath}')
        file_edited = f'{os.path.splitext(os.path.basename(target_abspath))[0]}.flac'
        print(f'to   : {file_edited}')

        # :: ffmpeg location setting
        ffmpeg_exe = fr"{Park4139.USERPROFILE}\Desktop\`workspace\tool\LosslessCut-win-x64\resources\ffmpeg.exe"
        destination = 'storage'
        try:
            os.makedirs(destination)
        except Exception as e:
            pass
        os.chdir(destination)
        print(f'"{ffmpeg_exe}" -i "{target_abspath}" -c:a flac "{file_edited}"        를 수행합니다.')
        subprocess.check_output(f'"{ffmpeg_exe}" -i "{target_abspath}" -c:a flac "{file_edited}"', shell=True)

    @staticmethod
    def convert_mp4_to_wav(target_abspath):
        '''테스트 필요'''
        print(f'from : {target_abspath}')
        file_edited = f'{os.path.splitext(os.path.basename(target_abspath))[0]}.wav'
        print(f'to   : {file_edited}')

        path_started = os.getcwd()

        os.system('mkdir storage')
        os.chdir('storage')
        if os.path.splitext(os.path.basename(target_abspath))[1] == '.mp4':
            videoclip = VideoFileClip(target_abspath)
            audioclip = videoclip.audio

            # audioclip.write_audiofile(file_edited, fps= 8000 )
            audioclip.write_audiofile(file_edited, fps=44100)
            audioclip.close()
            videoclip.close()

        os.chdir(path_started)

    @staticmethod
    def convert_mp4_to_flac(target_abspath):
        '''테스트 필요'''
        # :: 한글 인코딩 setting
        os.system("chcp 65001 >nul")
        print(f'from : {target_abspath}')
        file_edited = f'{os.path.splitext(os.path.basename(target_abspath))[0]}.flac'
        print(f'to   : {file_edited}')

        path_started = os.getcwd()

        # :: ffmpeg location setting
        ffmpeg_exe = fr"{Park4139.USERPROFILE}\Desktop\`workspace\tool\LosslessCut-win-x64\resources\ffmpeg.exe"
        destination = 'storage'
        try:
            os.makedirs(destination)
        except Exception as e:
            pass
        os.chdir(destination)
        print(f'"{ffmpeg_exe}" -i "{target_abspath}" -c:a flac "{file_edited}"        를 수행합니다.')
        subprocess.check_output(f'"{ffmpeg_exe}" -i "{target_abspath}" -c:a flac "{file_edited}"', shell=True)

        os.chdir(path_started)

    @staticmethod
    def convert_mp3_to_flac(target_abspath):
        '''테스트 필요'''
        os.system("chcp 65001 >nul")

        print(f'from : {target_abspath}')
        file_edited = f'{os.path.splitext(os.path.basename(target_abspath))[0]}.flac'
        print(f'to   : {file_edited}')

        path_started = os.getcwd()

        # :: ffmpeg location setting
        ffmpeg_exe = fr"{Park4139.USERPROFILE}\Desktop\`workspace\tool\LosslessCut-win-x64\resources\ffmpeg.exe"
        destination = 'storage'
        try:
            os.makedirs(destination)
        except Exception as e:
            pass
        os.chdir(destination)
        print(f'"{ffmpeg_exe}" -i "{target_abspath}" -c:a flac "{file_edited}"        를 수행합니다.')
        subprocess.check_output(f'"{ffmpeg_exe}" -i "{target_abspath}" -c:a flac "{file_edited}"', shell=True)

        os.chdir(path_started)

    @staticmethod
    # 이 메소드를 만들면서 권한을 얻는 여러가지 방법을 stack over flow 를 따라 시도해보았으나 적다한 해결책을 찾지 못함. pyautogui 로 시도 방법은 남아있으나
    # 일단은 regacy 한 방법으로 임시로 해결해두었다.
    def update_global_pkg_park4139():
        local_pkg = rf"{Park4139.USERPROFILE}\Desktop\services\archive_py\pkg_park4139"
        global_pkg = rf"C:\Python312\Lib\site-packages\pkg_park4139"
        updateignore_txt = rf"{Park4139.USERPROFILE}\Desktop\services\archive_py\pkg_park4139\updateignore.txt"
        try:
            if os.path.exists(global_pkg):
                # 삭제시도
                # shutil.rmtree(global_pkg)

                # 삭제시도
                # for file in os.scandir(global_pkg):
                # os.remove(file.path)

                # 덮어쓰기
                # src= local_pkg
                # dst =os.path.dirname(global_pkg)
                # os.system(f"echo y | copy {src} {dst}")
                # shutil.copytree(local_pkg, os.path.dirname(global_pkg))
                cmd = f'echo y | xcopy "{local_pkg}" "{global_pkg}" /k /e /h /exclude:{updateignore_txt} >nul'
                os.system(cmd)

                # 디버깅
                # Park4139.pause()
                print(f'{Park4139.indent_space_promised}{cmd}')
                print("")
                return "REPLACED global pkg_Park4139 AS local_pkg"
            else:
                return "pkg_Park4139 NOT FOUND AT GLOBAL LOCATION"

        except Exception as e:
            Park4139.trouble_shoot("202312030016")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()

    @staticmethod
    def merge_video_and_sound(file_v_abspath, file_a_abspath):
        Park4139.commentize('다운로드 디렉토리 생성')
        directories = ["storage"]
        for directory in directories:
            if not os.path.isdir(rf'./{directory}'):
                os.makedirs(rf'{directory}')

        Park4139.commentize(rf'yotube 에서 고해상도 음성 없는 영상과 음성을 받아 하나의 영상으로 merge')
        Park4139.commentize('비디오 파일, 음성 파일 절대주소 get')
        dst = rf'{os.getcwd()}\storage'
        paths = [os.path.abspath(dst), os.path.basename(file_v_abspath)]
        file_va = os.path.join(*paths)
        print(rf'file_v_abspath : {file_v_abspath}')
        print(rf'file_a_abspath : {file_a_abspath}')
        print(rf'file_va : {file_va}')

        Park4139.commentize('ffmpeg.exe 위치 설정')
        location_ffmpeg = fr"{Park4139.USERPROFILE}\Desktop\`workspace\tool\LosslessCut-win-x64\resources\ffmpeg.exe"
        trouble_characters = ['Ä']
        trouble_characters_alternatives = {'Ä': 'A'}
        for trouble_character in trouble_characters:
            file_v_abspath = file_v_abspath.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            file_a_abspath = file_a_abspath.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            file_va = file_va.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            Park4139.commentize('파일명 변경 시도')
            try:
                if trouble_character in file_va:
                    os.rename(file_v_abspath,
                              file_v_abspath.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
                    os.rename(file_a_abspath,
                              file_a_abspath.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
            except Exception as e:
                Park4139.trouble_shoot("202312030017")
                traceback.print_exc(file=sys.stdout)
                Park4139.pause()

        Park4139.commentize(' 파일머지 시도')
        try:
            print(fr'echo y | "{location_ffmpeg}" -i "{file_v_abspath}" -i "{file_a_abspath}" -c copy "{file_va}"')
            lines = subprocess.check_output(
                fr'echo y | "{location_ffmpeg}" -i "{file_v_abspath}" -i "{file_a_abspath}" -c copy "{file_va}"', shell=True).decode(
                'utf-8').split("\n")
            for line in lines:
                print(line)
        except Exception as e:
            Park4139.trouble_shoot("202312030018")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()

        print(rf'다운로드 및 merge 결과 확인 시도')
        try:
            print(rf'explorer "{file_va}"')
            subprocess.check_output(rf'explorer "{file_va}"', shell=True).decode('utf-8').split("\n")
        except Exception as e:
            Park4139.trouble_shoot("202312030019")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()

        Park4139.commentize(' 불필요 리소스 삭제 시도')
        try:
            if os.path.exists(file_va):
                subprocess.check_output(rf'echo y | del /f "{file_v_abspath}"', shell=True).decode('utf-8').split("\n")
                lines = subprocess.check_output(rf'echo y | del /f "{file_a_abspath}"', shell=True).decode('utf-8').split("\n")
                for line in lines:
                    print(line)
        except Exception as e:
            Park4139.trouble_shoot("202312030020")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()

    @staticmethod
    def move_without_overwrite(src, dst):
        try:
            Park4139.commentize('타겟이동 시도')
            shutil.move(src, dst)  # 이런 식으로 처리하면 안된다고 했던 것 같다
        except Exception as e:
            Park4139.commentize('타겟을 찾을 수 없거나 dst에 보내려는데 중복타겟명을 발견했습니다')
            src_dirname = os.path.dirname(src)
            src_basename = os.path.basename(src)
            src_n = os.path.splitext(src_basename)[0]
            src_x = os.path.splitext(src_basename)[1]
            spaceless_time_pattern = Park4139.get_time_as_(rf'_%Y_%m_%d_%H_%M_%S')

            Park4139.commentize('타겟이름 변경 시도')
            new_named = rf'{src_dirname}\{src_n}{spaceless_time_pattern}{src_x}'
            os.rename(src, new_named)
            try:
                Park4139.commentize('타겟 재이동 시도')
                shutil.move(src=new_named, dst=dst)
            except Exception as e:
                Park4139.trouble_shoot("202312030021")
                traceback.print_exc(file=sys.stdout)
                Park4139.pause()

    # @staticmethod
    # def elapsed(function):
    #     def wrapper(*args, **kwargs):
    #         import time
    #         time_s = time.time()
    #         function(*args, **kwargs)
    #         time_e = time.time()
    #         mesured_time = time_e - time_s
    #         print(f'측정시간은 {mesured_time} 입니다')
    #         Park4139.commentize(f'측정시간은 {mesured_time} 입니다')
    #     return wrapper

    @staticmethod
    def decorate_seconds_performance_measuring_code(function):
        """시간성능 측정 데코레이터 코드"""

        def wrapper():
            import time
            time_s = time.time()
            function()
            time_e = time.time()
            mesured_time = time_e - time_s
            Park4139.commentize(rf"시간 성능 측정결과")
            ment = f'측정시간은 {round(mesured_time, 2)} seconds 입니다 (소수점 2자리 숫자에서 반올림하였습니다)'
            print(ment)
            # Park4139.commentize(ment)

        return wrapper

    @staticmethod
    def decorate_milliseconds_performance_measuring_code(function):
        """시간성능 측정 코드"""

        def wrapper():
            import time
            time_s = time.time()
            function()
            time_e = time.time()
            mesured_time = time_e - time_s
            Park4139.commentize(rf"시간 성능 측정결과")
            ment = f'측정시간은 {round(mesured_time * 1000, 5)} milliseconds 입니다 (소수점 5자리 숫자에서 반올림하였습니다)'
            print(ment)
            # Park4139.commentize(ment)

        return wrapper

    @staticmethod
    def cls():
        import os
        os.system('cls')

    @staticmethod
    def replace_with_auto_no(contents: str, unique_word: str, auto_cnt_starting_no=0):
        """

        input   = "-----1-----1----1------"
        Output  = "-----1-----2----3------"

        input
        --------
        -----1--
        ---1----
        ---1----
        --------
         ouput
        --------
        -----1--
        ---2----
        ---3----
        --------

        """
        tmp = []
        for index, element in enumerate(contents.split(unique_word)):
            if index != len(contents.split(unique_word)) - 1:
                tmp.append(element + str(auto_cnt_starting_no))
                auto_cnt_starting_no = auto_cnt_starting_no + 1
            else:
                tmp.append(element)
        lines_new_as_str = "".join(tmp)
        return lines_new_as_str

    def replace_with_auto_no_orderless(contents: str, unique_word: str, auto_cnt_starting_no=0):
        # Park4139.commentize("항상 필요했던 부분인데 만들었다. 편하게 개발하자. //웹 서비스 형태로 아무때서나 접근이되면 더 좋을 것 같다.  웹 개발툴 을 만들어 보자")
        before = unique_word
        after = 0 + auto_cnt_starting_no
        contents_new = []
        # lines = contents.split("\n")
        lines = contents.strip().split("\n")  # 문제 없긴 했는데,  어떻게 되나 실험해보자 안되면 위의 코드로 주석 스와핑할것.
        for line in lines:
            # print(line)
            # print(before)
            # print(str(after))
            after = after + 1

            line_new = re.sub(str(before), str(after), str(line))
            # print(line_new)
            contents_new.append(line_new)

        # Park4139.commentize("str list to str")
        delimiter = "\n"
        contents_new_as_str = delimiter.join(contents_new)
        return contents_new_as_str

    @staticmethod
    def move_with_overwrite(src: str, dst: str):
        try:
            # 목적지에 있는 중복타겟 삭제
            os.remove(dst)
        except FileNotFoundError as e:
            pass
        except Exception as e:
            Park4139.trouble_shoot("%%%FOO%%%")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()
        try:
            # 목적지로 타겟 이동
            os.rename(src, dst)
        except Exception as e:
            Park4139.trouble_shoot("%%%FOO%%%")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()

    @staticmethod
    def raise_error(str: str):
        raise shutil.Error(str)

    @staticmethod
    def verify_target_edited(target_abspath: str, key: str):
        try:
            db_abspath = Park4139.db_abspath
            db = Park4139.read_db_toml(db_abspath=db_abspath)
            line_cnt_measured = Park4139.get_line_cnt_of_file(target_abspath)
            if line_cnt_measured != db[key]:
                Park4139.commentize("verify_target_edited")
                print("True")
            else:
                # print("False")
                pass
            if line_cnt_measured != db[key]:
                return True
            else:
                return False
        except:
            Park4139.commentize("데이터베이스 확인 중 예상되지 않은 에러가 감지되었습니다")
            Park4139.trouble_shoot("202312030000")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()

    @staticmethod
    def git_push_by_auto():
        while True:
            try:
                Park4139.commentize(f" git add.log {Park4139.get_time_as_('%Y-%m-%d %H:%M:%S')} s")
                cmd_result = subprocess.check_output('git add * ', shell=True).decode('utf-8')  # cmd 결과 를 python 에서 값읽기
                if "" in cmd_result:
                    # print('auto git add success')
                    os.system('color df')
                else:
                    print('auto git add fail')
                    os.system('color 04')
                Park4139.commentize(f" git add.log {Park4139.get_time_as_('%Y-%m-%d %H:%M:%S')} e")
                # commit_ment = Park4139.get_time_as_('%Y-%m-%d %H:%M:%S')
                # commit_ment = "auto pushed"
                commit_ment = "auto pushed at " + Park4139.get_time_as_('%Y-%m-%d %H:%M:%S')
                # commit_ment = Park4139.get_time_as_('%Y-%m-%d %H:%M:%S')
                # commit_ment = "auto pushed"
                # commit_ment = "auto pushed at " + Park4139.get_time_as_('%Y-%m-%d %H:%M:%S')
                # commit_ment = "테스트 커밋"
                # commit_ment = "프로젝트 이니셜 커밋"
                # commit_ment = "플러터 안드로이드 앱들 업데이트 PHASE 1"
                # commit_ment = "당근마껫 UI 업데이트"
                # commit_ment = "당근마껫 페이지 추가제작"
                cmd_result = subprocess.check_output('git commit -m "' + commit_ment + '"',shell=True).decode('utf-8')
                Park4139.commentize(f" git commit.log {Park4139.get_time_as_('%Y-%m-%d %H:%M:%S')} s")
                cmd_result = subprocess.check_output('git status | findstr "nothing to commit, working tree clean"',shell=True).decode('utf-8')
                print(rf"cmd_result: {cmd_result}")
                if "nothing to commit, working tree clean" in cmd_result:
                    # print('auto git commit success')
                    os.system('color df')
                else:
                    print('auto git commit fail')
                    os.system('color 04')
                Park4139.commentize(f"git commit.log {Park4139.get_time_as_('%Y-%m-%d %H:%M:%S')} e")
                Park4139.commentize(f"git push.log {Park4139.get_time_as_('%Y-%m-%d %H:%M:%S')} s")
                cmd_result2 = subprocess.check_output('git push -u origin main', shell=True).decode('utf-8')
                if "Everything up-to-date" or "branch 'main' set up to track 'origin/main'." in cmd_result2:
                    os.system('color df')  # OPERATION
                    if int('08') <= int(Park4139.get_time_as_('%H')) <= int('23'):  # 하도 자는데 시끄러워서 추가한 코드
                        Park4139.commentize("깃허브에 프로젝트 푸쉬를 완료했습니다")
                else:
                    print('auto git push fail')
                    os.system('color 04')
                Park4139.commentize(f" git push.log {Park4139.get_time_as_('%Y-%m-%d %H:%M:%S')} e")
            except:
                Park4139.commentize('깃허브에 푸쉬를 시도 중 익셉션이 발생하였습니다')
                Park4139.commentize('잠시 뒤에 깃허브에 푸쉬를 재시도합니다.')
                traceback.print_exc(file=sys.stdout)
                continue

            random_seconds = random.randint(400, 600)  # FOR GIT HUB CONTRIBUTION COUNT INCREASEMENT
            print(f"RPA works again in {str(random_seconds)} seconds...")
            os.system("echo .>> foo.txt")
            time.sleep(random_seconds)

    @staticmethod
    def save_all_list():
        """모든 파일 디렉토리에 대한 정보를 텍스트 파일로 저장하는 함수"""
        print("______________________________________________________ directory $cache_all_tree/all_tree.txt/proper_tree.txt 생성")
        os.system('chcp 65001 >nul')
        opening_directory = os.getcwd()
        proper_tree_txt = rf"{os.getcwd()}\$cache_all_tree\proper_tree.txt"
        all_tree_txt = rf"{os.getcwd()}\$cache_all_tree\all_tree.txt"
        if not os.path.exists(os.path.dirname(all_tree_txt)):
            os.makedirs(os.path.dirname(all_tree_txt))
            # os.system(f'echo. >> "{all_tree_txt}"')
            os.system(f'echo. >> "{all_tree_txt}" >nul')
            os.system(f'echo. >> "{proper_tree_txt}" >nul')
        print("______________________________________________________ all_tree.txt/proper_tree.txt 내용 지우기")
        with open(all_tree_txt, 'w', encoding="utf-8") as f:
            f.write(" ")
        with open(proper_tree_txt, 'w', encoding="utf-8") as f:
            f.write(" ")

        drives = win32api.GetLogicalDriveStrings()
        drives = drives.replace('\\', '').split('\000')[:-1]

        file_cnt = 0
        f = open(os.getcwd() + '\\all_list.txt', 'a', encoding="utf-8")  # >>  a    > w   각각 대응됨.
        for drive in drives:
            os.chdir(drive)
            for dirpath, subdirs, files in os.walk(os.getcwd()):
                for file in files:
                    file_cnt = file_cnt + 1
                    f.write(str(file_cnt) + " " + os.path.join(dirpath, file) + "\n")
        f.close()  # close() 를 사용하지 않으려면 with 문을 사용하는 방법도 있다.
        print("______________________________________________________ all_list.txt writing e")
        print("______________________________________________________ all_list_proper.txt rewriting s")
        texts_black = [
            "C:\\$WinREAgent",
            "C:\\mingw64",
            "C:\\PerfLogs",
            "C:\\Program Files (x86)",
            "C:\\Program Files",
            "C:\\ProgramData",
4            "C:\\Temp",
            "C:\\Users\\All Users",
            "C:\\Windows\\servicing",
            "C:\\Windows\\SystemResources",
            "C:\\Windows\\WinSxS",
            "C:\\Users\\Default",
            "C:\\Users\\Public",
            "C:\\Windows.old",
            "C:\\Windows",
            "C:\\$Recycle.Bin",
            "D:\\$RECYCLE.BIN",
            "E:\\$RECYCLE.BIN",
            "E:\\$Recycle.Bin",
            "F:\\$RECYCLE.BIN",
            fr"{Park4139.USERPROFILE}\\AppData",
        ]
        texts_white = [
            ".mkv",
        ]
        f = open(rf'{os.getcwd()}\all_list.txt', 'r+', encoding="utf-8")
        f2 = open(rf'{os.getcwd()}\all_list_proper.txt', 'a', encoding="utf-8")
        lines_cnt = 0
        while True:
            line = f.readline()
            if not line:
                break
            lines_cnt = lines_cnt + 1
            if any(text_black not in line for text_black in texts_black):
                # print(line)
                if any(text_white in line for text_white in texts_white):
                    # print(line.split("\n")[0] + " o")
                    f2.write(line.split("\n")[0] + " o " + "\n")
                    # print('o')
                    pass
                else:
                    # print(line.split("\n")[0] + " x")
                    # f2.write(line.split("\n")[0] + " x "+"\n")
                    # print('x')
                    pass
        f.close()
        f2.close()
        print("______________________________________________________ all_list_proper.txt rewriting e")

        print("______________________________________________________ files opening s")
        os.chdir(os.getcwd())
        os.system("chcp 65001 >nul")
        # os.system("type all_list.txt")
        # os.system("explorer all_list.txt")
        os.system("explorer all_list_proper.txt")
        print("______________________________________________________ files opening e")

        # os.system('del "'+os.getcwd()+'\\all_list.txt"')
        # mk("all_list.txt")
        print("______________________________________________________ e")

    @staticmethod
    def get_line_cnt_of_file(target_abspath: str):
        line_cnt = 0
        # 파일 변경 감지 이슈: linecache 모듈은 파일의 변경을 감지하지 못합니다.
        # 파일이 변경되었을 때에도 이전에 캐시된 내용을 반환하여 오래된 정보를 사용할 수 있습니다.
        # 실시간으로 파일의 변경을 감지해야 하는 경우에는 정확한 결과를 얻기 어려울 수 있습니다.
        # line_cnt = len(linecache.getlines(target_abspath))
        # print(f'line_cnt:{line_cnt}')  캐시된 내용을 반환하기 때문에. 실시간 정보가 아니다

        # 이 코드는 실시간으로 파일의 변경을 감지 처리 되도록 수정, 단, 파일이 크면 성능저하 이슈 있을 수 있다.
        with open(target_abspath, 'r', encoding="UTF-8") as file:
            # whole_contents = file.readlines()
            # print(whole_contents)
            # line_cnt = len(whole_contents)
            # line_cnt = list(en umerate(file))[-1][0] + 1
            line_cnt = file.read().count("\n") + 1
        return line_cnt

    @staticmethod
    def create_db_toml(db_abspath, db_template):
        if not os.path.exists(os.path.dirname(db_abspath)):
            # print("db 파일이 존재해야할 경로가 존재하지 않습니다")
            Park4139.commentize("db 트리 생성")
            os.makedirs(os.path.dirname(db_abspath))  # 이거 파일도 만들어지나? 테스트 해보니 안만들어짐 디렉토리만 만들어짐
        # Park4139.commentize("db 파일 존재 검사 시도")
        if not os.path.isfile(db_abspath):
            print("db가 존재하지 않습니다")
            print(db_abspath)
            Park4139.commentize("db 생성")
            with open(db_abspath, "w") as f2:
                toml.dump(db_template, f2)
            print(f"{db_abspath}를 만들었습니다")
        else:
            print(f"{db_abspath}가 이미 존재합니다")

    @staticmethod
    def read_db_toml(db_abspath: str):
        return toml.load(db_abspath)

    @staticmethod
    def update_db_toml(key, value, db_abspath: str):
        with open(db_abspath, 'r') as f:
            Park4139.commentize("DB 업데이트 전 모든 내용 출력")
            db = toml.load(f)
            print(db)
        with open(db_abspath, 'w') as f:
            Park4139.commentize("DB 업데이트 후 모든 내용 출력")
            db[key] = value
            toml.dump(db, f)
            print(db)

    @staticmethod
    def insert_db_toml(key, value, db_abspath: str):
        with open(db_abspath, "a") as f:
            db = toml.load(f)
            db[key] = value
            toml.dump(db, f)

    @staticmethod
    def bkup_db_toml(db_abspath: str):
        Park4139.bkup(db_abspath)

    @staticmethod
    def delete_db_toml(target_abspath):
        Park4139.convert_as_zip_with_timestamp(target_abspath)

    @staticmethod
    def convert_as_zip_with_timestamp(target_abspath):
        try:
            target_dirname = os.path.dirname(target_abspath)
            target_dirname_dirname = os.path.dirname(target_dirname)
            target_basename = os.path.basename(target_abspath).split(".")[0]
            target_zip = rf'$zip_{target_basename}.zip'
            target_yyyy_mm_dd_HH_MM_SS_zip = fr'{target_basename} - {Park4139.get_time_as_("%Y %m %d %H %M %S")}.zip'
            # Park4139.commentize(rf'# target_dirname_dirname 로 이동')
            os.chdir(target_dirname_dirname)
            # Park4139.commentize(rf'부모디렉토리로 빽업')
            cmd = f'bandizip.exe c "{target_zip}" "{target_abspath}"'
            Park4139.get_cmd_output(cmd)
            # Park4139.commentize(rf'이름변경')
            cmd = f'ren "{target_zip}" "$deleted_{target_yyyy_mm_dd_HH_MM_SS_zip}"'
            Park4139.get_cmd_output(cmd)
            # Park4139.commentize(rf'부모디렉토리에서 빽업될 디렉토리로 이동')
            cmd = f'move "$deleted_{target_yyyy_mm_dd_HH_MM_SS_zip}" "{target_dirname}"'
            Park4139.get_cmd_output(cmd)
            # Park4139.commentize(rf'빽업될 디렉토리로 이동')
            os.chdir(target_dirname)
            # Park4139.commentize("os.getcwd()")
            # print(os.getcwd())
            # Park4139.commentize("원본파일삭제")
            os.remove(target_abspath)

        except:
            Park4139.trouble_shoot("202312030000")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()
        finally:
            Park4139.commentize(rf'프로젝트 디렉토리로 이동')
            os.chdir(Park4139.working_directory)

    @staticmethod
    def bkup_by_manual(target_abspath):
        starting_directory = os.getcwd()
        try:
            target_dirname = os.path.dirname(target_abspath)
            target_dirname_dirname = os.path.dirname(target_dirname)
            target_basename = os.path.basename(target_abspath).split(".")[0]
            target_zip = rf'$zip_{target_basename}.zip'
            target_yyyy_mm_dd_HH_MM_SS_zip = fr'{target_basename} - {Park4139.get_time_as_("%Y %m %d %H %M %S")}.zip'
            # Park4139.commentize(rf'# target_dirname_dirname 로 이동')
            os.chdir(target_dirname_dirname)
            # Park4139.commentize(rf'부모디렉토리로 빽업')
            cmd = f'bandizip.exe c "{target_zip}" "{target_abspath}"'
            Park4139.get_cmd_output(cmd)
            # Park4139.commentize(rf'이름변경')
            cmd = f'ren "{target_zip}" "{target_yyyy_mm_dd_HH_MM_SS_zip}"'
            Park4139.get_cmd_output(cmd)
            # Park4139.commentize(rf'부모디렉토리에서 빽업될 디렉토리로 이동')
            cmd = f'move "{target_yyyy_mm_dd_HH_MM_SS_zip}" "{target_dirname}"'
            Park4139.get_cmd_output(cmd)
            # Park4139.commentize(rf'빽업될 디렉토리로 이동')
            # os.chdir(target_dirname)
            os.chdir(starting_directory)
            # Park4139.commentize("os.getcwd()")
            # print(os.getcwd())

        except:
            Park4139.trouble_shoot("202312030000")
            traceback.print_exc(file=sys.stdout)
            Park4139.pause()
        finally:
            Park4139.commentize(rf'프로젝트 디렉토리로 이동')
            # os.chdir(Park4139.working_directory)
            os.chdir(starting_directory)

    @staticmethod
    def move_mouse(abs_x: int, abs_y: int):
        pyautogui.moveTo(abs_x, abs_y)

    @staticmethod
    def mouse_move_rel_x(rel_x: int, rel_y: int):
        pyautogui.move(rel_x, rel_y)

    @staticmethod
    def get_current_mouse_abs_info():
        return pyautogui.position()  # x, y = get_current_mouse_abs_info() 이런식으로 받을수 있나 테스트

    @staticmethod
    def open_mouse_info():
        pyautogui.mouseInfo()

    @staticmethod
    def press(*presses: str):
        # 한글입력 해결 용 코드 + hotkey 동시 사용 가능 코드
        global key
        if len(presses) == 1:
            print(len(presses))
            import clipboard
            # print(pyautogui.KEYBOARD_KEYS) #이걸로 타이핑 지원 목록 확인 가능 필요시 아래에 추가하자
            presses_supported_pyautogui = [
                '@', 'altleft', 'altright', 'backspace', 'capslock', 'ctrlleft', 'ctrlright', 'del', 'delete', 'down', 'end', 'enter', 'esc', 'f1', 'f12', 'home', 'insert', 'left', 'numlock', 'pagedown', 'pageup', 'pause', 'printscreen', 'right', 'scrolllock', 'shiftleft', 'shiftright', 'space', 'tab', 'up',
                'command',  # macOS command 키
                'option',  # macOS option 키
                'winleft',  # 윈도우키
            ]
            for i in presses_supported_pyautogui:
                if presses[0] == i:
                    key = presses[0]
            if key is not None:
                pyautogui.press(key)
            else:
                clipboard.copy(str(presses[0]))
                pyautogui.hotkey("ctrl", "v")
            print(fr"{str(key)} 눌렸어요")
        else:
            pyautogui.hotkey(*presses)
            tmp = ' + '.join(i for i in presses)
            print(fr"{tmp} 눌렸어요")
        Park4139.sleep(milliseconds=100)

    @staticmethod
    def press_slow(presses: str):
        pyautogui.keyDown(presses)
        Park4139.sleep(milliseconds=500)
        print(fr"{str(presses)} 눌렸어요")

    @staticmethod
    def get_400px_screenshot(miliseconds=0):
        """pyautogui, 마우스의 위치 주변 가로 세로 400 px  400 px 로 스크린샷 찍어서 저장하는 코드"""
        # 재우기
        Park4139.sleep(milliseconds=miliseconds)

        # 현재 마우스 위치 가져오기
        x, y = pyautogui.position()
        width = 400
        height = 400
        left = x - width / 2  # height/2 일수도 있음
        top = y - height / 2  # 여기도 마찬가지 일수 있음

        # 스크린샷 찍기
        pygui = pyautogui.screenshot(region=(left, top, width, height))

        # 스크린샷 저장
        server_time = Park4139.get_time_as_('%Y_%m_%d_%H_%M_%S')
        screenshot_png = f'{os.getcwd()}\$cache_png\screenshot_{server_time}.png'
        try:
            os.makedirs(os.path.dirname(screenshot_png))
        except FileExistsError:
            pass
        pygui.save(screenshot_png)
        pygui.show(screenshot_png)

    @staticmethod
    def get_full_screenshot():
        try:
            # Park4139.press("winleft")
            # Park4139.sleep(milliseconds=300)
            # Park4139.write_fast('sni')
            # Park4139.press("enter")
            cmd = rf' explorer "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Snipping Tool.lnk" >nul'
            Park4139.get_cmd_output(cmd)
            Park4139.sleep(milliseconds=200)
            Park4139.press("alt", "m")
            Park4139.press_slow("s")
            Park4139.press("esc")
            Park4139.press("ctrlleft", "s")
            server_time = Park4139.get_time_as_('%Y_%m_%d_%H_%M_%S')
            file_ = rf'{os.getcwd()}\storage\full_screenshot\img_by_rpa_{server_time}.png'
            try:
                os.makedirs(os.path.dirname(file_))
            except FileExistsError:
                pass
            Park4139.write_fast(file_)
            Park4139.press("enter")

            # 이미지를 인식해서 닫는게 확인하고 닫는 것이 더 좋을 것 같다. 추후에 수정하자.
            Park4139.press("alt", "f4")

            try:
                cmd = rf'explorer "{file_}"'
                Park4139.get_cmd_output(cmd=cmd)
            except FileNotFoundError:
                pass
            Park4139.sleep(milliseconds=1000)
            Park4139.press("esc")

        except:
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def get_img_for_rpa(keyboardevent):
        try:
            cmd = rf' explorer "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Snipping Tool.lnk" >nul'
            Park4139.get_cmd_output(cmd)
            Park4139.sleep(milliseconds=200)
            Park4139.press("alt", "m")
            Park4139.press_slow("r")

            while True:
                if keyboard.is_pressed(['ctrlleft', 's']):
                    Park4139.sleep(3000)
                    server_time = Park4139.get_time_as_('%Y_%m_%d_%H_%M_%S')
                    file_ = rf'{os.getcwd()}\storage\full_screenshot\img_by_rpa_{server_time}_.png'  # 맨 언더바를 붙였다는 것은 rpa에 사용중이지 않은 이미지란 의미
                    try:
                        os.makedirs(os.path.dirname(file_))
                    except FileExistsError:
                        pass
                    Park4139.press(file_)
                    Park4139.sleep(3000)
                    Park4139.press("enter")
                    break
                else:
                    Park4139.sleep(100)

            # 이미지를 인식해서 닫는게 확인하고 닫는 것이 더 좋을 것 같다. 추후에 수정하자.
            Park4139.press("alt", "f4")
            # def mouse_click_left_when_img_recognition_succeed(file_abspath):
            # file_png = rf"{os.getcwd()}\$cache_png\screenshot_2023_12_11_21_14_14.png"
            # while True:
            #     xy_infos_of_imgs = pyautogui.locateOnScreen(file_png, confidence=0.7, grayscale=True)
            #     if xy_infos_of_imgs != None:
            #         if xy_infos_of_imgs:
            #             # 이미지 중심 좌표 얻기
            #             center_x = xy_infos_of_imgs.left + (xy_infos_of_imgs.width / 2)
            #             center_y = xy_infos_of_imgs.top + (xy_infos_of_imgs.height / 2)
            #
            #             # 이미지 중심 좌표 클릭
            #             Park4139.mouse_move(abs_x=center_x, abs_y=center_y)
            #             Park4139.mouse_click_left(abs_x=center_x, abs_y=center_y)
            #             break
            #     else:
            #         Park4139.sleep(milliseconds=100)
            #         Park4139.commentize("루프 아직 돌고 있어요")
            #         Park4139.commentize("이미지 찾는 중...")

            try:
                cmd = rf'explorer "{file_}"'
                Park4139.get_cmd_output(cmd=cmd)
            except FileNotFoundError:
                pass
            Park4139.sleep(milliseconds=1000)
            Park4139.press("esc")

        except:
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def run_rpa_program():
        Park4139.commentize("자동화 프로그램 실행 중...")
        pyautogui.FAILSAFE = False
        try:
            # Park4139.mouse_move(abs_x=3440 / 2, abs_y=1440 / 2)
            texts_promised = {
                '#macro': '#매크로 #RPA #자동화',
                '#question_to_ai': "#AI에게 질문",
                '#full_screenshot': "#풀스크린샷",
                '#youtube_webm': "#유튜브webm다운로드",
                '#youtube_webm_soundless': "#유튜브webm다운로드소리없이",
                '#youtube_wav': "#유튜브wav다운로드",
                '#백업': "#타겟백업",
                '#no_paste_memo': "#노페이스트메모",
                '#400px_screenshot_after_5_seconds': "#400px스크린샷 5초 후",
                '#400px_screenshot': "#400px스크린샷",
                '#remove_recycle_bin': "#휴지통비우기",
                '#get_img_for_rpa': "#자동화용 이미지 수집",
                '#rdp1': "#rdp-82106",
                '#torrent': "#애니",
                '#weather': "#날씨",
            }

            def do_macros(keyboardevent):
                tp = texts_promised
                answser = pyautogui.confirm(
                    text=tp['#macro'],
                    buttons=[
                        tp['#question_to_ai'],
                        tp["#full_screenshot"],
                        tp['#400px_screenshot'],
                        tp['#400px_screenshot_after_5_seconds'],
                        tp['#youtube_webm'],
                        tp['#youtube_webm_soundless'],  # https://www.youtube.com/watch?v=bEEL6HN718Y
                        tp['#youtube_wav'],
                        tp['#백업'],
                        tp['#remove_recycle_bin'],
                        tp['#get_img_for_rpa'],
                        tp['#rdp1'],
                        tp['#torrent'],
                    ],
                )
                if answser == tp['#full_screenshot']:
                    Park4139.get_full_screenshot()
                elif answser == tp['#400px_screenshot_after_5_seconds']:
                    Park4139.get_400px_screenshot(miliseconds=5000)
                elif answser == tp['#400px_screenshot']:
                    Park4139.get_400px_screenshot()
                elif answser == tp['#youtube_webm']:
                    Park4139.download_from_youtube_to_webm()
                elif answser == tp['#remove_recycle_bin']:
                    Park4139.remove_recycle_bin()
                elif answser == tp['#백업']:
                    file_abspath = pyautogui.prompt('백업할 타겟경로를 입력하세요')
                    Park4139.bkup(file_abspath)
                elif answser == tp['#rdp1']:
                    Park4139.connect_remote_rdp1()
                elif answser == tp['#torrent']:
                    Park4139.get_data_from_web()
                elif answser == tp['#get_img_for_rpa']:
                    Park4139.get_img_for_rpa(keyboardevent)
                elif answser == tp['#question_to_ai']:
                    question = pyautogui.prompt('AI 에게 할 질문을 입력하세요')
                    Park4139.ask_to_google(question=question)
                    Park4139.ask_to_bard(question=question)
                    Park4139.ask_to_wrtn(question=question)
                else:
                    Park4139.speak("아직 준비되지 않은 기능입니다")
                    pass

                # 아....confirm 대기 하느라 이 루프로 오질 못한다
                # 100ms 쉬어가며 이미지를 찾을때까지 열심히 일하는 코드
                # 실행되면 창이 active 안되니까 되도록 1회 클릭 하기 위한 코드
                # file_png = rf"{os.getcwd()}\$cache_png\screenshot_2023_12_11_21_14_14.png"
                # while True:
                #     xy_infos_of_imgs = pyautogui.locateOnScreen(file_png, confidence=0.7, grayscale=True)
                #     if xy_infos_of_imgs != None:
                #         if xy_infos_of_imgs:
                #             # 이미지 중심 좌표 얻기
                #             center_x = xy_infos_of_imgs.left + (xy_infos_of_imgs.width / 2)
                #             center_y = xy_infos_of_imgs.top + (xy_infos_of_imgs.height / 2)
                #
                #             # 이미지 중심 좌표 클릭
                #             Park4139.mouse_move(abs_x=center_x, abs_y=center_y)
                #             Park4139.mouse_click_left(abs_x=center_x, abs_y=center_y)
                #             break
                #     else:
                #         Park4139.sleep(milliseconds=100)
                #         Park4139.commentize("루프 아직 돌고 있어요")

            def print_key_event(e):
                try:
                    if keyboard.is_pressed("hanja"):
                        do_macros(e)
                    # elif keyboard.is_pressed(["`", "fewfjioew"]):
                    #     # 이런것도 있네
                    #     keyboard.press_and_release('shift + r, shift + k, \n')
                    #     keyboard.press_and_release('R, K')
                    #     keyboard.add_hotkey("ctrl+alt+p", lambda: print("CTRL+ALT+P Pressed!"))
                    #     keyboard.add_abbreviation("@email", "test@example.com")
                    #
                    #     # press space
                    #     keyboard.send("space")
                    #     keyboard.send("windows+d")

                    #     # send ALT+F4 in the same time, and then send space,
                    #     # (be carful, this will close any current open window)
                    #     # keyboard.send("alt+F4, space")
                    #
                    #     # press CTRL button
                    #     keyboard.press("ctrl")
                    #     # release the CTRL button
                    #     keyboard.release("ctrl")
                    #     keyboard.write("Python Programming is always fun!", delay=0.1)
                    #
                    #     # # record all keyboard clicks until esc is clicked
                    #     # events = keyboard.record('esc')
                    #     # # play these events
                    #     # keyboard.play(events)
                    #
                    #     # print all typed strings in the events
                    #     # print(list(keyboard.get_typed_strings(events)))
                    #
                    #     # # log all pressed keys
                    #     # keyboard.on_release(lambda e: print(e.name))
                    # elif keyboard.is_pressed(["esc", "left"]):
                    #     for i in range(0,4):
                    #         Park4139.press("left")
                    #         Park4139.commentize("mkr")
                    else:
                        print(f'{e.name}  :  {e.event_type}')
                except:
                    traceback.print_exc(file=sys.stdout)

            keyboard.hook(print_key_event)
            # keyboard.wait('esc')
            # Park4139.mouse_move(abs_x=3440 / 2, abs_y=1440 / 2)
            while True:
                key = keyboard.read_key()

                # if key == "esc":
                #     break
                # else:
                #     pass
                pass
            # endregion
        except pyautogui.FailSafeException and Exception:
            Park4139.move_mouse(abs_x=3440 / 2, abs_y=1440 / 2)
            pass

    def get_abs_x_and_y_from_img(img_abspath):
        return pyautogui.locateOnScreen(img_abspath)  # x, y = get_current_mouse_abs_info() 이런식으로 받을수 있나 테스트

    def convert_img_to_img_blurred(img_abspath):

        img_converted = Image.open(img_abspath).filter(ImageFilter.GaussianBlur(10))  # 가우시안 블러 적용 # 숫자크면 많이흐려짐
        img_converted.show()

    def convert_img_to_img_grey(img_abspath):
        img_converted = Image.open(img_abspath).convert("L")
        img_converted.show()

    def convert_img_to_img_resized(img_abspath, width_px, height_px):
        img_converted = Image.open(img_abspath).resize((width_px, height_px))
        img_converted.show()

    def convert_img_to_img_cropped(img_abspath, abs_x: int, abs_y: int, width_px: int, height_px: int):
        img_converted = Image.open(img_abspath).crop((abs_x, abs_y, width_px, height_px))
        img_converted.show()

    def convert_img_to_img_rotated(img_abspath, degree: int):
        img_converted = Image.open(img_abspath).rotate(degree)
        img_converted.show()
        img_converted.save(f"{os.path.dirname(img_abspath)}   {os.path.splitext(img_abspath)[0]}_$flipped_h{os.path.splitext(img_abspath)[1]}")

    def convert_img_to_img_flipped_horizontally(img_abspath):
        img_converted = Image.open(img_abspath).transpose(Image.FLIP_LEFT_RIGHT)
        img_converted.show()
        img_converted.save(f"{os.path.dirname(img_abspath)}   {os.path.splitext(img_abspath)[0]}_$flipped_h{os.path.splitext(img_abspath)[1]}")

    def convert_img_to_img_flipped_vertical(img_abspath):
        img_converted = Image.open(img_abspath).transpose(Image.FLIP_TOP_BOTTOM)
        img_converted.show()
        img_converted.save(f"{os.path.dirname(img_abspath)}   {os.path.splitext(img_abspath)[0]}_$flipped_v{os.path.splitext(img_abspath)[1]}")

    def convert_img_to_img_watermarked(img_abspath):
        from PIL import Image, ImageDraw, ImageFont

        # step2.워터마크 삽입할 이미지 불러오기
        img = Image.open('cat.jpg')
        width, height = img.size

        # step3.그림판에 이미지를 그대로 붙여넣는 느낌의 Draw() 함수
        draw = ImageDraw.Draw(img)

        # step4.삽입할 워터마크 문자
        text = "코딩유치원"

        # step5.삽입할 문자의 폰트 설정
        font = ImageFont.truetype('/Users/sangwoo/Downloads/나눔 글꼴/나눔손글씨_펜/NanumPen.ttf', 30)

        # step6.삽입할 문자의 높이, 너비 정보 가져오기
        width_txt, height_txt = draw.textsize(text, font)

        # step7.워터마크 위치 설정
        margin = 10
        x = width - width_txt - margin
        y = height - height_txt - margin

        # step8.텍스트 적용하기
        draw.text((x, y), text, fill='white', font=font)

        # step9.이미지 출력
        img.show()

        # step10.현재작업 경로에 완성 이미지 저장
        img.save("cat_watermakr.jpg")  # 절대경로 되는지 확인해보자.

    @staticmethod
    def write_fast(presses: str):
        Park4139.sleep(milliseconds=500)
        clipboard.copy(presses)
        Park4139.press("ctrl", "v")
        print(fr"{str(presses)} 눌렸어요")

    @staticmethod
    def write_slow(presses: str):
        pyautogui.write(presses, interval=0.09)
        print(fr"{str(presses)} 눌렸어요")

    @staticmethod
    def ask_to_wrtn(question: str):
        while True:
            cmd = f"explorer https://wrtn.ai/  >nul"
            Park4139.get_cmd_output(cmd)

            # Park4139.sleep(milliseconds=5000)
            # 광고닫기 버튼 클릭

            # 프롬프트 콘솔 이미지 중심 좌표 클릭
            file_png = rf"{os.getcwd()}\$cache_png\screenshot_2023_12_11_14_02_34.png"  # ctrl 0 에서 수집, 텍스트랑 아이콘 동시 들어가도록
            Park4139.click_center_of_img_recognized_by_mouse_left(img_abspath=file_png)

            # 질문 작성 및 확인
            Park4139.write_fast(question)
            Park4139.press('enter')

            # 크롬 최대화
            Park4139.press('winleft', 'up')

            # 크롬 화면
            Park4139.press('ctrlleft', '0')
            Park4139.press('ctrlleft', '-')
            Park4139.press('ctrlleft', '-')
            Park4139.press('ctrlleft', '-')

            # 뤼튼 프롬프트 콘솔 최하단 이동 버튼 클릭
            break

    @staticmethod
    def remove_recycle_bin():
        Park4139.commentize("휴지통 을 비우는 중...")
        Park4139.get_cmd_output('PowerShell.exe -NoProfile -Command Clear-RecycleBin -Confirm:$false')
        # 휴지통 삭제 (외장하드까지)
        # for %%a in (cdefghijk L mnopqrstuvwxyz) do (
        # 존재하는 경우 %%a:\$RECYCLE.BIN for /f "tokens=* usebackq" %%b in (`"dir /a:d/b %%a:\$RECYCLE.BIN\"`) do rd / q/s "%%a:\$RECYCLE.BIN\%%~b"
        # 존재하는 경우 %%a:\RECYCLER for /f "tokens=* usebackq" %%b in (`"dir /a:d/b %%a:\RECYCLER\"`) do rd /q/s "%% a:\RECYCLER\%%~b"
        # )

        # 타겟 삭제 with walking파이썬 이걸로 개발자로서 20년간 밥벌이가 될까?

        #  shutil.rmtree(path)
        #  path에 있는 folder를 지우면서 그 안에 있는 모든 파일을 지워준다.

        # 타겟 휴지통으로 이동
        # pip install send2trash
        # send2trash.send2trash('egg.txt')

        Park4139.commentize("휴지통 여는 중...")
        Park4139.get_cmd_output('explorer.exe shell:RecycleBinFolder')

        # Park4139.commentize("숨김 휴지통 열기")
        # cmd = 'explorer c:\$RECYCLE.BIN'
        # Park4139.get_cmd_output(cmd=cmd)
        # 외장하드 숨김 휴지통 을 보여드릴까요
        # explorer c:\$RECYCLE.BIN
        # explorer d:\$RECYCLE.BIN
        # explorer e:\$RECYCLE.BIN
        # explorer f:\$RECYCLE.BIN

    @staticmethod
    def debug_as_gui(context: str):
        pyautogui.prompt(text="GUI 디버거: ", default=context)
        Park4139.pause()

    @staticmethod
    def click_mouse_left(abs_x=None, abs_y=None):
        if abs_x and abs_y:
            pyautogui.click(button='left', clicks=1, interval=0)
        else:
            pyautogui.click(button='left', clicks=1, interval=0, x=abs_x, y=abs_y)

    @staticmethod
    def mouse_click_right(abs_x=None, abs_y=None):
        if abs_x and abs_y:
            pyautogui.click(button='right', clicks=1, interval=0)
        else:
            pyautogui.click(button='right', clicks=1, interval=0, x=abs_x, y=abs_y, )

    @staticmethod
    def ask_to_bard(question: str):
        while True:
            cmd = f"explorer https://bard.google.com/chat  >nul"
            Park4139.get_cmd_output(cmd)

            # 이시간은 web rendering time 대기 해주는 시간정도로 생각하고 있는데
            # 시간 성능에 대한 마지노선을 설정하는게 여간 편차가 크다.
            # web 크롤링 을 한뒤 연산하는게 훨씬 빠르겠다.
            Park4139.sleep(milliseconds=3000)

            # 질문 작성 및 확인
            Park4139.write_fast(question)
            Park4139.press('enter')

            # 크롬 최대화
            Park4139.press('winleft', 'up')

            # 크롬 화면
            Park4139.press('ctrlleft', '0')
            Park4139.press('ctrlleft', '-')
            Park4139.press('ctrlleft', '-')
            Park4139.press('ctrlleft', '-')
            Park4139.press('ctrlleft', '-')
            Park4139.press('ctrlleft', '-')
            break

    @staticmethod
    def ask_to_google(question: str):
        while True:
            question_ = question.replace(" ", "+")
            cmd = f'explorer "https://www.google.com/search?q={question_}"  >nul'
            Park4139.get_cmd_output(cmd)

            # 크롬 최대화
            Park4139.press('winleft', 'up')

            # 크롬 화면
            Park4139.press('ctrlleft', '0')
            Park4139.press('ctrlleft', '-')
            Park4139.press('ctrlleft', '-')
            break

    @staticmethod
    def get_infos_of_img_when_img_recognized_succeed(img_abspath):
        Park4139.press('ctrlleft', '0')  # 이미지 수집할때 ctrl 0 으로 크롬은 zoom 을 초기화 한뒤에 이미지를 수집.
        Park4139.press('ctrlleft', '0')
        chrome_zoom_steps = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        test_step_current = 0
        while True:
            # 속도개선 시도
            # pip install opencv-python # 이것은 고급 기능이 포함되지 않은 Python용 OpenCV의 미니 버전입니다. 우리의 목적에는 충분합니다.
            # confidence=0.7(70%)유사도를 낮춰 인식률개선, region 낮춰 속도개선, grayscale 흑백으로 판단해서 속도개선,
            # open cv 설치했는데 적용안되고 있음. 재부팅도 하였는 데도 안됨.
            # pycharm 에서 import 하는 부분에서 cv2 설치 시도 중에 옵션으로 opencv-python 이 있길래 설치했더니 결국 됨. 혹쉬 경로 설정 필요했나?
            # xy_infos_of_imgs = pyautogui.locateOnScreen(img_abspath, confidence=0.7, grayscale=True)
            # Park4139.debug_as_gui(xy_infos_of_imgs == None)
            infos_of_imgs = pyautogui.locateOnScreen(img_abspath, confidence=0.7, grayscale=True)
            # infos_of_imgs = pyautogui.locateOnScreen(img_abspath, confidence=0.5, grayscale=True)
            # infos_of_imgs = pyautogui.locateOnScreen(img_abspath, confidence=0.9, grayscale=True)
            # Park4139.sleep(milliseconds=1000)# confidence 를 구하는데 시간을 줘야 할것 같았다
            Park4139.commentize("infos_of_imgs")
            print(infos_of_imgs)
            print(infos_of_imgs != None)
            if infos_of_imgs != None:
                return infos_of_imgs
                # break
            else:
                Park4139.commentize(f"이미지 찾는 중...")
                print(img_abspath)
                Park4139.sleep(milliseconds=1000)

                if chrome_zoom_steps[test_step_current] == 0:
                    Park4139.press('ctrlleft', '0')
                elif chrome_zoom_steps[test_step_current] < 0:
                    for i in range(0, -chrome_zoom_steps[test_step_current]):
                        Park4139.press('ctrlleft', '-')
                else:
                    for i in range(0, chrome_zoom_steps[test_step_current]):
                        Park4139.press('ctrlleft', '+')
                if test_step_current == len(chrome_zoom_steps):
                    test_step_current = 0
                else:
                    test_step_current = test_step_current + 1

                # Park4139.get_cmd_output(rf'explorer "{file_png}"')

    @staticmethod
    def click_center_of_img_recognized_by_mouse_left(img_abspath: str):
        infos_of_img = Park4139.get_infos_of_img_when_img_recognized_succeed(img_abspath)
        center_x = infos_of_img.left + (infos_of_img.width / 2)
        center_y = infos_of_img.top + (infos_of_img.height / 2)
        Park4139.move_mouse(abs_x=center_x, abs_y=center_y)
        Park4139.click_mouse_left(abs_x=center_x, abs_y=center_y)

    @staticmethod
    def connect_remote_rdp1():
        cmd = rf"{os.getcwd()}\$cache_tools\dev_tools_bat\rdp-82106.bat"
        Park4139.get_cmd_output(cmd=cmd)

    @classmethod
    def get_data_from_web():
        pass
