import time
start_time = time.perf_counter_ns()

import pygame
import math
import pathlib
from pathlib import Path
from random import randint
import datetime

now = datetime.datetime.now()
print()
print((str(now))[0:19])

directiry = pathlib.Path.cwd()
print()
print(directiry)
dir_path = str(directiry)

print()
print("Траектория 0.5.2")
print()
start_time = time.perf_counter_ns()

Window = pygame.display.set_mode((1440, 810))
pygame.display.set_caption("Траектория")

FPS = 60

pygame.mouse.set_visible(True)
clock = pygame.time.Clock()

icon = pygame.image.load(dir_path+"/data/texture/icon.ico").convert()
icon.set_colorkey((0,0,0))
pygame.display.set_icon(icon)

IDL = [0]*100
for i in range(81):
    IDL[i] = pygame.image.load(dir_path+'/data/texture/ID_print/ID'+str(i+1)+'.png').convert()
    IDL[i].set_colorkey((0,0,0))

MT = [0]*100
for i in range(81): MT[i] = pygame.image.load(dir_path+'/data/texture/monitor_print/MT'+str(i+1)+'.png').convert()

start_button = [0]*12
for i in range (12):
    start_button[i] = pygame.image.load(dir_path+'/data/texture/start_button_flame'+str(i+1)+'.png').convert()
    start_button[i].set_colorkey((255,255,255))

print_button = [0]*4
for i in range (4):
    print_button[i] = pygame.image.load(dir_path+'/data/texture/print_button_flame'+str(i+1)+'.png').convert()
    print_button[i].set_colorkey((255,255,255))

repeat_button = [0]*18
for i in range (18):
    repeat_button[i] = pygame.image.load(dir_path+'/data/texture/repeat_button_flame'+str(i+1)+'.png').convert()
    repeat_button[i].set_colorkey((255,255,255))

infoprint = [0]*16
for i in range (16):
    infoprint[i] = pygame.image.load(dir_path+'/data/texture/infoprint.png').convert()
    infoprint[i].set_colorkey((255,255,255))

background_8x = [0]*3
background_4x = [0]*3
background_2x = [0]*3
background_1x = [0]*3
sky_background = [0]*3
sky_background1 = [0]*3
sky_background2 = [0]*3
sky_background3 = [0]*3
background_8x[0] = pygame.image.load(dir_path+'/data/texture/background_8x1.png').convert()
background_8x[1] = pygame.image.load(dir_path+'/data/texture/background_8x2.png').convert()
background_8x[2] = pygame.image.load(dir_path+'/data/texture/background_8x3.png').convert()
background_4x[0] = pygame.image.load(dir_path+'/data/texture/background_4x1.png').convert()
background_4x[1] = pygame.image.load(dir_path+'/data/texture/background_4x2.png').convert()
background_4x[2] = pygame.image.load(dir_path+'/data/texture/background_4x3.png').convert()
background_2x[0] = pygame.image.load(dir_path+'/data/texture/background_2x1.png').convert()
background_2x[1] = pygame.image.load(dir_path+'/data/texture/background_2x2.png').convert()
background_2x[2] = pygame.image.load(dir_path+'/data/texture/background_2x3.png').convert()
background_1x[0] = pygame.image.load(dir_path+'/data/texture/background_1x1.png').convert()
background_1x[1] = pygame.image.load(dir_path+'/data/texture/background_1x2.png').convert()
background_1x[2] = pygame.image.load(dir_path+'/data/texture/background_1x3.png').convert()
sky_background[0] = pygame.image.load(dir_path+'/data/texture/sky_background1.png').convert()
sky_background[1] = pygame.image.load(dir_path+'/data/texture/sky_background2.png').convert()
sky_background[2] = pygame.image.load(dir_path+'/data/texture/sky_background3.png').convert()
sky_background1[0] = pygame.image.load(dir_path+'/data/texture/sky_background1_1.png').convert()
sky_background1[1] = pygame.image.load(dir_path+'/data/texture/sky_background1_2.png').convert()
sky_background1[2] = pygame.image.load(dir_path+'/data/texture/sky_background1_3.png').convert()
sky_background2[0] = pygame.image.load(dir_path+'/data/texture/sky_background2_1.png').convert()
sky_background2[1] = pygame.image.load(dir_path+'/data/texture/sky_background2_2.png').convert()
sky_background2[2] = pygame.image.load(dir_path+'/data/texture/sky_background2_3.png').convert()
sky_background3[0] = pygame.image.load(dir_path+'/data/texture/sky_background3_1.png').convert()
sky_background3[1] = pygame.image.load(dir_path+'/data/texture/sky_background3_2.png').convert()
sky_background3[2] = pygame.image.load(dir_path+'/data/texture/sky_background3_3.png').convert()
found_line = pygame.image.load(dir_path+'/data/texture/found_line.png').convert()
base = pygame.image.load(dir_path+'/data/texture/base.png').convert()
tower = pygame.image.load(dir_path+'/data/texture/tower.png').convert()
dot_small = pygame.image.load(dir_path+'/data/texture/dot_small.png').convert()
dot_big = pygame.image.load(dir_path+'/data/texture/dot_big.png').convert()
dot_medium = pygame.image.load(dir_path+'/data/texture/dot_medium.png').convert()
button_group_first = pygame.image.load(dir_path+'/data/texture/button_group_first.png').convert()
button_group_second = pygame.image.load(dir_path+'/data/texture/button_group_second.png').convert()
button_group_third = pygame.image.load(dir_path+'/data/texture/button_group_third.png').convert()
vent = pygame.image.load(dir_path+'/data/texture/vent.png').convert()
forse_arrow = pygame.image.load(dir_path+'/data/texture/forse_arrow.png').convert()
infotable_up = pygame.image.load(dir_path+'/data/texture/Infotable_up.png').convert()
infotable_down = pygame.image.load(dir_path+'/data/texture/Infotable_down.png').convert()
infotable_highpoint = pygame.image.load(dir_path+'/data/texture/Infotable_highpoint.png').convert()
numpad_base = pygame.image.load(dir_path+'/data/texture/numpad_base.png').convert()
numpad_speed = pygame.image.load(dir_path+'/data/texture/numpad_speed.png').convert()
numpad_mass = pygame.image.load(dir_path+'/data/texture/numpad_mass.png').convert()
numpad_angle = pygame.image.load(dir_path+'/data/texture/numpad_angle.png').convert()
numpad_wind = pygame.image.load(dir_path+'/data/texture/numpad_wind.png').convert()
printmachine_part1 = pygame.image.load(dir_path+'/data/texture/printmachine_part1.png').convert()
printmachine_part2 = pygame.image.load(dir_path+'/data/texture/printmachine_part2.png').convert()
printmachine_close = pygame.image.load(dir_path+'/data/texture/printmachine_close.png').convert()
zero = pygame.image.load(dir_path+'/data/texture/0.png').convert()
one = pygame.image.load(dir_path+'/data/texture/1.png').convert()
two = pygame.image.load(dir_path+'/data/texture/2.png').convert()
three = pygame.image.load(dir_path+'/data/texture/3.png').convert()
four = pygame.image.load(dir_path+'/data/texture/4.png').convert()
five = pygame.image.load(dir_path+'/data/texture/5.png').convert()
six = pygame.image.load(dir_path+'/data/texture/6.png').convert()
seven = pygame.image.load(dir_path+'/data/texture/7.png').convert()
eight = pygame.image.load(dir_path+'/data/texture/8.png').convert()
nine = pygame.image.load(dir_path+'/data/texture/9.png').convert()
base_insidewall = pygame.image.load(dir_path+'/data/texture/base_insidewall.png').convert()
showside_base = pygame.image.load(dir_path+'/data/texture/showside_base.png').convert()
showside_push_base = pygame.image.load(dir_path+'/data/texture/showside_push_base.png').convert()
showside_push_base_tuggerbase1 = pygame.image.load(dir_path+'/data/texture/showside_push_base_tuggerbase1.png').convert()
showside_push_base_tuggerbase2 = pygame.image.load(dir_path+'/data/texture/showside_push_base_tuggerbase2.png').convert()
showside_push_tugger = pygame.image.load(dir_path+'/data/texture/showside_push_tugger.png').convert()
showside_push_tuggerfill = pygame.image.load(dir_path+'/data/texture/showside_push_tuggerfill.png').convert()
max_height_info = pygame.image.load(dir_path+'/data/texture/max_height_info.png').convert()
show_fps_base = pygame.image.load(dir_path+'/data/texture/show_fps_base.png').convert()
showside_speed = pygame.image.load(dir_path+'/data/texture/showside_speed.png').convert()

sprmasch_base = pygame.image.load(dir_path+'/data/texture/sprmasch_base.png').convert()
sprmasch_arrow = pygame.image.load(dir_path+'/data/texture/sprmasch_arrow.png').convert()
sprmasch_watch = pygame.image.load(dir_path+'/data/texture/sprmasch_watch.png').convert()
sprmasch_arrow.set_colorkey((0,0,0))
sprmasch_watch.set_colorkey((0,0,0))

ticker = [0]*5
ticker[0] = pygame.image.load(dir_path+'/data/texture/ticker_flame1.png').convert()
ticker[1] = pygame.image.load(dir_path+'/data/texture/ticker_flame2.png').convert()
ticker[2] = pygame.image.load(dir_path+'/data/texture/ticker_flame3.png').convert()
ticker[3] = pygame.image.load(dir_path+'/data/texture/ticker_flame4.png').convert()
ticker[4] = pygame.image.load(dir_path+'/data/texture/ticker_flame5.png').convert()
for i in range(5): ticker[i].set_colorkey((0,0,0))

printmachine_lamp_base = pygame.image.load(dir_path+'/data/texture/printmachine_lamp_base.png').convert()
printmachine_lamp_red1 = pygame.image.load(dir_path+'/data/texture/printmachine_lamp_red1.png').convert()
printmachine_lamp_red2 = pygame.image.load(dir_path+'/data/texture/printmachine_lamp_red2.png').convert()
printmachine_lamp_green1 = pygame.image.load(dir_path+'/data/texture/printmachine_lamp_green1.png').convert()
printmachine_lamp_green2 = pygame.image.load(dir_path+'/data/texture/printmachine_lamp_green2.png').convert()
printmachine_lamp_red1.set_colorkey((0,0,0))
printmachine_lamp_red2.set_colorkey((0,0,0))
printmachine_lamp_green1.set_colorkey((0,0,0))
printmachine_lamp_green2.set_colorkey((0,0,0))

ball1 = pygame.image.load(dir_path+'/data/texture/ball1.png').convert()
ball2 = pygame.image.load(dir_path+'/data/texture/ball2.png').convert()
ball3 = pygame.image.load(dir_path+'/data/texture/ball3.png').convert()
ball4 = pygame.image.load(dir_path+'/data/texture/ball4.png').convert()
ball5 = pygame.image.load(dir_path+'/data/texture/ball5.png').convert()
ball6 = pygame.image.load(dir_path+'/data/texture/ball6.png').convert()
ball7 = pygame.image.load(dir_path+'/data/texture/ball7.png').convert()
ball8 = pygame.image.load(dir_path+'/data/texture/ball8.png').convert()
ball9 = pygame.image.load(dir_path+'/data/texture/ball9.png').convert()
ball10 = pygame.image.load(dir_path+'/data/texture/ball10.png').convert()
ball11 = pygame.image.load(dir_path+'/data/texture/ball11.png').convert()
ball1.set_colorkey((0,0,0))
ball2.set_colorkey((0,0,0))
ball3.set_colorkey((0,0,0))
ball4.set_colorkey((0,0,0))
ball5.set_colorkey((0,0,0))
ball6.set_colorkey((0,0,0))
ball7.set_colorkey((0,0,0))
ball8.set_colorkey((0,0,0))
ball9.set_colorkey((0,0,0))
ball10.set_colorkey((0,0,0))
ball11.set_colorkey((0,0,0))

book_drop = [0]*8

book_drop[0] = pygame.image.load(dir_path+'/data/texture/book_drop1.png').convert()
book_drop[1] = pygame.image.load(dir_path+'/data/texture/book_drop2.png').convert()
book_drop[2] = pygame.image.load(dir_path+'/data/texture/book_drop3.png').convert()
book_drop[3] = pygame.image.load(dir_path+'/data/texture/book_drop4.png').convert()
book_drop[4] = pygame.image.load(dir_path+'/data/texture/book_drop5.png').convert()
book_drop[5] = pygame.image.load(dir_path+'/data/texture/book_drop6.png').convert()
book_drop[6] = pygame.image.load(dir_path+'/data/texture/book_drop7.png').convert()
book_drop[7] = pygame.image.load(dir_path+'/data/texture/book_drop8.png').convert()
for i in range (8): book_drop[i].set_colorkey((255,0,0))

monitor_base = pygame.image.load(dir_path+'/data/texture/monitor_base.png').convert()
podmonitor = pygame.image.load(dir_path+'/data/texture/podmonitor.png').convert()
monitor_on_button = pygame.image.load(dir_path+'/data/texture/monitor_on_button.png').convert()
monitor_loading1 = pygame.image.load(dir_path+'/data/texture/monitor_loading1.png').convert()
monitor_loading2 = pygame.image.load(dir_path+'/data/texture/monitor_loading2.png').convert()
monitor_loading3 = pygame.image.load(dir_path+'/data/texture/monitor_loading3.png').convert()
monitor_loading4 = pygame.image.load(dir_path+'/data/texture/monitor_loading4.png').convert()
monitor_loading5 = pygame.image.load(dir_path+'/data/texture/monitor_loading5.png').convert()
monitor_loading6 = pygame.image.load(dir_path+'/data/texture/monitor_loading6.png').convert()
monitor_loading7 = pygame.image.load(dir_path+'/data/texture/monitor_loading7.png').convert()
monitor_loading8 = pygame.image.load(dir_path+'/data/texture/monitor_loading8.png').convert()
monitor_loading_post = pygame.image.load(dir_path+'/data/texture/monitor_loading_post.png').convert()
monitor_mainmenu = pygame.image.load(dir_path+'/data/texture/monitor_mainmenu.png').convert()
monitor_text1 = pygame.image.load(dir_path+'/data/texture/monitor_text1.png').convert()
monitor_text2 = pygame.image.load(dir_path+'/data/texture/monitor_text2.png').convert()
monitor_text3 = pygame.image.load(dir_path+'/data/texture/monitor_text3.png').convert()
monitor_text4 = pygame.image.load(dir_path+'/data/texture/monitor_text4.png').convert()
monitor_text5 = pygame.image.load(dir_path+'/data/texture/monitor_text5.png').convert()
monitor_text6 = pygame.image.load(dir_path+'/data/texture/monitor_text6.png').convert()
monitor_text7 = pygame.image.load(dir_path+'/data/texture/monitor_text7.png').convert()
monitor_textset = pygame.image.load(dir_path+'/data/texture/monitor_textset.png').convert()
monitor_effect1 = pygame.image.load(dir_path+'/data/texture/monitor_effect1.png').convert()
monitor_effect2 = pygame.image.load(dir_path+'/data/texture/monitor_effect2.png').convert()

monitor_text1.set_colorkey((0, 0, 0))
monitor_text2.set_colorkey((0, 0, 0))
monitor_text3.set_colorkey((0, 0, 0))
monitor_text4.set_colorkey((0, 0, 0))
monitor_text5.set_colorkey((0, 0, 0))
monitor_text6.set_colorkey((0, 0, 0))
monitor_text7.set_colorkey((0, 0, 0))
monitor_textset.set_colorkey((230, 232, 242))

monitor_effect1.set_alpha(13)
monitor_effect2.set_alpha(13)

rotor_ticker = [0]*3
rotor_ticker[0] = pygame.image.load(dir_path+'/data/texture/rotor_ticker1.png').convert()
rotor_ticker[1] = pygame.image.load(dir_path+'/data/texture/rotor_ticker2.png').convert()
rotor_ticker[2] = pygame.image.load(dir_path+'/data/texture/rotor_ticker3.png').convert()
rotor_ticker[0].set_colorkey((0, 0, 0))
rotor_ticker[1].set_colorkey((0, 0, 0))
rotor_ticker[2].set_colorkey((0, 0, 0))

tr_slot1 = pygame.image.load(dir_path+'/data/texture/tr_slot1.png').convert()
tr_slot2 = pygame.image.load(dir_path+'/data/texture/tr_slot2.png').convert()
tr_slot3 = pygame.image.load(dir_path+'/data/texture/tr_slot3.png').convert()
tr_slot4 = pygame.image.load(dir_path+'/data/texture/tr_slot4.png').convert()
tr_slot5 = pygame.image.load(dir_path+'/data/texture/tr_slot5.png').convert()
tr_slot6 = pygame.image.load(dir_path+'/data/texture/tr_slot6.png').convert()
tr_slot7 = pygame.image.load(dir_path+'/data/texture/tr_slot7.png').convert()
tr_slot8 = pygame.image.load(dir_path+'/data/texture/tr_slot8.png').convert()

tr_color = [0]*8

tr_color[2] = pygame.image.load(dir_path+'/data/texture/tr_color_blue.png').convert()
tr_color[1] = pygame.image.load(dir_path+'/data/texture/tr_color_green.png').convert()
tr_color[5] = pygame.image.load(dir_path+'/data/texture/tr_color_lblue.png').convert()
tr_color[4] = pygame.image.load(dir_path+'/data/texture/tr_color_orange.png').convert()
tr_color[0] = pygame.image.load(dir_path+'/data/texture/tr_color_red.png').convert()
tr_color[6] = pygame.image.load(dir_path+'/data/texture/tr_color_violet.png').convert()
tr_color[7] = pygame.image.load(dir_path+'/data/texture/tr_color_white.png').convert()
tr_color[3] = pygame.image.load(dir_path+'/data/texture/tr_color_yellow.png').convert()

tr_delete = pygame.image.load(dir_path+'/data/texture/tr_delete.png').convert()
tr_save = pygame.image.load(dir_path+'/data/texture/tr_save.png').convert()
tr_unviev = pygame.image.load(dir_path+'/data/texture/tr_unviev.png').convert()
tr_viev = pygame.image.load(dir_path+'/data/texture/tr_viev.png').convert()

monitor_num = [0]*10
monitor_num[0]  = pygame.image.load(dir_path+'/data/texture/monitor_num1.png').convert()
monitor_num[1]  = pygame.image.load(dir_path+'/data/texture/monitor_num2.png').convert()
monitor_num[2]  = pygame.image.load(dir_path+'/data/texture/monitor_num3.png').convert()
monitor_num[3]  = pygame.image.load(dir_path+'/data/texture/monitor_num4.png').convert()
monitor_num[4]  = pygame.image.load(dir_path+'/data/texture/monitor_num5.png').convert()
monitor_num[5]  = pygame.image.load(dir_path+'/data/texture/monitor_num6.png').convert()
monitor_num[6]  = pygame.image.load(dir_path+'/data/texture/monitor_num7.png').convert()
monitor_num[7]  = pygame.image.load(dir_path+'/data/texture/monitor_num8.png').convert()
monitor_num[8]  = pygame.image.load(dir_path+'/data/texture/monitor_num9.png').convert()
monitor_num[9]  = pygame.image.load(dir_path+'/data/texture/monitor_num10.png').convert()

base.set_colorkey((255,255,255))

showside_push_diod1 = pygame.image.load(dir_path+'/data/texture/showside_push_diod1.png').convert()
showside_push_diod2 = pygame.image.load(dir_path+'/data/texture/showside_push_diod2.png').convert()
showside_push_diod3 = pygame.image.load(dir_path+'/data/texture/showside_push_diod3.png').convert()
showside_push_diod4 = pygame.image.load(dir_path+'/data/texture/showside_push_diod4.png').convert()
showside_push_diod5 = pygame.image.load(dir_path+'/data/texture/showside_push_diod5.png').convert()
showside_push_diod6 = pygame.image.load(dir_path+'/data/texture/showside_push_diod6.png').convert()
showside_push_diod7 = pygame.image.load(dir_path+'/data/texture/showside_push_diod7.png').convert()

showside_push_tugger.set_colorkey((255,255,255))
showside_push_tuggerfill.set_colorkey((255,255,255))
showside_push_lamp1 = pygame.image.load(dir_path+'/data/texture/showside_push_lamp1.png').convert()
showside_push_lamp2 = pygame.image.load(dir_path+'/data/texture/showside_push_lamp2.png').convert()

instr1  = pygame.image.load(dir_path+'/data/texture/instr1.png').convert()
instr2  = pygame.image.load(dir_path+'/data/texture/instr2.png').convert()

vent_close = pygame.image.load(dir_path+'/data/texture/vent_close.png').convert()
vent_close.set_colorkey((255,255,255))

decor1 = pygame.image.load(dir_path+'/data/texture/decor1.png').convert()
decor2 = pygame.image.load(dir_path+'/data/texture/decor2.png').convert()
decor3 = pygame.image.load(dir_path+'/data/texture/decor3.png').convert()
decor1.set_colorkey((255,255,255))

secundometr_base = pygame.image.load(dir_path+'/data/texture/secundometr_base.png').convert()
secundometr_base.set_colorkey((255,255,255))
secundometr_secarrow = pygame.image.load(dir_path+'/data/texture/secundometr_secarrow.png').convert()
secundometr_secarrow.set_colorkey((255,255,255))
secundometr_subarrow = pygame.image.load(dir_path+'/data/texture/secundometr_subarrow.png').convert()
secundometr_subarrow.set_colorkey((255,255,255))

decoran1_f1 = pygame.image.load(dir_path+'/data/texture/decoran1_f1.png').convert()
decoran1_f2 = pygame.image.load(dir_path+'/data/texture/decoran1_f2.png').convert()

rotor = pygame.image.load(dir_path+'/data/texture/rotor.png').convert()
rotor.set_colorkey((255,255,255))
rotor_close = pygame.image.load(dir_path+'/data/texture/rotor_close.png').convert()
rotor_close.set_colorkey((255,255,255))

indicator_off = pygame.image.load(dir_path+'/data/texture/indicator_off.png').convert()
indicator_on = pygame.image.load(dir_path+'/data/texture/indicator_on.png').convert()
indicator_off.set_colorkey((255,255,255))
indicator_on.set_colorkey((255,255,255))

on_pesser1 = pygame.image.load(dir_path+'/data/texture/on_pesser1.png').convert()
on_pesser2 = pygame.image.load(dir_path+'/data/texture/on_pesser2.png').convert()
on_pesser3 = pygame.image.load(dir_path+'/data/texture/on_pesser3.png').convert()
on_pesser4 = pygame.image.load(dir_path+'/data/texture/on_pesser4.png').convert()
on_pesser5 = pygame.image.load(dir_path+'/data/texture/on_pesser5.png').convert()
on_pesser1.set_colorkey((255,255,255))
on_pesser2.set_colorkey((255,255,255))
on_pesser3.set_colorkey((255,255,255))
on_pesser4.set_colorkey((255,255,255))
on_pesser5.set_colorkey((255,255,255))

decoran2_f1 = pygame.image.load(dir_path+'/data/texture/decoran2_f1.png').convert()
decoran2_f2 = pygame.image.load(dir_path+'/data/texture/decoran2_f2.png').convert()
decoran2_f3 = pygame.image.load(dir_path+'/data/texture/decoran2_f3.png').convert()
decoran2_f4 = pygame.image.load(dir_path+'/data/texture/decoran2_f4.png').convert()
decoran2_f5 = pygame.image.load(dir_path+'/data/texture/decoran2_f5.png').convert()
decoran2_f6 = pygame.image.load(dir_path+'/data/texture/decoran2_f6.png').convert()
decoran2_f7 = pygame.image.load(dir_path+'/data/texture/decoran2_f7.png').convert()
decoran2_f8 = pygame.image.load(dir_path+'/data/texture/decoran2_f8.png').convert()
decoran2_f1.set_colorkey((0,0,0))
decoran2_f2.set_colorkey((0,0,0))
decoran2_f3.set_colorkey((0,0,0))
decoran2_f4.set_colorkey((0,0,0))
decoran2_f5.set_colorkey((0,0,0))
decoran2_f6.set_colorkey((0,0,0))
decoran2_f7.set_colorkey((0,0,0))
decoran2_f8.set_colorkey((0,0,0))

Znumbers = [0]*10
Znumbers[0] = pygame.image.load(dir_path+'/data/texture/Z0.png').convert()
Znumbers[1] = pygame.image.load(dir_path+'/data/texture/Z1.png').convert()
Znumbers[2] = pygame.image.load(dir_path+'/data/texture/Z2.png').convert()
Znumbers[3] = pygame.image.load(dir_path+'/data/texture/Z3.png').convert()
Znumbers[4] = pygame.image.load(dir_path+'/data/texture/Z4.png').convert()
Znumbers[5] = pygame.image.load(dir_path+'/data/texture/Z5.png').convert()
Znumbers[6] = pygame.image.load(dir_path+'/data/texture/Z6.png').convert()
Znumbers[7] = pygame.image.load(dir_path+'/data/texture/Z7.png').convert()
Znumbers[8] = pygame.image.load(dir_path+'/data/texture/Z8.png').convert()
Znumbers[9] = pygame.image.load(dir_path+'/data/texture/Z9.png').convert()

height_info = pygame.image.load(dir_path+'/data/texture/height_info.png').convert()
height_info.set_colorkey((255,255,255))
Hnumbers = [0]*10
Hnumbers[0] = pygame.image.load(dir_path+'/data/texture/height_num_0.png').convert()
Hnumbers[1] = pygame.image.load(dir_path+'/data/texture/height_num_1.png').convert()
Hnumbers[2] = pygame.image.load(dir_path+'/data/texture/height_num_2.png').convert()
Hnumbers[3] = pygame.image.load(dir_path+'/data/texture/height_num_3.png').convert()
Hnumbers[4] = pygame.image.load(dir_path+'/data/texture/height_num_4.png').convert()
Hnumbers[5] = pygame.image.load(dir_path+'/data/texture/height_num_5.png').convert()
Hnumbers[6] = pygame.image.load(dir_path+'/data/texture/height_num_6.png').convert()
Hnumbers[7] = pygame.image.load(dir_path+'/data/texture/height_num_7.png').convert()
Hnumbers[8] = pygame.image.load(dir_path+'/data/texture/height_num_8.png').convert()
Hnumbers[9] = pygame.image.load(dir_path+'/data/texture/height_num_9.png').convert()

cif_numbers = [0]*10
cif_numbers[0] = pygame.image.load(dir_path+'/data/texture/cif_0.png').convert()
cif_numbers[1] = pygame.image.load(dir_path+'/data/texture/cif_1.png').convert()
cif_numbers[2] = pygame.image.load(dir_path+'/data/texture/cif_2.png').convert()
cif_numbers[3] = pygame.image.load(dir_path+'/data/texture/cif_3.png').convert()
cif_numbers[4] = pygame.image.load(dir_path+'/data/texture/cif_4.png').convert()
cif_numbers[5] = pygame.image.load(dir_path+'/data/texture/cif_5.png').convert()
cif_numbers[6] = pygame.image.load(dir_path+'/data/texture/cif_6.png').convert()
cif_numbers[7] = pygame.image.load(dir_path+'/data/texture/cif_7.png').convert()
cif_numbers[8] = pygame.image.load(dir_path+'/data/texture/cif_8.png').convert()
cif_numbers[9] = pygame.image.load(dir_path+'/data/texture/cif_9.png').convert()

sm_numbers = [0]*10
sm_numbers[0] = pygame.image.load(dir_path+'/data/texture/sm_0.png').convert()
sm_numbers[1] = pygame.image.load(dir_path+'/data/texture/sm_1.png').convert()
sm_numbers[2] = pygame.image.load(dir_path+'/data/texture/sm_2.png').convert()
sm_numbers[3] = pygame.image.load(dir_path+'/data/texture/sm_3.png').convert()
sm_numbers[4] = pygame.image.load(dir_path+'/data/texture/sm_4.png').convert()
sm_numbers[5] = pygame.image.load(dir_path+'/data/texture/sm_5.png').convert()
sm_numbers[6] = pygame.image.load(dir_path+'/data/texture/sm_6.png').convert()
sm_numbers[7] = pygame.image.load(dir_path+'/data/texture/sm_7.png').convert()
sm_numbers[8] = pygame.image.load(dir_path+'/data/texture/sm_8.png').convert()
sm_numbers[9] = pygame.image.load(dir_path+'/data/texture/sm_9.png').convert()

dot_kof = pygame.image.load(dir_path+'/data/texture/dot_kof.png').convert()

IPnumbers = [0]*11
IPnumbers[0] = pygame.image.load(dir_path+'/data/texture/IP0.png').convert()
IPnumbers[1] = pygame.image.load(dir_path+'/data/texture/IP1.png').convert()
IPnumbers[2] = pygame.image.load(dir_path+'/data/texture/IP2.png').convert()
IPnumbers[3] = pygame.image.load(dir_path+'/data/texture/IP3.png').convert()
IPnumbers[4] = pygame.image.load(dir_path+'/data/texture/IP4.png').convert()
IPnumbers[5] = pygame.image.load(dir_path+'/data/texture/IP5.png').convert()
IPnumbers[6] = pygame.image.load(dir_path+'/data/texture/IP6.png').convert()
IPnumbers[7] = pygame.image.load(dir_path+'/data/texture/IP7.png').convert()
IPnumbers[8] = pygame.image.load(dir_path+'/data/texture/IP8.png').convert()
IPnumbers[9] = pygame.image.load(dir_path+'/data/texture/IP9.png').convert()
IPnumbers[10] = pygame.image.load(dir_path+'/data/texture/IP_dot.png').convert()

IP_n = pygame.image.load(dir_path+'/data/texture/IP_n.png').convert()

input_space_green = pygame.image.load(dir_path+'/data/texture/input_space_green.png').convert()
g0 = pygame.image.load(dir_path+'/data/texture/mass_num0.png').convert()
g1 = pygame.image.load(dir_path+'/data/texture/mass_num1.png').convert()
g2 = pygame.image.load(dir_path+'/data/texture/mass_num2.png').convert()
g3 = pygame.image.load(dir_path+'/data/texture/mass_num3.png').convert()
g4 = pygame.image.load(dir_path+'/data/texture/mass_num4.png').convert()
g5 = pygame.image.load(dir_path+'/data/texture/mass_num5.png').convert()
g6 = pygame.image.load(dir_path+'/data/texture/mass_num6.png').convert()
g7 = pygame.image.load(dir_path+'/data/texture/mass_num7.png').convert()
g8 = pygame.image.load(dir_path+'/data/texture/mass_num8.png').convert()
g9 = pygame.image.load(dir_path+'/data/texture/mass_num9.png').convert()

p0 = pygame.image.load(dir_path+'/data/texture/zero.png').convert()
p1 = pygame.image.load(dir_path+'/data/texture/one.png').convert()
p2 = pygame.image.load(dir_path+'/data/texture/two.png').convert()
p3 = pygame.image.load(dir_path+'/data/texture/three.png').convert()
p4 = pygame.image.load(dir_path+'/data/texture/four.png').convert()
p5 = pygame.image.load(dir_path+'/data/texture/five.png').convert()
p6 = pygame.image.load(dir_path+'/data/texture/six.png').convert()
p7 = pygame.image.load(dir_path+'/data/texture/seven.png').convert()
p8 = pygame.image.load(dir_path+'/data/texture/eight.png').convert()
p9 = pygame.image.load(dir_path+'/data/texture/nine.png').convert()
input_space = pygame.image.load(dir_path+'/data/texture/input_space.png').convert()

book_page = [0]*16
book_page[0] = pygame.image.load(dir_path+'/data/texture/book1.png').convert()
book_page[1] = pygame.image.load(dir_path+'/data/texture/book2.png').convert()
book_page[2] = pygame.image.load(dir_path+'/data/texture/book3.png').convert()
book_page[3] = pygame.image.load(dir_path+'/data/texture/book4.png').convert()
book_page[4] = pygame.image.load(dir_path+'/data/texture/book5.png').convert()
book_page[5] = pygame.image.load(dir_path+'/data/texture/book6.png').convert()
book_page[6] = pygame.image.load(dir_path+'/data/texture/book7.png').convert()

count_up = pygame.image.load(dir_path+'/data/texture/count_up.png').convert()
count_up_clicked = pygame.image.load(dir_path+'/data/texture/count_up_clicked.png').convert()
count_down = pygame.image.load(dir_path+'/data/texture/count_down.png').convert()
count_down_clicked = pygame.image.load(dir_path+'/data/texture/count_down_clicked.png').convert()
M_P_S = pygame.image.load(dir_path+'/data/texture/M_P_S.png').convert()
KM_P_H = pygame.image.load(dir_path+'/data/texture/KM_P_H.png').convert()
SM_P_S = pygame.image.load(dir_path+'/data/texture/SM_P_S.png').convert()
TON = pygame.image.load(dir_path+'/data/texture/TON.png').convert()
KG = pygame.image.load(dir_path+'/data/texture/KG.png').convert()
GRAMM = pygame.image.load(dir_path+'/data/texture/GRAMM.png').convert()

abort_button_base = [0]*6
abort_button_base[0] = pygame.image.load(dir_path+'/data/texture/abort_button_base1.png').convert()
abort_button_base[1] = pygame.image.load(dir_path+'/data/texture/abort_button_base2.png').convert()
abort_button_base[2] = pygame.image.load(dir_path+'/data/texture/abort_button_base3.png').convert()
abort_button_base[3] = pygame.image.load(dir_path+'/data/texture/abort_button_base4.png').convert()
abort_button_base[4] = pygame.image.load(dir_path+'/data/texture/abort_button_base5.png').convert()
abort_button_base[5] = pygame.image.load(dir_path+'/data/texture/abort_button_base6.png').convert()

zero.set_colorkey((255,255,255))
one.set_colorkey((255,255,255))
two.set_colorkey((255,255,255))
three.set_colorkey((255,255,255))
four.set_colorkey((255,255,255))
five.set_colorkey((255,255,255))
six.set_colorkey((255,255,255))
seven.set_colorkey((255,255,255))
eight.set_colorkey((255,255,255))
nine.set_colorkey((255,255,255))
input_space.set_colorkey((255,255,255))

p0.set_colorkey((255,255,255))
p1.set_colorkey((255,255,255))
p2.set_colorkey((255,255,255))
p3.set_colorkey((255,255,255))
p4.set_colorkey((255,255,255))
p5.set_colorkey((255,255,255))
p6.set_colorkey((255,255,255))
p7.set_colorkey((255,255,255))
p8.set_colorkey((255,255,255))
p9.set_colorkey((255,255,255))

input_space_green.set_colorkey((255,255,255))

g0.set_colorkey((255,255,255))
g1.set_colorkey((255,255,255))
g2.set_colorkey((255,255,255))
g3.set_colorkey((255,255,255))
g4.set_colorkey((255,255,255))
g5.set_colorkey((255,255,255))
g6.set_colorkey((255,255,255))
g7.set_colorkey((255,255,255))
g8.set_colorkey((255,255,255))
g9.set_colorkey((255,255,255))

IPnumbers[0].set_colorkey((255,255,255))
IPnumbers[1].set_colorkey((255,255,255))
IPnumbers[2].set_colorkey((255,255,255))
IPnumbers[3].set_colorkey((255,255,255))
IPnumbers[4].set_colorkey((255,255,255))
IPnumbers[5].set_colorkey((255,255,255))
IPnumbers[6].set_colorkey((255,255,255))
IPnumbers[7].set_colorkey((255,255,255))
IPnumbers[8].set_colorkey((255,255,255))
IPnumbers[9].set_colorkey((255,255,255))
IPnumbers[10].set_colorkey((255,255,255))

first_num_p = (303,644)
second_num_p = (325,644)

infotable_up.set_colorkey((255,255,255))
infotable_down.set_colorkey((255,255,255))
infotable_highpoint.set_colorkey((255,255,255))
                            
dot_small.set_colorkey((255,255,255))
forse_arrow.set_colorkey((255,255,255))
vent.set_colorkey((255,255,255))

numbutton_1 = [0]*3
numbutton_2 = [0]*3
numbutton_3 = [0]*3
numbutton_4 = [0]*3
numbutton_5 = [0]*3
numbutton_6 = [0]*3
numbutton_7 = [0]*3
numbutton_8 = [0]*3
numbutton_9 = [0]*3
numbutton_0 = [0]*3
numbutton_b = [0]*3
numbutton_r = [0]*3

for j in range(3):
    numbutton_1[j] = pygame.image.load(dir_path+'/data/texture/numbutton_1_flame'+str(j+1)+'.png').convert()
    numbutton_2[j] = pygame.image.load(dir_path+'/data/texture/numbutton_2_flame'+str(j+1)+'.png').convert()        
    numbutton_3[j] = pygame.image.load(dir_path+'/data/texture/numbutton_3_flame'+str(j+1)+'.png').convert()
    numbutton_4[j] = pygame.image.load(dir_path+'/data/texture/numbutton_4_flame'+str(j+1)+'.png').convert()
    numbutton_5[j] = pygame.image.load(dir_path+'/data/texture/numbutton_5_flame'+str(j+1)+'.png').convert()
    numbutton_6[j] = pygame.image.load(dir_path+'/data/texture/numbutton_6_flame'+str(j+1)+'.png').convert()        
    numbutton_7[j] = pygame.image.load(dir_path+'/data/texture/numbutton_7_flame'+str(j+1)+'.png').convert()
    numbutton_8[j] = pygame.image.load(dir_path+'/data/texture/numbutton_8_flame'+str(j+1)+'.png').convert()
    numbutton_9[j] = pygame.image.load(dir_path+'/data/texture/numbutton_9_flame'+str(j+1)+'.png').convert()
    numbutton_0[j] = pygame.image.load(dir_path+'/data/texture/numbutton_0_flame'+str(j+1)+'.png').convert()        
    numbutton_b[j] = pygame.image.load(dir_path+'/data/texture/numbutton_back_flame'+str(j+1)+'.png').convert()
    numbutton_r[j] = pygame.image.load(dir_path+'/data/texture/numbutton_enter_flame'+str(j+1)+'.png').convert()
    numbutton_1[j].set_colorkey((255,255,255))
    numbutton_2[j].set_colorkey((255,255,255))
    numbutton_3[j].set_colorkey((255,255,255))
    numbutton_4[j].set_colorkey((255,255,255))
    numbutton_5[j].set_colorkey((255,255,255))
    numbutton_6[j].set_colorkey((255,255,255))
    numbutton_7[j].set_colorkey((255,255,255))
    numbutton_8[j].set_colorkey((255,255,255))
    numbutton_9[j].set_colorkey((255,255,255))
    numbutton_0[j].set_colorkey((255,255,255))
    numbutton_b[j].set_colorkey((255,255,255))
    numbutton_r[j].set_colorkey((255,255,255))
    
    
height = 350
x_pos = 0
y_pos = 0

Dot_spawn_x = [-6]*(2**18)
Dot_spawn_y = [-6]*(2**18)

pos_save_x = [-40]*(2**18)
pos_save_y = [-40]*(2**18)
lift_save = ["ND"]*(2**18)
dis_save = [0]*(2**16)

color = [(0,0,0)]*8
color[0] = (255,0,0)
color[1] = (0,255,35)
color[2] = (43,0,255)
color[3] = (225,255,0)
color[4] = (255,156,0)
color[5] = (0,216,255)
color[6] = (199,0,255)
color[7] = (234,234,234)

tr_pos_x=[]
for i in range(8):
    tr_pos_x.append([0]*(2**18))

tr_pos_y=[]
for i in range(8):
    tr_pos_y.append([0]*(2**18))

tr_count = [0]*(2**18)

speed = 5
angle = 45
G = 1

def rot_center(image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect
      
simulator_run = False
finish_sim = False
speed_ft = 90
Dot_count = 0
x_mouse = 0
y_mouse = 0
speed_word = "5"
sum_on = False
speed_enabled = False
speed_how = "meterspersecond"
count_up_bool = False
count_down_bool = False
start_button_play = False
Atick = 0
Max_pos = 0
curr_angle_vent = 0
angle_speed_vent = 5.625
repeat_button_up = False
repeat_button_rise_play = False
repeat_button_set_play = False
numbutton_bool = [False]*12
count_up_mass_bool = False
count_down_mass_bool = False
mass_how = "kg"
mass_word = "10"
mass_enabled = False
infoprint_pos_x = [971]*16
infoprint_pos_y = [629]*16
infoprint_status =["notuse"]*16
Atick_printmachine = 0
haveused = -1
infoprint_pointtaken_x = [-999]*16
infoprint_pointtaken_y = [-999]*16
infoprint_havetaken = [False]*16
infoprint_numtaken = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
timer = 0
timer2 = 0
speed_save = [0]*16
mass_save = [0]*16
speed_how_save = [0]*16
mass_how_save = [0]*16
angle_save = [0]*16
height_save = [0]*16
print_button_play = False
haveprinted = False
timer_save = [0]*16364
presser_off = True
presser_on = False
presser_play = False
kof_word = "0.5"
koff = 0.5
rotor_enabled = False
rotor_angle = -90
decor_tick = 0
decor_bool = False
anim_x_1 = 0
anim_y_1 = 0
anim_y_2 = 0
anim_y_3 = 0
sideshow_play_up = False
sideshow_play_down = False
Btick = 0
Hinfo_p = 586
Hinfo_enabled = False
Htimer = 0
sideshow_pos_y = 0
sideshow_bool = False
showsize_tugger_enabled = False
showsize_tugger_pos = 0
showsize_tugger_possize = 20
Ttimer = 0
Dtick = 0
decoran2_up = False
decoran2_down = False
decoran2_bool = False
animballangle = 0
koff = 0
Stick = 0
m16 = False
m8 = False
m4 = False
m2 = False
m1 = True
monitor_bool = False
monitor_start = False
monitor_start_load = False
MST = 0
enable_1 = False
enable_2 = False
enable_3 = False
enable_4 = False
draw_parabola = False
menu = "main"
viev_bool = [True]*8
viev_enable = [False]*8
color_tr = [0]*8
color_enable = [False]*8
save_enable = [False]*8
delete_enable = [False]*8
Ctick = 0
IP_speed = [0]*16
IP_angle = [0]*16
IP_height = [0]*16
IP_mass = [0]*16
IP_koff = [0]*16
IP_max = [0]*16
IP_dis = [0]*16
IP_time_all = [0]*16
IP_tr_x=[]
for i in range(8):IP_tr_x.append([0]*(2**16))
IP_tr_y=[]
for i in range(8):IP_tr_y.append([0]*(2**16))
IP_count = [0]*16
IP_masch = [0]*16
masch = 0
IP_time_DMV = [0]*16
IP_time_PMV = [0]*16
IP_dis_all = [0]*16
IP_dis_DMV = [0]*16
IP_dis_PMV = [0]*16
rotor_ticker_bool = False
RTA_nor = False
RTA_inv = False
Dtick = 0
koff_input = ''
koff_enable = False
Etick = 0
book_bool = False
book_pos_x = 0
book_pos_y = 0
book_take_x = 0
book_take_y = 0
book_take = False
Ftick = 0
Gtick = 0
tower_take_pos = height
tower_past_pos = height
HBA=[]
for i in range(18): HBA.append([randint(0,1)]*(4))
Htick = 0
Ktick = 0
masch_avto_bool = True
masch_avto_anim = False
masch_avto_curr = 960
masch_avto_take = False
hm2 = False
hm4 = False
hm8 = False
hm16 = False
hm32 = False
hm64 = False
hm128 = False
hm256 = False
Real_time_count = False
fps_count = 60
book_curr_page = 1
bgt = 0
gbgt = 0
abt = 0
abort_button_status = "off"
sim_speed = 1

def load_settings():
    global draw_parabola
    F_settings = open(dir_path+'/data/save/settings.txt','r')

    while True:
        S = F_settings.readline()

        if S == "end": break
        else:
            V,D,B = S.split()
            if V == "draw_parabola": draw_parabola = bool(int(B))

    F_settings.close()

    

def save_settings():
    global draw_parabola
    F_settings = open(dir_path+'/data/save/settings.txt','w')
    F_settings.write("draw_parabola = "+str(int(draw_parabola))+"\nend")
    F_settings.close()

load_settings()

light=[]
for i in range(21): light.append([-1]*(21))

light[10][10] = 10
                    
for k in range(10,0,-1):
    for x in range (21):
        for y in range (21):
            if ((light[x][y] == -1) and
                ((x+1 < 21 and light[x+1][y] == k) or
                (x-1 > 0 and light[x-1][y] == k) or
                (y+1 < 21 and light[x][y+1] == k) or
                (y-1 > 0 and light[x][y-1] == k))):
                                
                    light[x][y] = k-1
                                    
def effect_light(effect,x,y,k):
    global light
    
    NR = (effect.get_at((x,y)))[0]
    NG = (effect.get_at((x,y)))[1]
    NB = (effect.get_at((x,y)))[2]

    for kx in range (21):
        for ky in range (21):
            if (light[kx][ky] != -1)and (light[kx][ky] != 10):
                            
                OR = (effect.get_at((x-10+kx,y-10+ky)))[0]
                OG = (effect.get_at((x-10+kx,y-10+ky)))[1]
                OB = (effect.get_at((x-10+kx,y-10+ky)))[2]

                tk = (light[kx][ky]/(100/(k)))

                SR = NR * tk + OR * (1 - tk)
                SG = NG * tk + OG * (1 - tk)
                SB = NB * tk + OB * (1 - tk)
                
                effect.set_at((x-10+kx,y-10+ky),(SR,SG,SB))

    return effect

def tr_remember(X,Y,count,n):
    tr_count[n] = count
    for i in range(count):
        tr_pos_x[n][i] = X[i]
        tr_pos_y[n][i] = Y[i]

def tr_forgot(n):
    tr_count[n] = 0
    for i in range((2**16)):
        tr_pos_x[n][i] = 0
        tr_pos_y[n][i] = 0

def print_IP_number(S,x,y):
    if (S == '/'):Window.blit(IP_n, (x,y))
    else:
        if S[0] == ".": Window.blit(IPnumbers[10], (x,y))
        else: Window.blit(IPnumbers[int(S[0])], (x,y))
        if len(S)>1:
           print_IP_number(S[1:],x+6,y)

def print_IP_tr(X,Y,count,x,y,masch):
    for i in range(1,count,1):
        RX = int((int((X[i]+105)/masch))/8)
        RY = int((int(int((600-((600-Y[i])/masch)))))/8)
        EX = int((int((X[i-1]+105)/masch))/8)
        EY = int((int(int((600-((600-Y[i-1])/masch)))))/8)
        pygame.draw.line(Window, (43,35,35),(x+RX,y+RY),(x+EX,y+EY),1)
        
def rotor_update(rotor_angle):
    
    if (rotor_angle == 180): F = 0
    else: F = (int(int((rotor_angle+180)*10)/18))
    if (F/100 == 0) or (F/100 == 1):kof_word = str(int(F/100))
    else:kof_word = str(F/100)

    koff = F/100

    return koff, kof_word

def get_koff_numpad(number):
    if number == '': return 0,"0"
    else:
        kof = number
        kof_word = str(number)
        if len(kof_word) > 1: kof_word = kof_word[0]+"."+kof_word[1:]
        return float(kof_word), kof_word

def Hinfo_update(number):
    n = len(number)
    if (n != 0):

        if (n == 5): Window.blit(max_height_info,(6,22+Hinfo_p))
        else:

            if (n == 1):
                number = "0" + number
                n = len(number)

            pos_num  = [0]*4

            if (n == 2):
                    pos_num[0] = 54
                    pos_num[1] = 86

            elif (n == 3):
                    pos_num[0] = 30
                    pos_num[1] = 54
                    pos_num[2] = 86

            elif (n == 4):
                    pos_num[0] = 6
                    pos_num[1] = 30
                    pos_num[2] = 54
                    pos_num[3] = 86

            for i in range (n):
                if (number[i] == "0"):  Window.blit(Hnumbers[0],(pos_num[i],22+Hinfo_p))
                elif (number[i] == "1"):Window.blit(Hnumbers[1],(pos_num[i],22+Hinfo_p))
                elif (number[i] == "2"):Window.blit(Hnumbers[2],(pos_num[i],22+Hinfo_p))
                elif (number[i] == "3"):Window.blit(Hnumbers[3],(pos_num[i],22+Hinfo_p))
                elif (number[i] == "4"):Window.blit(Hnumbers[4],(pos_num[i],22+Hinfo_p))
                elif (number[i] == "5"):Window.blit(Hnumbers[5],(pos_num[i],22+Hinfo_p))
                elif (number[i] == "6"):Window.blit(Hnumbers[6],(pos_num[i],22+Hinfo_p))
                elif (number[i] == "7"):Window.blit(Hnumbers[7],(pos_num[i],22+Hinfo_p))
                elif (number[i] == "8"):Window.blit(Hnumbers[8],(pos_num[i],22+Hinfo_p))
                elif (number[i] == "9"):Window.blit(Hnumbers[9],(pos_num[i],22+Hinfo_p))

    
def sm_update(number,X,Y):

    number = str(number)
    dot_point = 0
    n = len(number)
    if (n != 0):
        for i in range (n):
            if number[i] == ".":
                number = number[:i] + number[i+1:]
                n = len(number)
                break

        pos_x = [68,74,82,88,96,102]

        numberm = str(int(number)//6000)
        nm = len(numberm)
        number = str(int(number)%6000)
        n = len(number)
        
        while (n < 4):
            number = "0" + number
            n = len(number)

        while (nm < 2):
            numberm = "0" + numberm
            nm = len(numberm)

        number = numberm + number
        n = len(number)
            
        for i in range(n):
            if (number[i] == "0"):Window.blit(sm_numbers[0],(X+pos_x[i],Y+65))
            elif (number[i] == "1"):Window.blit(sm_numbers[1],(X+pos_x[i],Y+65))
            elif (number[i] == "2"):Window.blit(sm_numbers[2],(X+pos_x[i],Y+65))
            elif (number[i] == "3"):Window.blit(sm_numbers[3],(X+pos_x[i],Y+65))
            elif (number[i] == "4"):Window.blit(sm_numbers[4],(X+pos_x[i],Y+65))
            elif (number[i] == "5"):Window.blit(sm_numbers[5],(X+pos_x[i],Y+65))
            elif (number[i] == "6"):Window.blit(sm_numbers[6],(X+pos_x[i],Y+65))
            elif (number[i] == "7"):Window.blit(sm_numbers[7],(X+pos_x[i],Y+65))
            elif (number[i] == "8"):Window.blit(sm_numbers[8],(X+pos_x[i],Y+65))
            elif (number[i] == "9"):Window.blit(sm_numbers[9],(X+pos_x[i],Y+65))


                   
def kof_update(number):

    if (presser_on):
        dot_place = 0
        n = len(number)
        if (n != 0):
            for i in range (n):
                if number[i] == ".":
                    dot_place = i
                    number = number[:i] + number[i+1:]
                    n = len(number)
                    break
                
            while (n > 6):
                number = number[:n-1]
                n = len(number)

            pos_num  = [0]*6
                
            if not (dot_place == 0): Window.blit(dot_kof,(467+18*((6-n)+i),658+anim_y_3))

            if (n == 1):
                pos_num[0] = 560

            elif (n == 2):
                pos_num[0] = 542
                pos_num[1] = 560

            elif (n == 3):
                pos_num[0] = 524
                pos_num[1] = 542
                pos_num[2] = 560

            elif (n == 4):
                pos_num[0] = 506
                pos_num[1] = 524
                pos_num[2] = 542
                pos_num[3] = 560

            elif (n == 5):
                pos_num[0] = 488
                pos_num[1] = 506
                pos_num[2] = 524
                pos_num[3] = 542
                pos_num[4] = 560

            elif (n == 6):
                pos_num[0] = 470
                pos_num[1] = 488
                pos_num[2] = 506
                pos_num[3] = 524
                pos_num[4] = 542
                pos_num[5] = 560

            for i in range (n):
                if (number[i] == "0"):
                    Window.blit(cif_numbers[0],(pos_num[i],633+anim_y_3))
                elif (number[i] == "1"):
                    Window.blit(cif_numbers[1],(pos_num[i],633+anim_y_3))
                elif (number[i] == "2"):
                    Window.blit(cif_numbers[2],(pos_num[i],633+anim_y_3))
                elif (number[i] == "3"):
                    Window.blit(cif_numbers[3],(pos_num[i],633+anim_y_3))
                elif (number[i] == "4"):
                    Window.blit(cif_numbers[4],(pos_num[i],633+anim_y_3))
                elif (number[i] == "5"):
                    Window.blit(cif_numbers[5],(pos_num[i],633+anim_y_3))
                elif (number[i] == "6"):
                    Window.blit(cif_numbers[6],(pos_num[i],633+anim_y_3))
                elif (number[i] == "7"):
                    Window.blit(cif_numbers[7],(pos_num[i],633+anim_y_3))
                elif (number[i] == "8"):
                    Window.blit(cif_numbers[8],(pos_num[i],633+anim_y_3))
                elif (number[i] == "9"):
                    Window.blit(cif_numbers[9],(pos_num[i],633+anim_y_3))
                    
def speed_update(number):

    if (speed_enabled):
        n = len(number)
        if (n < 7):
            number = number + "_"
    n = len(number)
    if (n != 0):
        while (n > 7):
            number = number[:n-1]
            n = len(number)

        pos_num  = [0]*7
        
        if (n == 1):
            pos_num[0] = 129

        elif (n == 2):
            pos_num[0] = 111
            pos_num[1] = 147

        elif (n == 3):
            pos_num[0] = 93
            pos_num[1] = 129
            pos_num[2] = 165

        elif (n == 4):
            pos_num[0] = 75
            pos_num[1] = 111
            pos_num[2] = 147
            pos_num[3] = 183

        elif (n == 5):
            pos_num[0] = 57
            pos_num[1] = 93
            pos_num[2] = 129
            pos_num[3] = 165
            pos_num[4] = 201

        elif (n == 6):
            pos_num[0] = 39
            pos_num[1] = 75
            pos_num[2] = 111
            pos_num[3] = 147
            pos_num[4] = 183
            pos_num[5] = 219

        elif (n == 7):
            pos_num[0] = 21
            pos_num[1] = 57
            pos_num[2] = 93
            pos_num[3] = 129
            pos_num[4] = 165
            pos_num[5] = 201
            pos_num[6] = 237

        for i in range (n):
            if (number[i] == "0"):
                Window.blit(p0,(pos_num[i]+11+anim_x_1,739+anim_y_1))
            elif (number[i] == "1"):
                Window.blit(p1,(pos_num[i]+11+anim_x_1,739+anim_y_1))
            elif (number[i] == "2"):
                Window.blit(p2,(pos_num[i]+11+anim_x_1,739+anim_y_1))
            elif (number[i] == "3"):
                Window.blit(p3,(pos_num[i]+11+anim_x_1,739+anim_y_1))
            elif (number[i] == "4"):
                Window.blit(p4,(pos_num[i]+11+anim_x_1,739+anim_y_1))
            elif (number[i] == "5"):
                Window.blit(p5,(pos_num[i]+11+anim_x_1,739+anim_y_1))
            elif (number[i] == "6"):
                Window.blit(p6,(pos_num[i]+11+anim_x_1,739+anim_y_1))
            elif (number[i] == "7"):
                Window.blit(p7,(pos_num[i]+11+anim_x_1,739+anim_y_1))
            elif (number[i] == "8"):
                Window.blit(p8,(pos_num[i]+11+anim_x_1,739+anim_y_1))
            elif (number[i] == "9"):
                Window.blit(p9,(pos_num[i]+11+anim_x_1,739+anim_y_1))
            elif (number[i] == "_") and (sum_on):
                Window.blit(input_space,(pos_num[i]+11+anim_x_1,739+anim_y_1))

def mass_update(number):

    if (mass_enabled):
        n = len(number)
        if (n < 7):
            number = number + "_"
    n = len(number)
    if (n != 0):
        while (n > 7):
            number = number[:n-1]
            n = len(number)

        pos_num  = [0]*7
        
        if (n == 1):
            pos_num[0] = 486

        elif (n == 2):
            pos_num[0] = 468
            pos_num[1] = 504

        elif (n == 3):
            pos_num[0] = 450
            pos_num[1] = 486
            pos_num[2] = 522

        elif (n == 4):
            pos_num[0] = 432
            pos_num[1] = 468
            pos_num[2] = 504
            pos_num[3] = 540

        elif (n == 5):
            pos_num[0] = 414
            pos_num[1] = 450
            pos_num[2] = 486
            pos_num[3] = 522
            pos_num[4] = 558

        elif (n == 6):
            pos_num[0] = 396
            pos_num[1] = 432
            pos_num[2] = 468
            pos_num[3] = 504
            pos_num[4] = 540
            pos_num[5] = 576

        elif (n == 7):
            pos_num[0] = 378
            pos_num[1] = 414
            pos_num[2] = 450
            pos_num[3] = 486
            pos_num[4] = 522
            pos_num[5] = 558
            pos_num[6] = 594

        for i in range (n):
            if (number[i] == "0"):
                Window.blit(g0,(pos_num[i]+11,739+anim_y_2))
            elif (number[i] == "1"):
                Window.blit(g1,(pos_num[i]+11,739+anim_y_2))
            elif (number[i] == "2"):
                Window.blit(g2,(pos_num[i]+11,739+anim_y_2))
            elif (number[i] == "3"):
                Window.blit(g3,(pos_num[i]+11,739+anim_y_2))
            elif (number[i] == "4"):
                Window.blit(g4,(pos_num[i]+11,739+anim_y_2))
            elif (number[i] == "5"):
                Window.blit(g5,(pos_num[i]+11,739+anim_y_2))
            elif (number[i] == "6"):
                Window.blit(g6,(pos_num[i]+11,739+anim_y_2))
            elif (number[i] == "7"):
                Window.blit(g7,(pos_num[i]+11,739+anim_y_2))
            elif (number[i] == "8"):
                Window.blit(g8,(pos_num[i]+11,739+anim_y_2))
            elif (number[i] == "9"):
                Window.blit(g9,(pos_num[i]+11,739+anim_y_2))
            elif (number[i] == "_") and (sum_on):
                Window.blit(input_space_green,(pos_num[i]+11,739+anim_y_2))

def monitor_time_update(x,y,menu):
    global enable_1, enable_2, enable_3, enable_4
    
    now = str(datetime.datetime.now())
    
    F1 = int(now[0])
    F2 = int(now[1])
    F3 = int(now[2])
    F4 = int(now[3])
    F5 = int(now[5])
    F6 = int(now[6])
    F7 = int(now[8])
    F8 = int(now[9])
    F9 = int(now[11])
    F10 = int(now[12])
    F11 = int(now[14])
    F12 = int(now[15])

    Window.blit(monitor_num[F9],(x+204,y+88))
    Window.blit(monitor_num[F10],(x+210,y+88))
    Window.blit(monitor_num[F11],(x+218,y+88))
    Window.blit(monitor_num[F12],(x+224,y+88))
    Window.blit(monitor_num[F7],(x+191,y+100))
    Window.blit(monitor_num[F8],(x+197,y+100))
    Window.blit(monitor_num[F5],(x+205,y+100))
    Window.blit(monitor_num[F6],(x+211,y+100))
    Window.blit(monitor_num[F1],(x+219,y+100))
    Window.blit(monitor_num[F2],(x+225,y+100))
    Window.blit(monitor_num[F3],(x+231,y+100))
    Window.blit(monitor_num[F4],(x+237,y+100))

    if x_mouse >= x+12 and x_mouse <= x+121+12:
        if y_mouse >= y+6-28 and y_mouse <= y+6-28+9: enable_1 = True
        else: enable_1 = False
        if y_mouse >= y+18-28 and y_mouse <= y+18-28+9: enable_2 = True
        else: enable_2 = False
        if y_mouse >= y+30-28 and y_mouse <= y+30-28+9: enable_3 = True
        else: enable_3 = False
        if y_mouse >= y+40-28+2 and y_mouse <= y+40-28+11: enable_4 = True
        else: enable_4 = False
    else:
        enable_1 = False
        enable_2 = False
        enable_3 = False
        enable_4 = False
    
    if menu == "main":
        if enable_1: monitor_text1.set_alpha(255)
        else: monitor_text1.set_alpha(127)
        if enable_2: monitor_text2.set_alpha(255)
        else: monitor_text2.set_alpha(127)
        if enable_3: monitor_text3.set_alpha(255)
        else: monitor_text3.set_alpha(127)
        if enable_4: monitor_text4.set_alpha(255)
        else: monitor_text4.set_alpha(127)        

        Window.blit(monitor_text1,(x+12,y+6-28))
        Window.blit(monitor_text2,(x+12,y+18-28))
        Window.blit(monitor_text3,(x+12,y+30-28))
        Window.blit(monitor_text4,(x+12,y+40-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_2: Window.blit(monitor_textset,(x+5,y+20-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))

    if menu == "settings":
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text6.set_alpha(255); monitor_text7.set_alpha(255)
        else: monitor_text6.set_alpha(127); monitor_text7.set_alpha(127)
        #if enable_4: monitor_text4.set_alpha(255)
        #else: monitor_text4.set_alpha(127)        

        Window.blit(monitor_text5,(x+12,y+6-28))
        #Window.blit(monitor_text2,(x+12,y+18-28))
        if draw_parabola : Window.blit(monitor_text6,(x+12,y+30-28))
        else: Window.blit(monitor_text7,(x+12,y+30-28))
        #Window.blit(monitor_text4,(x+12,y+40-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        #if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))

    if menu == "remember":

        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))

        if y_mouse >= y+28-28 and y_mouse <= y+28+13-28 and x_mouse >= x+28 and x_mouse <= x+28+39: tr_slot1.set_alpha(255)
        else: tr_slot1.set_alpha(200)
        Window.blit(tr_slot1,(x+28,y+28-28))

        if y_mouse >= y+44-28 and y_mouse <= y+44+13-28 and x_mouse >= x+28 and x_mouse <= x+28+39: tr_slot2.set_alpha(255)
        else: tr_slot2.set_alpha(200)
        Window.blit(tr_slot2,(x+28,y+44-28))

        if y_mouse >= y+60-28 and y_mouse <= y+60+13-28 and x_mouse >= x+28 and x_mouse <= x+28+39: tr_slot3.set_alpha(255)
        else: tr_slot3.set_alpha(200)
        Window.blit(tr_slot3,(x+28,y+60-28))

        if y_mouse >= y+76-28 and y_mouse <= y+76+13-28 and x_mouse >= x+28 and x_mouse <= x+28+39: tr_slot4.set_alpha(255)
        else: tr_slot4.set_alpha(200)
        Window.blit(tr_slot4,(x+28,y+76-28))

        if y_mouse >= y+28-28 and y_mouse <= y+28+13-28 and x_mouse >= x+127 and x_mouse <= x+127+39: tr_slot5.set_alpha(255)
        else: tr_slot5.set_alpha(200)
        Window.blit(tr_slot5,(x+127,y+28-28))

        if y_mouse >= y+44-28 and y_mouse <= y+44+13-28 and x_mouse >= x+127 and x_mouse <= x+127+39: tr_slot6.set_alpha(255)
        else: tr_slot6.set_alpha(200)
        Window.blit(tr_slot6,(x+127,y+44-28))

        if y_mouse >= y+60-28 and y_mouse <= y+60+13-28 and x_mouse >= x+127 and x_mouse <= x+127+39: tr_slot7.set_alpha(255)
        else: tr_slot7.set_alpha(200)
        Window.blit(tr_slot7,(x+127,y+60-28))

        if y_mouse >= y+76-28 and y_mouse <= y+76+13-28 and x_mouse >= x+127 and x_mouse <= x+127+39: tr_slot8.set_alpha(255)
        else: tr_slot8.set_alpha(200)
        Window.blit(tr_slot8,(x+127,y+76-28))

        global save_enable

        if y_mouse >= y+28-28 and y_mouse <= y+28+13-28 and x_mouse >= x+67 and x_mouse <= x+67+13: tr_save.set_alpha(255); save_enable[0] = False
        else: tr_save.set_alpha(200); save_enable[0] = True
        Window.blit(tr_save,(x+67,y+28-28))

        if y_mouse >= y+44-28 and y_mouse <= y+44+13-28 and x_mouse >= x+67 and x_mouse <= x+67+13: tr_save.set_alpha(255); save_enable[1] = False
        else: tr_save.set_alpha(200); save_enable[1] = True
        Window.blit(tr_save,(x+67,y+44-28))

        if y_mouse >= y+60-28 and y_mouse <= y+60+13-28 and x_mouse >= x+67 and x_mouse <= x+67+13: tr_save.set_alpha(255); save_enable[2] = False
        else: tr_save.set_alpha(200); save_enable[2] = True
        Window.blit(tr_save,(x+67,y+60-28))

        if y_mouse >= y+76-28 and y_mouse <= y+76+13-28 and x_mouse >= x+67 and x_mouse <= x+67+13: tr_save.set_alpha(255); save_enable[3] = False
        else: tr_save.set_alpha(200); save_enable[3] = True
        Window.blit(tr_save,(x+67,y+76-28))

        if y_mouse >= y+28-28 and y_mouse <= y+28+13-28 and x_mouse >= x+166 and x_mouse <= x+166+13: tr_save.set_alpha(255); save_enable[4] = False
        else: tr_save.set_alpha(200); save_enable[4] = True
        Window.blit(tr_save,(x+166,y+28-28))

        if y_mouse >= y+44-28 and y_mouse <= y+44+13-28 and x_mouse >= x+166 and x_mouse <= x+166+13: tr_save.set_alpha(255); save_enable[5] = False
        else: tr_save.set_alpha(200); save_enable[5] = True
        Window.blit(tr_save,(x+166,y+44-28))

        if y_mouse >= y+60-28 and y_mouse <= y+60+13-28 and x_mouse >= x+166 and x_mouse <= x+166+13: tr_save.set_alpha(255); save_enable[6] = False
        else: tr_save.set_alpha(200); save_enable[6] = True
        Window.blit(tr_save,(x+166,y+60-28))

        if y_mouse >= y+76-28 and y_mouse <= y+76+13-28 and x_mouse >= x+166 and x_mouse <= x+166+13: tr_save.set_alpha(255); save_enable[7] = False
        else: tr_save.set_alpha(200); save_enable[7] = True
        Window.blit(tr_save,(x+166,y+76-28))

        global delete_enable

        if y_mouse >= y+28-28 and y_mouse <= y+28+13-28 and x_mouse >= x+80 and x_mouse <= x+80+13: tr_delete.set_alpha(255); delete_enable[0] = False
        else: tr_delete.set_alpha(200); delete_enable[0] = True
        Window.blit(tr_delete,(x+80,y+28-28))

        if y_mouse >= y+44-28 and y_mouse <= y+44+13-28 and x_mouse >= x+80 and x_mouse <= x+80+13: tr_delete.set_alpha(255); delete_enable[1] = False
        else: tr_delete.set_alpha(200); delete_enable[1] = True
        Window.blit(tr_delete,(x+80,y+44-28))

        if y_mouse >= y+60-28 and y_mouse <= y+60+13-28 and x_mouse >= x+80 and x_mouse <= x+80+13: tr_delete.set_alpha(255); delete_enable[2] = False
        else: tr_delete.set_alpha(200); delete_enable[2] = True
        Window.blit(tr_delete,(x+80,y+60-28))

        if y_mouse >= y+76-28 and y_mouse <= y+76+13-28 and x_mouse >= x+80 and x_mouse <= x+80+13: tr_delete.set_alpha(255); delete_enable[3] = False
        else: tr_delete.set_alpha(200); delete_enable[3] = True
        Window.blit(tr_delete,(x+80,y+76-28))

        if y_mouse >= y+28-28 and y_mouse <= y+28+13-28 and x_mouse >= x+179 and x_mouse <= x+179+13: tr_delete.set_alpha(255); delete_enable[4] = False
        else: tr_delete.set_alpha(200); delete_enable[4] = True
        Window.blit(tr_delete,(x+179,y+28-28))

        if y_mouse >= y+44-28 and y_mouse <= y+44+13-28 and x_mouse >= x+179 and x_mouse <= x+179+13: tr_delete.set_alpha(255); delete_enable[5] = False
        else: tr_delete.set_alpha(200); delete_enable[5] = True
        Window.blit(tr_delete,(x+179,y+44-28))

        if y_mouse >= y+60-28 and y_mouse <= y+60+13-28 and x_mouse >= x+179 and x_mouse <= x+179+13: tr_delete.set_alpha(255); delete_enable[6] = False
        else: tr_delete.set_alpha(200); delete_enable[6] = True
        Window.blit(tr_delete,(x+179,y+60-28))

        if y_mouse >= y+76-28 and y_mouse <= y+76+13-28 and x_mouse >= x+179 and x_mouse <= x+179+13: tr_delete.set_alpha(255); delete_enable[7] = False
        else: tr_delete.set_alpha(200); delete_enable[7] = True
        Window.blit(tr_delete,(x+179,y+76-28))

        y_addpos = [28,44,60,76,28,44,60,76]
        x_addpos = [93,93,93,93,192,192,192,192]

        global viev_enable
        
        for i in range(8):
            if viev_bool[i]:
                if y_mouse >= y+y_addpos[i]-28 and y_mouse <= y+y_addpos[i]+13-28 and x_mouse >= x+x_addpos[i] and x_mouse <= x+x_addpos[i]+13: tr_viev.set_alpha(255); viev_enable[i] = True
                else: tr_viev.set_alpha(200); viev_enable[i] = False
                Window.blit(tr_viev,(x+x_addpos[i],y+y_addpos[i]-28))
                
            else:
                if y_mouse >= y+y_addpos[i]-28 and y_mouse <= y+y_addpos[i]+13-28 and x_mouse >= x+x_addpos[i] and x_mouse <= x+x_addpos[i]+13: tr_unviev.set_alpha(255); viev_enable[i] = True
                else: tr_unviev.set_alpha(200); viev_enable[i] = False
                Window.blit(tr_unviev,(x+x_addpos[i],y+y_addpos[i]-28))

        y_addpos = [28,44,60,76,28,44,60,76]
        x_addpos = [106,106,106,106,205,205,205,205]
        
        global color_enable, color_tr, tr_color
        
        for i in range(8):
                
                if y_mouse >= y+y_addpos[i]-28 and y_mouse <= y+y_addpos[i]+13-28 and x_mouse >= x+x_addpos[i] and x_mouse <= x+x_addpos[i]+13:
                    (tr_color[color_tr[i]]).set_alpha(255)
                    color_enable[i] = True
                else:
                    (tr_color[color_tr[i]]).set_alpha(200)
                    color_enable[i] = False
                Window.blit(tr_color[color_tr[i]],(x+x_addpos[i],y+y_addpos[i]-28))        

def draw_lines(X,Y,tick,masch,color):
    if (masch >= 8): W = 1
    elif (masch >= 2) and (masch <= 4): W = 2
    else: W = 3
    
    for i in range (1,tick,1):
        yrydpos = 600-Y[i-1]
        rydpos = 600-Y[i]
        pygame.draw.line(Window, color,((X[i]+105)/masch,(int((600-(rydpos/masch))))),((X[i-1]+105)/masch,(int((600-(yrydpos/masch))))),W)

def set_code(A):
    if (A == "а" or A == "A"): return "00"
    elif (A == "б" or A == "Б"): return "01"
    elif (A == "в" or A == "В"): return "02"
    elif (A == "г" or A == "Г"): return "03"
    elif (A == "д" or A == "Д"): return "04"
    elif (A == "е" or A == "Е"): return "05"
    elif (A == "ё" or A == "Ё"): return "06"    
    elif (A == "ж" or A == "Ж"): return "07"
    elif (A == "з" or A == "З"): return "08"
    elif (A == "и" or A == "И"): return "09"
    elif (A == "й" or A == "Й"): return "10"    
    elif (A == "к" or A == "К"): return "11"
    elif (A == "л" or A == "Л"): return "12"
    elif (A == "м" or A == "М"): return "13"    
    elif (A == "н" or A == "Н"): return "14"
    elif (A == "о" or A == "О"): return "15"
    elif (A == "п" or A == "П"): return "16"
    elif (A == "р" or A == "Р"): return "17"
    elif (A == "с" or A == "С"): return "18"
    elif (A == "т" or A == "Т"): return "19"
    elif (A == "у" or A == "У"): return "20"
    elif (A == "ф" or A == "Ф"): return "21"
    elif (A == "х" or A == "Ч"): return "22"
    elif (A == "ц" or A == "Ц"): return "23"
    elif (A == "ч" or A == "Ч"): return "24"
    elif (A == "ш" or A == "Ш"): return "25"    
    elif (A == "щ" or A == "Щ"): return "26"
    elif (A == "ъ" or A == "Ъ"): return "27"
    elif (A == "ы" or A == "Ы"): return "28"
    elif (A == "ь" or A == "Ь"): return "29"
    elif (A == "э" or A == "Э"): return "30"
    elif (A == "ю" or A == "Ю"): return "31"    
    elif (A == "я" or A == "Я"): return "32"

    elif (A == "a" or A == "A"): return "33"
    elif (A == "b" or A == "B"): return "34"
    elif (A == "c" or A == "C"): return "35"
    elif (A == "d" or A == "D"): return "36"
    elif (A == "e" or A == "E"): return "37"
    elif (A == "f" or A == "F"): return "38"
    elif (A == "g" or A == "G"): return "39"
    elif (A == "h" or A == "H"): return "40"
    elif (A == "i" or A == "I"): return "41"
    elif (A == "j" or A == "J"): return "42"
    elif (A == "k" or A == "K"): return "43"
    elif (A == "l" or A == "L"): return "44"
    elif (A == "m" or A == "M"): return "45"
    elif (A == "n" or A == "N"): return "46"
    elif (A == "o" or A == "O"): return "47"
    elif (A == "p" or A == "P"): return "48"
    elif (A == "q" or A == "Q"): return "49"
    elif (A == "r" or A == "R"): return "50"
    elif (A == "s" or A == "S"): return "51"
    elif (A == "t" or A == "T"): return "52"
    elif (A == "u" or A == "U"): return "53"
    elif (A == "v" or A == "V"): return "54"
    elif (A == "w" or A == "W"): return "55"
    elif (A == "x" or A == "X"): return "56"
    elif (A == "y" or A == "Y"): return "57"
    elif (A == "z" or A == "Z"): return "58"

    elif (A == "0"): return "59"
    elif (A == "1"): return "60"
    elif (A == "2"): return "61"
    elif (A == "3"): return "62"
    elif (A == "4"): return "63"
    elif (A == "5"): return "64"
    elif (A == "6"): return "65"
    elif (A == "7"): return "66"
    elif (A == "8"): return "67"
    elif (A == "9"): return "68"

    elif (A == "!"): return "69"
    elif (A == "?"): return "70"
    elif (A == "."): return "71"
    elif (A == ","): return "72"
    elif (A == " "): return "73"
    elif (A == ":"): return "74"
    elif (A == "("): return "75"
    elif (A == ")"): return "76"
    elif (A == "-"): return "77"
    elif (A == "+"): return "78"
    elif (A == "*"): return "79"

    else: return "80"

def text_print(S,x,y):
    SPR = IDL[int(set_code(S[0]))]
    Window.blit(SPR, (x,y))
    if len(S)>1:
        text_print(S[1:],x+6,y)

def monitor_text(S,x,y):
    SPR = MT[int(set_code(S[0]))]
    Window.blit(SPR, (x,y))
    if len(S)>1:
        text_print(S[1:],x+6,y)
    
def update():
    global decor_bool,decor_tick,x_pos,y_pos,Dot_count, speed_arrow, x_mouse, y_mouse, start_button_play, Atick, curr_angle_vent, repeat_button_rise_play, repeat_button_up, repeat_button_set_play
    global sideshow_play_up,sideshow_play_down,anim_x_1,anim_y_1,anim_y_2,anim_y_3,Btick,Hinfo_p, numbutton_bool, Atick_printmachine, print_button_play, presser_on, presser_off, presser_play, curr_angle_rotor
    global sideshow_pos_y, sideshow_bool, Dtick, decoran2_up, decoran2_down, decoran2_bool, animballangle, Stick, m16, m8, m4, m2, m1, monitor_bool, monitor_start, MST, monitor_start_load, Ctick, masch
    global RTA_nor, RTA_inv, rotor_ticker_bool, Dtick, rotor_angle, koff_input, koff, koff_word, koff_enable, Etick, book_bool, Ftick, Gtick, Window, HBA, Htick, Ktick, masch_avto_anim, masch_avto_bool
    global masch_avto_curr, hm16,hm8, hm4, hm2, hm32, hm64, hm128, hm256, bgt, gbgt, abt, abort_button_status

    DR = ((str(datetime.datetime.now()))[11:19])
    supertime = int(DR[0:2])*3600+int(DR[3:5])*60+int(DR[6:8])

    if (simulator_run) and (not(decoran2_bool)): decoran2_up = True
    if (finish_sim) and (decoran2_bool): decoran2_down = True
    
    if (sideshow_play_up):
        Btick = Btick + 1
        if (Btick < 11):
            anim_x_1 = 0
            anim_y_1 = int(1.5*Btick)
            anim_y_2 = int(1.5*Btick)
            anim_y_3 = int(1.5*Btick)
            sideshow_pos_y = 0

        elif (Btick >= 11) and (Btick < 48):
            anim_x_1 = -10*(Btick-10)
            anim_y_1 = 15
            anim_y_2 = 15 + 3*(Btick-10)
            anim_y_3 = 15 + (-3*(Btick-10))
            sideshow_pos_y = (-4*(Btick-10))

        if (Btick >= 48):
            
            sideshow_bool = True
            sideshow_play_up = False
            Btick = 48

    if (sideshow_play_down):
        Btick = Btick - 1
        if (Btick < 48) and (Btick >= 11):
            anim_x_1 = -10*(Btick-10)
            anim_y_1 = 15
            anim_y_2 = 15 + 3*(Btick-10)
            anim_y_3 = 15 + (-3*(Btick-10))
            sideshow_pos_y = (-4*(Btick-10))

        elif (Btick < 11):
            anim_x_1 = 0
            anim_y_1 = int(1.5*Btick)
            anim_y_2 = int(1.5*Btick)
            anim_y_3 = int(1.5*Btick)
            sideshow_pos_y = 0
            
        if (Btick < 1):

            sideshow_bool = False
            sideshow_play_down = False
            Btick = 0



    Window.fill((117,187,253))

    if (simulator_run): ry_pos = 600-y_pos
    else: ry_pos = 0

    if (125+x_pos > 184320) or (ry_pos+20 >= 76800):
        hm256 = True
    elif (125+x_pos > 92160) or (ry_pos+20 >= 38400):
        hm128 = True
    elif (125+x_pos > 46080) or (ry_pos+20 >= 19200):
        hm64 = True
    elif (125+x_pos > 23040) or (ry_pos+20 >= 9600):
        hm32 = True
    elif (125+x_pos > 11520) or (ry_pos+20 >= 4800):
        hm16 = True
    elif (125+x_pos > 5760) or (ry_pos+20 >= 2400):
        hm8 = True
    elif (125+x_pos > 2880) or (ry_pos+20 >= 1200):
        hm4 = True
    elif (125+x_pos > 1440) or (ry_pos+20 >= 600):
        hm2 = True
        
    if (masch_avto_bool):

        masch_procent = 0
        if (simulator_run):
            if (125+x_pos > 11520) or (ry_pos+20 >= 4800) or hm16:
                m16 = True
                masch_procent += 0.8
            elif (125+x_pos > 5760) or (ry_pos+20 >= 2400) or hm8:
                m8 = True
                masch_procent += 0.6
            elif (125+x_pos > 2880) or (ry_pos+20 >= 1200) or hm4:
                m4 = True
                masch_procent += 0.4
            elif (125+x_pos > 1440) or (ry_pos+20 >= 600) or hm2:
                m2 = True
                masch_procent += 0.2
            else:
                m1 = True
        
        if m16:
            masch = 16
            masch_procent_add_x = ((((125+x_pos)/23040))-0.5)*2
            masch_procent_add_y = ((((ry_pos+20)/9600))-0.5)*2
        elif m8:
            masch = 8
            masch_procent_add_x = ((((125+x_pos)/11520))-0.5)*2
            masch_procent_add_y = ((((ry_pos+20)/4800))-0.5)*2
        elif m4:
            masch = 4
            masch_procent_add_x = ((((125+x_pos)/5760))-0.5)*2
            masch_procent_add_y = ((((ry_pos+20)/2400))-0.5)*2
        elif m2:
            masch = 2
            masch_procent_add_x = ((((125+x_pos)/2880))-0.5)*2
            masch_procent_add_y = ((((ry_pos+20)/1200))-0.5)*2
        else:
            masch = 1
            masch_procent_add_x = ((125+x_pos)/1440)
            masch_procent_add_y = ((ry_pos+20)/600)
            
        if masch_procent_add_x >= masch_procent_add_y: masch_procent_add = masch_procent_add_x
        else: masch_procent_add = masch_procent_add_y

        masch_procent += (0.2 * masch_procent_add)

        if (masch_procent > 1): masch_procent = 1
        if (masch_procent < 0): masch_procent = 0
        
    else:
        m1 = False
        m2 = False
        m4 = False
        m8 = False
        m16 = False
        
        if masch_avto_curr >= 960 and masch_avto_curr < 973:
            masch = 1
            m1 = True
        elif masch_avto_curr >= 973 and masch_avto_curr < 987:
            masch = 2
            m2 = True
        elif masch_avto_curr >= 987 and masch_avto_curr < 1001:
            masch = 4
            m4 = True
        elif masch_avto_curr >= 1001 and masch_avto_curr < 1015:
            masch = 8
            m8 = True
        elif masch_avto_curr >= 1015 and masch_avto_curr <= 1029:
            masch = 16
            m16 = True

    gbgt += 1
    if gbgt > 6:
        gbgt = 0
        bgt += 1
        if bgt > 2: bgt = 0

    if masch == 1: Window.blit(background_1x[bgt],(0,0))
    if masch == 2: Window.blit(background_2x[bgt],(0,0))
    if masch == 4: Window.blit(background_4x[bgt],(0,0))
    if masch == 8: Window.blit(background_8x[bgt],(0,0))

    tower1 = pygame.transform.scale(tower,(int(150/masch),int(10000/masch)))
    Window.blit(tower1,(50/masch,(600-((600-height)/masch))))

    if(rotor_enabled):rotor_angle = math.degrees(math.atan2(y_mouse-658, x_mouse-629))

    if (rotor_angle > 0) and (rotor_angle < 90): rotor_angle = 0
    if (rotor_angle >= 90) and (rotor_angle < 180): rotor_angle = -180

    rotor_rect = rotor.get_rect(center=(629,658)) 
    rotor2, rotor_p = rot_center(rotor, rotor_rect, -rotor_angle-90)

    if not rotor_ticker_bool: koff, kof_word = rotor_update(rotor_angle)
    else: koff, kof_word = get_koff_numpad(koff_input)

    if not((simulator_run) or (finish_sim)):
        if masch == 1:
            forse_arrow_rect = forse_arrow.get_rect(center=(int(60),int(60))) 
            forse_arrow2, forse_arrow_p = rot_center(forse_arrow, forse_arrow_rect, (90-angle))
            forse_arrow3 = pygame.transform.flip(forse_arrow2, True, False)
            Window.blit(forse_arrow3, (forse_arrow_p[0]+20,forse_arrow_p[1]+height-80))
            if (presser_on):
                kof_word1 = float(kof_word)
                if (kof_word1 >= 0) and (kof_word1 < 0.05):
                    ball1_rect = ball1.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball1, ball1_rect, angle)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.05) and (kof_word1 < 0.15):
                    ball1_rect = ball2.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball2, ball1_rect, angle)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.15) and (kof_word1 < 0.25):
                    ball1_rect = ball3.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball3, ball1_rect, angle)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.25) and (kof_word1 < 0.35):
                    ball1_rect = ball4.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball4, ball1_rect, angle)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.35) and (kof_word1 < 0.45):
                    ball1_rect = ball5.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball5, ball1_rect, angle)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.45) and (kof_word1 < 0.55):
                    ball1_rect = ball6.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball6, ball1_rect, angle)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.55) and (kof_word1 < 0.65):
                    ball1_rect = ball7.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball7, ball1_rect, angle)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.65) and (kof_word1 < 0.75):
                    ball1_rect = ball8.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball8, ball1_rect, angle)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.75) and (kof_word1 < 0.85):
                    ball1_rect = ball9.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball9, ball1_rect, angle)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.85) and (kof_word1 < 0.95):
                    ball1_rect = ball10.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball10, ball1_rect, angle)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.95):
                    ball1_rect = ball11.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball11, ball1_rect, angle)
                    Window.blit(balln,(ball1_p))
                    
            else: Window.blit(ball6,(105+x_pos, height-40))
        
    Window.blit(height_info,(0, Hinfo_p-13))
    Hinfo_update(str(500-(height-100)))

    Window.blit(base_insidewall,(12, 612))

    Window.blit(showside_base,(12, 760+sideshow_pos_y))

    Window.blit(showside_speed,(203, 784+sideshow_pos_y))
    
    Window.blit(monitor_base,(468, 768+sideshow_pos_y))
    Window.blit(podmonitor,(468, 909+sideshow_pos_y))
    if monitor_bool or monitor_start or monitor_start_load:
        Window.blit(monitor_on_button,(471, 909+sideshow_pos_y))
        if monitor_bool:
            Window.blit(monitor_mainmenu,(468, 768+sideshow_pos_y))
            monitor_time_update(468, 768+sideshow_pos_y+28,menu)
            if randint(0,1): Window.blit(monitor_effect1,(471, 771+sideshow_pos_y))
            else: Window.blit(monitor_effect2,(471, 771+sideshow_pos_y))

    if monitor_start:
        MST += 1
        if MST >= 2 and MST < 4: Window.blit(monitor_loading1,(468, 768+sideshow_pos_y))
        elif MST >= 4 and MST < 6: Window.blit(monitor_loading2,(468, 768+sideshow_pos_y))
        elif MST >= 6 and MST < 8: Window.blit(monitor_loading3,(468, 768+sideshow_pos_y))
        elif MST >= 8 and MST < 10: Window.blit(monitor_loading4,(468, 768+sideshow_pos_y))
        elif MST >= 10 and MST < 12: Window.blit(monitor_loading5,(468, 768+sideshow_pos_y))
        elif MST >= 12 and MST < 14: Window.blit(monitor_loading6,(468, 768+sideshow_pos_y))
        elif MST >= 14 and MST < 16: Window.blit(monitor_loading7,(468, 768+sideshow_pos_y))
        elif MST >= 16 and MST < 18: Window.blit(monitor_loading8,(468, 768+sideshow_pos_y))
        elif MST >= 18:
            MST = 0
            monitor_start = False
            monitor_start_load = True
        if randint(0,1): Window.blit(monitor_effect1,(471, 771+sideshow_pos_y))
        else: Window.blit(monitor_effect2,(471, 771+sideshow_pos_y))

    if monitor_start_load:
        Window.blit(monitor_loading_post,(468, 768+sideshow_pos_y))
        pygame.draw.rect(Window, (230, 232, 242),(468+73, 768+70+sideshow_pos_y, MST, 8))
        MST += 1
        if MST > 100:
            MST = 0 
            monitor_start_load = False
            monitor_bool = True
        if randint(0,1): Window.blit(monitor_effect1,(471, 771+sideshow_pos_y))
        else: Window.blit(monitor_effect2,(471, 771+sideshow_pos_y))

    if (decoran2_up):
        Dtick = Dtick + 1
        if (Dtick > 6):
            Dtick = 6
            decoran2_up = False
            decoran2_bool = True

    if (decoran2_down):
        decoran2_bool = False
        Dtick = Dtick - 1
        if (Dtick < 0):
            Dtick = 0
            decoran2_down = False

    if (decoran2_bool):
        if (Dtick == 6) and (randint(0,2) == 0): Dtick = 7
        elif (Dtick == 7) and (randint(0,2) == 0): Dtick = 6

    if(Dtick == 0):Window.blit(decoran2_f1,(21, 914+sideshow_pos_y))
    elif(Dtick == 1):Window.blit(decoran2_f2,(21, 914+sideshow_pos_y))
    elif(Dtick == 2):Window.blit(decoran2_f3,(21, 914+sideshow_pos_y))
    elif(Dtick == 3):Window.blit(decoran2_f4,(21, 914+sideshow_pos_y))
    elif(Dtick == 4):Window.blit(decoran2_f5,(21, 914+sideshow_pos_y))
    elif(Dtick == 5):Window.blit(decoran2_f6,(21, 914+sideshow_pos_y))
    elif(Dtick == 6):Window.blit(decoran2_f7,(21, 914+sideshow_pos_y))
    elif(Dtick == 7):Window.blit(decoran2_f8,(21, 914+sideshow_pos_y))
    
    Window.blit(secundometr_base,(17, 765+sideshow_pos_y))

    Tper = str((timer*100)/100)
    Tnin = len(Tper)
    for h in range(Tnin):
        if (Tper[h] == "."):
            Tper = Tper[:h+3]
            break
    sm_update(Tper,17,765+sideshow_pos_y)

    curr_angle_subsec = ((int(timer*100))%100)*3.6
    subsec_rect = secundometr_subarrow.get_rect(center=(104,885+sideshow_pos_y)) 
    subsec2, subsec_p = rot_center(secundometr_subarrow, subsec_rect, -curr_angle_subsec+90)

    Window.blit(subsec2, (subsec_p))

    curr_angle_sec = timer*6
    sec_rect = secundometr_secarrow.get_rect(center=(104,852+sideshow_pos_y)) 
    sec2, sec_p = rot_center(secundometr_secarrow, sec_rect, -curr_angle_sec+90)

    Window.blit(sec2, (sec_p))

    Window.blit(show_fps_base,(203, 768+sideshow_pos_y))
    fpc_procent = fps_count/FPS
    if (fpc_procent > 1): fpc_procent = 1
    if (fpc_procent < 0): fpc_procent = 0
    for i in range (int(fpc_procent*100)):
        pygame.draw.rect(Window, (int((i/100)*255),127,255-int((i/100)*255)),(205+i*2, 770+sideshow_pos_y, 2, 10))

    
                                
    Window.blit(button_group_first,(11+anim_x_1, 611+anim_y_1))
    Window.blit(button_group_second,(366, 704+anim_y_2))
    Window.blit(button_group_third,(366, 611+anim_y_3))
    Window.blit(rotor2, (rotor_p[0],rotor_p[1]+anim_y_3))
    Window.blit(rotor_ticker[Ctick],(681, 622+anim_y_3))
    Window.blit(decor2,(366, 591+anim_y_3))

    Htick += 1
    if Htick > 60:
        Htick = 0
        for i in range(18):
            for j in range(4):
                HBA[i][j] = randint(0,1)
                
    for i in range(18):
        for j in range(4):
            if (HBA[i][j]) and False: pygame.draw.rect(Window, (255,0,0),(i*6+467, j*6+675+anim_y_3, 2, 2))
    
    if RTA_nor:
        if (Ctick > 2): Ctick = 2
        if (Ctick < 0): Ctick = 0
        Dtick += 1
        if Dtick == 4:
            Ctick += 1
            Dtick = 0
        if Ctick > 2:
            Сtick = 2
            Dtick = 0
            RTA_nor = False
            rotor_ticker_bool = True
        if (Ctick > 2): Ctick = 2
        if (Ctick < 0): Ctick = 0

    if RTA_inv:
        koff_enable = False
        if (Ctick > 2): Ctick = 2
        if (Ctick < 0): Ctick = 0
        Dtick += 1
        if Dtick == 4:
            Ctick -= 1
            Dtick = 0
        if Ctick < 0:
            Сtick = 0
            Dtick = 0
            rotor_ticker_bool = False
            RTA_inv = False
        if (Ctick > 2): Ctick = 2
        if (Ctick < 0): Ctick = 0

    decor_tick = decor_tick + 1
    if (decor_tick > 5):
        decor_tick = 0
        decor_bool = bool(randint(0,1))
    if decor_bool: Window.blit(decoran1_f2,(298+anim_x_1, 688+anim_y_1))
    else: Window.blit(decoran1_f1,(298+anim_x_1, 688+anim_y_1))

    Window.blit(rotor_close,(588, 617+anim_y_3))
    if(presser_on):Window.blit(indicator_on,(689, 655+anim_y_3))
    else:Window.blit(indicator_off,(689, 655+anim_y_3))

    if (presser_on):curr_angle_vent = curr_angle_vent + angle_speed_vent*(1/(koff+1))
    else: curr_angle_vent = curr_angle_vent + angle_speed_vent
    vent_rect = vent.get_rect(center=(379,624+anim_y_3)) 
    vent2, vent_p = rot_center(vent, vent_rect, -curr_angle_vent)

    Window.blit(vent2, (vent_p[0]+34,vent_p[1]+34))

    Window.blit(vent_close,(376, 621+anim_y_3))

    if (speed_how == "meterspersecond"): Window.blit(M_P_S,(302+anim_x_1, 733+anim_y_1))
    elif (speed_how == "kilometersperhour"): Window.blit(KM_P_H,(302+anim_x_1, 733+anim_y_1))
    elif (speed_how == "santimeterspersecond"): Window.blit(SM_P_S,(302+anim_x_1, 733+anim_y_1))

    if (mass_how == "ton"): Window.blit(TON,(657, 733+anim_y_2))
    elif (mass_how == "kg"): Window.blit(KG,(657, 733+anim_y_2))
    elif (mass_how == "gramm"): Window.blit(GRAMM,(657, 733+anim_y_2))

    if (count_up_bool): Window.blit(count_up_clicked,(302+anim_x_1, 762+anim_y_1))
    else: Window.blit(count_up,(302+anim_x_1, 762+anim_y_1))
    if (count_down_bool): Window.blit(count_down_clicked,(331+anim_x_1, 762+anim_y_1))
    else: Window.blit(count_down,(331+anim_x_1, 762+anim_y_1))

    if (count_up_mass_bool): Window.blit(count_up_clicked,(657, 762+anim_y_2))
    else: Window.blit(count_up,(657, 762+anim_y_2))
    if (count_down_mass_bool): Window.blit(count_down_clicked,(686, 762+anim_y_2))
    else: Window.blit(count_down,(686, 762+anim_y_2))

    if (presser_on) and (presser_play):
        Atick = Atick + 1
        if (Atick >= 1) and ( Atick < 3):Window.blit(on_pesser4,(677, 660+anim_y_3))
        elif (Atick >= 3) and ( Atick < 5):Window.blit(on_pesser3,(677, 660+anim_y_3))
        elif (Atick >= 5) and ( Atick < 7):Window.blit(on_pesser2,(677, 660+anim_y_3))
        elif (Atick >= 7):

            Window.blit(on_pesser1,(677, 660+anim_y_3))
            
            presser_off = True
            presser_on = False
            presser_play = False
            koff_enable = False
            Atick = 0

    if (presser_off) and (presser_play):
        Atick = Atick + 1
        if (Atick >= 1) and ( Atick < 3):Window.blit(on_pesser2,(677, 660+anim_y_3))
        elif (Atick >= 3) and ( Atick < 5):Window.blit(on_pesser3,(677, 660+anim_y_3))
        elif (Atick >= 5) and ( Atick < 7):Window.blit(on_pesser4,(677, 660+anim_y_3))
        elif (Atick >= 7):

            Window.blit(on_pesser5,(677, 660+anim_y_3))
            
            presser_on = True
            presser_off = False
            presser_play = False
            Atick = 0

    if (presser_on) and not(presser_play): Window.blit(on_pesser5,(677, 660+anim_y_3))
    if (presser_off) and not(presser_play): Window.blit(on_pesser1,(677, 660+anim_y_3))

    if (angle > 9):
        str_angle = str(angle)
        first_num = str_angle[0]
        second_num = str_angle[1]

        if (first_num == "0"): Window.blit(zero,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "1"): Window.blit(one,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "2"): Window.blit(two,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "3"): Window.blit(three,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "4"): Window.blit(four,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "5"): Window.blit(five,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "6"): Window.blit(six,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "7"): Window.blit(seven,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "8"): Window.blit(eight,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "9"): Window.blit(nine,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))

        if (second_num == "0"): Window.blit(zero,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "1"): Window.blit(one,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "2"): Window.blit(two,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "3"): Window.blit(three,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "4"): Window.blit(four,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "5"): Window.blit(five,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "6"): Window.blit(six,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "7"): Window.blit(seven,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "8"): Window.blit(eight,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "9"): Window.blit(nine,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))

    elif (angle <= 9):
        str_angle = str(angle)
        first_num = "0"
        second_num = str_angle[0]

        if (first_num == "0"): Window.blit(zero,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "1"): Window.blit(one,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "2"): Window.blit(two,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "3"): Window.blit(three,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "4"): Window.blit(four,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "5"): Window.blit(five,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "6"): Window.blit(six,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "7"): Window.blit(seven,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "8"): Window.blit(eight,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (first_num == "9"): Window.blit(nine,(first_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))

        if (second_num == "0"): Window.blit(zero,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "1"): Window.blit(one,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "2"): Window.blit(two,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "3"): Window.blit(three,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "4"): Window.blit(four,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "5"): Window.blit(five,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "6"): Window.blit(six,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "7"): Window.blit(seven,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "8"): Window.blit(eight,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))
        elif (second_num == "9"): Window.blit(nine,(second_num_p[0]+anim_x_1,first_num_p[1]+anim_y_1))

    for i in range(90-angle):
        pygame.draw.rect(Window, (255,(int(180-((i*2)))),(int(180-((i*2))))),(21+i*3+anim_x_1, 643+anim_y_1, 3, 56))

    speed_update(speed_word)
    mass_update(mass_word)
    kof_update(kof_word)



    Window.blit(base,(0, 600))

    if masch == 1: Window.blit(sky_background2[bgt],(328, 0))
    if masch == 2: Window.blit(sky_background1[bgt],(328, 0))
    if masch == 4: Window.blit(sky_background[bgt],(328, 0))
    if masch == 8: Window.blit(sky_background3[bgt],(328, 0))

    if draw_parabola:
        draw_lines(Dot_spawn_x,Dot_spawn_y,Dot_count,masch,(0,0,0))
    else:
        for i in range(Dot_count):
            rydpos = 600-Dot_spawn_y[i]
            if (masch >= 8):Window.blit(dot_big,((Dot_spawn_x[i]+105)/masch,(int((600-(rydpos/masch))))))
            elif (masch >= 2) and (masch <= 4):Window.blit(dot_medium,((Dot_spawn_x[i]+105)/masch,(int((600-(rydpos/masch))))))
            else:Window.blit(dot_small,((Dot_spawn_x[i]+105)/masch,(int((600-(rydpos/masch))))))

    if draw_parabola:
        for i in range(8):
            if viev_bool[i]:
                draw_lines((tr_pos_x[i]),(tr_pos_y[i]),tr_count[i],masch,color[color_tr[i]])
    else: 
        for i in range(8):
            if viev_bool[i]:
                for j in range(tr_count[i]):
                    rydpos = 600-tr_pos_y[i][j]
                    if (masch >= 8): w = 1
                    elif (masch >= 2) and (masch <= 4): w = 2
                    else: w = 3

                    X = ((tr_pos_x[i][j]+105)/masch)
                    Y = (int((600-(rydpos/masch))))
                    C = color[color_tr[i]]

                    pygame.draw.rect(Window, C,(X,Y,w,w))


            
    if (simulator_run) or (finish_sim):
        yadd = 0
        if (finish_sim):
            if (600-(ry_pos/masch)) >= 600:
                yadd = int(40/masch)
        if (presser_on):
            kof_word1 = float(kof_word)
            if (kof_word1 >= 0) and (kof_word1 < 0.05):
                ball1_rect = ball1.get_rect(center=(125+x_pos, y_pos+20)) 
                balln, ball1_p = rot_center(ball1, ball1_rect, -animballangle)
                ballns = pygame.transform.scale(balln,(int(40/masch),int(40/masch)))
                Window.blit(ballns,((ball1_p[0])/masch, (600-((600-ball1_p[1])/masch))-yadd))
            elif (kof_word1 >= 0.05) and (kof_word1 < 0.15):
                ball1_rect = ball2.get_rect(center=(125+x_pos, y_pos+20)) 
                balln, ball1_p = rot_center(ball2, ball1_rect, -animballangle)
                ballns = pygame.transform.scale(balln,(int(40/masch),int(40/masch)))
                Window.blit(ballns,((ball1_p[0])/masch, (600-((600-ball1_p[1])/masch))-yadd))
            elif (kof_word1 >= 0.15) and (kof_word1 < 0.25):
                ball1_rect = ball3.get_rect(center=(125+x_pos, y_pos+20)) 
                balln, ball1_p = rot_center(ball3, ball1_rect, -animballangle)
                ballns = pygame.transform.scale(balln,(int(40/masch),int(40/masch)))
                Window.blit(ballns,((ball1_p[0])/masch, (600-((600-ball1_p[1])/masch))-yadd))
            elif (kof_word1 >= 0.25) and (kof_word1 < 0.35):
                ball1_rect = ball4.get_rect(center=(125+x_pos, y_pos+20)) 
                balln, ball1_p = rot_center(ball4, ball1_rect, -animballangle)
                ballns = pygame.transform.scale(balln,(int(40/masch),int(40/masch)))
                Window.blit(ballns,((ball1_p[0])/masch, (600-((600-ball1_p[1])/masch))-yadd))
            elif (kof_word1 >= 0.35) and (kof_word1 < 0.45):
                ball1_rect = ball5.get_rect(center=(125+x_pos, y_pos+20)) 
                balln, ball1_p = rot_center(ball5, ball1_rect, -animballangle)
                ballns = pygame.transform.scale(balln,(int(40/masch),int(40/masch)))
                Window.blit(ballns,((ball1_p[0])/masch, (600-((600-ball1_p[1])/masch))-yadd))
            elif (kof_word1 >= 0.45) and (kof_word1 < 0.55):
                ball1_rect = ball6.get_rect(center=(125+x_pos, y_pos+20)) 
                balln, ball1_p = rot_center(ball6, ball1_rect, -animballangle)
                ballns = pygame.transform.scale(balln,(int(40/masch),int(40/masch)))
                Window.blit(ballns,((ball1_p[0])/masch, (600-((600-ball1_p[1])/masch))-yadd))
            elif (kof_word1 >= 0.55) and (kof_word1 < 0.65):
                ball1_rect = ball7.get_rect(center=(125+x_pos, y_pos+20)) 
                balln, ball1_p = rot_center(ball7, ball1_rect, -animballangle)
                ballns = pygame.transform.scale(balln,(int(40/masch),int(40/masch)))
                Window.blit(ballns,((ball1_p[0])/masch, (600-((600-ball1_p[1])/masch))-yadd))
            elif (kof_word1 >= 0.65) and (kof_word1 < 0.75):
                ball1_rect = ball8.get_rect(center=(125+x_pos, y_pos+20)) 
                balln, ball1_p = rot_center(ball8, ball1_rect, -animballangle)
                ballns = pygame.transform.scale(balln,(int(40/masch),int(40/masch)))
                Window.blit(ballns,((ball1_p[0])/masch, (600-((600-ball1_p[1])/masch))-yadd))
            elif (kof_word1 >= 0.75) and (kof_word1 < 0.85):
                ball1_rect = ball9.get_rect(center=(125+x_pos, y_pos+20)) 
                balln, ball1_p = rot_center(ball9, ball1_rect, -animballangle)
                ballns = pygame.transform.scale(balln,(int(40/masch),int(40/masch)))
                Window.blit(ballns,((ball1_p[0])/masch, (600-((600-ball1_p[1])/masch))-yadd))
            elif (kof_word1 >= 0.85) and (kof_word1 < 0.95):
                ball1_rect = ball10.get_rect(center=(125+x_pos, y_pos+20)) 
                balln, ball1_p = rot_center(ball10, ball1_rect, -animballangle)
                ballns = pygame.transform.scale(balln,(int(40/masch),int(40/masch)))
                Window.blit(ballns,((ball1_p[0])/masch, (600-((600-ball1_p[1])/masch))-yadd))
            elif (kof_word1 >= 0.95):
                ball1_rect = ball11.get_rect(center=(125+x_pos, y_pos+20)) 
                balln, ball1_p = rot_center(ball11, ball1_rect, -animballangle)
                ballns = pygame.transform.scale(balln,(int(40/masch),int(40/masch)))
                Window.blit(ballns,((ball1_p[0])/masch, (600-((600-ball1_p[1])/masch))-yadd))
        else:
            ball6s = pygame.transform.scale(ball6,(int(40/masch),int(40/masch)))
            Window.blit(ball6s,((105+x_pos)/masch, (600-(ry_pos/masch))-yadd))
    
    if (not (simulator_run)) and (finish_sim):
        first_place_taken = False
        if (y_mouse <= 600):
            Window.blit(found_line,(0, y_mouse))
            if (int(pos_save_y[Max_pos]+20) >= (600-((600-y_mouse)*masch))):
                    Window.blit(infotable_highpoint,(1160, 20))
                    
                    pos_viev = ["0"]*5
                        
                    viev_pos_x = str(int(pos_save_x[Max_pos]))
                    n = len(viev_pos_x)
                    if (n == 1):
                        pos_viev[0] = viev_pos_x[0]
                        pos_viev[1] = "0"
                        pos_viev[2] = "0"
                        pos_viev[3] = "0"
                        pos_viev[4] = "0"
                    elif (n == 2):
                        pos_viev[1] = viev_pos_x[0]
                        pos_viev[0] = viev_pos_x[1]
                        pos_viev[2] = "0"
                        pos_viev[3] = "0"
                        pos_viev[4] = "0"
                    elif (n == 3):
                        pos_viev[2] = viev_pos_x[0]
                        pos_viev[1] = viev_pos_x[1]
                        pos_viev[0] = viev_pos_x[2]
                        pos_viev[3] = "0"
                        pos_viev[4] = "0"
                    elif (n == 4):
                        pos_viev[3] = viev_pos_x[0]
                        pos_viev[2] = viev_pos_x[1]
                        pos_viev[1] = viev_pos_x[2]
                        pos_viev[0] = viev_pos_x[3]
                        pos_viev[4] = "0"
                    elif (n == 5):
                        pos_viev[4] = viev_pos_x[0]
                        pos_viev[3] = viev_pos_x[1]
                        pos_viev[2] = viev_pos_x[2]
                        pos_viev[1] = viev_pos_x[3]
                        pos_viev[0] = viev_pos_x[4]

                    for i in range(5):
                        for j in range(10):
                            if (pos_viev[i] == str(j)):
                                if (i == 0): Window.blit(Znumbers[j],(1325, 45))
                                elif (i == 1): Window.blit(Znumbers[j],(1309, 45))
                                elif (i == 2): Window.blit(Znumbers[j],(1297, 45))
                                elif (i == 3): Window.blit(Znumbers[j],(1285, 45))
                                elif (i == 4): Window.blit(Znumbers[j],(1273, 45))

                    pos_viev = ["0"]*6
                        
                    viev_pos_timer = str(int(timer_save[Max_pos]*1000))
                    n = len(viev_pos_timer)
                    if (n == 1):
                        pos_viev[5] = viev_pos_timer[0]
                        pos_viev[4] = "0"
                        pos_viev[3] = "0"
                        pos_viev[2] = "0"
                        pos_viev[1] = "0"
                        pos_viev[0] = "0"
                    elif (n == 2):
                        pos_viev[4] = viev_pos_timer[0]
                        pos_viev[5] = viev_pos_timer[1]
                        pos_viev[3] = "0"
                        pos_viev[2] = "0"
                        pos_viev[1] = "0"
                        pos_viev[0] = "0"
                    elif (n == 3):
                        pos_viev[3] = viev_pos_timer[0]
                        pos_viev[4] = viev_pos_timer[1]
                        pos_viev[5] = viev_pos_timer[2]
                        pos_viev[2] = "0"
                        pos_viev[1] = "0"
                        pos_viev[0] = "0"
                    elif (n == 4):
                        pos_viev[2] = viev_pos_timer[0]
                        pos_viev[3] = viev_pos_timer[1]
                        pos_viev[4] = viev_pos_timer[2]
                        pos_viev[5] = viev_pos_timer[3]
                        pos_viev[1] = "0"
                        pos_viev[0] = "0"
                    elif (n == 5):
                        pos_viev[1] = viev_pos_timer[0]
                        pos_viev[2] = viev_pos_timer[1]
                        pos_viev[3] = viev_pos_timer[2]
                        pos_viev[4] = viev_pos_timer[3]
                        pos_viev[5] = viev_pos_timer[4]
                        pos_viev[0] = "0"
                    elif (n == 6):
                        pos_viev[0] = viev_pos_timer[0]
                        pos_viev[1] = viev_pos_timer[1]
                        pos_viev[2] = viev_pos_timer[2]
                        pos_viev[3] = viev_pos_timer[3]
                        pos_viev[4] = viev_pos_timer[4]
                        pos_viev[5] = viev_pos_timer[5]

                    for i in range(6):
                        for j in range(10):
                            if (pos_viev[i] == str(j)):
                                if (i == 0): Window.blit(Znumbers[j],(1257, 89))
                                elif (i == 1): Window.blit(Znumbers[j],(1269, 89))
                                elif (i == 2): Window.blit(Znumbers[j],(1281, 89))
                                elif (i == 3): Window.blit(Znumbers[j],(1297, 89))
                                elif (i == 4): Window.blit(Znumbers[j],(1309, 89))
                                elif (i == 5): Window.blit(Znumbers[j],(1321, 89))


                    pos_viev = ["0"]*5
                        
                    viev_pos_y = str(int(810-(pos_save_y[Max_pos]+250)))
                    n = len(viev_pos_y)
                    if (n == 1):
                        pos_viev[0] = viev_pos_y[0]
                        pos_viev[1] = "0"
                        pos_viev[2] = "0"
                        pos_viev[3] = "0"
                        pos_viev[4] = "0"
                    elif (n == 2):
                        pos_viev[1] = viev_pos_y[0]
                        pos_viev[0] = viev_pos_y[1]
                        pos_viev[2] = "0"
                        pos_viev[3] = "0"
                        pos_viev[4] = "0"
                    elif (n == 3):
                        pos_viev[2] = viev_pos_y[0]
                        pos_viev[1] = viev_pos_y[1]
                        pos_viev[0] = viev_pos_y[2]
                        pos_viev[3] = "0"
                        pos_viev[4] = "0"
                    elif (n == 4):
                        pos_viev[3] = viev_pos_y[0]
                        pos_viev[2] = viev_pos_y[1]
                        pos_viev[1] = viev_pos_y[2]
                        pos_viev[0] = viev_pos_y[3]
                        pos_viev[4] = "0"
                    elif (n == 5):
                        pos_viev[4] = viev_pos_y[0]
                        pos_viev[3] = viev_pos_y[1]
                        pos_viev[2] = viev_pos_y[2]
                        pos_viev[1] = viev_pos_y[3]
                        pos_viev[0] = viev_pos_y[4]
                            
                    for i in range(5):
                        for j in range(10):
                            if (pos_viev[i] == str(j)):
                                if (i == 0): Window.blit(Znumbers[j],(1325, 25))
                                elif (i == 1): Window.blit(Znumbers[j],(1309, 25))
                                elif (i == 2): Window.blit(Znumbers[j],(1297, 25))
                                elif (i == 3): Window.blit(Znumbers[j],(1285, 25))
                                elif (i == 4): Window.blit(Znumbers[j],(1273, 25))

            else:
                    for k in range(0,Max_pos):
                        if (pos_save_y[k]+20 >= (600-((600-y_mouse)*masch))) and ((600-((600-y_mouse)*masch)) > pos_save_y[Max_pos]+20):
                            first_place_taken = True
                            S = k
                            Window.blit(infotable_up,(1160, 20))

                            pos_viev = ["0"]*5
                            
                            viev_pos_x = str(int(pos_save_x[S]))
                            n = len(viev_pos_x)
                            if (n == 1):
                                pos_viev[0] = viev_pos_x[0]
                                pos_viev[1] = "0"
                                pos_viev[2] = "0"
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 2):
                                pos_viev[1] = viev_pos_x[0]
                                pos_viev[0] = viev_pos_x[1]
                                pos_viev[2] = "0"
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 3):
                                pos_viev[2] = viev_pos_x[0]
                                pos_viev[1] = viev_pos_x[1]
                                pos_viev[0] = viev_pos_x[2]
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 4):
                                pos_viev[3] = viev_pos_x[0]
                                pos_viev[2] = viev_pos_x[1]
                                pos_viev[1] = viev_pos_x[2]
                                pos_viev[0] = viev_pos_x[3]
                                pos_viev[4] = "0"
                            elif (n == 5):
                                pos_viev[4] = viev_pos_x[0]
                                pos_viev[3] = viev_pos_x[1]
                                pos_viev[2] = viev_pos_x[2]
                                pos_viev[1] = viev_pos_x[3]
                                pos_viev[0] = viev_pos_x[4]

                            for i in range(5):
                                for j in range(10):
                                    if (pos_viev[i] == str(j)):
                                        if (i == 0): Window.blit(Znumbers[j],(1325, 45))
                                        elif (i == 1): Window.blit(Znumbers[j],(1309, 45))
                                        elif (i == 2): Window.blit(Znumbers[j],(1297, 45))
                                        elif (i == 3): Window.blit(Znumbers[j],(1285, 45))
                                        elif (i == 4): Window.blit(Znumbers[j],(1273, 45))

                            pos_viev = ["0"]*6
                            
                            viev_pos_timer = str(int(timer_save[S]*1000))
                            n = len(viev_pos_timer)
                            if (n == 1):
                                pos_viev[5] = viev_pos_timer[0]
                                pos_viev[4] = "0"
                                pos_viev[3] = "0"
                                pos_viev[2] = "0"
                                pos_viev[1] = "0"
                                pos_viev[0] = "0"
                            elif (n == 2):
                                pos_viev[4] = viev_pos_timer[0]
                                pos_viev[5] = viev_pos_timer[1]
                                pos_viev[3] = "0"
                                pos_viev[2] = "0"
                                pos_viev[1] = "0"
                                pos_viev[0] = "0"
                            elif (n == 3):
                                pos_viev[3] = viev_pos_timer[0]
                                pos_viev[4] = viev_pos_timer[1]
                                pos_viev[5] = viev_pos_timer[2]
                                pos_viev[2] = "0"
                                pos_viev[1] = "0"
                                pos_viev[0] = "0"
                            elif (n == 4):
                                pos_viev[2] = viev_pos_timer[0]
                                pos_viev[3] = viev_pos_timer[1]
                                pos_viev[4] = viev_pos_timer[2]
                                pos_viev[5] = viev_pos_timer[3]
                                pos_viev[1] = "0"
                                pos_viev[0] = "0"
                            elif (n == 5):
                                pos_viev[1] = viev_pos_timer[0]
                                pos_viev[2] = viev_pos_timer[1]
                                pos_viev[3] = viev_pos_timer[2]
                                pos_viev[4] = viev_pos_timer[3]
                                pos_viev[5] = viev_pos_timer[4]
                                pos_viev[0] = "0"
                            elif (n == 6):
                                pos_viev[0] = viev_pos_timer[0]
                                pos_viev[1] = viev_pos_timer[1]
                                pos_viev[2] = viev_pos_timer[2]
                                pos_viev[3] = viev_pos_timer[3]
                                pos_viev[4] = viev_pos_timer[4]
                                pos_viev[5] = viev_pos_timer[5]

                            for i in range(6):
                                for j in range(10):
                                    if (pos_viev[i] == str(j)):
                                        if (i == 0): Window.blit(Znumbers[j],(1257, 89))
                                        elif (i == 1): Window.blit(Znumbers[j],(1269, 89))
                                        elif (i == 2): Window.blit(Znumbers[j],(1281, 89))
                                        elif (i == 3): Window.blit(Znumbers[j],(1297, 89))
                                        elif (i == 4): Window.blit(Znumbers[j],(1309, 89))
                                        elif (i == 5): Window.blit(Znumbers[j],(1321, 89))

                                        

                            pos_viev = ["0"]*5
                            
                            viev_pos_y = str(int(810-(pos_save_y[S]+250)))
                            n = len(viev_pos_y)
                            if (n == 1):
                                pos_viev[0] = viev_pos_y[0]
                                pos_viev[1] = "0"
                                pos_viev[2] = "0"
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 2):
                                pos_viev[1] = viev_pos_y[0]
                                pos_viev[0] = viev_pos_y[1]
                                pos_viev[2] = "0"
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 3):
                                pos_viev[2] = viev_pos_y[0]
                                pos_viev[1] = viev_pos_y[1]
                                pos_viev[0] = viev_pos_y[2]
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 4):
                                pos_viev[3] = viev_pos_y[0]
                                pos_viev[2] = viev_pos_y[1]
                                pos_viev[1] = viev_pos_y[2]
                                pos_viev[0] = viev_pos_y[3]
                                pos_viev[4] = "0"
                            elif (n == 5):
                                pos_viev[4] = viev_pos_y[0]
                                pos_viev[3] = viev_pos_y[1]
                                pos_viev[2] = viev_pos_y[2]
                                pos_viev[1] = viev_pos_y[3]
                                pos_viev[0] = viev_pos_y[4]
                                
                            for i in range(5):
                                for j in range(10):
                                    if (pos_viev[i] == str(j)):
                                        if (i == 0): Window.blit(Znumbers[j],(1325, 25))
                                        elif (i == 1): Window.blit(Znumbers[j],(1309, 25))
                                        elif (i == 2): Window.blit(Znumbers[j],(1297, 25))
                                        elif (i == 3): Window.blit(Znumbers[j],(1285, 25))
                                        elif (i == 4): Window.blit(Znumbers[j],(1273, 25))

                    for k in range(tick,Max_pos,-1):
                        if (pos_save_y[k]+20 >= (600-((600-y_mouse)*masch))) and ((600-((600-y_mouse)*masch)) <= 580) and (pos_save_y[Max_pos]+20 < (600-((600-y_mouse)*masch))):
                            S = k
                            if not (first_place_taken): FPT = 120
                            else: FPT = 0
                            Window.blit(infotable_down,(1160, 140-FPT))
                            
                            pos_viev = ["0"]*5
                            
                            viev_pos_x = str(int(pos_save_x[S]))
                            n = len(viev_pos_x)
                            if (n == 1):
                                pos_viev[0] = viev_pos_x[0]
                                pos_viev[1] = "0"
                                pos_viev[2] = "0"
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 2):
                                pos_viev[1] = viev_pos_x[0]
                                pos_viev[0] = viev_pos_x[1]
                                pos_viev[2] = "0"
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 3):
                                pos_viev[2] = viev_pos_x[0]
                                pos_viev[1] = viev_pos_x[1]
                                pos_viev[0] = viev_pos_x[2]
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 4):
                                pos_viev[3] = viev_pos_x[0]
                                pos_viev[2] = viev_pos_x[1]
                                pos_viev[1] = viev_pos_x[2]
                                pos_viev[0] = viev_pos_x[3]
                                pos_viev[4] = "0"
                            elif (n == 5):
                                pos_viev[4] = viev_pos_x[0]
                                pos_viev[3] = viev_pos_x[1]
                                pos_viev[2] = viev_pos_x[2]
                                pos_viev[1] = viev_pos_x[3]
                                pos_viev[0] = viev_pos_x[4]

                            for i in range(5):
                                for j in range(10):
                                    if (pos_viev[i] == str(j)):
                                        if (i == 0): Window.blit(Znumbers[j],(1325, 165-FPT))
                                        elif (i == 1): Window.blit(Znumbers[j],(1309, 165-FPT))
                                        elif (i == 2): Window.blit(Znumbers[j],(1297, 165-FPT))
                                        elif (i == 3): Window.blit(Znumbers[j],(1285, 165-FPT))
                                        elif (i == 4): Window.blit(Znumbers[j],(1273, 165-FPT))

                            pos_viev = ["0"]*6
                            
                            viev_pos_timer = str(int(timer_save[S]*1000))
                            n = len(viev_pos_timer)
                            if (n == 1):
                                pos_viev[5] = viev_pos_timer[0]
                                pos_viev[4] = "0"
                                pos_viev[3] = "0"
                                pos_viev[2] = "0"
                                pos_viev[1] = "0"
                                pos_viev[0] = "0"
                            elif (n == 2):
                                pos_viev[4] = viev_pos_timer[0]
                                pos_viev[5] = viev_pos_timer[1]
                                pos_viev[3] = "0"
                                pos_viev[2] = "0"
                                pos_viev[1] = "0"
                                pos_viev[0] = "0"
                            elif (n == 3):
                                pos_viev[3] = viev_pos_timer[0]
                                pos_viev[4] = viev_pos_timer[1]
                                pos_viev[5] = viev_pos_timer[2]
                                pos_viev[2] = "0"
                                pos_viev[1] = "0"
                                pos_viev[0] = "0"
                            elif (n == 4):
                                pos_viev[2] = viev_pos_timer[0]
                                pos_viev[3] = viev_pos_timer[1]
                                pos_viev[4] = viev_pos_timer[2]
                                pos_viev[5] = viev_pos_timer[3]
                                pos_viev[1] = "0"
                                pos_viev[0] = "0"
                            elif (n == 5):
                                pos_viev[1] = viev_pos_timer[0]
                                pos_viev[2] = viev_pos_timer[1]
                                pos_viev[3] = viev_pos_timer[2]
                                pos_viev[4] = viev_pos_timer[3]
                                pos_viev[5] = viev_pos_timer[4]
                                pos_viev[0] = "0"
                            elif (n == 6):
                                pos_viev[0] = viev_pos_timer[0]
                                pos_viev[1] = viev_pos_timer[1]
                                pos_viev[2] = viev_pos_timer[2]
                                pos_viev[3] = viev_pos_timer[3]
                                pos_viev[4] = viev_pos_timer[4]
                                pos_viev[5] = viev_pos_timer[5]

                            for i in range(6):
                                for j in range(10):
                                    if (pos_viev[i] == str(j)):
                                        if (i == 0): Window.blit(Znumbers[j],(1257, 209-FPT))
                                        elif (i == 1): Window.blit(Znumbers[j],(1269, 209-FPT))
                                        elif (i == 2): Window.blit(Znumbers[j],(1281, 209-FPT))
                                        elif (i == 3): Window.blit(Znumbers[j],(1297, 209-FPT))
                                        elif (i == 4): Window.blit(Znumbers[j],(1309, 209-FPT))
                                        elif (i == 5): Window.blit(Znumbers[j],(1321, 209-FPT))

                            pos_viev = ["0"]*5
                  
                            viev_pos_y = str(int(810-(pos_save_y[S]+250)))
                            n = len(viev_pos_y)
                            if (n == 1):
                                pos_viev[0] = viev_pos_y[0]
                                pos_viev[1] = "0"
                                pos_viev[2] = "0"
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 2):
                                pos_viev[1] = viev_pos_y[0]
                                pos_viev[0] = viev_pos_y[1]
                                pos_viev[2] = "0"
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 3):
                                pos_viev[2] = viev_pos_y[0]
                                pos_viev[1] = viev_pos_y[1]
                                pos_viev[0] = viev_pos_y[2]
                                pos_viev[3] = "0"
                                pos_viev[4] = "0"
                            elif (n == 4):
                                pos_viev[3] = viev_pos_y[0]
                                pos_viev[2] = viev_pos_y[1]
                                pos_viev[1] = viev_pos_y[2]
                                pos_viev[0] = viev_pos_y[3]
                                pos_viev[4] = "0"
                            elif (n == 5):
                                pos_viev[4] = viev_pos_y[0]
                                pos_viev[3] = viev_pos_y[1]
                                pos_viev[2] = viev_pos_y[2]
                                pos_viev[1] = viev_pos_y[3]
                                pos_viev[0] = viev_pos_y[4]
                                
                            for i in range(5):
                                for j in range(10):
                                    if (pos_viev[i] == str(j)):
                                        if (i == 0): Window.blit(Znumbers[j],(1325, 145-FPT))
                                        elif (i == 1): Window.blit(Znumbers[j],(1309, 145-FPT))
                                        elif (i == 2): Window.blit(Znumbers[j],(1297, 145-FPT))
                                        elif (i == 3): Window.blit(Znumbers[j],(1285, 145-FPT))
                                        elif (i == 4): Window.blit(Znumbers[j],(1273, 145-FPT))
                            
    Window.blit(showside_push_base, (1207,718))
    if (Btick == 1): Window.blit(showside_push_diod7, (1222,754))
    elif (Btick != 0):
        if (Btick <= 2): Window.blit(showside_push_diod1, (1222,754))
        elif (Btick <= 4): Window.blit(showside_push_diod2, (1222,754))
        elif (Btick <= 6): Window.blit(showside_push_diod3, (1222,754))
        elif (Btick <= 8): Window.blit(showside_push_diod4, (1222,754))
        elif (Btick <= 10): Window.blit(showside_push_diod5, (1222,754))
        elif (Btick >= 11): Window.blit(showside_push_diod6, (1222,754))
    
    if(Btick >= 11):
        for i in range(Btick - 11):
            pygame.draw.rect(Window, (int(6.9*(i)),127,int(6.9*(36-i))),(1217+i, 775, 1, 10))
        
    if (sideshow_bool) and (not(showsize_tugger_pos == 0)): Window.blit(showside_push_lamp2, (1258,773))
    else: Window.blit(showside_push_lamp1, (1258,773))
        
    if (showsize_tugger_pos <= 20):
        showside_push_tuggerfill2 = pygame.transform.scale(showside_push_tuggerfill,(50,int(showsize_tugger_possize*0.8)))
        Window.blit(showside_push_tuggerfill2, (1218,750-showsize_tugger_possize-(2-showsize_tugger_possize*0.125)))
        Window.blit(showside_push_base_tuggerbase1, (1215,745))
    else:
        showside_push_tuggerfill2 = pygame.transform.scale(showside_push_tuggerfill,(50,int(-showsize_tugger_possize*0.8)))
        Window.blit(showside_push_tuggerfill2, (1218,747))
        Window.blit(showside_push_base_tuggerbase2, (1215,745))
    
    Window.blit(showside_push_tugger, (1213,723+showsize_tugger_pos))
    
    Window.blit(numpad_base,(723, 611))
    Window.blit(decor1,(723, 771))
    Window.blit(decor3,(1279,755))

    if book_bool:   Window.blit(instr2,(823, 611))
    else:   Window.blit(instr1,(823, 611))

    Window.blit(printmachine_part1,(951, 611))

    for i in range (16):
        if (infoprint_status[infoprint_numtaken[15-i]] != "printed") and (infoprint_status[infoprint_numtaken[15-i]] != "printing"):
            Window.blit(infoprint[infoprint_numtaken[15-i]],(infoprint_pos_x[infoprint_numtaken[15-i]], infoprint_pos_y[infoprint_numtaken[15-i]]))

    for i in range (16):
        if (infoprint_status[infoprint_numtaken[15-i]] == "printing"):
            Window.blit(infoprint[infoprint_numtaken[15-i]],(infoprint_pos_x[infoprint_numtaken[15-i]], infoprint_pos_y[infoprint_numtaken[15-i]]))
            print_IP_number(str(IP_speed[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+29)
            print_IP_number(str(IP_angle[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+39)
            print_IP_number(str(IP_height[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+49)
            print_IP_number(str(IP_mass[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+59)
            print_IP_number(str(IP_koff[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+69)
            print_IP_number(str(IP_max[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+99)
            print_IP_number(str(IP_dis[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+109)
            print_IP_number(str(IP_time_all[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+129)
            print_IP_number(str(IP_time_DMV[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+139)
            print_IP_number(str(IP_time_PMV[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+149)
            print_IP_tr(IP_tr_x[infoprint_numtaken[15-i]],IP_tr_y[infoprint_numtaken[15-i]],IP_count[infoprint_numtaken[15-i]],infoprint_pos_x[infoprint_numtaken[15-i]]+10,infoprint_pos_y[infoprint_numtaken[15-i]]+205,IP_masch[infoprint_numtaken[15-i]])
            print_IP_number(str(IP_masch[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+11,infoprint_pos_y[infoprint_numtaken[15-i]]+206)
            print_IP_number(str(IP_dis_all[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+169)
            print_IP_number(str(IP_dis_DMV[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+179)
            print_IP_number(str(IP_dis_PMV[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+189)
    
    Window.blit(printmachine_part2,(951, 634))
    Window.blit(printmachine_close,(951, 651))

    Window.blit(printmachine_lamp_base,(1091, 661))

    if ("printing" in infoprint_status):
        Window.blit(printmachine_lamp_red2,(1098, 661))
        Window.blit(printmachine_lamp_green1,(1098, 683))
    else:
        if not(haveprinted) and (finish_sim) and (haveused < 15):
            Window.blit(printmachine_lamp_red1,(1098, 661))
            Window.blit(printmachine_lamp_green2,(1098, 683))
        else:
            Window.blit(printmachine_lamp_red2,(1098, 661))
            Window.blit(printmachine_lamp_green1,(1098, 683))

    Window.blit(sprmasch_base,(951, 661))
    if masch == 1: Window.blit(sprmasch_watch,(961, 668))
    elif masch == 2: Window.blit(sprmasch_watch,(975, 668))
    elif masch == 4: Window.blit(sprmasch_watch,(989, 668))
    elif masch == 8: Window.blit(sprmasch_watch,(1003, 668))
    elif masch == 16: Window.blit(sprmasch_watch,(1017, 668))

    if masch_avto_bool: Window.blit(sprmasch_arrow,(960+int(69*masch_procent), 693))
    else: Window.blit(sprmasch_arrow,(masch_avto_curr, 693))

    if (masch_avto_anim):
        if masch_avto_bool:
            Ktick += 1
            if Ktick  >= 4:
                Ktick = 4
                masch_avto_anim = False
                masch_avto_bool = False
                masch_avto_curr = 960+int(69*masch_procent)
        else:
            Ktick -= 1
            if Ktick  <= 0:
                Ktick = 0
                masch_avto_anim = False
                masch_avto_bool = True
                m1 = False
                m2 = False
                m4 = False
                m8 = False
                m16 = False

    Window.blit(ticker[Ktick],(1067, 668))
    
    if (speed_enabled): Window.blit(numpad_speed,(734, 622))
    if (mass_enabled): Window.blit(numpad_mass,(734, 622))
    if (koff_enable): Window.blit(numpad_wind,(734, 622))

    for i in range (16):
        if (infoprint_status[i] == "printing"):
            Atick_printmachine = Atick_printmachine + 1
            if (Atick_printmachine >= 0) and ( Atick_printmachine < 1): infoprint_pos_y[i] = 614
            elif (Atick_printmachine >= 1) and ( Atick_printmachine < 2): infoprint_pos_y[i] = 604
            elif (Atick_printmachine >= 2) and ( Atick_printmachine < 3): infoprint_pos_y[i] = 594
            elif (Atick_printmachine >= 3) and ( Atick_printmachine < 4): infoprint_pos_y[i] = 584
            elif (Atick_printmachine >= 4) and ( Atick_printmachine < 5): infoprint_pos_y[i] = 574
            elif (Atick_printmachine >= 5) and ( Atick_printmachine < 6): infoprint_pos_y[i] = 564
            elif (Atick_printmachine >= 6) and ( Atick_printmachine < 7): infoprint_pos_y[i] = 554
            elif (Atick_printmachine >= 7) and ( Atick_printmachine < 8): infoprint_pos_y[i] = 544
            elif (Atick_printmachine >= 8) and ( Atick_printmachine < 9): infoprint_pos_y[i] = 534
            elif (Atick_printmachine >= 9) and ( Atick_printmachine < 10): infoprint_pos_y[i] = 524
            elif (Atick_printmachine >= 10) and ( Atick_printmachine < 11): infoprint_pos_y[i] = 514
            elif (Atick_printmachine >= 11) and ( Atick_printmachine < 12): infoprint_pos_y[i] = 504
            elif (Atick_printmachine >= 12) and ( Atick_printmachine < 13): infoprint_pos_y[i] = 494
            elif (Atick_printmachine >= 13) and ( Atick_printmachine < 14): infoprint_pos_y[i] = 484
            elif (Atick_printmachine >= 14) and ( Atick_printmachine < 15): infoprint_pos_y[i] = 474
            elif (Atick_printmachine >= 15) and ( Atick_printmachine < 16): infoprint_pos_y[i] = 464
            elif (Atick_printmachine >= 16) and ( Atick_printmachine < 17): infoprint_pos_y[i] = 454
            elif (Atick_printmachine >= 17) and ( Atick_printmachine < 18): infoprint_pos_y[i] = 444
            elif (Atick_printmachine >= 18) and ( Atick_printmachine < 19): infoprint_pos_y[i] = 434
            elif (Atick_printmachine >= 19) and ( Atick_printmachine < 20): infoprint_pos_y[i] = 424
            elif (Atick_printmachine >= 20) and ( Atick_printmachine < 21): infoprint_pos_y[i] = 414
            elif (Atick_printmachine >= 21) and ( Atick_printmachine < 22): infoprint_pos_y[i] = 404
            elif (Atick_printmachine >= 22) and ( Atick_printmachine < 23): infoprint_pos_y[i] = 394
            elif (Atick_printmachine >= 23) and ( Atick_printmachine < 24): infoprint_pos_y[i] = 384
            elif (Atick_printmachine >= 24) and ( Atick_printmachine < 25): infoprint_pos_y[i] = 374
            elif (Atick_printmachine >= 25) and ( Atick_printmachine < 26): infoprint_pos_y[i] = 364
            elif (Atick_printmachine >= 26) and ( Atick_printmachine < 27): infoprint_pos_y[i] = 354
            elif (Atick_printmachine >= 27) and ( Atick_printmachine < 28): infoprint_pos_y[i] = 344
            elif (Atick_printmachine >= 28) and ( Atick_printmachine < 29): infoprint_pos_y[i] = 334
            elif (Atick_printmachine >= 29) and ( Atick_printmachine < 30): infoprint_pos_y[i] = 324
            elif (Atick_printmachine >= 30) and ( Atick_printmachine < 31): infoprint_pos_y[i] = 314
            elif (Atick_printmachine >= 31):

                infoprint_status[i] = "printed"
                Atick_printmachine = 0
        
    if not(repeat_button_rise_play or repeat_button_set_play):
        if (repeat_button_up): Window.blit(repeat_button[17],(1201, 611))
        else: Window.blit(repeat_button[0],(1201, 611))

    if (repeat_button_rise_play):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 1):Window.blit(repeat_button[0],(1201, 611))
        elif (Atick >= 1) and ( Atick < 2):Window.blit(repeat_button[1],(1201, 611))
        elif (Atick >= 2) and ( Atick < 3):Window.blit(repeat_button[2],(1201, 611))
        elif (Atick >= 3) and ( Atick < 4):Window.blit(repeat_button[3],(1201, 611))
        elif (Atick >= 4) and ( Atick < 5):Window.blit(repeat_button[4],(1201, 611))
        elif (Atick >= 5) and ( Atick < 6):Window.blit(repeat_button[5],(1201, 611))
        elif (Atick >= 6) and ( Atick < 7):Window.blit(repeat_button[6],(1201, 611))
        elif (Atick >= 7) and ( Atick < 8):Window.blit(repeat_button[7],(1201, 611))
        elif (Atick >= 8) and ( Atick < 9):Window.blit(repeat_button[8],(1201, 611))
        elif (Atick >= 9) and ( Atick < 10):Window.blit(repeat_button[9],(1201, 611))
        elif (Atick >= 10) and ( Atick < 11):Window.blit(repeat_button[10],(1201, 611))
        elif (Atick >= 11) and ( Atick < 12):Window.blit(repeat_button[11],(1201, 611))
        elif (Atick >= 12) and ( Atick < 13):Window.blit(repeat_button[12],(1201, 611))
        elif (Atick >= 13) and ( Atick < 14):Window.blit(repeat_button[13],(1201, 611))
        elif (Atick >= 14) and ( Atick < 15):Window.blit(repeat_button[14],(1201, 611))
        elif (Atick >= 15) and ( Atick < 16):Window.blit(repeat_button[15],(1201, 611))
        elif (Atick >= 16) and ( Atick < 17):Window.blit(repeat_button[16],(1201, 611))
        elif (Atick >= 17) and ( Atick < 18):Window.blit(repeat_button[17],(1201, 611))
        elif (Atick >= 18):

            Window.blit(repeat_button[17],(1201, 611))
            repeat_button_up = True
            repeat_button_rise_play = False
            Atick = 0

    if (repeat_button_set_play):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 1):Window.blit(repeat_button[17],(1201, 611))
        elif (Atick >= 1) and ( Atick < 2):Window.blit(repeat_button[16],(1201, 611))
        elif (Atick >= 2) and ( Atick < 3):Window.blit(repeat_button[15],(1201, 611))
        elif (Atick >= 3) and ( Atick < 4):Window.blit(repeat_button[14],(1201, 611))
        elif (Atick >= 4) and ( Atick < 5):Window.blit(repeat_button[13],(1201, 611))
        elif (Atick >= 5) and ( Atick < 6):Window.blit(repeat_button[12],(1201, 611))
        elif (Atick >= 6) and ( Atick < 7):Window.blit(repeat_button[11],(1201, 611))
        elif (Atick >= 7) and ( Atick < 8):Window.blit(repeat_button[10],(1201, 611))
        elif (Atick >= 8) and ( Atick < 9):Window.blit(repeat_button[9],(1201, 611))
        elif (Atick >= 9) and ( Atick < 10):Window.blit(repeat_button[8],(1201, 611))
        elif (Atick >= 10) and ( Atick < 11):Window.blit(repeat_button[7],(1201, 611))
        elif (Atick >= 11) and ( Atick < 12):Window.blit(repeat_button[6],(1201, 611))
        elif (Atick >= 12) and ( Atick < 13):Window.blit(repeat_button[5],(1201, 611))
        elif (Atick >= 13) and ( Atick < 14):Window.blit(repeat_button[4],(1201, 611))
        elif (Atick >= 14) and ( Atick < 15):Window.blit(repeat_button[3],(1201, 611))
        elif (Atick >= 15) and ( Atick < 16):Window.blit(repeat_button[2],(1201, 611))
        elif (Atick >= 16) and ( Atick < 17):Window.blit(repeat_button[1],(1201, 611))
        elif (Atick >= 17) and ( Atick < 18):Window.blit(repeat_button[0],(1201, 611))
        elif (Atick >= 18):

            Window.blit(repeat_button[0],(1201, 611))
            repeat_button_up = False
            repeat_button_set_play = False
            Atick = 0
        
    if (start_button_play):
        Stick = Stick + 1
        if (Stick >= 0) and ( Stick < 1):Window.blit(start_button[11],(1301, 611))
        elif (Stick >= 1) and ( Stick < 2):Window.blit(start_button[9],(1301, 611))
        elif (Stick >= 2) and ( Stick < 3):Window.blit(start_button[7],(1301, 611))
        elif (Stick >= 3) and ( Stick < 4):Window.blit(start_button[5],(1301, 611))
        elif (Stick >= 4) and ( Stick < 5):Window.blit(start_button[3],(1301, 611))
        elif (Stick >= 5) and ( Stick < 6):Window.blit(start_button[1],(1301, 611))
        elif (Stick >= 6) and ( Stick < 7):Window.blit(start_button[0],(1301, 611))
        elif (Stick >= 7) and ( Stick < 8):Window.blit(start_button[1],(1301, 611))
        elif (Stick >= 8) and ( Stick < 9):Window.blit(start_button[3],(1301, 611))
        elif (Stick >= 9) and ( Stick < 10):Window.blit(start_button[5],(1301, 611))
        elif (Stick >= 10) and ( Stick < 11):Window.blit(start_button[7],(1301, 611))
        elif (Stick >= 11) and ( Stick < 12):Window.blit(start_button[9],(1301, 611))
        elif (Stick >= 12):

            Window.blit(start_button[11],(1301, 611))
            
            start_button_play = False
            Stick = 0
            
    else: Window.blit(start_button[11],(1301, 611))

    if (print_button_play):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(print_button[1],(1127, 641))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(print_button[2],(1127, 641))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(print_button[3],(1127, 641))
        elif (Atick >= 6) and ( Atick < 8):Window.blit(print_button[2],(1127, 641))
        elif (Atick >= 8) and ( Atick < 10):Window.blit(print_button[1],(1127, 641))
        elif (Atick >= 10):

            Window.blit(print_button[0],(1127, 641))
            print_button_play = False
            Atick = 0
            
    else: Window.blit(print_button[0],(1127, 641))

    if (abort_button_status == "rise") and (abt < 5):
        abt += 1
    if (abort_button_status == "down") and (abt > 0):
        abt -= 1
    if (abort_button_status != "off") and (abt == 0):
        abort_button_status = "off"
    if (abort_button_status != "set") and (abt == 5):
        abort_button_status = "set" 
    
    Window.blit(abort_button_base[abt],(1116, 740))

    if (numbutton_bool[0]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_1[1],(736, 655))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_1[2],(736, 655))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_1[1],(736, 655))
        elif (Atick >= 6):

            Window.blit(numbutton_1[1],(736, 655))
            numbutton_bool[0] = False
            Atick = 0
            
    else: Window.blit(numbutton_1[0],(736, 655))

    if (numbutton_bool[1]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_2[1],(761, 655))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_2[2],(761, 655))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_2[1],(761, 655))
        elif (Atick >= 6):

            Window.blit(numbutton_2[1],(761, 655))
            numbutton_bool[1] = False
            Atick = 0
            
    else: Window.blit(numbutton_2[0],(761, 655))

    if (numbutton_bool[2]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_3[1],(786, 655))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_3[2],(786, 655))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_3[1],(786, 655))
        elif (Atick >= 6):

            Window.blit(numbutton_3[1],(786, 655))
            numbutton_bool[2] = False
            Atick = 0
            
    else: Window.blit(numbutton_3[0],(786, 655))
    
    if (numbutton_bool[3]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_4[1],(736, 680))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_4[2],(736, 680))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_4[1],(736, 680))
        elif (Atick >= 6):

            Window.blit(numbutton_4[1],(736, 680))
            numbutton_bool[3] = False
            Atick = 0
            
    else: Window.blit(numbutton_4[0],(736, 680))

    if (numbutton_bool[4]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_5[1],(761, 680))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_5[2],(761, 680))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_5[1],(761, 680))
        elif (Atick >= 6):

            Window.blit(numbutton_5[1],(761, 680))
            numbutton_bool[4] = False
            Atick = 0
            
    else: Window.blit(numbutton_5[0],(761, 680))

    if (numbutton_bool[5]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_6[1],(786, 680))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_6[2],(786, 680))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_6[1],(786, 680))
        elif (Atick >= 6):

            Window.blit(numbutton_6[1],(786, 680))
            numbutton_bool[5] = False
            Atick = 0
            
    else: Window.blit(numbutton_6[0],(786, 680))

    if (numbutton_bool[6]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_7[1],(736, 705))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_7[2],(736, 705))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_7[1],(736, 705))
        elif (Atick >= 6):

            Window.blit(numbutton_7[1],(736, 705))
            numbutton_bool[6] = False
            Atick = 0
            
    else: Window.blit(numbutton_7[0],(736, 705))

    if (numbutton_bool[7]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_8[1],(761, 705))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_8[2],(761, 705))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_8[1],(761, 705))
        elif (Atick >= 6):

            Window.blit(numbutton_8[1],(761, 705))
            numbutton_bool[7] = False
            Atick = 0
            
    else: Window.blit(numbutton_8[0],(761, 705))

    if (numbutton_bool[8]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_9[1],(786, 705))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_9[2],(786, 705))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_9[1],(786, 705))
        elif (Atick >= 6):

            Window.blit(numbutton_9[1],(786, 705))
            numbutton_bool[8] = False
            Atick = 0
            
    else: Window.blit(numbutton_9[0],(786, 705))
    
    if (numbutton_bool[9]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_b[1],(736, 730))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_b[2],(736, 730))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_b[1],(736, 730))
        elif (Atick >= 6):

            Window.blit(numbutton_b[1],(736, 730))
            numbutton_bool[9] = False
            Atick = 0
            
    else: Window.blit(numbutton_b[0],(736, 730))

    if (numbutton_bool[10]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_0[1],(761, 730))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_0[2],(761, 730))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_0[2],(761, 730))
        elif (Atick >= 6):

            Window.blit(numbutton_0[2],(761, 730))
            numbutton_bool[10] = False
            Atick = 0
            
    else: Window.blit(numbutton_0[0],(761, 730))

    if (numbutton_bool[11]):
        Atick = Atick + 1
        if (Atick >= 0) and ( Atick < 2):Window.blit(numbutton_r[1],(786, 730))
        elif (Atick >= 2) and ( Atick < 4):Window.blit(numbutton_r[2],(786, 730))
        elif (Atick >= 4) and ( Atick < 6):Window.blit(numbutton_r[1],(786, 730))
        elif (Atick >= 6):
            
            Window.blit(numbutton_r[1],(786, 730))
            numbutton_bool[11] = False
            Atick = 0
            
    else: Window.blit(numbutton_r[0],(786, 730))

    if book_take:
        Gtick += 1
        if Gtick > 3:
            Gtick = 0
            Ftick += 1
            if Ftick > 7: Ftick = 0
        Window.blit(book_drop[Ftick],(687, 467))
        
    for i in range (16):
        if (infoprint_status[infoprint_numtaken[15-i]] == "printed"):
            Window.blit(infoprint[infoprint_numtaken[15-i]],(infoprint_pos_x[infoprint_numtaken[15-i]], infoprint_pos_y[infoprint_numtaken[15-i]]))
            print_IP_number(str(IP_speed[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+29)
            print_IP_number(str(IP_angle[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+39)
            print_IP_number(str(IP_height[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+49)
            print_IP_number(str(IP_mass[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+59)
            print_IP_number(str(IP_koff[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+69)
            print_IP_number(str(IP_max[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+99)
            print_IP_number(str(IP_dis[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+109)
            print_IP_number(str(IP_time_all[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+129)
            print_IP_number(str(IP_time_DMV[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+139)
            print_IP_number(str(IP_time_PMV[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+149)
            print_IP_tr(IP_tr_x[infoprint_numtaken[15-i]],IP_tr_y[infoprint_numtaken[15-i]],IP_count[infoprint_numtaken[15-i]],infoprint_pos_x[infoprint_numtaken[15-i]]+10,infoprint_pos_y[infoprint_numtaken[15-i]]+205,IP_masch[infoprint_numtaken[15-i]])
            print_IP_number(str(IP_masch[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+11,infoprint_pos_y[infoprint_numtaken[15-i]]+206)
            print_IP_number(str(IP_dis_all[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+169)
            print_IP_number(str(IP_dis_DMV[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+179)
            print_IP_number(str(IP_dis_PMV[infoprint_numtaken[15-i]]),infoprint_pos_x[infoprint_numtaken[15-i]]+82,infoprint_pos_y[infoprint_numtaken[15-i]]+189)

    if book_bool:
        Window.blit(book_page[book_curr_page],(book_pos_x, book_pos_y))
        if (book_curr_page == 1):
            text_print("       Главы",book_pos_x+20,book_pos_y+15)
            text_print("3 - Входные данные",book_pos_x+17,book_pos_y+39)
                     
            text_print("     Траектория",book_pos_x+165,book_pos_y+15)
            text_print(" С помощью данной",book_pos_x+165,book_pos_y+39)
            text_print("программы вы сможете",book_pos_x+165,book_pos_y+51)
            text_print("смоделировать",book_pos_x+165,book_pos_y+63)
            text_print("траекторию тела,",book_pos_x+165,book_pos_y+75)
            text_print("брошеного под углом",book_pos_x+165,book_pos_y+87)
            text_print("к горизонту.",book_pos_x+165,book_pos_y+99)
        elif (book_curr_page == 2):
            text_print("   Входные данные",book_pos_x+17,book_pos_y+15)
            text_print(" Вы можете ввести",book_pos_x+17,book_pos_y+39)
            text_print("5 параметров броска:",book_pos_x+17,book_pos_y+51)
            text_print("  - Скорость",book_pos_x+17,book_pos_y+63)
            text_print("  - Угол",book_pos_x+17,book_pos_y+75)
            text_print("  - Высота",book_pos_x+17,book_pos_y+87)
            text_print("  - Масса",book_pos_x+17,book_pos_y+99)
            text_print("  - Сопротивление",book_pos_x+17,book_pos_y+111)

            text_print("      Скорость",book_pos_x+165,book_pos_y+15)
            
    Window = effect_light(Window,303,693,10)
    if not decor_bool: Window = effect_light(Window,317,693,10)

    CS = pygame.display.get_surface()
    #CS = pygame.transform.scale(CS,(int(1920/(4/3)),int(180*(3/3))))
    Window.blit(CS,(0, 0))
    

#Window = pygame.display.set_mode((1920, 1080),pygame.FULLSCREEN)
    
tick = 0
tower_enabled = False
angle_enabled = False

print("Время загрузки составило",int((time.perf_counter_ns()-start_time)/1000000)/1000,"секунд")
print()

previous_time = time.perf_counter_ns()

Run = True
while Run:
    clock.tick(FPS)

    new_time = time.perf_counter_ns()
    fps_count = 1/(((new_time-previous_time)/1000000000))
    previous_time = new_time
    if Real_time_count:
        round_time = ((new_time-previous_time)/1000000000)
        if round_time > (1/FPS): round_time = 1/FPS
    else: round_time = 1/(FPS/sim_speed)
    
    x_mouse,y_mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: Run = False
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE): Run = False
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE) and (sideshow_bool) and not(finish_sim) and not(simulator_run):
            simulator_run = True
            past_x_pos = 0
            past_y_pos = height - 40
            Dot_count = -1
            speed_enabled = False
            mass_enabled = False
            sum_on = False
            speed = int(speed_word)
            mass = int(mass_word)
            speed_save[haveused] = speed
            mass_save[haveused] = mass
            speed_how_save[haveused] = speed_how
            mass_how_save[haveused] = mass_how
            angle_save[haveused] = angle
            height_save[haveused] = (height - 40)     
            if (speed_how != "meterspersecond"):
                if (speed_how == "kilometersperhour"): speed = speed/3.6
                if (speed_how == "santimeterspersecond"): speed = speed/100
            if (mass_how != "kg"):
                if (mass_how == "ton"): mass = mass*1000
                if (mass_how == "gramm"): mass = mass/1000
        if (speed_enabled):
            n = len(speed_word)
            if (n < 7):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_1): speed_word = speed_word + "1"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_2): speed_word = speed_word + "2"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_3): speed_word = speed_word + "3"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_4): speed_word = speed_word + "4"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_5): speed_word = speed_word + "5"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_6): speed_word = speed_word + "6"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_7): speed_word = speed_word + "7"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_8): speed_word = speed_word + "8"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_9): speed_word = speed_word + "9"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_0):
                    n = len(speed_word)
                    if (n > 0): speed_word = speed_word + "0"
                
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_BACKSPACE):
                n = len(speed_word)
                if (n > 0): speed_word = speed_word[:n-1]

            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
                speed_enabled = False
                sum_on = False
                if (speed_word == ''): speed_word = '0'

        if (mass_enabled):
            n = len(mass_word)
            if (n < 7):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_1): mass_word = mass_word + "1"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_2): mass_word = mass_word + "2"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_3): mass_word = mass_word + "3"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_4): mass_word = mass_word + "4"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_5): mass_word = mass_word + "5"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_6): mass_word = mass_word + "6"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_7): mass_word = mass_word + "7"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_8): mass_word = mass_word + "8"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_9): mass_word = mass_word + "9"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_0):
                    n = len(mass_word)
                    if (n > 0): mass_word = mass_word + "0"
                
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_BACKSPACE):
                n = len(mass_word)
                if (n > 0): mass_word = mass_word[:n-1]

            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
                mass_enabled = False
                sum_on = False
                if (mass_word == ''): mass_word = '1'

        if (koff_enable) and (presser_on):
            n = len(koff_input)
            if (n < 6):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_1): koff_input = koff_input + "1"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_2): koff_input = koff_input + "2"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_3): koff_input = koff_input + "3"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_4): koff_input = koff_input + "4"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_5): koff_input = koff_input + "5"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_6): koff_input = koff_input + "6"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_7): koff_input = koff_input + "7"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_8): koff_input = koff_input + "8"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_9): koff_input = koff_input + "9"
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_0): koff_input = koff_input + "0"
    
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_BACKSPACE):
                n = len(koff_input)
                if (n > 0): koff_input = koff_input[:n-1]

            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
                koff_enable = False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (((x_mouse >= 1323) and (x_mouse <= 1407) and (y_mouse >= 633) and (y_mouse <= 717)) or ((x_mouse >= 1307) and (x_mouse <= 1423) and (y_mouse >= 654) and (y_mouse <= 782)) or ((x_mouse >= 1344) and (x_mouse <= 1386) and (y_mouse >= 617) and (y_mouse <= 733))) and (sideshow_bool) and (not (simulator_run)) and (not (finish_sim)):
            start_button_play = True
            simulator_run = True
            past_x_pos = 0
            past_y_pos = height - 40
            Dot_count = -1
            speed_enabled = False
            mass_enabled = False
            sum_on = False
            speed = int(speed_word)
            mass = int(mass_word)
            speed_save[haveused] = speed
            mass_save[haveused] = mass
            speed_how_save[haveused] = speed_how
            mass_how_save[haveused] = mass_how
            angle_save[haveused] = angle
            height_save[haveused] = (height - 40)     
            if (speed_how != "meterspersecond"):
                if (speed_how == "kilometersperhour"): speed = speed/3.6
                if (speed_how == "santimeterspersecond"): speed = speed/100
            if (mass_how != "kg"):
                if (mass_how == "ton"): mass = mass*1000
                if (mass_how == "gramm"): mass = mass/1000

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 1206) and (x_mouse <= 1280) and (y_mouse >= 624) and (y_mouse <= 697) and (not (simulator_run)) and (finish_sim) and (repeat_button_up):
            repeat_button_set_play = True
            simulator_run = False
            finish_sim = False
            x_pos = 0
            y_pos = 0
            tick = 0
            timer = 0
            timer2 = 0
            Dot_spawn_x = [-6]*(2**16)
            Dot_spawn_y = [-6]*(2**16)
            pos_save_x = [-40]*(2**16)
            pos_save_y = [-40]*(2**16)
            lift_save = ["ND"]*(2**16)
            haveprinted = False
            m16 = False
            m8 = False
            m4 = False
            m2 = False
            m1 = True
            hm16 = False
            hm8 = False
            hm4 = False
            hm2 = False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 831) and (x_mouse <= 864) and (y_mouse >= 619) and (y_mouse <= 753) and not(book_bool):
            book_bool = True
            book_pos_x = 697
            book_pos_y = 447
            book_take_x = 0
            book_take_y = 0
            book_take = False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (book_bool) and (x_mouse >= book_pos_x) and (x_mouse <= book_pos_x+300) and (y_mouse >= book_pos_y) and (y_mouse <= book_pos_y+200):
            if (x_mouse >= book_pos_x+14) and (x_mouse <= book_pos_x+36) and (y_mouse >= book_pos_y+164) and (y_mouse <= book_pos_y+186):
                if book_curr_page > 0: book_curr_page -= 1
            elif (x_mouse >= book_pos_x+264) and (x_mouse <= book_pos_x+286) and (y_mouse >= book_pos_y+164) and (y_mouse <= book_pos_y+186):
                if book_curr_page < 6: book_curr_page += 1
            else:
                book_take_x = x_mouse - book_pos_x
                book_take_y = y_mouse - book_pos_y
                book_take = True

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 1067) and (x_mouse <= 1082) and (y_mouse >= 668) and (y_mouse <= 699):
            masch_avto_anim = True

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 1138) and (x_mouse <= 1169) and (y_mouse >= 764) and (y_mouse <= 795):
            if (abort_button_status == "off") and (simulator_run): abort_button_status = "rise"
            if (abort_button_status == "set"):
                abort_button_status = "down"
                simulator_run = False
                finish_sim = False
                x_pos = 0
                y_pos = 0
                tick = 0
                timer = 0
                timer2 = 0
                Dot_spawn_x = [-6]*(2**16)
                Dot_spawn_y = [-6]*(2**16)
                pos_save_x = [-40]*(2**16)
                pos_save_y = [-40]*(2**16)
                lift_save = ["ND"]*(2**16)
                haveprinted = False
                m16 = False
                m8 = False
                m4 = False
                m2 = False
                m1 = True
                hm16 = False
                hm8 = False
                hm4 = False
                hm2 = False                

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= masch_avto_curr) and (x_mouse <=  masch_avto_curr+7) and (y_mouse >= 693) and (y_mouse <= 704) and not(masch_avto_bool):
            masch_avto_take = True
            
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 679) and (x_mouse <= 715) and (y_mouse >= 672) and (y_mouse <= 698) and (not (simulator_run)) and (not (sideshow_bool)) and (not (finish_sim)) and not(presser_play):
            presser_play = True
            
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 681) and (x_mouse <= 711) and (y_mouse >= 622) and (y_mouse <= 652) and (not (simulator_run)) and (not (sideshow_bool)) and (not (finish_sim)) and not((RTA_nor) or (RTA_inv)):
            if rotor_ticker_bool: RTA_inv = True; rotor_ticker_bool = False
            else: RTA_nor = True; rotor_ticker_bool = False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 588) and (x_mouse <= 670) and (y_mouse >= 617) and (y_mouse <= 699) and (not (simulator_run)) and (not (sideshow_bool)) and (not (finish_sim)) and not(rotor_enabled):
            rotor_enabled = True
            
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 302) and (x_mouse <= 329) and (y_mouse >= 762) and (y_mouse <= 789) and (not (simulator_run)) and (not (sideshow_bool)) and (not (finish_sim)) and not(count_up_bool):
            count_up_bool = True
            if (speed_how == "kilometersperhour"): speed_how = "meterspersecond"
            elif (speed_how == "santimeterspersecond"): speed_how = "kilometersperhour"
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 331) and (x_mouse <= 358) and (y_mouse >= 762) and (y_mouse <= 789) and (not (simulator_run)) and (not (sideshow_bool)) and (not (finish_sim)) and not(count_down_bool):
            count_down_bool = True
            if (speed_how == "meterspersecond"): speed_how = "kilometersperhour"
            elif (speed_how == "kilometersperhour"): speed_how = "santimeterspersecond"

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 657) and (x_mouse <= 684) and (y_mouse >= 762) and (y_mouse <= 789) and (not (simulator_run)) and (not (sideshow_bool)) and (not (finish_sim)) and not(count_up_mass_bool):
            count_up_mass_bool = True
            if (mass_how == "kg"): mass_how = "ton"
            elif (mass_how == "gramm"): mass_how = "kg"
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 686) and (x_mouse <= 713) and (y_mouse >= 762) and (y_mouse <= 789) and (not (simulator_run)) and (not (sideshow_bool)) and (not (finish_sim)) and not(count_down_mass_bool):
            count_down_mass_bool = True
            if (mass_how == "kg"): mass_how = "gramm"
            elif (mass_how == "ton"): mass_how = "kg"

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 1127) and (x_mouse <= 1187) and (y_mouse >= 641) and (y_mouse <= 701) and (finish_sim) and not(print_button_play):
            print_button_play = True
            if not(haveprinted):
                haveprinted = True
                haveused = haveused + 1
                if (haveused < 16): 
                    infoprint_status[haveused] = "printing"
                    IP_speed[haveused] = speed
                    IP_angle[haveused] = angle
                    IP_height[haveused] = (600-height)/10
                    IP_mass[haveused] = mass
                    if not rotor_ticker_bool: koff, kof_word = rotor_update(rotor_angle)
                    else: koff, kof_word = get_koff_numpad(koff_input)
                    if (presser_on) and ((koff) != 0): IP_koff[haveused] = koff
                    else: IP_koff[haveused] = "/"
                    if (angle != 0) and (speed != 0): IP_max[haveused] = (int(((600-pos_save_y[Max_pos])-40)*100))/1000
                    else: IP_max[haveused] = IP_height[haveused]
                    IP_dis[haveused] = (int(pos_save_x[tick]*100))/1000
                    IP_time_all[haveused] = (int(timer_save[tick]*1000))/1000
                    if (angle != 0) and (speed != 0): IP_time_DMV[haveused] = (int(timer_save[Max_pos]*1000))/1000
                    else: IP_time_DMV[haveused] = "/"
                    IP_time_PMV[haveused] = (int((timer_save[tick]-timer_save[Max_pos])*1000))/1000
                    IP_tr_x[haveused] = Dot_spawn_x
                    IP_tr_y[haveused] = Dot_spawn_y
                    IP_count[haveused] = Dot_count
                    if hm256: IP_masch[haveused] = 256
                    elif hm128: IP_masch[haveused] = 128
                    elif hm64: IP_masch[haveused] = 64
                    elif hm32: IP_masch[haveused] = 32
                    elif hm16: IP_masch[haveused] = 16
                    elif hm8: IP_masch[haveused] = 8
                    elif hm4: IP_masch[haveused] = 4
                    elif hm2: IP_masch[haveused] = 2
                    else: IP_masch[haveused] = 1
                    IP_dis_all[haveused] = (int(dis_save[tick]*100))/1000
                    if (angle != 0) and (speed != 0): IP_dis_DMV[haveused] = (int(dis_save[Max_pos]*100))/1000
                    else: IP_dis_DMV[haveused] = "/"
                    IP_dis_PMV[haveused] = (int((dis_save[tick]-dis_save[Max_pos])*100))/1000
                    
                else: haveused = 15

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 736) and (x_mouse <= 760) and (y_mouse >= 655) and (y_mouse <= 679) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[0]):
            numbutton_bool[0] = True
            if (speed_enabled):
                n = len(speed_word)
                if (n < 7): speed_word = speed_word + "1"
            if (mass_enabled):
                n = len(mass_word)
                if (n < 7): mass_word = mass_word + "1"
            if (koff_enable):
                n = len(koff_input)
                if (n < 6): koff_input = koff_input + "1"

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 761) and (x_mouse <= 785) and (y_mouse >= 655) and (y_mouse <= 679) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[1]):
            numbutton_bool[1] = True
            if (speed_enabled):
                n = len(speed_word)
                if (n < 7): speed_word = speed_word + "2"
            if (mass_enabled):
                n = len(mass_word)
                if (n < 7): mass_word = mass_word + "2"
            if (koff_enable):
                n = len(koff_input)
                if (n < 6): koff_input = koff_input + "2"
            
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 786) and (x_mouse <= 810) and (y_mouse >= 655) and (y_mouse <= 679) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[2]):
            numbutton_bool[2] = True
            if (speed_enabled):
                n = len(speed_word)
                if (n < 7): speed_word = speed_word + "3"
            if (mass_enabled):
                n = len(mass_word)
                if (n < 7): mass_word = mass_word + "3"
            if (koff_enable):
                n = len(koff_input)
                if (n < 6): koff_input = koff_input + "3"

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 736) and (x_mouse <= 760) and (y_mouse >= 680) and (y_mouse <= 704) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[3]):
            numbutton_bool[3] = True
            if (speed_enabled):
                n = len(speed_word)
                if (n < 7): speed_word = speed_word + "4"
            if (mass_enabled):
                n = len(mass_word)
                if (n < 7): mass_word = mass_word + "4"
            if (koff_enable):
                n = len(koff_input)
                if (n < 6): koff_input = koff_input + "4"

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 761) and (x_mouse <= 785) and (y_mouse >= 680) and (y_mouse <= 704) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[4]):
            numbutton_bool[4] = True
            if (speed_enabled):
                n = len(speed_word)
                if (n < 7): speed_word = speed_word + "5"
            if (mass_enabled):
                n = len(mass_word)
                if (n < 7): mass_word = mass_word + "5"
            if (koff_enable):
                n = len(koff_input)
                if (n < 6): koff_input = koff_input + "5"
            
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 786) and (x_mouse <= 810) and (y_mouse >= 680) and (y_mouse <= 704) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[5]):
            numbutton_bool[5] = True
            if (speed_enabled):
                n = len(speed_word)
                if (n < 7): speed_word = speed_word + "6"
            if (mass_enabled):
                n = len(mass_word)
                if (n < 7): mass_word = mass_word + "6"
            if (koff_enable):
                n = len(koff_input)
                if (n < 6): koff_input = koff_input + "6"

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 736) and (x_mouse <= 760) and (y_mouse >= 705) and (y_mouse <= 729) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[6]):
            numbutton_bool[6] = True
            if (speed_enabled):
                n = len(speed_word)
                if (n < 7): speed_word = speed_word + "7"
            if (mass_enabled):
                n = len(mass_word)
                if (n < 7): mass_word = mass_word + "7"
            if (koff_enable):
                n = len(koff_input)
                if (n < 6): koff_input = koff_input + "7"

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 761) and (x_mouse <= 785) and (y_mouse >= 705) and (y_mouse <= 729) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[7]):
            numbutton_bool[7] = True
            if (speed_enabled):
                n = len(speed_word)
                if (n < 7): speed_word = speed_word + "8"
            if (mass_enabled):
                n = len(mass_word)
                if (n < 7): mass_word = mass_word + "8"
            if (koff_enable):
                n = len(koff_input)
                if (n < 6): koff_input = koff_input + "8"
            
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 786) and (x_mouse <= 810) and (y_mouse >= 705) and (y_mouse <= 729) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[8]):
            numbutton_bool[8] = True
            if (speed_enabled):
                n = len(speed_word)
                if (n < 7): speed_word = speed_word + "9"
            if (mass_enabled):
                n = len(mass_word)
                if (n < 7): mass_word = mass_word + "9"
            if (koff_enable):
                n = len(koff_input)
                if (n < 6): koff_input = koff_input + "9"

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 736) and (x_mouse <= 760) and (y_mouse >= 730) and (y_mouse <= 754) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[9]):
            numbutton_bool[9] = True
            if (speed_enabled):
                n = len(speed_word)
                if (n > 0): speed_word = speed_word[:n-1]
            if (mass_enabled):
                n = len(mass_word)
                if (n > 0): mass_word = mass_word[:n-1]
            if (koff_enable):
                n = len(koff_input)
                if (n > 0): koff_input = koff_input[:n-1]

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 761) and (x_mouse <= 785) and (y_mouse >= 730) and (y_mouse <= 754) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[10]):
            numbutton_bool[10] = True
            if (speed_enabled):
                n = len(speed_word)
                if (n < 7) and (n > 0): speed_word = speed_word + "0"
            if (mass_enabled):
                n = len(mass_word)
                if (n < 7) and (n > 0): mass_word = mass_word + "0"
            if (koff_enable):
                n = len(koff_input)
                if (n < 6): koff_input = koff_input + "0"
            
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 786) and (x_mouse <= 810) and (y_mouse >= 730) and (y_mouse <= 754) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[11]):
            numbutton_bool[11] = True
            speed_enabled = False
            mass_enabled = False
            koff_enable = False
            sum_on = False
            if (speed_word == ''): speed_word = '0'
            if (mass_word == ''): mass_word = '1'
                
        
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 0) and (x_mouse <= 45) and (y_mouse >= Hinfo_p-13) and (y_mouse <= Hinfo_p+13)and (not(sideshow_bool)) and (not (sideshow_bool)) and (not (simulator_run)) and (not (finish_sim)): Hinfo_enabled = True
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 1213) and (x_mouse <= 1273) and (y_mouse >= 723+showsize_tugger_pos) and (y_mouse <= 730+showsize_tugger_pos) and (not((sideshow_play_down) or (sideshow_play_up))) and (not (simulator_run)) and (not (finish_sim)): showsize_tugger_enabled = True
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 50) and (x_mouse <= 200) and (y_mouse >= 0) and (y_mouse <= 600)and (not(sideshow_bool)) and (not (sideshow_bool)) and (not (simulator_run)) and (not (finish_sim)):
            tower_enabled = True
            tower_take_pos = y_mouse
            tower_past_pos = height
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 24) and (x_mouse <= 294) and (y_mouse >= 624) and (y_mouse <= 680)and (not(sideshow_bool)) and (not (sideshow_bool)) and (not (simulator_run)) and (not (finish_sim)): angle_enabled = True
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 24) and (x_mouse <= 294) and (y_mouse >= 733) and (y_mouse <= 789)and (not(sideshow_bool)) and (not (sideshow_bool)) and (not (simulator_run)) and (not (finish_sim)):
            speed_enabled = True
            mass_enabled = False
            koff_enable = False
            
            if (mass_word == ''): mass_word = '1'
            if (speed_word == "0"): speed_word = ''
            input_timer = 0
            sum_on = True
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 381) and (x_mouse <= 651) and (y_mouse >= 733) and (y_mouse <= 789)and (not(sideshow_bool)) and (not (simulator_run)) and (not (finish_sim)):
            mass_enabled = True
            speed_enabled = False
            koff_enable = False
            
            if (speed_word == ''): speed_word = '0'
            input_timer = 0
            sum_on = True
            
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (rotor_ticker_bool) and(x_mouse >= 467) and (x_mouse <= 578) and (y_mouse >= 630) and (y_mouse <= 663)and (not(sideshow_bool)) and (not (sideshow_bool)) and (not (simulator_run)) and (not (finish_sim)):
            speed_enabled = False
            mass_enabled = False
            koff_enable = True
            
            if (mass_word == ''): mass_word = '1'
            if (speed_word == ""): speed_word = '0'
            input_timer = 0
            sum_on = True
            
        for i in range (16):
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and not(book_take) and (x_mouse >= infoprint_pos_x[infoprint_numtaken[i]]) and (x_mouse <= infoprint_pos_x[infoprint_numtaken[i]]+200) and (y_mouse >= infoprint_pos_y[infoprint_numtaken[i]]) and (y_mouse <= infoprint_pos_y[infoprint_numtaken[i]]+300) and (infoprint_status[infoprint_numtaken[i]] == "printed"):
                infoprint_pointtaken_x[infoprint_numtaken[i]] = x_mouse - infoprint_pos_x[infoprint_numtaken[i]]
                infoprint_pointtaken_y[infoprint_numtaken[i]] = y_mouse - infoprint_pos_y[infoprint_numtaken[i]]
                infoprint_havetaken[infoprint_numtaken[i]] = True

                C = infoprint_numtaken[i]

                for j in range(i,0,-1):
                    infoprint_numtaken[j] = infoprint_numtaken[j-1]
                infoprint_numtaken[0] = C

                break

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (not(monitor_start_load)) and (not(monitor_start)) and (((x_mouse >= 471) and (x_mouse <= 501) and (y_mouse >= 768) and (y_mouse <= 798)) and (sideshow_bool)):
            if monitor_bool:
                monitor_bool = False
            else: 
                monitor_start = True

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "main")):
            if (enable_1): menu = "remember"
            if (enable_4): menu = "settings"
            
        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "settings")):
            if (enable_1): menu = "main"
            if (enable_3): draw_parabola = not draw_parabola

        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "remember")):
            if (enable_1): menu = "main"
            
            for i in range (8):
                if viev_enable[i]:
                    viev_bool[i] = not viev_bool[i]

            for i in range (8):
                if color_enable[i]:
                    color_tr[i] += 1
                    if color_tr[i] > 7: color_tr[i] = 0

            for i in range (8):
                if not save_enable[i] and (finish_sim):
                    tr_remember(Dot_spawn_x,Dot_spawn_y,Dot_count,i)

            for i in range (8):
                if not delete_enable[i]:
                    tr_forgot(i)





        if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
            Hinfo_enabled = False
            showsize_tugger_enabled = False
            tower_enabled = False
            angle_enabled = False
            count_up_bool = False
            count_down_bool = False
            count_up_mass_bool = False
            count_down_mass_bool = False
            rotor_enabled = False
            masch_avto_take = False
            for i in range(16):
                infoprint_havetaken[i] = False
            if (book_take):
                if (book_pos_x >= 687) and (book_pos_x <= 707) and (book_pos_y >= 467) and (book_pos_y <= 487): book_bool = False
            book_take = False
            
    for i in range(16):
        if (infoprint_havetaken[i]):
            infoprint_pos_x[i] = x_mouse - infoprint_pointtaken_x[i]
            infoprint_pos_y[i] = y_mouse - infoprint_pointtaken_y[i]

    if (book_take):
            book_pos_x = x_mouse - book_take_x
            book_pos_y = y_mouse - book_take_y
            
    if not (speed_enabled) and not(mass_enabled): sum_on = False
    
    if (speed_enabled) or (mass_enabled):
        input_timer = input_timer + 1
        if (input_timer >= FPS):
            if (sum_on): sum_on = False
            else: sum_on = True
            input_timer = 0

    if (masch_avto_take): masch_avto_curr = x_mouse-3
    if (masch_avto_curr < 960): masch_avto_curr = 960
    if (masch_avto_curr > 1029): masch_avto_curr = 1029
        
    if (tower_enabled): height = tower_past_pos - (tower_take_pos - y_mouse)
    if (height > 600): height = 600
    if (height < -9400): height = -9400

    if (not(showsize_tugger_enabled)) and (showsize_tugger_pos != 0) and (showsize_tugger_pos != 40):
        Ttimer = Ttimer + 1.5/FPS
        if (showsize_tugger_pos <= 20): showsize_tugger_pos = showsize_tugger_pos - (Ttimer)**2
        else: showsize_tugger_pos = showsize_tugger_pos + (Ttimer)**2
    else: Ttimer = 0

    if (showsize_tugger_enabled):showsize_tugger_pos = y_mouse-726
    if (showsize_tugger_pos > 40): showsize_tugger_pos = 40
    if (showsize_tugger_pos < 0): showsize_tugger_pos = 0

    showsize_tugger_possize = (20-showsize_tugger_pos)

    if (showsize_tugger_pos == 0) and (not(sideshow_play_down)) and (sideshow_bool == True):
        speed_enabled = False
        mass_enabled = False
        koff_enable = False
        Hinfo_enabled = False
        showsize_tugger_enabled = False
        tower_enabled = False
        angle_enabled = False
        count_up_bool = False
        count_down_bool = False
        count_up_mass_bool = False
        count_down_mass_bool = False
        rotor_enabled = False
        sideshow_play_down = True       
    if (showsize_tugger_pos == 40) and (not(sideshow_play_up)) and (sideshow_bool == False):
        speed_enabled = False
        mass_enabled = False
        koff_enable = False
        Hinfo_enabled = False
        showsize_tugger_enabled = False
        tower_enabled = False
        angle_enabled = False
        count_up_bool = False
        count_down_bool = False
        count_up_mass_bool = False
        count_down_mass_bool = False
        rotor_enabled = False
        Hinfo_p = Hinfo_p + 1
        sideshow_play_up = True

    
    if (Hinfo_p > 535) and (not(Hinfo_enabled)):
        if (sideshow_bool):
            if (Hinfo_p < 613): 
                Htimer = Htimer + 3.5/FPS
                Hinfo_p = Hinfo_p + (Htimer)**2
            else: Htimer = 0
        else:
            if (Hinfo_p < 586):
                Htimer = Htimer + 3.5/FPS
                Hinfo_p = Hinfo_p + (Htimer)**2
            else: Htimer = 0
    else: Htimer = 0

    if (Hinfo_enabled): Hinfo_p = y_mouse
    
    if (sideshow_bool):
        if (Hinfo_p > 613): Hinfo_p = 613
    else:
        if (Hinfo_p > 586):
            if (Hinfo_enabled): Hinfo_p = 586
            elif (Hinfo_p > 587): Hinfo_p -= 1
        
    if (Hinfo_p < 535): Hinfo_p = 535

    if (angle_enabled): angle = 90-int((x_mouse-24)/3)
    if (angle > 90): angle = 90
    if (angle < 0): angle = 0

    forse_arrow_rect = forse_arrow.get_rect(center=(60,60))
    forse_arrow2, forse_arrow_p = rot_center(forse_arrow, forse_arrow_rect, (90-angle))
    forse_arrow3 = pygame.transform.flip(forse_arrow2, True, False)

    if (y_pos > 560):
        y_pos = 560
        finish_sim = True
        simulator_run = False
        repeat_button_rise_play = True
        if (abort_button_status == "set"): abort_button_status = "down"
        
        up_found = False
        down_found = False
        for i in range(0,tick):
            if (pos_save_y[i-1] < pos_save_y[i]):
                lift_save[i] = "DW"
                up_found = True
            elif (pos_save_y[i] > pos_save_y[i+1]):
                lift_save[i] = "UP"
                down_found = True

        if (up_found and down_found):
            Max = 9999
            for i in range (2,tick-1):
                if (pos_save_y[i] < Max):
                    Max = pos_save_y[i]
                    Max_pos = i
                    
            lift_save[Max_pos] = "HP"

    if (simulator_run):
        if not rotor_ticker_bool: koff, kof_word = rotor_update(rotor_angle)
        else: koff, kof_word = get_koff_numpad(koff_input)
        if (presser_on) and (koff != 0):
            tick = tick + 1
            timer = (timer + round_time)
            x_pos = ((speed*10*math.cos(math.radians(angle)))*(mass/koff)*(1-(math.e**(-(koff/mass)*timer))))
            y_pos = -((mass/koff)*(((speed*10*math.sin(math.radians(angle)))+((mass*9.81)/koff))*(1-(math.e**(-(koff/mass)*timer)))-9.81*timer)) + height - 40
            animballangle = math.degrees(math.atan2(y_pos-past_y_pos,x_pos-past_x_pos))
            if tick > 0: dis_save[tick] = dis_save[tick-1] + (math.sqrt((x_pos-past_x_pos)**2 + (y_pos-past_y_pos)**2))
            past_x_pos = x_pos
            past_y_pos = y_pos
            pos_save_x[tick] = x_pos
            pos_save_y[tick] = y_pos
            timer_save[tick] = timer
            if (tick%(int(FPS/3)) == 0):
                Dot_count = Dot_count + 1
                Dot_spawn_x[Dot_count] = int(x_pos + 17)
                Dot_spawn_y[Dot_count] = int(y_pos + 17)
        else:
            tick = tick + 1
            timer = (timer + round_time)
            x_pos = (((speed*10)))* timer * math.cos(math.radians(angle))
            y_pos = -((((speed*10))) * timer * math.sin(math.radians(angle)) - ((G*9.81 * (timer*timer))/2)) + height - 40
            animballangle = math.degrees(math.atan2(y_pos-past_y_pos,x_pos-past_x_pos))
            if tick > 0: dis_save[tick] = dis_save[tick-1] + (math.sqrt((x_pos-past_x_pos)**2 + (y_pos-past_y_pos)**2))
            past_x_pos = x_pos
            past_y_pos = y_pos
            pos_save_x[tick] = x_pos
            pos_save_y[tick] = y_pos
            timer_save[tick] = timer
            if (tick%(int(FPS/3)) == 0):
                Dot_count = Dot_count + 1
                Dot_spawn_x[Dot_count] = int(x_pos + 17)
                Dot_spawn_y[Dot_count] = int(y_pos + 17)
            
    update()
    pygame.display.flip()

save_settings()

pygame.quit()
