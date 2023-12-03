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


# _________________________________________________________________________________________ mkr: regacy


AI_available_cmd_code_list = ['']
high_frequency_batch_cmd_routine_pattern_list = ['']


def all_info():
    # :: get 현재 pc에 연결된 드라이브
    connected_drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
    print(f"현재 pc에 연결된 드라이브 : {connected_drives}")

    # :: get 현재 디렉토리 위치
    print(f"현재 디렉토리 위치 : {os.getcwd()}")

    # :: get 현재 디렉토리 파일의 Modified/Created/Accessed 일자
    current_files = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만
    lines = current_files.split("\n")
    for line in lines:
        try:
            print("Modified : " + time.ctime(os.path.getmtime(line)))
            print("Created : " + time.ctime(os.path.getctime(line)))
            print("Accessed : " + time.ctime(os.path.getatime(line)))
        except:
            pass

    # :: get 현재 디렉토리 파일의 일자
    # print("_______________________________________________________________________________________________________________ 생성된지 7일 된 모든 확장자 파일 출력 s")
    # os.system('forfiles /P os.getcwd() /S /M *.* /D -7 /C "cmd /c @echo @path" ')
    # print("_______________________________________________________________________________________________________________ 생성된지 7일 된 모든 확장자 파일 출력 e")
    # print("_______________________________________________________________________________________________________________ 생성된지 1일 된 zip 확장자의 백업 파일 삭제 s")
    # os.system('forfiles /P os.getcwd() /S /M *.zip /D -1 /C "cmd /c del @file" ')  # 2003 년 이후 설치 된 PC !주의! forfiles의 옵션이 달라서 큰 사이드 이펙트 일으킬 수 있음.
    # print("_______________________________________________________________________________________________________________ 생성된지 1일 된 zip 확장자의 백업 파일 삭제 e")

    foo = subprocess.check_output('dir /b /s /o /ad', shell=True).decode('utf-8')  # 폴더만 with walking
    foo = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만 with walking
    foo = subprocess.check_output('dir /b /s /o /a', shell=True).decode('utf-8')  # 전부 with walking
    print(foo)

    # :: 현재 디렉토리 파일만 사이즈 출력
    # current_files = os.popen('dir /b /s /o /a').readlines()    # 전부 with walking
    # current_files = os.popen('dir /b /s /o /ad').readlines()   # 폴더만 with walking
    current_files = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만 with walking
    lines = current_files.split("\n")
    for line in lines:
        try:
            foo = round(os.path.getsize(line.strip()) / (1024.0 * 1024.0), 2)
            if (foo < 1):
                print(line.strip() + " : " + str(round(os.path.getsize(line.strip()) / (1024.0), 2)) + ' KB')
            elif (foo < 1024):
                print(line.strip() + " : " + str(round(os.path.getsize(line.strip()) / (1024.0 * 1024.0), 2)) + ' MB')
            else:
                print(line.strip() + " : " + str(round(os.path.getsize(line.strip()) / (1024.0 * 1024.0 * 1024.0), 2)) + ' GB')
        except:
            pass

    # :: 현재 디렉토리 파일만 사이즈 출력 2
    def convert_size(size_bytes):
        import math
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    current_files = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만
    lines = current_files.split("\n")
    for line in lines:
        try:
            print(line.strip() + "{{seperator}}" + str(convert_size(os.path.getsize(line.strip()))))
        except:
            pass

    # :: 현재 디렉토리 파일생성일자 출력 with walking
    current_files = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만
    lines = current_files.split("\n")
    for line in lines:
        try:
            # print(os.path.getmtime(line.strip()))
            # print(time.ctime(os.path.getmtime(line.strip())))
            # print(line.strip() + "{{seperator}}" + str(os.path.getctime(line.strip())))
            # print(line.strip() + "{{seperator}}" + str(datetime.datetime.fromtimestamp(os.path.getctime(line.strip())).strftime('%Y-%m-%d %H:%M:%S')))
            print(line.strip() + "{{seperator}}" + str(time.ctime(os.path.getmtime(line.strip()))))
        except:
            pass
    print("_______________________________________________________________________________________________________________ 현재 디렉토리 파일만 생성일자 출력 e")
    print("_______________________________________________________________________________________________________________ 20230414 18:00 이후 생성된 파일 출력 s")
    inputDate = datetime.strptime(str(input('Searching Input Date : ')), '%Y%m%d %H:%M')
    opening_directory = r'D:\test'
    for (path, dir, files) in os.walk(opening_directory):
        for filename in files:
            fileMtime = datetime.fromtimestamp(os.path.getmtime(path + '\\' + filename))
            if inputDate < fileMtime:
                print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' % (path, filename, fileMtime))
    print("_______________________________________________________________________________________________________________ 20180526 14:00 이후 생성된 파일 출력 e")
    print("_______________________________________________________________________________________________________________ 20230414 18:00 이전 생성된 파일 출력 s")
    inputDate = datetime.strptime(str(input('Searching Input Date : ')), '%Y%m%d %H:%M')
    opening_directory = r'D:\test'
    for (path, dir, files) in os.walk(opening_directory):
        for filename in files:
            fileMtime = datetime.fromtimestamp(os.path.getmtime(path + '\\' + filename))
            if inputDate > fileMtime:
                print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' % (path, filename, fileMtime))
                print('[%s\%s]' % (path, filename))
    print("_______________________________________________________________________________________________________________ 20180526 14:00 이전 생성된 파일 출력 e")
    print("_______________________________________________________________________________________________________________ 현재시간기준 생성된지 1일 된 zip 확장자 파일만 출력 s")
    times = park4139.get_time_as_('%Y-%m-%d %H:%M:%S').split(' ')
    time_inputed = times[0] + times[1] + str(int(times[2]) - 1) + " " + times[3] + ":" + times[4]
    print(time_inputed)
    time_inputed = '20230414 20:53'
    print(time_inputed)
    inputDate = datetime.strptime(str(time_inputed), '%Y%m%d %H:%M')
    opening_directory = opening_directory
    for (path, dir, files) in os.walk(opening_directory):
        for filename in files:
            fileMtime = datetime.fromtimestamp(os.path.getmtime(path + '\\' + filename))
            if inputDate < fileMtime:
                print('[%s\%s    modified : %s]' % (path, filename, fileMtime))
                print('[%s\%s]' % (path, filename))
                print('[%s]' % (filename))
    print("_______________________________________________________________________________________________________________ 현재시간기준 생성된지 1일 된 zip 확장자 파일만 출력 e")


# for i in os.listdir():
#     # print(i, end = " ")
#     print(i)  


def get_length_of_mp3(target_address):
    try:
        audio = MP3(target_address)
        # print(audio.info.length)
        return audio.info.length
    except:
        print('get_length_of_mp3 메소드에서 에러가 발생하였습니다')


def tasklist():
    for proc in psutil.process_iter():
        try:
            process_im_name = proc.name()
            processID = proc.pid
            print(process_im_name, ' - ', processID)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  # 예외처리
            pass

 

def startRecordCommand(file_address):
    # sys.stdout = open('py cmd recording.txt', 'a', encoding='utf-8')  #
    # sys.stdout = open('py cmd recording.txt', 'w', encoding='utf-8')  #
    # sys.stdout = open('py cmd recording.txt', 'r', encoding='utf-8')  #
    sys.stdout = open(file_address, 'w', encoding='utf-8')  #


def endRecordCommand():
    sys.stdout.close()


def saveFileAs(fileAddress):
    startRecordCommand(fileAddress)
    print("이것은 param 두개가 더 필요해 보입니다.")
    endRecordCommand()


def readFile(fileAddress):
    with open(fileAddress, 'r', encoding='utf-8') as f:
        readed_text = f.read()
    return readed_text




def getTimeAsStyle(time_style):
    now = time
    localtime = now.localtime()
    if time_style == '0':
        default = str(now.strftime('%Y_%m_%d_%H_%M_%S').replace('_', " "))
        return default
    elif time_style == '1':
        timestamp = str(now.time())
        return timestamp
    elif time_style == '2':
        yyyy_MM_dd_HH_mm_ss = str(now.strftime('%Y_%m_%d_%H_%M_%S'))
        return yyyy_MM_dd_HH_mm_ss
    elif time_style == '3':
        customTime1 = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        return customTime1
    elif time_style == '4':
        office_style = str(now.strftime('%Y-%m-%d %H:%M'))
        return office_style
    elif time_style == '5':
        yyyy = str(localtime.tm_year)
        return yyyy
    elif time_style == '6':
        MM = str(localtime.tm_mon)
        return MM
    elif time_style == '7':
        dd = str(localtime.tm_mday)
        return dd
    elif time_style == '8':
        HH = str(localtime.tm_hour)
        return HH
    elif time_style == '9':
        mm = str(localtime.tm_min)
        return mm
    elif time_style == '10':
        ss = str(localtime.tm_sec)
        return ss
    elif time_style == '11':
        weekday = str(localtime.tm_wday)
        return weekday
    elif time_style == '12':
        elapsedDaysFromJan01 = str(localtime.tm_yday)
        return elapsedDaysFromJan01


def AI_Crawlweb(dataWebLocation, copied_html_selector):
    dataWebLocation = unquote(dataWebLocation)  # url decoding
    page = requests.get(dataWebLocation)
    soup = bs(page.text, "html.parser")

    # print_deprecated_by_me(page.text.split('\n'))#전체페이지를 본다

    elements = soup.select(copied_html_selector)
    for index, element in enumerate(elements, 1):
        # print("{} 번째 text: {}".format(index, element.text))
        continue

    return str(element.text)




def AI_respon(usr_input_txt):
    if usr_input_txt == 'pass':
        pass

    elif usr_input_txt == 'x':
        print('fake AI 를 종료합니다')


    elif usr_input_txt == '미세먼지랭킹':
        # print('미세먼지랭킹 날씨 정보를 디스플레이 시도합니다')
        # AI_run('https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103')
        # print('시도완료했습니다')
        # print('미세먼지랭킹 날씨 정보에 접근을 시도합니다')
        # print('미세먼지랭킹 정보 접근 시도')
        # print('미세먼지랭킹 정보')
        AI_run('https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103')

    elif usr_input_txt == '종합날씨':
        AI_run('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B8%B0%EC%98%A8')

    elif usr_input_txt == 'taskkill(알송)':
        taskkill('ALSong.exe')
        taskkill('Alsong.exe')

    elif usr_input_txt == '시간':
        yyyy = getTimeAsStyle('5')
        MM = getTimeAsStyle('6')
        dd = getTimeAsStyle('7')
        HH = getTimeAsStyle('8')
        mm = getTimeAsStyle('9')
        ss = getTimeAsStyle('10')
        print('현재 시간은')
        print(yyyy + '년')
        print(MM + '월')
        print(dd + '일')
        print(HH + '시')
        print(mm + '분')
        print(ss + '초')
        print('입니다')
        pass

    elif usr_input_txt == '초미세먼지':
        # print('네이버 초미세먼지 정보 웹크롤링을 시도합니다.')
        dataWebLocation = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%A0%84%EA%B5%AD%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
        copied_html_selector = '#main_pack > section.sc_new._atmospheric_environment > div > div.api_cs_wrap > div > div:nth-child(3) > div.main_box > div.detail_box'

        lines = "네이버 초미세먼지 정보\n" + AI_Crawlweb(dataWebLocation, copied_html_selector).replace("관측지점 현재 오전예보 오후예보", "",
                                                                                              1).replace("지역별 미세먼지 정보",
                                                                                                         "").strip().replace(
            "서울", "\n서울").replace("경기", "\n경기").replace("인천", "\n인천").replace("강원", "\n강원").replace("세종",
                                                                                                    "\n세종").replace(
            "충북", "\n충북").replace("충남", "\n충남").replace("전남", "\n전남").replace("전북", "\n전북").replace("광주",
                                                                                                    "\n광주").replace(
            "제주", "\n제주").replace("대전", "\n대전").replace("경북", "\n경북").replace("경남", "\n경남").replace("대구",
                                                                                                    "\n대구").replace(
            "울산", "\n울산").replace("부산", "\n부산").replace("     ", " ").replace("\n ", "\n").replace("  ", " ").replace(
            "  ", " ")
        # print('웹크롤링이 완료되었습니다')
        # print('서울과 경기도에 대한 초미세먼지 정보를 말씀드립니다')
        print('서울 경기도 초미세먼지 정보')

        # for line in range(0,len(lines.split('\n'))):
        # print(lines.split('\n')[line])

        # for line in range(0,len(lines.split(' '))):
        # print(lines.split(' ')[line].strip())

        for line in range(0, len(lines.split('\n'))):
            if '서울' in lines.split('\n')[line]:
                foo = lines.split('\n')[line].split(' ')
                for i in range(0, len(foo) - 3):
                    print(foo[i])

            if '경기' in lines.split('\n')[line]:
                foo = lines.split('\n')[line].split(' ')
                for i in range(0, len(foo) - 3):
                    print(foo[i])



    elif usr_input_txt == '공간':

        # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s
        INFO_NAME = '네이버 지역 정보'
        dataWebLocation = 'https://weather.naver.com/'
        copied_html_selector = '#now > div > div.location_info_area > div.location_area > strong'
        # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e

        # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s
        # INFO_NAME='구글 지역 정보'
        # dataWebLocation = "https://www.google.com/search?q=%EA%B8%B0%EC%98%A8&oq=%EA%B8%B0%EC%98%A8&aqs=chrome..69i57j35i39j46i131i199i433i465i512j0i131i433i512l3j46i199i465i512j69i61.1706j1j7&sourceid=chrome&ie=UTF-8"
        # copied_html_selector = '#oFNiHe > div > div > div > div.eKPi4 > span.BBwThe'
        # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e

        # print(INFO_NAME+' '+'웹크롤링을 시도합니다')
        # print('웹크롤링이 완료되었습니다')
        # print('현재위치에 대한 정보를 말씀드립니다')
        lines = AI_Crawlweb(dataWebLocation, copied_html_selector)
        # print_deprecated_by_me(lines)
        # print(lines)
        # print(INFO_NAME +'크롤링 결과를 말씀드립니다')
        print(INFO_NAME + '는')
        print(lines.strip())
        print('인 것으로 추측됩니다')


    elif usr_input_txt == '체감온도':  # [웹 스크랩핑 및 유효텍스트 파싱]

        # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s
        INFO_NAME = '네이버 체감온도 정보'
        dataWebLocation = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B8%B0%EC%98%A8'
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(2)'
        # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e

        # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s
        # INFO_NAME='구글 체감온도 정보'
        # dataWebLocation = ''
        # copied_html_selector = ''
        # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e

        dataWebLocation = unquote(dataWebLocation)  # url decoding
        page = requests.get(dataWebLocation)
        soup = bs(page.text, "html.parser")

        # print_deprecated_by_me(page.text.split('\n'))#전체페이지를 본다

        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text
        print(element_str)

        print(INFO_NAME + '는')
        print(element_str.strip())
        print('인 것으로 추측됩니다')

    elif usr_input_txt == '미세먼지':
        try:
            print("_______________________________________________________________________________________________________________ 미세먼지] ")
            INFO_NAME = '미세먼지랭킹 미세먼지 정보'
            dataWebLocation = 'https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103'
            dataWebLocation = unquote(dataWebLocation)  # url decoding
            selenium_browser_mgr = webdriver.Chrome()
            # 이 주석은 '첫한글자_유실예방코드' 입니다>첫한글자_유실현상발견>원인분석실패>비온전대응
            selenium_browser_mgr.get(dataWebLocation)
            selenium_browser_mgr.implicitly_wait(5)
            selenium_browser_mgr.switch_to_frame('ifram id 를 수집해서 여기에 작성')

            time.sleep(random.uniform(3, 5))
            selenium_browser_mgr.find_element_by_xpath('').click()

            time.sleep(random.uniform(1, 2))
            print(selenium_browser_mgr.find_element_by_xpath('').text)

            # time.sleep(random.uniform(4, 5))
            selenium_browser_mgr.quit()

            # print(element_str)
            print('미세먼지')
            # print(element_str.strip())
        except:
            park4139.trouble_shoot('20231202235939')


    elif usr_input_txt == '위드비전 근태관리':
        try:
            print("_______________________________________________________________________________________________________________ 근태관리] ")
            INFO_NAME = '미세먼지랭킹 미세먼지 정보'
            web_path = 'https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103'
            # web_path = unquote(web_path)  # url decoding
            selenium_browser_mgr = webdriver.Chrome()
            selenium_browser_mgr.implicitly_wait(5)
            selenium_browser_mgr.get(web_path)
            selenium_browser_mgr.switch_to_frame('ifram id 를 수집해서 여기에 작성')

            time.sleep(random.uniform(1, 2))
            selenium_browser_mgr.find_elements_by_css_selector('id').send_keys("pjh4139")
            selenium_browser_mgr.find_element_by_id('pw').send_keys("비밀번호")

            time.sleep(random.uniform(3, 5))
            selenium_browser_mgr.find_element_by_xpath('').click()

            time.sleep(random.uniform(3, 5))
            selenium_browser_mgr.find_element_by_xpath('').click()

            time.sleep(random.uniform(1, 3))  # 자동화탐지를 우회 하기 위한 delay
            selenium_browser_mgr.find_element_by_id('pw').submit()

            time.sleep(random.uniform(1, 3))  # 자동화탐지를 우회 하기 위한 delay
            # driver.find_element_by_id("log.login").click()

            print('______________________________________________________  captcha alternative 1 s')
            # input_js = ' \
            #         document.getElementById("id").value = "{id}"; \
            #         document.getElementById("pw").value = "{pw}"; \
            #     '.format(id="test_id", pw="test_pw")
            # time.sleep(random.uniform(1, 3))  # 자동화탐지를 우회 하기 위한 delay
            # driver.execute_script(input_js)
            #
            # time.sleep(random.uniform(1, 3))  # 자동화탐지를 우회 하기 위한 delay
            # driver.find_element_by_id("log.login").click()
            print('______________________________________________________  captcha alternative 1 e')

            time.sleep(random.uniform(1, 2))
            print(selenium_browser_mgr.find_element_by_xpath('').text)

            # 기존 scrollHeight를 저장
            last_height = selenium_browser_mgr.execute_script("return document.body.scrollHeight")
            while True:
                # Scroll down
                selenium_browser_mgr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # page loading를 위한 대기 시간
                time.sleep(random.uniform(1.5, 2))  # Feed를 불러올 수 있도록 램덤 대기
                # 기존 height하고 변화가 발생하지 않을시 break
                new_height = selenium_browser_mgr.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            # time.sleep(random.uniform(4, 5))
            selenium_browser_mgr.quit()

            # print(element_str)
            print('미세먼지')
            # print(element_str.strip())
        except:
            park4139.trouble_shoot('20231202235939')

    elif usr_input_txt == '종합날씨정보':

        # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s
        INFO_NAME = '네이버 종합날씨정보 정보'
        dataWebLocation = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B8%B0%EC%98%A8'
        # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e

        dataWebLocation = unquote(dataWebLocation)  # url decoding
        page = requests.get(dataWebLocation)
        soup = bs(page.text, "html.parser")

        print("_______________________________________________________________________________________________________________ 전체페이지 출력 시도] ")
        print_deprecated_by_me(page.text.split('\n'))

        print("_______________________________________________________________________________________________________________ 기온] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(2)'
        elements = soup.select(copied_html_selector)

        soup.prettify()

        print(str(soup))

        print(str(soup.prettify()))

        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text.strip()
        print(element_str)
        print('기온')
        print(element_str.strip().replace('°', ''))
        print('도')
        print("_______________________________________________________________________________________________________________ 현재온도] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.weather_graphic > div.temperature_text > strong'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text.strip().replace('현재 온도', '')
        print(element_str)
        print('현재온도')
        print(element_str.replace('°', ''))
        print('도')
        print("_______________________________________________________________________________________________________________ 체감온도] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(2)'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text.strip()
        print(element_str)
        print('체감온도')
        print(element_str.replace('°', ''))
        print('도')
        print("_______________________________________________________________________________________________________________ 습도] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(4)'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text.strip()
        print(element_str)
        print('습도')
        print(element_str.replace('%', ''))
        print('퍼센트')
        print("_______________________________________________________________________________________________________________ 바람] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(6)'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text
        print(element_str)
        print('바람')
        print(element_str.strip().replace('m/s', ''))
        print('미터퍼세크')
        print("_______________________________________________________________________________________________________________ 자외선] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div.report_card_wrap > ul > li.item_today.level2 > a > span'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text
        print(element_str)
        print('자외선')
        print(element_str.strip())
        print("_______________________________________________________________________________________________________________ 미세먼지] ")
        # 미세먼지랭킹 미세먼지 정보 s# 미세먼지랭킹 미세먼지 정보 s# 미세먼지랭킹 미세먼지 정보 s# 미세먼지랭킹 미세먼지 정보 s
        INFO_NAME = '미세먼지랭킹 미세먼지 정보'
        dataWebLocation = 'https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103'
        # 미세먼지랭킹 미세먼지 정보 e # 미세먼지랭킹 미세먼지 정보 e # 미세먼지랭킹 미세먼지 정보 e # 미세먼지랭킹 미세먼지 정보 e
        dataWebLocation = unquote(dataWebLocation)  # url decoding
        page = requests.get(dataWebLocation)
        soup = bs(page.text, "html.parser")
        copied_html_selector = '#body_main > table:nth-child(7) > tbody > tr:nth-child(2) > td:nth-child(1) > div'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text
        print(element_str)
        print('미세먼지')
        print(element_str.strip().replace('m/s', ''))
        print("_______________________________________________________________________________________________________________ 초미세먼지] ")
        copied_html_selector = '#body_main > table:nth-child(7) > tbody > tr:nth-child(2) > td:nth-child(2) > div'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text
        print(element_str)
        print('초미세먼지')
        print(element_str.strip())
        print('입니다')

        # print("_______________________________________________________________________________________________________________ _________] ")
        # copied_html_selector = '_________'
        # elements = soup.select(copied_html_selector)
        # print_deprecated_by_me(elements)#추출된 elements 출력 시도

    elif usr_input_txt == 'hardcode json 처리':
        print("_______________________________________________________________________________________________________________ json 처리 시작] ")
        print('준비중인 기능입니다')

        # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s
        INFO_NAME = '네이버 체감온도 정보'
        dataWebLocation = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B8%B0%EC%98%A8'
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(2)'
        # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e

        dataWebLocation = unquote(dataWebLocation)  # url decoding
        page = requests.get(dataWebLocation)
        soup = bs(page.text, "html.parser")

        copied_html_selector = '_________'
        elements = soup.select(copied_html_selector)
        print_deprecated_by_me(elements)  # 추출된 elements 출력 시도
        for i in range(0, len(page.text.split('\n'))):
            if 'hourlyFcastListJson' in page.text.split('\n')[i]:
                # print("_______________________________________________________________________________________________________________ hourlyFcastListJson 들어있는 줄들 출력시도] ")
                str_containing_hourlyFcastListJson = page.text.split('\n')[i].strip()
                # print(type(str_containing_hourlyFcastListJson))
                # print(str_containing_hourlyFcastListJson)
                print("_______________________________________________________________________________________________________________ json_str] ")
                json_str = str_containing_hourlyFcastListJson.split('=')[-1].split(';')[0].strip()
                # print(type(json_str))
                # print(json_str)
                # print(json.dumps(json_str, indent=4, sort_keys=True))
                print("_______________________________________________________________________________________________________________ json_obj] ")
                json_obj = json.loads(json_str)
                # print(type(json_str))
                # print(json_obj)
                # print(json.dumps(json_obj, indent=4, sort_keys=True))

        print("_______________________________________________________________________________________________________________ json_obj[i]['windSpd']][json obj 내부의")
        # for i in range(0,len(json_obj)):
        # print(str(i),':', str(json_obj[i]['windSpd']))
        # pass

        print("_______________________________________________________________________________________________________________ foo.json 에 저장] ")
        file_path = "./json/foo.json"

        json_dict = {}
        json_dict['head'] = []
        json_dict['head'].append({
            "title": "Android Q, Scoped Storage",
            "url": "https://codechacha.com/ko/android-q-scoped-storage/",
            "draft": "false"
        })
        json_dict['body'] = []
        json_dict['body'].append({
            "that i want to save": str(json_obj[40]['windSpd']),
            "that i want to save2": "foo"
            # "that i want to save": str(json.dump(json_obj[40]['windSpd']))
        })
        json_dict['tail'] = []
        json_dict['tail'].append({
            "title": "Android Q, Scoped Storage",
            "url": "https://codechacha.com/ko/android-q-scoped-storage/",
            "draft": "false"
        })
        json_dict['tail'].append({
            "that i want to save str": "i",
            "that i want to save str2": "love",
            "that i want to save str2": "love"
        })
        print(json_dict)
        print(type(json_dict))

        with open(file_path, 'w') as outfile:
            json.dump(json_dict, outfile, indent=4)

        print(INFO_NAME + '는')
        print('________')
        print('인 것으로 추측됩니다')


    elif usr_input_txt == '네이버 미세먼지':
        print('네이버 미세먼지 정보 웹크롤링을 시도합니다.')
        dataWebLocation = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%A0%84%EA%B5%AD%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
        copied_html_selector = '#main_pack > section.sc_new._atmospheric_environment > div > div.api_cs_wrap > div > div:nth-child(3) > div.main_box > div.detail_box'

        lines = "네이버 미세먼지정보\n" + AI_Crawlweb(dataWebLocation, copied_html_selector).replace("관측지점 현재 오전예보 오후예보", "",
                                                                                            1).replace("지역별 미세먼지 정보",
                                                                                                       "").strip().replace(
            "서울", "\n서울").replace("경기", "\n경기").replace("인천", "\n인천").replace("강원", "\n강원").replace("세종",
                                                                                                    "\n세종").replace(
            "충북", "\n충북").replace("충남", "\n충남").replace("전남", "\n전남").replace("전북", "\n전북").replace("광주",
                                                                                                    "\n광주").replace(
            "제주", "\n제주").replace("대전", "\n대전").replace("경북", "\n경북").replace("경남", "\n경남").replace("대구",
                                                                                                    "\n대구").replace(
            "울산", "\n울산").replace("부산", "\n부산").replace("     ", " ").replace("\n ", "\n").replace("  ", " ").replace(
            "  ", " ")
        # print(lines.replace("관측지점 현재 오전예보 오후예보","관측지점 현재 오전예보 오후예보\n"))
        # print('웹 크롤링된 네이버 미세먼지 정보 접근을 시도합니다.')
        # print('네이버 미세먼지 정보입니다')
        # print('다음은 네이버 미세먼지 정보입니다')
        # print('관측지점 현재 오전예보 오후예보')
        # print('웹 크롤링된 네이버 미세먼지 정보를 말씀드립니다')
        print('웹크롤링이 완료되었습니다')
        print('서울과 경기도에 대한 정보를 말씀드립니다')

        # for line in range(0,len(lines.split('\n'))):
        # print(lines.split('\n')[line])

        # for line in range(0,len(lines.split(' '))):
        # print(lines.split(' ')[line].strip())

        for line in range(0, len(lines.split('\n'))):
            if '서울' in lines.split('\n')[line]:
                foo = lines.split('\n')[line].split(' ')
                for i in range(0, len(foo) - 3):
                    print(foo[i])

            if '경기' in lines.split('\n')[line]:
                foo = lines.split('\n')[line].split(' ')
                for i in range(0, len(foo) - 3):
                    print(foo[i])

    elif usr_input_txt == '가용코드목록':
        print_deprecated_by_me(AI_available_cmd_code_list)
        print("조회되었습니다")

    # elif usr_input_txt == 'voiceless mode':
    # def print(text):
    # print(text)

    # elif usr_input_txt == 'voice mode':
    # def print(text):
    # address=os.getcwd()+'\\mp3\\'+ text +'.mp3'

    # if os.path.exists(address):
    # os.system('call "'+address+'"')
    # length_of_mp3 = get_length_of_mp3(address)
    # length_of_mp3 = float(length_of_mp3)
    # length_of_mp3 = round(length_of_mp3,1)
    # time.sleep(length_of_mp3*1.05)

    # else:
    # mgr_gTTS = gTTS(text=text, lang='ko')
    # mgr_gTTS.save('./mp3/'+ text +'.mp3')
    # os.system('call "'+address+'"')

    # length_of_mp3 = get_length_of_mp3(address)
    # length_of_mp3 = float(length_of_mp3)
    # length_of_mp3 = round(length_of_mp3,1)
    # time.sleep(length_of_mp3*1.05)

    # taskkill('ALSong.exe')

    # elif usr_input_txt == '`':
    #     print('single mode 가 시작되었습니다')
    #     # print('single mode s single mode s single mode s single mode s single mode s single mode s single mode s single mode s single mode s ')
    #     while(True):
    #         batch_mode_input=input('>>>')
    #         if batch_mode_input =='x':
    #             print('single mode를 종료합니다')
    #             break
    #         elif len(batch_mode_input)==1:
    #             usr_input_txt=AI_available_cmd_code_list[int(batch_mode_input)-1].split(':')[0]
    #             AI_respon(usr_input_txt)
    #         elif batch_mode_input =='':
    #             print('아무것도 입력되지 않았습니다')
    #         elif batch_mode_input =='`':
    #             print('백팁은 single mode에서 입력하실 수 없습니다.')
    #         else:
    #             print('single mode 에서는 1자리만 입력하실 수 있습니다.')
    #     # print('eingle mode e eingle mode e eingle mode e eingle mode e eingle mode e eingle mode e eingle mode e eingle mode e eingle mode e ')
    #

    # elif usr_input_txt == '``':
    #     print('batch mode 가 시작되었습니다')
    #     # print('batch mode s batch mode s batch mode s batch mode s batch mode s batch mode s batch mode s batch mode s batch mode s ')
    #     while(True):
    #         batch_mode_input=input('>>>')
    #         if batch_mode_input=='x' or batch_mode_input=='X' :
    #             print('batch mode를 종료합니다')
    #             break
    #         # batch_mode_input=list(batch_mode_input)                         # batch_mode_input = [3,2,1]
    #         # print('입력된 배치명령의 개수는' + str(len(batch_mode_input)+1) +'개 입니다')
    #         if batch_mode_input == '':
    #             print('아무것도 입력되지 않았습니다')
    #             print('명령코드를 입력해주세요')
    #         else:
    #             print('입력된 배치명령의 개수는' + str(len(batch_mode_input)) +'개 입니다')
    #             for i in range(0,len(batch_mode_input)):                      # i=0
    #                 usr_input_txt=AI_available_cmd_code_list[int(batch_mode_input[i])-1].split(':')[0] #usr_input_txt=AI_available_cmd_code_list[2].split(':')[0]
    #                 print(str(i+1)+'번째 코드를 실행시도합니다')
    #                 AI_respon(usr_input_txt)
    #
    #     # print('batch mode e batch mode e batch mode e batch mode e batch mode e batch mode e batch mode e batch mode e batch mode e ')

    elif usr_input_txt == '`':
        print('advanced batch mode 가 시작되었습니다')
        print('advanced batch mode s advanced batch mode s advanced batch mode s advanced batch mode s advanced batch mode s advanced batch mode s advanced batch mode s')
        os.system('echo "202312031429" && pause')
        print("")
        print("")
        print("")
        print("")
        # print(' '+'가용명령코드목록')
        print('                                     ' + '가용명령코드목록')
        print("")
        print_deprecated_by_me(AI_available_cmd_code_list)
        print("")
        while (True):
            batch_mode_input = input("                                                                                                ")
            if batch_mode_input == 'x' or batch_mode_input == 'X':
                print('advanced batch mode를 종료합니다')
                break
            elif batch_mode_input == '':
                print('아무것도 입력되지 않았습니다')
                print('명령코드를 입력해주세요')
            else:
                list = batch_mode_input.split(' ')
                # print('입력된 코드 목록 입니다')
                # for str in list:
                #     print(str)
                # for i in range(0,len(list)-2):
                for list_element in list:
                    # print(str((i+1))+'번째 코드를 실행시도합니다')
                    # print(list[i])
                    # AI_respon(str(list[i]))
                    # if len(AI_available_cmd_code_list)<AI_available_cmd_code_list[int(list[i])-1].split(':')[0]:
                    # AI_respon(AI_available_cmd_code_list[int(list[i])-1].split(':')[0])
                    # print(list_element)
                    # for i in range(0, len(AI_available_cmd_code_list) - 1):
                    #     if usr_input_txt in AI_available_cmd_code_list[i].split(':')[0]:
                    #         # if usr_input_txt!='' or usr_input_txt!='`':
                    #         if usr_input_txt != '':
                    #             # print(AI_available_cmd_code_list[i].split(':')[0]+'에 대한 명령코드가 입력되었습니다')
                    #             pass
                    #
                    # AI_respon(usr_input_txt)
                    # try:
                    # print(len(AI_available_cmd_code_list[int(list_element) - 1]))
                    # print(AI_available_cmd_code_list[int(list_element) - 1])
                    # print(AI_available_cmd_code_list[int(list_element) - 1].split(':')[0])
                    try:
                        AI_respon(AI_available_cmd_code_list[int(list_element) - 1].split(':')[0])
                    except:  # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
                        print('advanced batch mode 실행 중 예외가 발생했습니다')
                        print('advanced batch mode 실행 중 예외가 발생했습니다')
                        # print('가용코드 목록에 없는 코드입니다')

        print('advanced batch mode e advanced batch mode e advanced batch mode e advanced batch mode e advanced batch mode e advanced batch mode e advanced batch mode e')


    elif usr_input_txt == '가용명령개수':
        print('가용명령의 개수는')
        print(str(len(AI_available_cmd_code_list)))
        print('개 입니다')
        AI_respon('3 ')

    elif usr_input_txt == '식물조언':
        print('식물에게 물샤워를 줄시간입니다')
        print('물샤워를 시켜주세요')
        print('오늘은 식물에게 햇빛샤워를 시켜주는날입니다')
        print('하늘이가 없을때 샤워를 시켜주세요')
        print('하트축전에게 빠르게 식물등빛을 주세요')
        print('이러다 죽습니다')
        print('서둘러 등빛을 주세요')

    elif usr_input_txt == '':
        print('아무것도 입력되지 않았습니다')
        print('명령코드를 입력해주세요')

    elif usr_input_txt == '몇 시야' or usr_input_txt == '몇시야':
        # print(getTimeAsStyle('5'))
        # print('년')
        # print(getTimeAsStyle('6'))
        # print('월')
        # print(getTimeAsStyle('7'))
        # print('일')
        print(getTimeAsStyle('8'))
        print('시')
        print(getTimeAsStyle('9'))
        print('분')
        print('입니다')

    elif usr_input_txt == 'jhppc1':
        jhppc1 = 'https://remotedesktop.google.com/access/session/b797cd99-b738-f4db-9b38-9a2e25a57a47'
        AI_run(jhppc1)

    elif usr_input_txt == 'remotedesktop':
        remotedesktop = 'https://remotedesktop.google.com/access'
        AI_run(remotedesktop)

    else:
        # print('입력하신 내용이 usr_input_txt 는 oooo 과 유사합니다') #[to do]
        # print('해당 기능은 아직 준비되지 않았습니다')
        available_no_cmd_list = []
        try:
            for i in range(0, len(AI_available_cmd_code_list)):
                available_no_cmd_list.append(i + 1)

            print(available_no_cmd_list)
        except:
            print('______________________________________________________  error id 2023 02 18 13 58 s')
            # :: trouble shooting
            print(f':: trouble shooting id : 20231129111853')
            print(f'traceback.print_exc(file=sys.stdout) : {traceback.print_exc(file=sys.stdout)}')
            # traceback.print_exc(file=sys.stdout)
            print('______________________________________________________  error id 2023 02 18 13 58 e')
            print('익셉션이 발생하였습니다. 익셉션을 발생시키고 넘어가도록 하는 것은. 익셉션을 발생시키지 않고 처리하는 것보다 좋은 방법은 아닌 것 같습니다. 추후에 수정을 해주세요. 일단은 진행합니다')
            # print('익셉션이 발생하였습니다')
            # print('익셉션을 발생시키고 넘어가도록 하는 것은 익셉션을 발생시키지 않고 처리하는 것보다 좋은 방법은 아닌 것 같습니다')
            # print('추후에 수정을 해주세요')
            # print('일단은 진행합니다')


def AI_run(target_str):
    last_txt = target_str.split('.')[-1]
    if 'http' in target_str:
        if '%' in target_str:
            target_str = 'explorer "' + unquote(target_str).strip() + '"'  # url decoding
            # print("mkr749 : "+target_str)
            os.system(target_str)
        else:
            os.system('start ' + target_str)
            # os.system('explorer ' + target_str)
            # __________________________________________________________________________________ 방법1 s
            chromeMgr = webdriver.Chrome()
            # 이 주석은 '첫한글자_유실예방코드' 입니다>첫한글자_유실현상발견>원인분석실패>비온전대응
            chromeMgr.get(target_str)
            # __________________________________________________________________________________ 방법1 e

    elif 'txt' in last_txt:
        os.system('start ' + target_str)
        # os.startfile(os.getcwd()+'/mp3/'+ text +'.mp3') #비동기처리방식
        # os.system('call "'+os.getcwd()+'/mp3/'+ text +'.mp3"')  #동기처리방식[실패]

    elif 'mp3' in last_txt:
        os.system('start ' + target_str)

    elif 'mp4' in last_txt:
        os.system('start ' + target_str)


def print_deprecated_by_me(target_list):
    cnt = 1
    for target in target_list:
        print(f'                                        {str(cnt)} : {target} ')
        cnt += 1


def convert_path_style(path_str, style_no):
    if style_no == "/":
        if "\\" in path_str:
            path_str = path_str.replace("\\", "/")
            return path_str
        if "//" in path_str:
            path_str = path_str.replace("//", "/")
            return path_str

    elif style_no == "\\":
        if "/" in path_str:
            path_str = path_str.replace("/", "\\")
            return path_str
        if "\\\\" in path_str:
            path_str = path_str.replace("\\\\", "\\")
            return path_str

    elif style_no == "//":
        if "/" in path_str:
            path_str = path_str.replace("/", "//")
            return path_str

    elif style_no == "\\\\":
        if "\\" in path_str:
            path_str = path_str.replace("\\", "\\\\")
            return path_str

    if style_no == "1":
        if "\\" in path_str:
            path_str = path_str.replace("\\", "/")
            return path_str

    elif style_no == "2":
        if "/" in path_str:
            path_str = path_str.replace("/", "\\")
            return path_str

    elif style_no == "3":
        if "\\\\" in path_str:
            path_str = path_str.replace("\\\\", "\\")
            return path_str

    elif style_no == "4":
        if "//" in path_str:
            path_str = path_str.replace("//", "/")
            return path_str

    elif style_no == "5":
        if "/" in path_str:
            path_str = path_str.replace("/", "//")
            return path_str

    elif style_no == "6":
        if "\\" in path_str:
            path_str = path_str.replace("\\", "\\\\")
            return path_str

    else:
        print('trouble shooting info id')
        print('yyyy MM dd HH mm ss')


def get_length_by_using_(______tuple):  # done
    return len(______tuple)


def get_keys_by_using_(______tuple, _____as):
    if _____as == 'as_str':
        return str(______tuple.keys()).replace("dict_keys([", "").replace("])", "").replace("\'", "")
    elif _____as == 'as_list':
        return get_keys_by_using_(______tuple, "as_str").split(", ")
    else:
        print("it is not magical word. so do nothing")


def print_key_with_index_by_using_(______tuple):
    for ______tuple_key in get_keys_by_using_(______tuple, "as_list"):
        print(str(get_keys_by_using_(______tuple, "as_list").index(______tuple_key)) + " " + ______tuple_key)


def replace_text_B_and_text_C_interchangeably_at_text_A_by_using_(____text_A, ____text_B, ____text_C, _____and):
    foo_foo = "{{kono foo wa sekai de uituna mono ni motomo chikai desu}}"
    text_special = "{{no}}"
    text_B_cnt = ____text_A.count(____text_B)
    foo_list = []
    foo_str = ""
    foo_cmt = 0
    if ____text_C == "":
        ____text_A = ____text_A.replace(____text_B, ____text_C)
    elif text_special in ____text_C:
        print("text_A 에서 " + ____text_B + " 를 총" + str(text_B_cnt) + "개 발견하였습니다")
        foo_list = ____text_A.split(____text_B)
        if ____text_B in ____text_C:
            foo_cmt = 0
            for j in foo_list:
                if j == foo_list[-1]:
                    pass
                else:
                    foo_str = foo_str + j + ____text_C.split(text_special)[0] + str(foo_cmt)
                foo_cmt = foo_cmt + 1
            ____text_A = ""
            ____text_A = foo_str
        else:
            foo_cmt = 0
            for j in foo_list:
                if j == foo_list[-1]:
                    pass
                else:
                    foo_str = foo_str + j + ____text_C.split(text_special)[0] + str(foo_cmt)
                foo_cmt = foo_cmt + 1
            ____text_A = ""
            ____text_A = foo_str
    else:
        ____text_A = ____text_A.replace(____text_C, foo_foo)
        ____text_A = ____text_A.replace(____text_B, ____text_C)
        ____text_A = ____text_A.replace(foo_foo, ____text_B)


def act_via_interchangeable_triangle_model_by_using_(____text_A, ____text_B, ____text_C, _____and):
    foo_foo = "{{kono foo wa sekai de uituna mono ni motomo chikai desu}}"
    if ____text_C == "":
        ____text_A = ____text_A.replace(____text_B, ____text_C)
    else:
        ____text_A = ____text_A.replace(____text_C, foo_foo)
        ____text_A = ____text_A.replace(____text_B, ____text_C)
        ____text_A = ____text_A.replace(foo_foo, ____text_B)

 
 
# _________________________________________________________________________________________ mkr: new
class park4139:
    project_directory = ''
    log_directory=''

    def __init__(self,project_directory,log_directory):
        self.project_directory =project_directory
        self.log_directory=log_directory
        os.system('chcp 65001')
        

    # 2023-12-03 일요일 13:06 최신화 함수
    def get_python_pkg_global_path(self):
        for path in sys.path:
            print(path)
            if self.is_regex_searched(context=path, regex='site-packages') == True:
                print(rf'echo "{path}"')
                os.system(rf'echo "{path}" | clip.exe ')
                os.system(rf'explorer "{path}"')
                os.exit()

    # 2023-12-03 일요일 13:25 최신화 함수
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

    # 2023-12-03 일요일 13:25 최신화 변수명 출력함수
    def print(variable):
        def namestr(obj, namespace):
            get_name = [name for name in namespace if namespace[name] is obj]
            return get_name[0]
        def Change(variable):
            print(namestr(variable, globals()), "=", variable)

        print(f'{Change(variable)} : {variable}')

    

    def speak(self,ment):
        # helper_py = rf"C:\Users\WIN10PROPC3\Desktop\services\helper-from-text-to-speech\helper.py"
        # try:
        #     os.system(rf'python "{helper_py}" "{ment}"')
        #     os.chdir(self.project_directory)
        # except:
        #     park4139.trouble_shoot('20231202231750')
        print(ment)

    def speaks(self,ments):
        for ment in ments:
            self.speak(ment)


    # 2023-12-03 일요일 13:25 최신화 함수
    def trouble_shoot(self,id: str):
        print(f':: _______________________________________________________________________________________ trouble shooting id : {id}  s')
        os.system(f'echo {id}| clip.exe')
        traceback.print_exc(file=sys.stdout)
        self.speak('트러블슈팅코드를 클립보드에 붙여넣었습니다')
        print('트러블슈팅코드를 클립보드에 붙여넣었습니다')
        print(f':: _______________________________________________________________________________________ trouble shooting id : {id}  e')
        os.system('pause')


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



    # 디스플레이 정보 가져오기
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


    def is_regex_searched(context, regex):
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


    def run_command(self,cmd,service_directory):
        os.chdir(service_directory)
        print(rf'test command > :{cmd}')
        try:
            lines = subprocess.check_output(cmd, shell=True).decode('utf-8').split('\n')
            for line in lines:
                print(line)
        except:
            self.trouble_shoot('20231203144559')
        os.chdir(self.project_directory)


    # 시작로깅(json 형태로 넣을 수 있도록 코드 업데이트 할것)
    def log_s(self):
        lines = subprocess.check_output('chcp 65001', shell=True).decode('utf-8').split('\n')  # 한글 엔코딩 설정 , shell=True).decode('utf-8').split('\n')
        self.time_s = time.time()  # 서버라이프사이클 계산용 변수 설정
        server_time = self.get_time_as_(f'%Y-%m-%d %H:%M:%S')
        lines = subprocess.check_output(rf'echo "server_time  : {server_time} ,  project_directory  : {self.project_directory},  __file__  : {__file__},  log_title : 시작로깅 " >> "{self.log_directory}\success.log"', shell=True).decode('utf-8').split('\n')
        for line in lines:
            print(line)

    def log_mid(self):
        server_time = self.get_time_as_(f'%Y-%m-%d %H:%M:%S')
        lines = subprocess.check_output(rf'echo "server_time  : {server_time} ,  project_directory  : {self.project_directory},  __file__  : {__file__},  log_title : 중간로깅 " >> "{self.log_directory}\success.log"', shell=True).decode('utf-8').split('\n')
        # os.system('cls')


    def log_e(self):
        self.time_e = time.time()  # 서버라이프사이클 계산용 변수 설정
        server_time = self.get_time_as_(f'%Y-%m-%d %H:%M:%S')
        server_life_cycle = self.time_e - self.time_s
        lines = subprocess.check_output(rf'echo "server_time  : {server_time} ,  project_directory  : {self.project_directory},  __file__  : {__file__},  log_title : 종료로깅,  server_life_cycle : {server_life_cycle}  " >> "{self.log_directory}\success.log"', shell=True).decode('utf-8').split('\n')
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


class etc:
    # 버튼 멘트 셋팅
    button_ments = {
        'yes': '해라',
        'no': '마라',
        'again': '이따 다시물어라',
    }