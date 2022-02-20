import random
import win32gui
import time
import api
import argparse
from configparser import ConfigParser
import ast
from datetime import datetime
from threading import Thread
import os

parser = argparse.ArgumentParser(description='Пробная версия запуска')
parser.add_argument(
    '--title',
    type=str,
    default=''
)

my_namespace = parser.parse_args()
name = my_namespace.title

#winname = 'BlueStacks'
winname = name
file = 'config.ini'
config = ConfigParser()
config.read(file)

global_adb_folder = ast.literal_eval(config['Global_settings']['adb_folder'])
global_dev = ast.literal_eval(config['Global_settings']['global_dev'])
global_folder = ast.literal_eval(config['Global_settings']['folder'])
global_play = ast.literal_eval(config['Global_settings']['play'])
global_play_res = ast.literal_eval(config['Global_settings']['play_res'])
global_star = ast.literal_eval(config['Global_settings']['star'])
global_star_res = ast.literal_eval(config['Global_settings']['star_res'])
global_sword = ast.literal_eval(config['Global_settings']['sword'])
global_sword_res = ast.literal_eval(config['Global_settings']['sword_res'])
global_combo = ast.literal_eval(config['Global_settings']['combo'])
global_combo_res = ast.literal_eval(config['Global_settings']['combo_res'])


dev = ast.literal_eval(config['Tiron']['global_dev'])
folder = ast.literal_eval(config['Tiron']['folder'])
fol_check = ast.literal_eval(config['Tiron']['folder_check'])
tiron_bank_img = ast.literal_eval(config['Tiron']['bank'])
tiron_bank_res = ast.literal_eval(config['Tiron']['bank_res'])
tiron_bank_dev = ast.literal_eval(config['Tiron']['bank_dev'])
tiron_use_storage_img = ast.literal_eval(config['Tiron']['use_storage'])
tiron_use_storage_res = ast.literal_eval(config['Tiron']['use_storage_res'])
tiron_use_storage_dev = ast.literal_eval(config['Tiron']['use_storage_dev'])
tiron_ore_mining_img = ast.literal_eval(config['Tiron']['ore_mining'])
tiron_ore_mining_res = ast.literal_eval(config['Tiron']['ore_mining_res'])
tiron_ore_mining_dev = ast.literal_eval(config['Tiron']['ore_mining_dev'])


sf1_dev = ast.literal_eval(config['sf1']['global_dev'])
sf1_folder = ast.literal_eval(config['sf1']['folder'])
sf1_fol_check = ast.literal_eval(config['sf1']['folder_check'])
sf1_bank_img = ast.literal_eval(config['sf1']['bank'])
sf1_bank_res = ast.literal_eval(config['sf1']['bank_res'])
sf1_bank_dev = ast.literal_eval(config['sf1']['bank_dev'])
sf1_destroy_img = ast.literal_eval(config['sf1']['destroy'])
sf1_destroy_res = ast.literal_eval(config['sf1']['destroy_res'])
sf1_destroy_dev = ast.literal_eval(config['sf1']['destroy_dev'])
sf1_drop_img = ast.literal_eval(config['sf1']['drop'])
sf1_drop_res = ast.literal_eval(config['sf1']['drop_res'])
sf1_drop_dev = ast.literal_eval(config['sf1']['drop_dev'])
sf1_ore_img = ast.literal_eval(config['sf1']['ore'])
sf1_ore_res = ast.literal_eval(config['sf1']['ore_res'])
sf1_ore_dev = ast.literal_eval(config['sf1']['ore_dev'])
sf1_inproc_img = ast.literal_eval(config['sf1']['inproc'])
sf1_inproc_res = ast.literal_eval(config['sf1']['inproc_res'])
sf1_inproc_dev = ast.literal_eval(config['sf1']['inproc_dev'])
sf1_invfull_img = ast.literal_eval(config['sf1']['invfull'])
sf1_invfull_res = ast.literal_eval(config['sf1']['invfull_res'])
sf1_invfull_dev = ast.literal_eval(config['sf1']['invfull_dev'])


bswinname = ast.literal_eval(config[winname]['ip'])
bstimer = ast.literal_eval(config[winname]['close_timer1'])
bstimer1 = ast.literal_eval(config[winname]['close_timer2'])
bstimer2 = ast.literal_eval(config[winname]['restart_timer1'])
bstimer3 = ast.literal_eval(config[winname]['restart_timer2'])
rserver = ast.literal_eval(config[winname]['random_server'])
typebot = ast.literal_eval(config[winname]['typebot'])


sf2_dev = ast.literal_eval(config['sf2']['global_dev'])
sf2_folder = ast.literal_eval(config['sf2']['folder'])
sf2_fol_check = ast.literal_eval(config['sf2']['folder_check'])
sf2_bank_img = ast.literal_eval(config['sf2']['bank'])
sf2_bank_res = ast.literal_eval(config['sf2']['bank_res'])
sf2_bank_dev = ast.literal_eval(config['sf2']['bank_dev'])
sf2_destroy_img = ast.literal_eval(config['sf2']['destroy'])
sf2_destroy_res = ast.literal_eval(config['sf2']['destroy_res'])
sf2_destroy_dev = ast.literal_eval(config['sf2']['destroy_dev'])
sf2_drop_img = ast.literal_eval(config['sf2']['drop'])
sf2_drop_res = ast.literal_eval(config['sf2']['drop_res'])
sf2_drop_dev = ast.literal_eval(config['sf2']['drop_dev'])
sf2_ore_img = ast.literal_eval(config['sf2']['ore'])
sf2_ore_res = ast.literal_eval(config['sf2']['ore_res'])
sf2_ore_dev = ast.literal_eval(config['sf2']['ore_dev'])
sf2_inproc_img = ast.literal_eval(config['sf2']['inproc'])
sf2_inproc_res = ast.literal_eval(config['sf2']['inproc_res'])
sf2_inproc_dev = ast.literal_eval(config['sf2']['inproc_dev'])
sf2_invfull_img = ast.literal_eval(config['sf2']['invfull'])
sf2_invfull_res = ast.literal_eval(config['sf2']['invfull_res'])
sf2_invfull_dev = ast.literal_eval(config['sf2']['invfull_dev'])
sf2_arch_icon_img = ast.literal_eval(config['sf2']['arch_icon'])
sf2_arch_icon_res = ast.literal_eval(config['sf2']['arch_icon_res'])
sf2_arch_icon_dev = ast.literal_eval(config['sf2']['arch_icon_dev'])
sf2_arch_icon_to_storage = ast.literal_eval(config['sf2']['arch_icon_to_storage'])
sf2_arch_icon_to_mining = ast.literal_eval(config['sf2']['arch_icon_to_mining'])

g_dev = ast.literal_eval(config['Gold_bar_artisans']['dev'])
g_folder = ast.literal_eval(config['Gold_bar_artisans']['folder'])
g_bank_img = ast.literal_eval(config['Gold_bar_artisans']['bank_p'])
g_bank_res = ast.literal_eval(config['Gold_bar_artisans']['bank_p_res'])
g_storage_img = ast.literal_eval(config['Gold_bar_artisans']['storage'])
g_storage_res = ast.literal_eval(config['Gold_bar_artisans']['storage_res'])
g_preset_img = ast.literal_eval(config['Gold_bar_artisans']['preset'])
g_preset_res = ast.literal_eval(config['Gold_bar_artisans']['preset_res'])
g_check_img = ast.literal_eval(config['Gold_bar_artisans']['check'])
g_check_res = ast.literal_eval(config['Gold_bar_artisans']['check_res'])
g_furnace_img = ast.literal_eval(config['Gold_bar_artisans']['furnace'])
g_furnace_res = ast.literal_eval(config['Gold_bar_artisans']['furnace_res'])
g_begin_project_img = ast.literal_eval(config['Gold_bar_artisans']['begin_project'])
g_begin_project_res = ast.literal_eval(config['Gold_bar_artisans']['begin_project_res'])
g_gold_bar_img = ast.literal_eval(config['Gold_bar_artisans']['gold_bar'])
g_gold_bar_res = ast.literal_eval(config['Gold_bar_artisans']['gold_bar_res'])


bar_type = ast.literal_eval(config['all_bar']['bar_type'])
hwnd = win32gui.FindWindow(None, winname)

camera = 0
player_pos = 0
in_game = 0
info = 0
stop = False
timer = 0


os.system(global_adb_folder + " connect " + str(bswinname))

bronze_bar = [(440, 176), 'bronze_bar.png']
iron_bar = [(524, 176), 'iron_bar.png']
steel_bar = [(610, 176), 'steel_bar.png']
mithril_bar = [(695, 176), 'mithril_bar.png']

adamant_bar = [(440, 260), 'adamant_bar.png']
rune_bar = [(524, 260), 'rune_bar.png']
orikalkum_bar = [(610, 260), 'orikalkum_bar.png']
necronium_bar = [(695, 260), 'necronium_bar.png']

bane_bar = [(440, 344), 'bane_bar.png']
elder_bar = [(524, 344), 'elder_rune_bar.png']

# 0 - Bronze bar , 1 - Iron bar, 2 - Steel bar , 3 - Mithril bar
# 4 - Adamant bar , 5 - Rune bar , 6 - Orikalkum bar , 7 - Nekronium bar
# 8 - Bane bar , 9 - Elder Rune bar
bar_list = [bronze_bar, iron_bar, steel_bar,
            mithril_bar, adamant_bar, rune_bar,
            orikalkum_bar, necronium_bar, bane_bar,
            elder_bar]

# bar_list[0] - вывод списка [(440, 176), 'bronze_bar.png']

def real_time():
    dateTimeObj = datetime.now()
    timeStr = dateTimeObj.strftime("%H:%M:%S")
    t = '[' + winname + ']' + ' ' + timeStr + ' '
    return t


def timer_check():
    global timer_restart, need_close, info, stop
    i = 0
    while not stop:
        time.sleep(1)
        i = i + 1
        info = i
    else:
        info = 0
        timer_off()


def timer_off():
    global timer
    timer = random.randint(bstimer, bstimer1)


def play_login(x1=0, y1=0):
    b = api.imgsearch(global_folder, global_play, global_play_res, winname, dev).img_search(global_dev)
    if b[0] != -1:
        x, y = b[0]
        r = random.randint(1, 25)
        # api.core(x+x1+r, y+y1+r, winname).click(0.4)  # Arrow up (my_x, my_y, my_time, my_random, my_winname)
        api.core(x + x1 + r, y + y1 + r, winname).adb_tap(bswinname, 0, 0, 0, 'tap')
        time.sleep(10)
    else:
        print(real_time() + 'Not found img')


def play_now(x1=50, y1=0):
    global in_game, camera, player_pos
    b = api.imgsearch(global_folder, global_star, global_star_res, winname, dev).img_search(global_dev)
    if b[0] != -1:
        print(real_time() + 'Вхожу на избранный сервер')
        in_game = 0
        x, y = b[0]
        rx = random.randint(1, 10)
        # +50 (первый) +126(второй) +210(третий)
        rs = 50
        if rserver == 1:
            rs = random.sample((50, 126, 210), 1)
            rs = rs[0]
        #api.core(x+x1+r, y+y1, winname).click(0.4)  # Arrow up (my_x, my_y, my_time, my_random, my_winname)
        api.core(x + rs + rx, y + y1, winname).adb_tap(bswinname, 0, 0, 0, 'tap')
        i = 0
        while i <= 20:
            time.sleep(1)
            b = api.imgsearch(global_folder, global_sword, global_sword_res, winname, dev).img_search(global_dev)
            i += 1
            if b[0] != -1:
                print(real_time() + 'Мы в игре ...')
                camera = 0
                player_pos = 0
                time.sleep(5)
                break
    else:
        print(real_time() + 'Not found img')


def game_check():
    global in_game, camera, player_pos
    b = api.imgsearch(global_folder, global_sword, global_sword_res, winname, dev).img_search(global_dev)
    time.sleep(.5)
    if b[0] != -1:
        in_game = 2
    else:
        print(real_time() + 'Включаю вторую проверку')
        in_game = 0
        b = api.imgsearch(global_folder, global_combo, global_combo_res, winname, dev).img_search(global_dev)
        img = b[1]
        time.sleep(.5)
        if img == 'star.png':
            print(real_time() + 'Мы в Lobby')
            play_now()
        time.sleep(.5)
        if img == 'play.png':
            print(real_time() + 'Мы На странице Авторизации')
            play_login()
        if img == 'b_exit.png':
            print(real_time() + 'Не закрыл окно!')
            ax, ay = b[0]
            rx = random.randint(-5, 5)
            ry = random.randint(-5, 5)
            api.core(ax + rx, ay + ry, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
            i = 0
            while i <= 20:
                time.sleep(1)
                b = api.imgsearch(global_folder, global_sword, global_sword_res, winname, dev).img_search(global_dev)
                i += 1
                if b[0] != -1:
                    print(real_time() + 'Мы в игре ...')
                    camera = 0
                    player_pos = 0
                    time.sleep(5)
                    break


def gold_bar():  # Preset 1, artisans workshop
    if in_proc():
        b = api.imgsearch(g_folder, g_bank_img, g_bank_res, winname, 0).img_search(g_dev)
        if b[0] != -1:
            print(real_time() + 'Нашел точку сундука!!!')
            x, y = b[0]
            ry = random.randint(-2, 2)
            api.core(x + -16, y + ry, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
            time.sleep(8)
            b = api.imgsearch(g_folder, g_storage_img, g_storage_res, winname, 0).img_search(g_dev)
            if b[0] != -1:
                print(real_time() + 'Нашел сундук, кликаю!!!')
                x, y = b[0]
                ry = random.randint(-7, 7)
                api.core(x + ry, y + ry, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
                i = 0
                while i <= 5:
                    time.sleep(1)
                    b = api.imgsearch(g_folder, g_preset_img, g_preset_res, winname, 0).img_search(g_dev)
                    i += 1
                    if b[0] != -1:
                        print(real_time() + 'Нашел Preset_1, Жму ...')
                        x, y = b[0]
                        r = random.randint(-15, 15)
                        api.core(x + r, y + r, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
                        time.sleep(1)
                        i = 0
                        while i <= 5:
                            time.sleep(1)
                            b = api.imgsearch(g_folder, g_check_img, g_check_res, winname, 0).img_search(g_dev)
                            i += 1
                            if b[0] != -1:
                                print(real_time() + 'Вижу sword.png')
                                b = api.imgsearch(g_folder, g_furnace_img, g_furnace_res, winname, 0).img_search(g_dev)
                                i += 1
                                if b[0] != -1:
                                    print(real_time() + 'Нашел Станок, Жму ...')
                                    x, y = b[0]
                                    r = random.randint(-5, 12)
                                    api.core(x + r, y + r, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
                                    i = 0
                                    while i <= 10:
                                        time.sleep(1)
                                        b = api.imgsearch(g_folder, g_begin_project_img, g_begin_project_res, winname, 0).img_search(g_dev)
                                        i += 1
                                        if b[0] != -1:
                                            print(real_time() + 'Вижу begin_project.png')
                                            time.sleep(.5)
                                            c = api.imgsearch(g_folder, g_gold_bar_img, g_gold_bar_res, winname, 0).img_search(g_dev)
                                            if c[0] != -1:
                                                print(real_time() + 'Gold bar - Selected')
                                                b = api.imgsearch(g_folder, g_begin_project_img, g_begin_project_res,
                                                                  winname, 0).img_search(g_dev)
                                                x, y = b[0]
                                                rx1 = random.randint(-40, 40)
                                                ry1 = random.randint(-5, 5)
                                                api.core(x + rx1, y + ry1, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
                                                time.sleep(5)
                                                break
                                            else:
                                                print(real_time() + 'Need select Gold bar 612 594')
                                                rb = random.randint(-10, 10)
                                                api.core(612 + rb, 594 + rb, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
                                                time.sleep(2)
                                                b = api.imgsearch(g_folder, g_begin_project_img, g_begin_project_res,
                                                                  winname, 0).img_search(g_dev)
                                                x, y = b[0]
                                                rx2 = random.randint(-40, 40)
                                                ry2 = random.randint(-5, 5)
                                                api.core(x + rx2, y + ry2, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
                                                time.sleep(5)
                                                break


def in_proc():
    cancel = ['in_proc.png']
    b = api.imgsearch(g_folder, cancel, 0.9, winname, 0).img_search(g_dev)
    if b[0] != -1:
        return False
    else:
        return True


def smithing_bar_u():
    if in_proc():
        folder = './img_smithing/'
        craft_img = ['low_smithing_store.png']
        b = api.imgsearch(folder, craft_img, 0.93, winname, 0).img_search(1)
        if b[0] != -1:
            print(real_time() + 'Нашел станок, открываю!!!')
            x, y = b[0]
            rx = random.randint(-50, 50)
            ry = random.randint(-10, 10)
            api.core(x + rx, y + ry, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
            i = 0
            while i <= 6:
                time.sleep(1)
                point1_pic = ['low_smithing_depoall.png']
                b = api.imgsearch(folder, point1_pic, 0.94, winname, 0).img_search(dev)
                i += 1
                if b[0] != -1:
                    print(real_time() + 'Нашел Deposit All btn, Жму ...')
                    x, y = b[0]
                    rx = random.randint(-40, 40)
                    ry = random.randint(-10, 10)
                    api.core(x + rx, y + ry, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
                    time.sleep(1)
                    a = bar_list[bar_type]
                    bar = [a[1]]
                    bar_x, bar_y = a[0]
                    c = api.imgsearch(folder, bar, 0.93, winname, 0).img_search(1)
                    if c[0] != -1:
                        begin_img = ['begin_project.png']
                        a = api.imgsearch(folder, begin_img, 0.93, winname, 0).img_search(1)
                        if a[0] != -1:
                            ax, ay = a[0]
                            rx = random.randint(-40, 40)
                            ry = random.randint(-10, 10)
                            api.core(ax + rx, ay + ry, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
                            time.sleep(3)
                            break
                    else:
                        brx = random.randint(-15, 15)
                        bry = random.randint(-10, 10)
                        api.core(bar_x + brx, bar_y + bry, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
                        time.sleep(2)
                        begin_img = ['begin_project.png']
                        a = api.imgsearch(folder, begin_img, 0.93, winname, 0).img_search(1)
                        if a[0] != -1:
                            ax, ay = a[0]
                            rx = random.randint(-40, 40)
                            ry = random.randint(-10, 10)
                            api.core(ax + rx, ay + ry, winname).adb_tap(bswinname, 0, 0, 0, 'tap_swipe')
                            time.sleep(3)
                            break


def magic_universal():
    print('Magic skills')



def main():
    global player_pos, camera, stop
    print('Добро пожаловать // Скрипт 3.0')
    print('( Мульти крафтер )')
    ran = random.randint(bstimer2, bstimer3)
    print('Время сна после выключения примерно: ', ran, ' сек')
    time.sleep(1)
    q = 0
    thread_timer = Thread(target=timer_check)
    thread_timer.start()
    timer_off()
    typebot = 1
    while True:
        try:
            time.sleep(.5)
            q += 1
            if q >= 5:
                game_check()
                q = 0
            if info >= timer:
                ran = random.randint(bstimer2, bstimer3)
                stop = True
                print('Надо закрыть бота')
                thread_timer.join()
                timer_off()
                time.sleep(2)
                api.core(0, 0, winname).kill_app(bswinname)
                time.sleep(ran)
                api.core(0, 0, winname).run_app(bswinname)
                stop = False
                thread_timer = Thread(target=timer_check)
                thread_timer.start()
            if in_game == 2:
                time.sleep(.5)
                if camera == 0 and player_pos == 0:
                    time.sleep(5)
                    rs = random.randint(300, 500)
                    rx = random.randint(300, 600)
                    ry = random.randint(100, 200)
                    rtime = random.randint(3, 5)
                    api.core(rx, ry, winname).adb_tap(bswinname, 0, rs, rtime, 'swipe')
                    time.sleep(3)
                    camera = 1
                elif camera == 1 and player_pos == 0:
                    if typebot == 1:
                        gold_bar()
                    elif typebot == 2:
                        smithing_bar_u()
        except Exception:
            print(real_time() + 'Исключение сработало, цыкл нарушен')
            continue

if __name__ == '__main__':
    main()