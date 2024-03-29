# -*- coding: utf-8 -*-
# 일일 던전, 마을의뢰 플레이

import sys
from time import sleep
import time
import pyautogui
import pywinauto
import auto_daily_2 as ad
import os

def odin1_write(stage):
    with open("odin1.txt", "w") as f:
        f.write(stage)

def odin2_write(stage):
    with open("odin2.txt", "w") as f:
        f.write(stage)

def odin1_read():
    with open("odin1.txt", "r") as f:
        stage = f.read()
    return stage

def odin2_read():
    with open("odin2.txt", "r") as f:
        stage = f.read()
    return stage

# 데일리 오딘1 스케줄
def play_odin1():
    # 1번 캐릭터
    if odin1 == 1:
        ad.active_mecro_1()
        ad.ck_popup()
        tr_end = ad.town_request()
        if tr_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('3')
            ad.get_mimir() # 미미르 받고 못 받으면 포션 먹기
            ad.daily_gold_item() # 매일 골드 상품 구매
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            ad.go_town() # 물약 구매

    if odin1 == 2:
        ad.active_mecro_1()
        ad.ck_popup()
        ad.create_party(2) # 파티던전 레벨
        paly_party_dg = ad.paly_party_dg()
        if paly_party_dg == 1:
            odin1_write('3')

    if odin1 == 3:
        ad.active_mecro_1()
        ad.ck_popup()
        money_dg_end = ad.money_dg_entrance(5)
        if money_dg_end == 1:
            odin1_write('4')

    if odin1 == 4:
        ad.active_mecro_1()
        ad.ck_popup()
        scroll_dg_end = ad.scroll_dg_entrance(5)
        if scroll_dg_end == 1:
            odin1_write('5')
            
    if odin1 == 5:
        ad.active_mecro_1()
        ad.ck_popup()
        event_dg_end = ad.event_dg_entrance(3)
        if event_dg_end == 1:
            odin1_write('21')
            # ad.char_change(2) # 1번 캐릭터만 플레이하기로 함

    # 2번 캐릭터 다시 추가하려면 번호 카운팅 다시 해야 함
    # if odin1 == 5:
    #     ad.active_mecro_1()
    #     tr_end = ad.town_request()
    #     if tr_end == 1:
    #         odin1_write('6')
    #         ad.get_mimir() # 미미르 받고 못 받으면 포션 먹기
    #         ad.guild_check() # 길드 출석 체크
    #         ad.item_bunhae() # 아이템 분해
    #         ad.go_town() # 물약 구매

    if odin1 == 6:
        ad.active_mecro_1()
        ad.create_party(1) # 파티던전 레벨
        paly_party_dg = ad.paly_party_dg()
        if paly_party_dg == 1:
            odin1_write('7')

    if odin1 == 7:
        ad.active_mecro_1()
        money_dg_end = ad.money_dg_entrance(2)
        if money_dg_end == 1:
            odin1_write('8')

    if odin1 == 8:
        ad.active_mecro_1()
        scroll_dg_end = ad.scroll_dg_entrance(2)
        if scroll_dg_end == 1:
            odin1_write('9')
            ad.char_change(3)

    # 3번 캐릭터
    if odin1 == 9:
        ad.active_mecro_1()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin1_write('10')
            ad.get_mimir() # 미미르 받고 못 받으면 포션 먹기
            ad.guild_check() # 길드 출석 체크
            ad.item_bunhae() # 아이템 분해
            ad.go_town() # 물약 구매

    if odin1 == 10:
        ad.active_mecro_1()
        ad.create_party(1) # 파티던전 레벨
        paly_party_dg = ad.paly_party_dg()
        if paly_party_dg == 1:
            odin1_write('11')

    if odin1 == 11:
        ad.active_mecro_1()
        money_dg_end = ad.money_dg_entrance(2)
        if money_dg_end == 1:
            odin1_write('12')

    if odin1 == 12:
        ad.active_mecro_1()
        scroll_dg_end = ad.scroll_dg_entrance(2)
        if scroll_dg_end == 1:
            odin1_write('13')
            ad.char_change(4)     
                        

    # 4번 캐릭터
    if odin1 == 13:
        ad.active_mecro_1()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin1_write('14')
            ad.get_mimir() # 미미르 받고 못 받으면 포션 먹기
            ad.guild_check() # 길드 출석 체크
            ad.item_bunhae() # 아이템 분해
            ad.go_town() # 물약 구매

    if odin1 == 14:
        ad.active_mecro_1()
        ad.create_party(1) # 파티던전 레벨
        paly_party_dg = ad.paly_party_dg()
        if paly_party_dg == 1:
            odin1_write('15')

    if odin1 == 15:
        ad.active_mecro_1()
        money_dg_end = ad.money_dg_entrance(2)
        if money_dg_end == 1:
            odin1_write('16')

    if odin1 == 16:
        ad.active_mecro_1()
        scroll_dg_end = ad.scroll_dg_entrance(2)
        if scroll_dg_end == 1:
            odin1_write('17')  
            ad.char_change(5)


    # 5번 캐릭터
    if odin1 == 17:
        ad.active_mecro_1()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin1_write('18')
            ad.get_mimir() # 미미르 받고 못 받으면 포션 먹기
            ad.guild_check() # 길드 출석 체크
            ad.item_bunhae() # 아이템 분해
            ad.go_town() # 물약 구매

    if odin1 == 18:
        ad.active_mecro_1()
        ad.create_party(1) # 파티던전 레벨
        paly_party_dg = ad.paly_party_dg()
        if paly_party_dg == 1:
            odin1_write('19')

    if odin1 == 19:
        ad.active_mecro_1()
        money_dg_end = ad.money_dg_entrance(2)
        if money_dg_end == 1:
            odin1_write('20')

    if odin1 == 20:
        ad.active_mecro_1()
        scroll_dg_end = ad.scroll_dg_entrance(2)
        if scroll_dg_end == 1:
            odin1_write('21')
            ad.char_change(1)

# 데일리 오딘2 스케줄
def play_odin2():
    # 1번 캐릭터
    if odin2 == 1:
        ad.active_mecro_2()
        ad.ck_popup()
        tr_end = ad.town_request()
        if tr_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('3')
            ad.get_mimir() # 미미르 받고 못 받으면 포션 먹기
            ad.daily_gold_item() # 매일 골드 상품 구
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            ad.go_town() # 물약 구매

    if odin2 == 2:
        ad.active_mecro_2()
        ad.ck_popup()        
        ad.create_party(2) # 파티던전 레벨
        paly_party_dg = ad.paly_party_dg()
        if paly_party_dg == 1:
            odin2_write('3')

    if odin2 == 3:
        ad.active_mecro_2()
        ad.ck_popup()
        money_dg_end = ad.money_dg_entrance(5)
        if money_dg_end == 1:
            odin2_write('4')

    if odin2 == 4:
        ad.active_mecro_2()
        ad.ck_popup()
        scroll_dg_end = ad.scroll_dg_entrance(5)
        if scroll_dg_end == 1:
            odin2_write('5')
            
    if odin2 == 5:
        ad.active_mecro_2()
        ad.ck_popup()
        event_dg_end = ad.event_dg_entrance(3)
        if event_dg_end == 1:
            odin2_write('21')
            # ad.char_change(2) # 1번 캐릭터만 플레이하기로 함

    # 2번 캐릭터
    # if odin2 == 5:
    #     ad.active_mecro_2()
    #     tr_end = ad.town_request()
    #     if tr_end == 1:
    #         odin2_write('6')
    #         ad.get_mimir() # 미미르 받고 못 받으면 포션 먹기
    #         ad.guild_check() # 길드 출석 체크
    #         ad.item_bunhae() # 아이템 분해
    #         ad.go_town() # 물약 구매

    if odin2 == 6:
        ad.active_mecro_2()
        ad.create_party(1) # 파티던전 레벨
        paly_party_dg = ad.paly_party_dg()
        if paly_party_dg == 1:
            odin2_write('7')

    if odin2 == 7:
        ad.active_mecro_2()
        money_dg_end = ad.money_dg_entrance(2)
        if money_dg_end == 1:
            odin2_write('8')

    if odin2 == 8:
        ad.active_mecro_2()
        scroll_dg_end = ad.scroll_dg_entrance(2)
        if scroll_dg_end == 1:
            odin2_write('9')
            ad.char_change(3)

    # 3번 캐릭터
    if odin2 == 9:
        ad.active_mecro_2()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin2_write('10')
            ad.get_mimir() # 미미르 받고 못 받으면 포션 먹기
            ad.guild_check() # 길드 출석 체크
            ad.item_bunhae() # 아이템 분해
            ad.go_town() # 물약 구매

    if odin2 == 10:
        ad.active_mecro_2()
        ad.create_party(1) # 파티던전 레벨
        paly_party_dg = ad.paly_party_dg()
        if paly_party_dg == 1:
            odin2_write('11')

    if odin2 == 11:
        ad.active_mecro_2()
        money_dg_end = ad.money_dg_entrance(2)
        if money_dg_end == 1:
            odin2_write('12')

    if odin2 == 12:
        ad.active_mecro_2()
        scroll_dg_end = ad.scroll_dg_entrance(2)
        if scroll_dg_end == 1:
            odin2_write('13')
            ad.char_change(4)        
                        

    # 4번 캐릭터
    if odin2 == 13:
        ad.active_mecro_2()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin2_write('14')
            ad.get_mimir() # 미미르 받고 못 받으면 포션 먹기
            ad.guild_check() # 길드 출석 체크
            ad.item_bunhae() # 아이템 분해
            ad.go_town() # 물약 구매

    if odin2 == 14:
        ad.active_mecro_2()
        ad.create_party(1) # 파티던전 레벨
        paly_party_dg = ad.paly_party_dg()
        if paly_party_dg == 1:
            odin2_write('15')

    if odin2 == 15:
        ad.active_mecro_2()
        money_dg_end = ad.money_dg_entrance(2)
        if money_dg_end == 1:
            odin2_write('16')

    if odin2 == 16:
        ad.active_mecro_2()
        scroll_dg_end = ad.scroll_dg_entrance(2)
        if scroll_dg_end == 1:
            odin2_write('17') 
            ad.char_change(5)


    # 5번 캐릭터
    if odin2 == 17:
        ad.active_mecro_2()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin2_write('18')
            ad.get_mimir() # 미미르 받고 못 받으면 포션 먹기
            ad.guild_check() # 길드 출석 체크
            ad.item_bunhae() # 아이템 분해
            ad.go_town() # 물약 구매

    if odin2 == 18:
        ad.active_mecro_2()
        ad.create_party(1) # 파티던전 레벨
        paly_party_dg = ad.paly_party_dg()
        if paly_party_dg == 1:
            odin2_write('19')

    if odin2 == 19:
        ad.active_mecro_2()
        money_dg_end = ad.money_dg_entrance(2)
        if money_dg_end == 1:
            odin2_write('20')

    if odin2 == 20:
        ad.active_mecro_2()
        scroll_dg_end = ad.scroll_dg_entrance(2)
        if scroll_dg_end == 1:
            odin2_write('21')
            ad.char_change(1)

# 오딘1 지하감옥 스케줄
def play_week_dg_odin1():
    if odin1 == 21:
        ad.active_mecro_1()
        week_end = ad.week_dg_entrance(6)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('27')
            # ad.char_change(2) # 1번만 플레이
    
    if odin1 == 22:
        ad.active_mecro_1()
        week_end = ad.week_dg_entrance(2)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('23')
            ad.char_change(3)

    if odin1 == 23:
        ad.active_mecro_1()
        week_end = ad.week_dg_entrance(2)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('24')
            ad.char_change(4)

    if odin1 == 24:
        ad.active_mecro_1()
        week_end = ad.week_dg_entrance(2)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('25')
            ad.char_change(5)
    
    if odin1 == 25:
        ad.active_mecro_1()
        week_end = ad.week_dg_entrance(2)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('26')
            ad.char_change(1)

# 오딘2 지하감옥 스케줄
def play_week_dg_odin2():
    # 1번 캐릭터
    if odin2 == 21:
        ad.active_mecro_2()
        week_end = ad.week_dg_entrance(6)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('27')
            # ad.char_change(2) # 1번만 플레이

    if odin2 == 22:
        ad.active_mecro_2()
        week_end = ad.week_dg_entrance(2)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('23')
            ad.char_change(3)

    if odin2 == 23:
        ad.active_mecro_2()
        week_end = ad.week_dg_entrance(2)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('24')
            ad.char_change(4)

    if odin2 == 24:
        ad.active_mecro_2()
        week_end = ad.week_dg_entrance(2)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('25')
            ad.char_change(5)

    if odin2 == 25:
        ad.active_mecro_2()
        week_end = ad.week_dg_entrance(2)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('26')
            ad.char_change(1)

# 필드 사냥(즐겨찾기 1번) - 사용안함(퀘스트 밀기로 함)
def field_play_odin1(): 
    if odin1 == 27:
        ad.active_mecro_1()
        fp = ad.field_play()
def field_play_odin2():         
    if odin2 == 27:
        ad.active_mecro_2()
        fp = ad.field_play()

# 메인 퀘스트
def main_quest_start_odin1():
    if odin1 == 26:
        ad.active_mecro_1()
        ad.main_quest()
def main_quest_start_odin2():        
    if odin2 == 26:
        ad.active_mecro_2()
        ad.main_quest()

############################### 오딘 플레이 ###############################
# 매크로 시작 오딘 창 불러오기
ad.get_mecro()

#최초 실행시 어디까지 진행했는지 읽어옴
odin1 = int(odin1_read())
odin2 = int(odin2_read())

while True:
    # try:
    # 스테이지 불러오기
    odin1 = int(odin1_read())
    odin2 = int(odin2_read())

    ad.active_mecro_1()
    loding_page = ad.loding_page()
    if loding_page == 1:
        pass
    else:
        # 오딘 1 - 물약 및 부활 체크
        ad.no_potion()
        ad.resurrection()
        ad.ck_popup()

        play_odin1()
        play_week_dg_odin1()
        main_quest_start_odin1()
        field_play_odin1()

    ad.active_mecro_2()
    loding_page = ad.loding_page()
    if loding_page == 1:
        pass
    else:
        # 오딘 2 - 물약 및 부활 체크
        ad.no_potion()
        ad.resurrection()
        ad.ck_popup()

        play_odin2()
        play_week_dg_odin2()
        main_quest_start_odin2()
        field_play_odin2()


    # 10시 초기화
    find_hour = time.strftime('%H', time.localtime(time.time()))
    print('시간체크 :' + find_hour + '시(10시 초기화)')
    if find_hour == '10': # 코드 수정하면 10으로 변경
        if odin1 == 1 or odin1 == 2 or odin1 == 3 or odin1 == 4: # 1, 2번 이면 초기화 안함
            print('1, 2, 3, 4번 진행 시라면 초기화 하지 않음')
            pass
        else:
            odin1_write('1')
            ad.active_mecro_1()
            ad.char_change(1)
        
        if odin2 == 1 or odin2 == 2 or odin2 == 3 or odin2 == 4:
            print('1, 2, 3, 4번 진행 시라면 초기화 하지 않음')
            pass
        else:
            odin2_write('1')
            ad.active_mecro_2()
            ad.char_change(1)

    # 체크 주기
    sleep(30)
    # except:
    #     sleep(5)
    #     print('오류 발생')
    #     os.execl(sys.executable, sys.executable, *sys.argv)
