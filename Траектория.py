import time         #Загрузка модулей
start_time = time.perf_counter_ns()

import pygame
pygame.init()
import math
import pathlib
from pathlib import Path
from random import randint
import datetime

now = datetime.datetime.now() 
print()
print((str(now))[0:19])

directiry = pathlib.Path.cwd() #Нахождение директории
print()
print(directiry)
dir_path = str(directiry)

print()
print("Траектория 1.0.0")
print()
start_time = time.perf_counter_ns()

Window = pygame.display.set_mode((1440,810)) #Создание окна
pygame.display.set_caption("Траектория") #Наименование окна

window_mode = (pygame.display.list_modes())

FPS = 60

pygame.mouse.set_visible(True)
clock = pygame.time.Clock()

icon = pygame.image.load(dir_path+"/data/texture/icon.ico").convert()
icon.set_colorkey((0,0,0))
pygame.display.set_icon(icon)  #Установить иконку окна

#Начинается загрузка текстур

blackscreen = pygame.image.load(dir_path+"/data/texture/blackscreen.png").convert()
blackscreen.set_alpha(255)

python_logo = pygame.image.load(dir_path+"/data/texture/python_logo.png").convert()
python_logo.set_alpha(0)
intro_text1 = pygame.image.load(dir_path+"/data/texture/intro_text1.png").convert()
intro_text1.set_alpha(0)

IDL = [0]*100
for i in range(84):
    IDL[i] = pygame.image.load(dir_path+'/data/texture/ID_print/ID'+str(i+1)+'.png').convert()
    IDL[i].set_colorkey((0,0,0))

MT = [0]*100
for i in range(85):
    MT[i] = pygame.image.load(dir_path+'/data/texture/monitor_print/MT'+str(i+1)+'.png').convert()
    MT[i].set_colorkey((0,0,0))

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

background_16x = [0]*3
background_8x = [0]*3
background_4x = [0]*3
background_2x = [0]*3
background_1x = [0]*3
sky_background = [0]*3
sky_background1 = [0]*3
sky_background2 = [0]*3
sky_background3 = [0]*3
sky_background4 = [0]*3
background_16x[0] = pygame.image.load(dir_path+'/data/texture/background_16x1.png').convert()
background_16x[1] = pygame.image.load(dir_path+'/data/texture/background_16x2.png').convert()
background_16x[2] = pygame.image.load(dir_path+'/data/texture/background_16x3.png').convert()
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
sky_background4[0] = pygame.image.load(dir_path+'/data/texture/sky_background4_1.png').convert()
sky_background4[1] = pygame.image.load(dir_path+'/data/texture/sky_background4_2.png').convert()
sky_background4[2] = pygame.image.load(dir_path+'/data/texture/sky_background4_3.png').convert()
found_line = pygame.image.load(dir_path+'/data/texture/found_line.png').convert()
found_point = pygame.image.load(dir_path+'/data/texture/found_point.png').convert()
found_point2 = pygame.image.load(dir_path+'/data/texture/found_point2.png').convert()
found_point3 = pygame.image.load(dir_path+'/data/texture/found_point3.png').convert()
found_point4 = pygame.image.load(dir_path+'/data/texture/found_point4.png').convert()
base = pygame.image.load(dir_path+'/data/texture/base.png').convert()
simspeed_base = pygame.image.load(dir_path+'/data/texture/simspeed_base.png').convert()
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
anglometr = pygame.image.load(dir_path+'/data/texture/anglometr.png').convert()
anglometr_arrow = pygame.image.load(dir_path+'/data/texture/anglometr_arrow.png').convert()
anglometr_close = pygame.image.load(dir_path+'/data/texture/anglometr_close.png').convert()
simspeed_block = pygame.image.load(dir_path+'/data/texture/simspeed_block.png').convert()
simspeed_button_set1 = pygame.image.load(dir_path+'/data/texture/simspeed_button_set1.png').convert()
simspeed_button_set2 = pygame.image.load(dir_path+'/data/texture/simspeed_button_set2.png').convert()
simspeed_button_on1 = pygame.image.load(dir_path+'/data/texture/simspeed_button_on1.png').convert()
simspeed_button_on2 = pygame.image.load(dir_path+'/data/texture/simspeed_button_on2.png').convert()
sppanel = pygame.image.load(dir_path+'/data/texture/sppanel.png').convert()
airship1 = pygame.image.load(dir_path+'/data/texture/airship1.png').convert()
airship2 = pygame.image.load(dir_path+'/data/texture/airship2.png').convert()
sppanel_arrow = pygame.image.load(dir_path+'/data/texture/sppanel_arrow.png').convert()
decor5 = pygame.image.load(dir_path+'/data/texture/decor5.png').convert()
monitor_lampdecor = pygame.image.load(dir_path+'/data/texture/monitor_lampdecor.png').convert()
superangle_input = pygame.image.load(dir_path+'/data/texture/superangle_input.png').convert()
superangle_off = pygame.image.load(dir_path+'/data/texture/superangle_off.png').convert()
decor6 = pygame.image.load(dir_path+'/data/texture/decor6.png').convert()

VS_info = pygame.image.load(dir_path+'/data/texture/VS_info.png')
VS_input = pygame.image.load(dir_path+'/data/texture/VS_input.png')
VS_sqr_tugger = pygame.image.load(dir_path+'/data/texture/VS_sqr_tugger.png')
VS_volume_tugger = pygame.image.load(dir_path+'/data/texture/VS_volume_tugger.png')

VS_base_button = [0]*2
VS_base_button[0] = pygame.image.load(dir_path+'/data/texture/VS_base_button1.png')
VS_base_button[1] = pygame.image.load(dir_path+'/data/texture/VS_base_button2.png')

VS_sqr_num = [0]*10
for i in range(10): VS_sqr_num[i] = pygame.image.load(dir_path+'/data/texture/VS_sqr_num'+str(i)+'.png')
VS_sqr_dot = pygame.image.load(dir_path+'/data/texture/VS_sqr_dot.png')
VS_sqr_M = pygame.image.load(dir_path+'/data/texture/VS_sqr_M.png')

VS_volume_num = [0]*10
for i in range(10): VS_volume_num[i] = pygame.image.load(dir_path+'/data/texture/VS_volume_num'+str(i)+'.png')
VS_volume_dot = pygame.image.load(dir_path+'/data/texture/VS_volume_dot.png')
VS_volume_M = pygame.image.load(dir_path+'/data/texture/VS_volume_M.png')
    
dvig_rotor = pygame.image.load(dir_path+'/data/texture/dvig_rotor.png')
dvig_rotor.set_colorkey((0,0,0))
dvig_palka = pygame.image.load(dir_path+'/data/texture/dvig_palka.png')
dvig_palka.set_colorkey((0,0,0))
dvig_push = pygame.image.load(dir_path+'/data/texture/dvig_push.png')
dvig_push.set_colorkey((0,0,0))

plotnost_atm = pygame.image.load(dir_path+'/data/texture/plotnost_atm.png').convert()
plotnost_atm.set_colorkey((0, 0, 0))
plotnost_num = [0]*10
for i in range(10):
    plotnost_num[i] = pygame.image.load(dir_path+'/data/texture/plotnost_num'+str(i)+'.png').convert()
    plotnost_num[i].set_colorkey((0, 0, 0))
plotnost_dot = pygame.image.load(dir_path+'/data/texture/plotnost_dot.png').convert()
plotnost_dot.set_colorkey((0, 0, 0))

dumout_cast = pygame.image.load(dir_path+'/data/texture/dumout_cast.png').convert() 
dumout_cast.set_alpha(255)
    
plotnost_base_button = [0]*2
plotnost_down_button = [0]*2
plotnost_up_button = [0]*2
plotnost_base_button[0] = pygame.image.load(dir_path+'/data/texture/plotnost_base_button_1.png').convert()
plotnost_base_button[1] = pygame.image.load(dir_path+'/data/texture/plotnost_base_button_2.png').convert()
plotnost_down_button[0] = pygame.image.load(dir_path+'/data/texture/plotnost_down_button_1.png').convert()
plotnost_down_button[1] = pygame.image.load(dir_path+'/data/texture/plotnost_down_button_2.png').convert()
plotnost_up_button[0] = pygame.image.load(dir_path+'/data/texture/plotnost_up_button_1.png').convert()
plotnost_up_button[1] = pygame.image.load(dir_path+'/data/texture/plotnost_up_button_2.png').convert()
plotnost_dumout = pygame.image.load(dir_path+'/data/texture/plotnost_dumout.png').convert()
plotnost_vent = pygame.image.load(dir_path+'/data/texture/plotnost_vent.png').convert()
plotnost_input = pygame.image.load(dir_path+'/data/texture/plotnost_input.png').convert()
plotnost_info = pygame.image.load(dir_path+'/data/texture/plotnost_info.png').convert()
plotnost_vent.set_colorkey((0, 0, 0))

decoran8a = pygame.image.load(dir_path+'/data/texture/decoran8a.png').convert()

decoran8 = [0]*20
for i in range(20):
    decoran8[i] = pygame.image.load(dir_path+'/data/texture/decoran8_'+str(i+1)+'.png').convert()

gravityshow = [0]*12
for i in range(10):
    gravityshow[i] = pygame.image.load(dir_path+'/data/texture/gravityshow_num'+str(i)+'.png').convert()

gravityshow[10] = pygame.image.load(dir_path+'/data/texture/gravityshow_dot.png').convert()
gravityshow[11] = pygame.image.load(dir_path+'/data/texture/gravityshow_g.png').convert()

decoran_7 = [0]*4
for i in range(4):
    decoran_7[i] = pygame.image.load(dir_path+'/data/texture/decoran7_'+str(i+1)+'.png').convert()

decoran_6 = [0]*2
for i in range(2):
    decoran_6[i] = pygame.image.load(dir_path+'/data/texture/decoran6_'+str(i+1)+'.png').convert()

colapanel_close = pygame.image.load(dir_path+'/data/texture/colapanel_close.png').convert()

gravity_base = pygame.image.load(dir_path+'/data/texture/gravity_base.png').convert()
gravity_bit = pygame.image.load(dir_path+'/data/texture/gravity_bit.png').convert()
gravity_info = pygame.image.load(dir_path+'/data/texture/gravity_info.png').convert()
gravity_info.set_colorkey((0, 0, 0))

gravity_wheel = [0]*21
for i in range(21):
    gravity_wheel[i] = pygame.image.load(dir_path+'/data/texture/gravity_wheel'+str(i)+'.png').convert()
    gravity_wheel[i].set_colorkey((0, 0, 0))

gravity_shadow = [0]*7
for i in range(7):
    gravity_shadow[i] = pygame.image.load(dir_path+'/data/texture/gravity_shadow_'+str(i+1)+'.png').convert()
    gravity_shadow[i].set_colorkey((0, 0, 0))
    gravity_shadow[i].set_alpha(255)

decoran5 = [0]*26
for i in range(26): decoran5[i] = pygame.image.load(dir_path+'/data/texture/decoran5_'+str(i+1)+'.png').convert()

angle_off = pygame.image.load(dir_path+'/data/texture/angle_off.png').convert()

superangle_off.set_colorkey((0, 0, 0))

superangle_angleinfo = pygame.image.load(dir_path+'/data/texture/superangle_angleinfo.png').convert()

superangle_number = [0]*10
for i in range(10):
    superangle_number[i] = pygame.image.load(dir_path+'/data/texture/superangle_number'+str(i)+'.png').convert()
    superangle_number[i].set_colorkey((0, 0, 0))
    
superangle_info = [0]*4
for i in range(4): superangle_info[i] = pygame.image.load(dir_path+'/data/texture/superangle_info'+str(i+1)+'.png').convert()

superangle_tugger = [0]*5
for i in range(5): superangle_tugger[i] = pygame.image.load(dir_path+'/data/texture/superangle_tugger'+str(i+1)+'.png').convert()

decoran4 = [0]*5
for i in range(5): decoran4[i] = pygame.image.load(dir_path+'/data/texture/decoran4_'+str(i+1)+'.png').convert()

sppanel_arrow.set_colorkey((0, 0, 0))
airship1.set_colorkey((0, 0, 0))
airship2.set_colorkey((0, 0, 0))

python_nake = pygame.image.load(dir_path+'/data/texture/python_nake.png').convert()
pi_nake = pygame.image.load(dir_path+'/data/texture/pi_nake.png').convert()
aseprint_nake = pygame.image.load(dir_path+'/data/texture/aseprint_nake.png').convert()

python_nake.set_colorkey((0, 0, 0))
pi_nake.set_colorkey((0, 0, 0))
aseprint_nake.set_colorkey((0, 0, 0))

addsettings_button_a = [0]*4
addsettings_button_g = [0]*4
addsettings_button_p = [0]*4
addsettings_button_vs = [0]*4
for i in range(4):
    addsettings_button_a[i] = pygame.image.load(dir_path+'/data/texture/addsettings_button_a'+str(i+1)+'.png').convert()
    addsettings_button_a[i].set_colorkey((0, 0, 0))
    addsettings_button_g[i] = pygame.image.load(dir_path+'/data/texture/addsettings_button_g'+str(i+1)+'.png').convert()
    addsettings_button_g[i].set_colorkey((0, 0, 0))
    addsettings_button_p[i] = pygame.image.load(dir_path+'/data/texture/addsettings_button_p'+str(i+1)+'.png').convert()
    addsettings_button_p[i].set_colorkey((0, 0, 0))
    addsettings_button_vs[i] = pygame.image.load(dir_path+'/data/texture/addsettings_button_vs'+str(i+1)+'.png').convert()
    addsettings_button_vs[i].set_colorkey((0, 0, 0))

addsettings_under = pygame.image.load(dir_path+'/data/texture/addsettings_under.png').convert()
addsettings = [0]*14
for i in range(14):
    addsettings[i] = pygame.image.load(dir_path+'/data/texture/addsettings'+str(i+1)+'.png').convert()
    addsettings[i].set_colorkey((0, 0, 0))

colapanel_under = pygame.image.load(dir_path+'/data/texture/colapanel_under.png').convert()
colapanel = [0]*14
for i in range(14):
    colapanel[i] = pygame.image.load(dir_path+'/data/texture/colapanel'+str(i+1)+'.png').convert()
    colapanel[i].set_colorkey((0, 0, 0))

found_point.set_colorkey((0, 0, 0))
found_point2.set_colorkey((0, 0, 0))
found_point3.set_colorkey((0, 0, 0))
found_point4.set_colorkey((0, 0, 0))

infotable_up.set_alpha(215)
infotable_down.set_alpha(215)
infotable_highpoint.set_alpha(215)

smoke = pygame.image.load(dir_path+'/data/texture/smoke.png').convert()
smoke.set_colorkey((0, 0, 0))

simspeed_rotor = pygame.image.load(dir_path+'/data/texture/simspeed_rotor.png').convert()
simspeed_rotor.set_colorkey((0, 0, 0))
simspeed_top = pygame.image.load(dir_path+'/data/texture/simspeed_top.png').convert()
simspeed_top.set_colorkey((0, 0, 0))
simspeed_rotte = [0]*4
simspeed_rotte[0] = pygame.image.load(dir_path+'/data/texture/simspeed_rotte1.png').convert()
simspeed_rotte[1] = pygame.image.load(dir_path+'/data/texture/simspeed_rotte2.png').convert()
simspeed_rotte[2] = pygame.image.load(dir_path+'/data/texture/simspeed_rotte3.png').convert()
simspeed_rotte[3] = pygame.image.load(dir_path+'/data/texture/simspeed_rotte4.png').convert()
simspeed_rotte[0].set_colorkey((0, 0, 0))
simspeed_rotte[1].set_colorkey((0, 0, 0))
simspeed_rotte[2].set_colorkey((0, 0, 0))
simspeed_rotte[3].set_colorkey((0, 0, 0))

showside_speed_num = [0]*11
for i in range(0,10): showside_speed_num[i] = pygame.image.load(dir_path+'/data/texture/showside_speed_num'+str(i)+'.png').convert()
showside_speed_num[10] = pygame.image.load(dir_path+'/data/texture/showside_speed_numdot.png').convert()

SSN =[0]*10
for i in range(0,10): SSN[i] = pygame.image.load(dir_path+'/data/texture/simspeed_num'+str(i)+'.png').convert()

energy_name = pygame.image.load(dir_path+'/data/texture/energy_name.png').convert()
energy_base = pygame.image.load(dir_path+'/data/texture/energy_base.png').convert()

EK1 = pygame.image.load(dir_path+'/data/texture/EK1.png').convert()
EK2 = pygame.image.load(dir_path+'/data/texture/EK2.png').convert()
EK3 = pygame.image.load(dir_path+'/data/texture/EK3.png').convert()

EN = [0]*10
EN[0] = pygame.image.load(dir_path+'/data/texture/EN10.png').convert()
for i in range(1,10): EN[i] = pygame.image.load(dir_path+'/data/texture/EN'+str(i)+'.png').convert()

mehatron_under = pygame.image.load(dir_path+'/data/texture/mehatron_under.png').convert()

decoran3 = [0]*6
decoran3[0] = pygame.image.load(dir_path+'/data/texture/decoran3_1.png').convert()
decoran3[1] = pygame.image.load(dir_path+'/data/texture/decoran3_2.png').convert()
decoran3[2] = pygame.image.load(dir_path+'/data/texture/decoran3_3.png').convert()
decoran3[3] = pygame.image.load(dir_path+'/data/texture/decoran3_4.png').convert()
decoran3[4] = pygame.image.load(dir_path+'/data/texture/decoran3_5.png').convert()
decoran3[5] = pygame.image.load(dir_path+'/data/texture/decoran3_6.png').convert()
decoran3[0].set_colorkey((0, 0, 0))
decoran3[1].set_colorkey((0, 0, 0))
decoran3[2].set_colorkey((0, 0, 0))
decoran3[3].set_colorkey((0, 0, 0))
decoran3[4].set_colorkey((0, 0, 0))
decoran3[5].set_colorkey((0, 0, 0))

oblako = [0]*4
oblako[0] = pygame.image.load(dir_path+'/data/texture/oblako1.png').convert()
oblako[1] = pygame.image.load(dir_path+'/data/texture/oblako2.png').convert()
oblako[2] = pygame.image.load(dir_path+'/data/texture/oblako3.png').convert()
oblako[3] = pygame.image.load(dir_path+'/data/texture/oblako4.png').convert()
oblako[0].set_alpha(127)
oblako[1].set_alpha(127)
oblako[2].set_alpha(127)
oblako[3].set_alpha(127)
oblako[0].set_colorkey((0, 0, 0))
oblako[1].set_colorkey((0, 0, 0))
oblako[2].set_colorkey((0, 0, 0))
oblako[3].set_colorkey((0, 0, 0))

anglometr.set_colorkey((0,0,0))
anglometr_arrow.set_colorkey((0,0,0))
anglometr_close.set_colorkey((0,0,0))

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
monitor_fileinfo = pygame.image.load(dir_path+'/data/texture/monitor_fileinfo.png').convert()
monitor_saveinfo = pygame.image.load(dir_path+'/data/texture/monitor_saveinfo.png').convert()
monitor_text1 = pygame.image.load(dir_path+'/data/texture/monitor_text1.png').convert()
monitor_text2 = pygame.image.load(dir_path+'/data/texture/monitor_text2.png').convert()
monitor_text3 = pygame.image.load(dir_path+'/data/texture/monitor_text3.png').convert()
monitor_text4 = pygame.image.load(dir_path+'/data/texture/monitor_text4.png').convert()
monitor_text5 = pygame.image.load(dir_path+'/data/texture/monitor_text5.png').convert()
monitor_text6 = pygame.image.load(dir_path+'/data/texture/monitor_text6.png').convert()
monitor_text7 = pygame.image.load(dir_path+'/data/texture/monitor_text7.png').convert()
monitor_text8 = pygame.image.load(dir_path+'/data/texture/monitor_text8.png').convert()
monitor_text9 = pygame.image.load(dir_path+'/data/texture/monitor_text9.png').convert()
monitor_text10 = pygame.image.load(dir_path+'/data/texture/monitor_text10.png').convert()
monitor_text11 = pygame.image.load(dir_path+'/data/texture/monitor_text11.png').convert()
monitor_text12 = pygame.image.load(dir_path+'/data/texture/monitor_text12.png').convert()
monitor_text13 = pygame.image.load(dir_path+'/data/texture/monitor_text13.png').convert()
monitor_text14 = pygame.image.load(dir_path+'/data/texture/monitor_text14.png').convert()
monitor_text15 = pygame.image.load(dir_path+'/data/texture/monitor_text15.png').convert()
monitor_text16 = pygame.image.load(dir_path+'/data/texture/monitor_text16.png').convert()
monitor_text17 = pygame.image.load(dir_path+'/data/texture/monitor_text17.png').convert()
monitor_text18 = pygame.image.load(dir_path+'/data/texture/monitor_text18.png').convert()
monitor_text19 = pygame.image.load(dir_path+'/data/texture/monitor_text19.png').convert()
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
monitor_text10.set_colorkey((0, 0, 0))
monitor_text11.set_colorkey((0, 0, 0))
monitor_text12.set_colorkey((0, 0, 0))
monitor_text13.set_colorkey((0, 0, 0))
monitor_text14.set_colorkey((0, 0, 0))
monitor_text15.set_colorkey((0, 0, 0))
monitor_text16.set_colorkey((0, 0, 0))
monitor_text17.set_colorkey((0, 0, 0))
monitor_text18.set_colorkey((0, 0, 0))
monitor_text19.set_colorkey((0, 0, 0))
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
decor2.set_colorkey((255,255,255))
decor3.set_colorkey((255,255,255))

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

Znumbers_dot = pygame.image.load(dir_path+'/data/texture/Zdot.png').convert()
Znumbers_ang = pygame.image.load(dir_path+'/data/texture/Zangle.png').convert()
Znumbers_mps = pygame.image.load(dir_path+'/data/texture/Zmps.png').convert()

Znumbers[0].set_colorkey((229,213,213))
Znumbers[1].set_colorkey((229,213,213))
Znumbers[2].set_colorkey((229,213,213))
Znumbers[3].set_colorkey((229,213,213))
Znumbers[4].set_colorkey((229,213,213))
Znumbers[5].set_colorkey((229,213,213))
Znumbers[6].set_colorkey((229,213,213))
Znumbers[7].set_colorkey((229,213,213))
Znumbers[8].set_colorkey((229,213,213))
Znumbers[9].set_colorkey((229,213,213))
Znumbers_dot.set_colorkey((229,213,213))
Znumbers_ang.set_colorkey((229,213,213))
Znumbers_mps.set_colorkey((229,213,213))

Znumbers[0].set_alpha(215)
Znumbers[1].set_alpha(215)
Znumbers[2].set_alpha(215)
Znumbers[3].set_alpha(215)
Znumbers[4].set_alpha(215)
Znumbers[5].set_alpha(215)
Znumbers[6].set_alpha(215)
Znumbers[7].set_alpha(215)
Znumbers[8].set_alpha(215)
Znumbers[9].set_alpha(215)
Znumbers_dot.set_alpha(215)
Znumbers_ang.set_alpha(215)
Znumbers_mps.set_alpha(215)

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

book_page = [0]*128
for i in range(51): book_page[i] = pygame.image.load(dir_path+'/data/texture/book'+str(i+1)+'.png').convert()

book_coffee = pygame.image.load(dir_path+'/data/texture/book_coffee.png').convert()
book_coffee.set_colorkey((0,0,0))
book_coffee.set_alpha(127)

shadow_book = pygame.image.load(dir_path+'/data/texture/shadow_book.png').convert()
shadow_book.set_colorkey((255,0,0))
shadow_book.set_alpha(63)

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
abort_button_base[0].set_colorkey((143,143,143))
abort_button_base[1].set_colorkey((143,143,143))
abort_button_base[2].set_colorkey((143,143,143))
abort_button_base[3].set_colorkey((143,143,143))
abort_button_base[4].set_colorkey((143,143,143))
abort_button_base[5].set_colorkey((143,143,143))

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

#Загрузка текстур закончилась


#Загрузка звуков

button_tub = pygame.mixer.Sound(dir_path+'/data/audio/button_tub.mp3')
monitor_tub = pygame.mixer.Sound(dir_path+'/data/audio/monitor_tub.mp3')
tugger_sound = pygame.mixer.Sound(dir_path+'/data/audio/tugger_sound.mp3')
koff_tugger = pygame.mixer.Sound(dir_path+'/data/audio/koff_tugger.mp3')
numpud_tub = pygame.mixer.Sound(dir_path+'/data/audio/numpad_tub.mp3')

#Загрузка звуков закончилась

    
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

def rot_center(image, rect, angle): #Функция поворота
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

def changColor(image, color): #Функция, меняющая цвет
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(color)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage

#Объявление переменных

height = 350
x_pos = 0
y_pos = 0
speed = 5
angle = 45
G = 1
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
enable_5 = False
enable_6 = False
enable_7 = False
enable_8 = False
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
oblako_pos = [(0,0)]*1024
oblako_speed = [0]*1024
oblako_active = [False]*1024
oblako_type = [0]*1024
ED_tick = 0
ED_subtick = 0
Energy_potencial = 0
Energy_kinetikal = 0
Energy_body = 0
FS_bool = False
stime = 0
simspeed_enable = False
sim_angle = -90
smoke_count = -1
smoke_active = [False]*32
smoke_posx = [-4]*32
smoke_posy = [-4]*32
smoke_a = [0]*32
smoke_tick = 0
smoke_spawntick = 0
simspeed_on = False
simspeed_set = False
speed_xr = 0
speed_yr = 0
speed_or = 0
EP_save = [(0,0,0)]*16364
file_name = [0]*5
file_datetime = [0]*5
file_speed = [0]*5
file_angle = [0]*5
file_height = [0]*5
file_mass = [0]*5
file_koff = [0]*5
if randint(0,5) == 0: inputfilename = ['эксперемент I','эксперемент II','эксперемент III','эксперемент IV']
else: inputfilename = ['эксперемент 1','эксперемент 2','эксперемент 3','эксперемент 4']
file_namechange = -1
filename_tick = True
filename_subtick = 0
AB_tick = 0
AB_bool = False
speed_x_save = [0]*16364
speed_y_save = [0]*16364
speed_o_save = [0]*16364
angle_save = [0]*16364
perfect_line = False
Atick_pmsubtick = 0
BS_a = 255
BS_bool = True
PL_a = 0
PL_bool = False
loadtick = 0
asbutton_tick = [0,0,0,0]
asbutton_play = [False,False,False,False]
asbutton_subtick = [0,0,0,0]
addsettings_panel_tick = 0
addsettings_panel_subtick = 0
addsettings_panel_bool = False
random_nake = randint(0,3)
random_nake_x = randint(16,106)
if random_nake == 1: random_nake_y = randint(614,619)
elif random_nake == 2: random_nake_y = randint(614,617)
elif random_nake == 3: random_nake_y = randint(614,618)
airship_pos = [randint(0,2833),300+randint(0,100)]
airship_tick = 0
airship_subtick = 0
airship_turn = bool(randint(0,1))
TF = randint(0,4)
TF_tick = 0
addsettings_panel_closeandopen = False
ASP_tick = 0
monitor_LD = [False,False,False,False]
monitor_LD_tick = 0
monitor_savetick = 0
superangle_tick = 0
superangle_subtick = 0
addsettings_menu = "None"
addsettings_menu_past = "None"
array_subtick = [0]*64
array_tick = [0]*64
array_trigger = [False]*64
array_bool = [False]*64
superangle_DD = 45
superangle_MM = 0
superangle_SS = 0
superangle = 45
IT1_a = 0
IT1_bool = False
gravity_a = [0]*7
gravity_bit_active = [True]*4
gravity_bit_pos = [randint(874,935),randint(874,935),randint(874,935),randint(874,935)]
gravity_bit_turn = [bool(randint(0,1))]*4
gravity_up_button_bool = False
gravity_down_button_bool = False
gravity_setbase_button_bool = False
array_bool[7] = (randint(0,5)==0)
drlevel = [3,3,3]
plotnost_cast_pos_x = [0]*200
for i in range(200): plotnost_cast_pos_x[i] = randint(0,49)
plotnost_cast_pos_y = [0]*200
for i in range(200): plotnost_cast_pos_y[i] = randint(0,49)
plotnost_cast_speed_x = [0]*200
for i in range(200): plotnost_cast_speed_x[i] = (randint(-50,50)/100)
plotnost_cast_speed_y = [0]*200
for i in range(200): plotnost_cast_speed_y[i] = (randint(-50,50)/100)
plotnost = 1
volume = 1
sqr = 1
realkoss = 0
pva = 0
plotnost_up_button_bool = False
plotnost_down_button_bool = False
plotnost_setbase_button_bool = False
pva_lamplist = [False,False,False]
fps_past_list = [1]*16
dvig_angle = 0
VS_volume_tugger_pos = 0
VS_sqr_tugger_pos = 0
VS_volume_tugger_take = False
VS_sqr_tugger_take = False
VS_volume_tugger_postake = 0
VS_sqr_tugger_postake = 0
VS_base_button_bool = False
tick = 0
tower_enabled = False
angle_enabled = False
avtosave_tick = 0
avtosave_mode = "1m"
avtosave_exitmode = False
book_coffee_page = randint(3,44)
vol = 40

#Переменные объявленны

#Функции загрузки - сохранения файла

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

def load_file(ID):
    if ID == 5: F = open(dir_path+'/data/save/avtosave.txt','r', encoding='utf-8')
    else: F = open(dir_path+'/data/save/save'+str(ID)+'.txt','r', encoding='utf-8')

    S = F.readline()
    file_name[ID-1] = (str(S))[7:len(S)-1]
    
    while True:
        S = F.readline()

        if S == "end": break
        else:
            V,D,B = S.split()
            if V == "datetime": file_datetime[ID-1] = str(B)
            if V == "speed":
                if float(B) == int(float(B)): file_speed[ID-1] = int(B)
                else: file_speed[ID-1] = float(B)
            if V == "angle":
                if B[0] == "|":
                    file_angle[ID-1] = B
                else:
                    if float(B) == int(float(B)): file_angle[ID-1] = int(B)
                    else: file_angle[ID-1] = float(B)
            if V == "height":
                if float(B) == int(float(B)): file_height[ID-1] = int(B)
                else: file_height[ID-1] = float(B)
            if V == "mass":
                if float(B) == int(float(B)): file_mass[ID-1] = int(B)
                else: file_mass[ID-1] = float(B)
            if V == "koff":
                if float(B) == int(float(B)): file_koff[ID-1] = int(B)
                else: file_koff[ID-1] = float(B)
    
def save_file(ID):
    if ID == 5: F = open(dir_path+'/data/save/avtosave.txt','w', encoding='utf-8')
    else: F = open(dir_path+'/data/save/save'+str(ID)+'.txt','w', encoding='utf-8')

    now = str(datetime.datetime.now())

    F1 = (now[17])
    F2 = (now[18])   
    F3 = (now[2])
    F4 = (now[3])
    F5 = (now[5])
    F6 = (now[6])
    F7 = (now[8])
    F8 = (now[9])
    F9 = (now[11])
    F10 = (now[12])
    F11 = (now[14])
    F12 = (now[15])

    d = F7+F8+F5+F6+F3+F4+F9+F10+F11+F12+F1+F2

    if speed_word != '': ps = int(speed_word)
    else: ps = 0
    if mass_word != '': pm = int(mass_word)
    else: pm = 0

    if (speed_how != "meterspersecond"):
        if (speed_how == "kilometersperhour"): ps = ps/3.6
        if (speed_how == "santimeterspersecond"): ps = ps/100
    if (mass_how != "kg"):
        if (mass_how == "ton"): pm = pm*1000
        if (mass_how == "gramm"): pm = pm/1000

    if ps == int(ps): ps = int(ps)
    if pm == int(pm): pm = int(pm)

    if ((600-height)/10) == int((600-height)/10): h = int((600-height)/10)
    else: h = ((600-height)/10)

    if not(presser_on): k = '0'
    else:
        if rotor_ticker_bool:
            if koff_input == '': '0'
            else:
                k = koff_input
                if len(k) > 1: k = k[0] + '.' + k[1:]
        else:
            koff, kof_word = rotor_update(rotor_angle)
            k = kof_word

    if (array_tick[0] == 4):

            SAD = str(superangle_DD)
            if len(SAD) < 2: SAD = '0'+SAD
            SAM = str(superangle_MM)
            if len(SAM) < 2: SAM = '0'+SAM
            SAS = str(superangle_SS)
            if len(SAS) < 2: SAS = '0'+SAS

            ea = '|'+SAD+'|'+SAM+'|'+SAS+'|'
    else: ea = angle
        
    if ID == 5: F.write("name = автосохранение\n")
    else: F.write("name = "+inputfilename[ID-1]+"\n")
    F.write("datetime = "+d+"\n")
    F.write("speed = "+str(ps)+"\n")
    F.write("angle = "+str(ea)+"\n")
    F.write("height = "+str(h)+"\n")
    F.write("mass = "+str(pm)+"\n")
    F.write("koff = "+k+"\nend")
    F.close()

def save_settings():
    global draw_parabola
    F_settings = open(dir_path+'/data/save/settings.txt','w')
    F_settings.write("draw_parabola = "+str(int(draw_parabola))+"\nend")
    F_settings.close()


# Загрузка файлов
load_settings()
load_file(1)
load_file(2)
load_file(3)
load_file(4)
load_file(5)


#Дополнительные функции и функции отрисовки  

def rotor_update(rotor_angle):
    
    if (rotor_angle == 180): F = 0
    else: F = (int(int((rotor_angle+180)*10)/18))
    if (F/100 == 0) or (F/100 == 1):kof_word = str(int(F/100))
    else:kof_word = str(F/100)

    koff = F/100

    return koff, kof_word

def RPNW(P,H,G):

    P = P*1.2255
    g = G*9.80665
    M = 0.0289644
    R = 8.31447
    T = 288.15

    NP = P * math.e**((-M*g*H)/(R*T))
    
    return NP

def dvig_update(angle):

    (279, 788+sideshow_pos_y)

    xa = 9*math.cos(math.radians(angle))
    ya = -9*math.sin(math.radians(angle))

    dvig_palka_rect = dvig_palka.get_rect(center=(294+ya,803+sideshow_pos_y-xa)) 
    dvig_palka2, dvig_palka_p = rot_center(dvig_palka, dvig_palka_rect, math.degrees(math.atan2(-9*math.sin(math.radians(90+angle)), 27)))
    dvig_palka2.set_colorkey((0,0,0))
    Window.blit(dvig_palka2, dvig_palka_p)

    XA = 9*math.cos(math.radians(90+angle))

    Window.blit(dvig_push, (294+23+XA,801+sideshow_pos_y))

    dvig_rotor_rect = dvig_rotor.get_rect(center=(294,803+sideshow_pos_y)) 
    dvig_rotor2, dvig_rotor_p = rot_center(dvig_rotor, dvig_rotor_rect, 180+angle)
    dvig_rotor2.set_colorkey((0,0,0))
    Window.blit(dvig_rotor2, dvig_rotor_p)
    
def get_random_posy():
    y = 60-randint(0,120)
    t = randint(3,4)
    for i in range(t):
        k = 1.5+((randint(0,100))/100)
        if randint(0,1): y = y/k

    return y

def plotnost_cast_update(addspeed):
    for i in range(200):
        plotnost_cast_pos_x[i] += plotnost_cast_speed_x[i]*addspeed
        if plotnost_cast_pos_x[i]+882 <= 883 or plotnost_cast_pos_x[i]+882 >= 931: plotnost_cast_speed_x[i] = -plotnost_cast_speed_x[i]
        plotnost_cast_pos_y[i] += plotnost_cast_speed_y[i]*addspeed
        if plotnost_cast_pos_y[i]+650 <= 651 or plotnost_cast_pos_y[i]+650 >= 699: plotnost_cast_speed_y[i] = -plotnost_cast_speed_y[i] 

    for i in range(round(plotnost*20)):
        pygame.draw.rect(Window, (0,0,0),(plotnost_cast_pos_x[i]+882, plotnost_cast_pos_y[i]+650, 1, 1))

def decorline_update(x,y,addspeed):
    global drlevel
    
    Window.blit(decoran8a, (x,y))
    for f in range(drlevel[0]): pygame.draw.rect(Window, (224,32,32),(x+f*6+5, y+4, 5, 3))
    for f in range(drlevel[1]): pygame.draw.rect(Window, (70,215,40),(x+f*6+5, y+9, 5, 3))    
    for f in range(drlevel[2]): pygame.draw.rect(Window, (38,60,204),(x+f*6+5, y+14, 5, 3))

def plotnost_num_print(S,color):

    if S == int(S): S = int(S)

    S = str(S)

    if len(S) == 4:
        Window.blit(changColor(plotnost_num[int(S[0])],color),(883,629))
        Window.blit(changColor(plotnost_dot,color),(892,629))
        Window.blit(changColor(plotnost_num[int(S[2])],color),(895,629))
        Window.blit(changColor(plotnost_num[int(S[3])],color),(904,629))
    elif len(S) == 3:
        Window.blit(changColor(plotnost_num[int(S[0])],color),(888,629))
        Window.blit(changColor(plotnost_dot,color),(897,629))
        Window.blit(changColor(plotnost_num[int(S[2])],color),(900,629))
    elif len(S) == 1:
        Window.blit(changColor(plotnost_num[int(S[0])],color),(894,629))
    else:
        Window.blit(changColor(plotnost_num[int(S[0])],color),(889,629))
        Window.blit(changColor(plotnost_num[int(S[1])],color),(898,629))
 
def print_g(S,x,y):
    if (S == 'g'):
        Window.blit(gravityshow[11], (x,y))
        if len(S)>1:
            print_g(S[1:],x+5,y)
    else:
        if S[0] == ".":
            Window.blit(gravityshow[10], (x,y))
            if len(S)>1:
                print_g(S[1:],x+2,y)
        else:
            Window.blit(gravityshow[int(S[0])], (x,y))
            if len(S)>1:
               print_g(S[1:],x+6,y)
           
def gravityshow_update(g,addx,addy):
    if g == int(g): g = int(g)

    S = str(g)+'g'

    if len(S) == 2: posx = 294
    elif len(S) == 3: posx = 291
    elif len(S) == 4: posx = 290
    elif len(S) == 5: posx = 287
    
    print_g(str(g)+'g',posx+addx,621+addy)
            
def create_oblako(h):
    if bool(randint(0,1)):
        oblako_pos[h] = (randint(-21,1419),get_random_posy())
        oblako_active[h] = True
        oblako_speed[h] = 0.25 + ((125 - randint(0,250))/10000)
    else:
        oblako_pos[h] = (randint(0,1440),get_random_posy())
        oblako_active[h] = True
        oblako_speed[h] = -(0.25 + ((125 - randint(0,250))/10000))

    oblako_type[i] = randint(0,3)

for i in range(256): create_oblako(i)

def VS_printtext_sqr(S,x,y):
    if (S == 'M'):
        Window.blit(VS_sqr_M, (x,y))
        if len(S)>1:
            VS_printtext_sqr(S[1:],x+10,y)
    else:
        if S[0] == ".":
            Window.blit(VS_sqr_dot, (x,y))
            if len(S)>1:
                VS_printtext_sqr(S[1:],x+2,y)
        else:
            Window.blit(VS_sqr_num[int(S[0])], (x,y))
            if len(S)>1:
                VS_printtext_sqr(S[1:],x+6,y)
                
def VS_printtext_volume(S,x,y):
    if (S == 'M'):
        Window.blit(VS_volume_M, (x,y))
        if len(S)>1:
            VS_printtext_volume(S[1:],x+10,y)
    else:
        if S[0] == ".":
            Window.blit(VS_volume_dot, (x,y))
            if len(S)>1:
                VS_printtext_volume(S[1:],x+2,y)
        else:
            Window.blit(VS_volume_num[int(S[0])], (x,y))
            if len(S)>1:
                VS_printtext_volume(S[1:],x+6,y)

def VS_countpos(S):

    count = 0
    for i in S:
        if i == "M":
            count += 5
        elif i == ".":
            count += 1
        else:
            count += 3

    F = 25-count
        
    return F
               
def VS_text_update(V,S):
    if V == int(V): V = int(V)
    if S == int(S): S = int(S)
    
    VF = str(V)+"M"
    SF = str(S)+"M"

    VS_printtext_volume(VF,883+VS_countpos(VF),682)
    VS_printtext_sqr(SF,883+VS_countpos(SF),648)
    
def airship_update(masch,addspeed):
    global airship_pos, airship_tick, airship_turn, airship_subtick

    airship_subtick += 1*addspeed
    if airship_subtick >= 6:
        airship_tick = int(not bool(airship_tick))
        airship_subtick -= 6

    if airship_pos[0] > 2880:
        airship_turn = False
        airship_pos[1] = 300+randint(0,100)
    if airship_pos[0] < -96:
        airship_turn = True
        airship_pos[1] = 300+randint(0,100)
        
    if airship_turn:
        if airship_tick == 0: airship = pygame.transform.flip(airship1, True, False)
        else: airship = pygame.transform.flip(airship2, True, False)
        airship_pos[0] += 0.5*addspeed
    else:
        if airship_tick == 0: airship = airship1
        else: airship = airship2
        airship_pos[0] -= 0.5*addspeed
        
    if masch > 4:
        if masch == 8: rm = 1
        elif masch == 16: rm = 2

        Window.blit(pygame.transform.scale(airship,(round(96/rm),round(31/rm))),(round(airship_pos[0]/rm),round((600-(((airship_pos[1])+170))/rm))))         

def gravity_bit_update(addspeed):

    global gravity_bit_turn, gravity_bit_pos, gravity_bit_active
    
    for i in range(4):

        if gravity_bit_active[i]:
        
            if gravity_bit_turn[i]:
                gravity_bit_pos[i] += 4*addspeed
                Window.blit(gravity_bit,(round(gravity_bit_pos[i]),(704+i*4)))

            else:
                gravity_bit_pos[i] -= 4*addspeed
                Window.blit(pygame.transform.flip(gravity_bit, True, False),(round(gravity_bit_pos[i]),(704+i*4)))

            if gravity_bit_pos[i] >= 935 or gravity_bit_pos[i] <= 874: gravity_bit_active[i] = False
            
        else:
            if randint(0,15) == 0:
                gravity_bit_active[i] = True
                if bool(randint(0,1)):
                    gravity_bit_pos[i] = 874
                    gravity_bit_turn[i] = True
                else:
                    gravity_bit_pos[i] = 935
                    gravity_bit_turn[i] = False
                    
def oblako_update(masch,addspeed):

    rm = masch

    if masch == 16: masch = 1
    elif masch == 8: masch = 2
    elif masch == 4: masch = 4
    elif masch == 2: masch = 8
    elif masch == 1: masch = 16
    
    for i in range(1024):
        if oblako_active[i]:
            oblako_speed[i] += ((125 - randint(0,250))/10000)

            if 0:
                for j in range(1024):
                    if oblako_active[j]:
                        if ((oblako_pos[j])[0]) > (oblako_pos[i])[0]-10 and ((oblako_pos[j])[0]) < (oblako_pos[i])[0]+10:
                            F = ((((oblako_pos[j])[0] - (oblako_pos[i])[0]))/10000)
                            oblako_speed[i] += F
            
            if oblako_speed[i] > 1: oblako_speed[i] = 1
            if oblako_speed[i] < -1: oblako_speed[i] = -1
            oblako_pos[i] = (((oblako_pos[i])[0])+oblako_speed[i]*addspeed,((oblako_pos[i])[1]))
            if ((oblako_pos[i])[0] > 1440) or ((oblako_pos[i])[0] < -21):
                oblako_speed[i] = oblako_speed[i] * -1
                oblako_pos[i] = (((oblako_pos[i])[0]),get_random_posy())

            X = ((oblako_pos[i])[0])*masch
            Y = 600-(((oblako_pos[i])[1]+170)*masch)
            
            if X < 1440 and Y > 0: Window.blit(pygame.transform.scale(oblako[oblako_type[i]],(21*masch,14*masch)),(X,Y))

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

def draw_apoligon(color,pos,drawposs,drawpose):
    t = pygame.Surface((1440,810), pygame.SRCALPHA)   
    pygame.draw.polygon(t, color, pos)
    Window.blit(t, drawposs, (drawposs,drawpose))

def shadow_rect(D,sx,sy,ex,ey,a,s):
        D1 = D*math.tan(math.radians(s))
        D2 = D*math.tan(math.radians(s))
        
        pos1 = [sx+D1*math.cos(math.radians(a)),sy+D2*math.sin(math.radians(a))] 
        pos2 = [sx+D1*math.cos(math.radians(a)),ey+D2*math.sin(math.radians(a))]   
        pos4 = [ex+D1*math.cos(math.radians(a)),sy+D2*math.sin(math.radians(a))]
        pos3 = [ex+D1*math.cos(math.radians(a)),ey+D2*math.sin(math.radians(a))]
        
        draw_apoligon((0,0,0,63),[[sx,sy],[ex,sy],pos4,pos3,pos2,[sx,ey]],[sx,sy],[ex,ey])
        
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

def set_code(A):
    if (A == "а" or A == "А"): return "00"
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
    elif (A == "х" or A == "Х"): return "22"
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
    elif (A == "/"): return "80"
    elif (A == "№"): return "81"
    elif (A == "_"): return "82"
    elif (A == "|"): return "84"
    
    else: return "83"

def monitor_text(S,x,y,alpha):
    SPR = MT[int(set_code(S[0]))]
    SPR.set_alpha(alpha)
    Window.blit(SPR, (x,y-2))
    if len(S)>1:
        monitor_text(S[1:],x+6,y,alpha)

def print_znum(S,x,y):
    T = S[0]
    if T == ".":
        Window.blit(Znumbers_dot, (x,y))
        if len(S) > 1: print_znum(S[1:],x+4,y)
    elif T == "№":
        Window.blit(Znumbers_ang, (x,y))
        if len(S) > 1: print_znum(S[1:],x+8,y)
    elif T == "#":
        Window.blit(Znumbers_mps, (x,y))
        if len(S) > 1: print_znum(S[1:],x+12,y) 
    else:
        Window.blit(Znumbers[int(T)], (x,y))
        if len(S) > 1: print_znum(S[1:],x+12,y)

def draw_angle(x,y,angle):

    x -= 12

    pygame.draw.aaline(Window, (0,0,0), (x+28+25,y+34),(x+78,y+34),1)

    xa = 25*math.cos(math.radians(angle))
    ya = 25*math.sin(math.radians(angle))
                
    pygame.draw.aaline(Window, (0,0,0), (x+28+25,y+34),(x+28+25+xa,y+34+ya),1)

    if angle > 0 and int(angle) != 180:
        if int(angle) == 90:
            pygame.draw.aaline(Window, (0,0,0), (x+28+25,y+34+8),(x+28+25+8,y+34+8),1)
            pygame.draw.aaline(Window, (0,0,0), (x+28+25+8,y+34),(x+28+25+8,y+34+8),1)
        else:
            for i in range(0,int(angle),1):
                xa = 8*math.cos(math.radians(i))
                ya = 8*math.sin(math.radians(i))
                pygame.draw.aaline(Window, (0,0,0), (x+28+25+xa,y+34+ya),(x+28+25+xa,y+34+ya),1)
    else:
        if int(angle) == -90:
            pygame.draw.aaline(Window, (0,0,0), (x+28+25,y+34-8),(x+28+25+8,y+34-8),1)
            pygame.draw.aaline(Window, (0,0,0), (x+28+25+8,y+34),(x+28+25+8,y+34-8),1)
        else:
            for i in range(int(-angle),0,-1):
                xa = 8*math.cos(math.radians(i))
                ya = -8*math.sin(math.radians(i))
                pygame.draw.aaline(Window, (0,0,0), (x+28+25+xa,y+34+ya),(x+28+25+xa,y+34+ya),1)
    
    
        
def monitor_time_update(x,y,menu):
    global enable_1, enable_2, enable_3, enable_4, enable_5, enable_6, enable_7, enable_8
    
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

    enable_1 = False
    enable_2 = False
    enable_3 = False
    enable_4 = False
    enable_5 = False
    enable_6 = False
    enable_7 = False
    enable_8 = False
            
    if (x_mouse >= 559 and x_mouse <= 711) and (y_mouse >= 623 and y_mouse <= 734) and not(menu == "main" or menu == "settings" or menu == "loadsave"):
        monitor_fileinfo.set_alpha(255)
        monitor_saveinfo.set_alpha(255)
        filepoint = 255
    else:
        monitor_fileinfo.set_alpha(127)
        monitor_saveinfo.set_alpha(127)
        filepoint = 127
        if x_mouse >= x+12 and x_mouse <= x+121+12:
            if y_mouse >= y+6-28 and y_mouse <= y+6-28+9: enable_1 = True
            else: enable_1 = False
            if y_mouse >= y+18-28 and y_mouse <= y+18-28+9: enable_2 = True
            else: enable_2 = False
            if y_mouse >= y+30-28 and y_mouse <= y+30-28+9: enable_3 = True
            else: enable_3 = False
            if y_mouse >= y+42-28 and y_mouse <= y+42-28+9: enable_4 = True
            else: enable_4 = False
            if y_mouse >= y+54-28 and y_mouse <= y+54-28+9: enable_5 = True
            else: enable_5 = False
            if y_mouse >= y+66-28 and y_mouse <= y+66-28+9: enable_6 = True
            else: enable_6 = False
            if y_mouse >= y+78-28 and y_mouse <= y+78-28+9: enable_7 = True
            else: enable_7 = False
            if y_mouse >= y+90-28 and y_mouse <= y+90-28+9: enable_8 = True
            else: enable_8 = False
    
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
        if enable_3: monitor_text19.set_alpha(255); monitor_text19.set_alpha(255); tra = 255
        else: monitor_text19.set_alpha(127); monitor_text19.set_alpha(127); tra = 127
        #if enable_4: monitor_text.set_alpha(255); monitor_text9.set_alpha(255)
        #else: monitor_text8.set_alpha(127); monitor_text9.set_alpha(127)  

        Window.blit(monitor_text5,(x+12,y+6-28))
        Window.blit(monitor_text19,(x+12,y+30-28))
        monitor_text(str(vol),x+12+71,y+30-28,tra)
        #if draw_parabola : Window.blit(monitor_text6,(x+12,y+30-28))
        #else: Window.blit(monitor_text7,(x+12,y+30-28))
        #if 0 : Window.blit(monitor_text8,(x+12,y+40-28))
        #else: Window.blit(monitor_text9,(x+12,y+40-28))

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

    if menu == "loadsave":
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text10.set_alpha(255)
        else: monitor_text10.set_alpha(127)
        if enable_4: monitor_text11.set_alpha(255)
        else: monitor_text11.set_alpha(127)
        if enable_5: monitor_text12.set_alpha(255)
        else: monitor_text12.set_alpha(127)
        if enable_6: monitor_text13.set_alpha(255)
        else: monitor_text13.set_alpha(127)
        if enable_8: monitor_text18.set_alpha(255)
        else: monitor_text18.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))
        
        Window.blit(monitor_text10,(x+12,y+30-28))
        Window.blit(monitor_text11,(x+12,y+42-28))
        Window.blit(monitor_text12,(x+12,y+54-28))
        Window.blit(monitor_text13,(x+12,y+66-28))

        Window.blit(monitor_text18,(x+12,y+90-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))
        if enable_5: Window.blit(monitor_textset,(x+5,y+56-28))
        if enable_6: Window.blit(monitor_textset,(x+5,y+68-28))
        if enable_8: Window.blit(monitor_textset,(x+5,y+92-28))


    if menu == "filesave":
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text10.set_alpha(255)
        else: monitor_text10.set_alpha(127)
        if enable_4: monitor_text11.set_alpha(255)
        else: monitor_text11.set_alpha(127)
        if enable_5: monitor_text12.set_alpha(255)
        else: monitor_text12.set_alpha(127)
        if enable_6: monitor_text13.set_alpha(255)
        else: monitor_text13.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))
        
        Window.blit(monitor_text10,(x+12,y+30-28))
        Window.blit(monitor_text11,(x+12,y+42-28))
        Window.blit(monitor_text12,(x+12,y+54-28))
        Window.blit(monitor_text13,(x+12,y+66-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))
        if enable_5: Window.blit(monitor_textset,(x+5,y+56-28))
        if enable_6: Window.blit(monitor_textset,(x+5,y+68-28))

    if menu == "load_1":

        Window.blit(monitor_saveinfo,(559,y-25))

        monitor_text(file_name[0],633 - 3 * len(file_name[0]) ,y-25+6,filepoint)

        monitor_text((file_datetime[0])[0:2],594+14,y-25+18,filepoint)
        monitor_text((file_datetime[0])[2:4],608+14,y-25+18,filepoint)
        monitor_text((file_datetime[0])[4:6],622+14,y-25+18,filepoint)
        monitor_text((file_datetime[0])[6:8],640+14,y-25+18,filepoint)
        monitor_text((file_datetime[0])[8:10],654+14,y-25+18,filepoint)
        monitor_text((file_datetime[0])[10:12],668+14,y-25+18,filepoint)

        monitor_text(str(file_speed[0]) + " м/с",626,y-25+38,filepoint)
        monitor_text(str(file_angle[0]) + "№",626,y-25+48,filepoint)
        monitor_text(str(file_height[0]) + " м",626,y-25+58,filepoint)
        monitor_text(str(file_mass[0]) + " кг",626,y-25+68,filepoint)
        monitor_text(str(file_koff[0]),626,y-25+78,filepoint)
        
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text14.set_alpha(255)
        else: monitor_text14.set_alpha(127)
        #if enable_4: monitor_text15.set_alpha(255)
        #else: monitor_text15.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))
        Window.blit(monitor_text14,(x+12,y+30-28))
        #Window.blit(monitor_text15,(x+12,y+42-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        #if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))

    if menu == "load_2":

        Window.blit(monitor_saveinfo,(559,y-25))

        monitor_text(file_name[1],633 - 3 * len(file_name[1]) ,y-25+6,filepoint)

        monitor_text((file_datetime[1])[0:2],594+14,y-25+18,filepoint)
        monitor_text((file_datetime[1])[2:4],608+14,y-25+18,filepoint)
        monitor_text((file_datetime[1])[4:6],622+14,y-25+18,filepoint)
        monitor_text((file_datetime[1])[6:8],640+14,y-25+18,filepoint)
        monitor_text((file_datetime[1])[8:10],654+14,y-25+18,filepoint)
        monitor_text((file_datetime[1])[10:12],668+14,y-25+18,filepoint)

        monitor_text(str(file_speed[1]) + " м/с",626,y-25+38,filepoint)
        monitor_text(str(file_angle[1]) + "№",626,y-25+48,filepoint)
        monitor_text(str(file_height[1]) + " м",626,y-25+58,filepoint)
        monitor_text(str(file_mass[1]) + " кг",626,y-25+68,filepoint)
        monitor_text(str(file_koff[1]),626,y-25+78,filepoint)
        
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text14.set_alpha(255)
        else: monitor_text14.set_alpha(127)
        #if enable_4: monitor_text15.set_alpha(255)
        #else: monitor_text15.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))
        Window.blit(monitor_text14,(x+12,y+30-28))
        #Window.blit(monitor_text15,(x+12,y+42-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        #if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))

    if menu == "load_3":

        Window.blit(monitor_saveinfo,(559,y-25))

        monitor_text(file_name[2],633 - 3 * len(file_name[2]) ,y-25+6,filepoint)

        monitor_text((file_datetime[2])[0:2],594+14,y-25+18,filepoint)
        monitor_text((file_datetime[2])[2:4],608+14,y-25+18,filepoint)
        monitor_text((file_datetime[2])[4:6],622+14,y-25+18,filepoint)
        monitor_text((file_datetime[2])[6:8],640+14,y-25+18,filepoint)
        monitor_text((file_datetime[2])[8:10],654+14,y-25+18,filepoint)
        monitor_text((file_datetime[2])[10:12],668+14,y-25+18,filepoint)

        monitor_text(str(file_speed[2]) + " м/с",626,y-25+38,filepoint)
        monitor_text(str(file_angle[2]) + "№",626,y-25+48,filepoint)
        monitor_text(str(file_height[2]) + " м",626,y-25+58,filepoint)
        monitor_text(str(file_mass[2]) + " кг",626,y-25+68,filepoint)
        monitor_text(str(file_koff[2]),626,y-25+78,filepoint)
        
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text14.set_alpha(255)
        else: monitor_text14.set_alpha(127)
        #if enable_4: monitor_text15.set_alpha(255)
        #else: monitor_text15.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))
        Window.blit(monitor_text14,(x+12,y+30-28))
        #Window.blit(monitor_text15,(x+12,y+42-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        #if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))
        
    if menu == "load_4":

        Window.blit(monitor_saveinfo,(559,y-25))

        monitor_text(file_name[3],633 - 3 * len(file_name[3]) ,y-25+6,filepoint)

        monitor_text((file_datetime[3])[0:2],594+14,y-25+18,filepoint)
        monitor_text((file_datetime[3])[2:4],608+14,y-25+18,filepoint)
        monitor_text((file_datetime[3])[4:6],622+14,y-25+18,filepoint)
        monitor_text((file_datetime[3])[6:8],640+14,y-25+18,filepoint)
        monitor_text((file_datetime[3])[8:10],654+14,y-25+18,filepoint)
        monitor_text((file_datetime[3])[10:12],668+14,y-25+18,filepoint)

        monitor_text(str(file_speed[3]) + " м/с",626,y-25+38,filepoint)
        monitor_text(str(file_angle[3]) + "№",626,y-25+48,filepoint)
        monitor_text(str(file_height[3]) + " м",626,y-25+58,filepoint)
        monitor_text(str(file_mass[3]) + " кг",626,y-25+68,filepoint)
        monitor_text(str(file_koff[3]),626,y-25+78,filepoint)
        
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text14.set_alpha(255)
        else: monitor_text14.set_alpha(127)
        #if enable_4: monitor_text15.set_alpha(255)
        #else: monitor_text15.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))
        Window.blit(monitor_text14,(x+12,y+30-28))
        #Window.blit(monitor_text15,(x+12,y+42-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        #if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))

    if menu == "load_avto":

        Window.blit(monitor_saveinfo,(559,y-25))

        monitor_text(file_name[4],633 - 3 * len(file_name[4]) ,y-25+6,filepoint)

        monitor_text((file_datetime[4])[0:2],594+14,y-25+18,filepoint)
        monitor_text((file_datetime[4])[2:4],608+14,y-25+18,filepoint)
        monitor_text((file_datetime[4])[4:6],622+14,y-25+18,filepoint)
        monitor_text((file_datetime[4])[6:8],640+14,y-25+18,filepoint)
        monitor_text((file_datetime[4])[8:10],654+14,y-25+18,filepoint)
        monitor_text((file_datetime[4])[10:12],668+14,y-25+18,filepoint)

        monitor_text(str(file_speed[4]) + " м/с",626,y-25+38,filepoint)
        monitor_text(str(file_angle[4]) + "№",626,y-25+48,filepoint)
        monitor_text(str(file_height[4]) + " м",626,y-25+58,filepoint)
        monitor_text(str(file_mass[4]) + " кг",626,y-25+68,filepoint)
        monitor_text(str(file_koff[4]),626,y-25+78,filepoint)
        
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text14.set_alpha(255)
        else: monitor_text14.set_alpha(127)
        #if enable_4: monitor_text15.set_alpha(255)
        #else: monitor_text15.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))
        Window.blit(monitor_text14,(x+12,y+30-28))
        #Window.blit(monitor_text15,(x+12,y+42-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        #if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))

    if menu == "save_1":

        Window.blit(monitor_fileinfo,(559,y-25))

        if file_namechange == 0 and len(inputfilename[0]) < 24:
            if filename_tick: F = inputfilename[0]+' '
            else: F = inputfilename[0]+'_'
        else: F = inputfilename[0]
        monitor_text(F,636 - 3 * len(F) ,y-25+6,filepoint)

        if speed_word != '': ps = int(speed_word)
        else: ps = 0
        if mass_word != '': pm = int(mass_word)
        else: pm = 0

        if (speed_how != "meterspersecond"):
                if (speed_how == "kilometersperhour"): ps = ps/3.6
                if (speed_how == "santimeterspersecond"): ps = ps/100
        if (mass_how != "kg"):
                if (mass_how == "ton"): pm = pm*1000
                if (mass_how == "gramm"): pm = pm/1000

        if ps == int(ps): ps = int(ps)
        if pm == int(pm): pm = int(pm)

        if (array_tick[0] == 4):
            
            SAD = str(superangle_DD)
            if len(SAD) < 2: SAD = '0'+SAD
            SAM = str(superangle_MM)
            if len(SAM) < 2: SAM = '0'+SAM
            SAS = str(superangle_SS)
            if len(SAS) < 2: SAS = '0'+SAS

            ea = '|'+SAD+'|'+SAM+'|'+SAS+'|'
            
        else: ea = angle
            
        monitor_text(str(ps) + " м/с",626,y-25+28,filepoint)
        monitor_text(str(ea) + "№",626,y-25+38,filepoint)
        if ((600-height)/10) == int((600-height)/10): monitor_text(str(int((600-height)/10)) + " м",626,y-25+48,filepoint)
        else: monitor_text(str((600-height)/10) + " м",626,y-25+48,filepoint)
        monitor_text(str(pm) + " кг",626,y-25+58,filepoint)
        if not(presser_on): monitor_text("0",626,y-25+68,filepoint)
        else:
            if rotor_ticker_bool:
                if koff_input == '': monitor_text("0",626,y-25+68,filepoint)
                else:
                    S = koff_input
                    if len(S) > 1: S = S[0] + '.' + S[1:]
                    monitor_text(S,626,y-25+68,filepoint)
            else:
                koff, kof_word = rotor_update(rotor_angle)
                monitor_text(kof_word,626,y-25+68,filepoint)
        
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text16.set_alpha(255)
        else: monitor_text16.set_alpha(127)
        if enable_4: monitor_text17.set_alpha(255)
        else: monitor_text17.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))
        Window.blit(monitor_text16,(x+12,y+30-28))
        Window.blit(monitor_text17,(x+12,y+42-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))

    if menu == "save_2":

        Window.blit(monitor_fileinfo,(559,y-25))

        if file_namechange == 1 and len(inputfilename[1]) < 24:
            if filename_tick: F = inputfilename[1]+' '
            else: F = inputfilename[1]+'_'
        else: F = inputfilename[1]
        monitor_text(F,636 - 3 * len(F) ,y-25+6,filepoint)

        if speed_word != '': ps = int(speed_word)
        else: ps = 0
        if mass_word != '': pm = int(mass_word)
        else: pm = 0

        if (speed_how != "meterspersecond"):
                if (speed_how == "kilometersperhour"): ps = ps/3.6
                if (speed_how == "santimeterspersecond"): ps = ps/100
        if (mass_how != "kg"):
                if (mass_how == "ton"): pm = pm*1000
                if (mass_how == "gramm"): pm = pm/1000

        if ps == int(ps): ps = int(ps)
        if pm == int(pm): pm = int(pm)

        if (array_tick[0] == 4):
            
            SAD = str(superangle_DD)
            if len(SAD) < 2: SAD = '0'+SAD
            SAM = str(superangle_MM)
            if len(SAM) < 2: SAM = '0'+SAM
            SAS = str(superangle_SS)
            if len(SAS) < 2: SAS = '0'+SAS

            ea = '|'+SAD+'|'+SAM+'|'+SAS+'|'
            
        else: ea = angle
        
        monitor_text(str(ps) + " м/с",626,y-25+28,filepoint)
        monitor_text(str(ea) + "№",626,y-25+38,filepoint)
        if ((600-height)/10) == int((600-height)/10): monitor_text(str(int((600-height)/10)) + " м",626,y-25+48,filepoint)
        else: monitor_text(str((600-height)/10) + " м",626,y-25+48,filepoint)
        monitor_text(str(pm) + " кг",626,y-25+58,filepoint)
        if not(presser_on): monitor_text("0",626,y-25+68,filepoint)
        else:
            if rotor_ticker_bool:
                if koff_input == '': monitor_text("0",626,y-25+68,filepoint)
                else:
                    S = koff_input
                    if len(S) > 1: S = S[0] + '.' + S[1:]
                    monitor_text(S,626,y-25+68,filepoint)
            else:
                koff, kof_word = rotor_update(rotor_angle)
                monitor_text(kof_word,626,y-25+68,filepoint)
                
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text16.set_alpha(255)
        else: monitor_text16.set_alpha(127)
        if enable_4: monitor_text17.set_alpha(255)
        else: monitor_text17.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))
        Window.blit(monitor_text16,(x+12,y+30-28))
        Window.blit(monitor_text17,(x+12,y+42-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))

    if menu == "save_3":

        Window.blit(monitor_fileinfo,(559,y-25))

        if file_namechange == 2 and len(inputfilename[2]) < 24:
            if filename_tick: F = inputfilename[2]+' '
            else: F = inputfilename[2]+'_'
        else: F = inputfilename[2]
        monitor_text(F,636 - 3 * len(F) ,y-25+6,filepoint)

        if speed_word != '': ps = int(speed_word)
        else: ps = 0
        if mass_word != '': pm = int(mass_word)
        else: pm = 0

        if (speed_how != "meterspersecond"):
                if (speed_how == "kilometersperhour"): ps = ps/3.6
                if (speed_how == "santimeterspersecond"): ps = ps/100
        if (mass_how != "kg"):
                if (mass_how == "ton"): pm = pm*1000
                if (mass_how == "gramm"): pm = pm/1000

        if ps == int(ps): ps = int(ps)
        if pm == int(pm): pm = int(pm)

        if (array_tick[0] == 4):
            
            SAD = str(superangle_DD)
            if len(SAD) < 2: SAD = '0'+SAD
            SAM = str(superangle_MM)
            if len(SAM) < 2: SAM = '0'+SAM
            SAS = str(superangle_SS)
            if len(SAS) < 2: SAS = '0'+SAS

            ea = '|'+SAD+'|'+SAM+'|'+SAS+'|'
            
        else: ea = angle
        
        monitor_text(str(ps) + " м/с",626,y-25+28,filepoint)
        monitor_text(str(ea) + "№",626,y-25+38,filepoint)
        if ((600-height)/10) == int((600-height)/10): monitor_text(str(int((600-height)/10)) + " м",626,y-25+48,filepoint)
        else: monitor_text(str((600-height)/10) + " м",626,y-25+48,filepoint)
        monitor_text(str(pm) + " кг",626,y-25+58,filepoint)
        if not(presser_on): monitor_text("0",626,y-25+68,filepoint)
        else:
            if rotor_ticker_bool:
                if koff_input == '': monitor_text("0",626,y-25+68,filepoint)
                else:
                    S = koff_input
                    if len(S) > 1: S = S[0] + '.' + S[1:]
                    monitor_text(S,626,y-25+68,filepoint)
            else:
                koff, kof_word = rotor_update(rotor_angle)
                monitor_text(kof_word,626,y-25+68,filepoint)
        
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text16.set_alpha(255)
        else: monitor_text16.set_alpha(127)
        if enable_4: monitor_text17.set_alpha(255)
        else: monitor_text17.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))
        Window.blit(monitor_text16,(x+12,y+30-28))
        Window.blit(monitor_text17,(x+12,y+42-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))
        
    if menu == "save_4":

        Window.blit(monitor_fileinfo,(559,y-25))

        if file_namechange == 3 and len(inputfilename[3]) < 24:
            if filename_tick: F = inputfilename[3]+' '
            else: F = inputfilename[3]+'_'
        else: F = inputfilename[3]
        monitor_text(F,636 - 3 * len(F) ,y-25+6,filepoint)

        if speed_word != '': ps = int(speed_word)
        else: ps = 0
        if mass_word != '': pm = int(mass_word)
        else: pm = 0

        if (speed_how != "meterspersecond"):
                if (speed_how == "kilometersperhour"): ps = ps/3.6
                if (speed_how == "santimeterspersecond"): ps = ps/100
        if (mass_how != "kg"):
                if (mass_how == "ton"): pm = pm*1000
                if (mass_how == "gramm"): pm = pm/1000

        if ps == int(ps): ps = int(ps)
        if pm == int(pm): pm = int(pm)

        if (array_tick[0] == 4):
            
            SAD = str(superangle_DD)
            if len(SAD) < 2: SAD = '0'+SAD
            SAM = str(superangle_MM)
            if len(SAM) < 2: SAM = '0'+SAM
            SAS = str(superangle_SS)
            if len(SAS) < 2: SAS = '0'+SAS

            ea = '|'+SAD+'|'+SAM+'|'+SAS+'|'
            
        else: ea = angle
                
        monitor_text(str(ps) + " м/с",626,y-25+28,filepoint)
        monitor_text(str(ea) + "№",626,y-25+38,filepoint)
        if ((600-height)/10) == int((600-height)/10): monitor_text(str(int((600-height)/10)) + " м",626,y-25+48,filepoint)
        else: monitor_text(str((600-height)/10) + " м",626,y-25+48,filepoint)
        monitor_text(str(pm) + " кг",626,y-25+58,filepoint)
        if not(presser_on): monitor_text("0",626,y-25+68,filepoint)
        else:
            if rotor_ticker_bool:
                if koff_input == '': monitor_text("0",626,y-25+68,filepoint)
                else:
                    S = koff_input
                    if len(S) > 1: S = S[0] + '.' + S[1:]
                    monitor_text(S,626,y-25+68,filepoint)
            else:
                koff, kof_word = rotor_update(rotor_angle)
                monitor_text(kof_word,626,y-25+68,filepoint)
        
        if enable_1: monitor_text5.set_alpha(255)
        else: monitor_text5.set_alpha(127)
        if enable_3: monitor_text16.set_alpha(255)
        else: monitor_text16.set_alpha(127)
        if enable_4: monitor_text17.set_alpha(255)
        else: monitor_text17.set_alpha(127)

        Window.blit(monitor_text5,(x+12,y+6-28))
        Window.blit(monitor_text16,(x+12,y+30-28))
        Window.blit(monitor_text17,(x+12,y+42-28))

        if enable_1: Window.blit(monitor_textset,(x+5,y+8-28))
        if enable_3: Window.blit(monitor_textset,(x+5,y+32-28))
        if enable_4: Window.blit(monitor_textset,(x+5,y+44-28))


def draw_lines(X,Y,tick,masch,color):

    for i in range (1,tick,1):
        yrydpos = 600-Y[i-1]
        rydpos = 600-Y[i]

        if perfect_line:

            if (masch >= 4): W = 1
            elif (masch >= 2) and (masch <= 2): W = 2
            else: W = 3
    
            pygame.draw.aaline(Window, color,((X[i]+105)/masch,(int((600-(rydpos/masch))))),((X[i-1]+105)/masch,(int((600-(yrydpos/masch))))),W)

            if  W == 2:
                pygame.draw.aaline(Window, color,((X[i]+105)/masch+1,(int((600-(rydpos/masch))))),((X[i-1]+105)/masch+1,(int((600-(yrydpos/masch))))),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch-1,(int((600-(rydpos/masch))))),((X[i-1]+105)/masch-1,(int((600-(yrydpos/masch))))),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch,(int((600-(rydpos/masch))))+1),((X[i-1]+105)/masch,(int((600-(yrydpos/masch))))+1),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch,(int((600-(rydpos/masch))))-1),((X[i-1]+105)/masch,(int((600-(yrydpos/masch))))-1),W)

            if W == 3:
                pygame.draw.aaline(Window, color,((X[i]+105)/masch+1,(int((600-(rydpos/masch))))),((X[i-1]+105)/masch+1,(int((600-(yrydpos/masch))))),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch-1,(int((600-(rydpos/masch))))),((X[i-1]+105)/masch-1,(int((600-(yrydpos/masch))))),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch,(int((600-(rydpos/masch))))+1),((X[i-1]+105)/masch,(int((600-(yrydpos/masch))))+1),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch,(int((600-(rydpos/masch))))-1),((X[i-1]+105)/masch,(int((600-(yrydpos/masch))))-1),W)

                pygame.draw.aaline(Window, color,((X[i]+105)/masch+1,(int((600-(rydpos/masch))))+1),((X[i-1]+105)/masch+1,(int((600-(yrydpos/masch))))+1),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch+1,(int((600-(rydpos/masch))))-1),((X[i-1]+105)/masch+1,(int((600-(yrydpos/masch))))-1),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch-1,(int((600-(rydpos/masch))))+1),((X[i-1]+105)/masch-1,(int((600-(yrydpos/masch))))+1),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch-1,(int((600-(rydpos/masch))))-1),((X[i-1]+105)/masch-1,(int((600-(yrydpos/masch))))-1),W)

                pygame.draw.aaline(Window, color,((X[i]+105)/masch+2,(int((600-(rydpos/masch))))),((X[i-1]+105)/masch+2,(int((600-(yrydpos/masch))))),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch-2,(int((600-(rydpos/masch))))),((X[i-1]+105)/masch-2,(int((600-(yrydpos/masch))))),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch,(int((600-(rydpos/masch))))+2),((X[i-1]+105)/masch,(int((600-(yrydpos/masch))))+2),W)
                pygame.draw.aaline(Window, color,((X[i]+105)/masch,(int((600-(rydpos/masch))))-2),((X[i-1]+105)/masch,(int((600-(yrydpos/masch))))-2),W)

        else:

            if (masch >= 8): W = 1
            elif (masch >= 2) and (masch <= 4): W = 2
            else: W = 3

            pygame.draw.line(Window, color,((X[i]+105)/masch,(int((600-(rydpos/masch))))),((X[i-1]+105)/masch,(int((600-(yrydpos/masch))))),W)

            

def text_print(S,x,y):
    SPR = IDL[int(set_code(S[0]))]
    Window.blit(SPR, (x,y))
    if len(S)>1:
        text_print(S[1:],x+6,y)

def book_text_update():
    
        if (book_curr_page == 1):
            text_print("      Разделы",book_pos_x+17,book_pos_y+15)
            text_print("3   - Управление",book_pos_x+17,book_pos_y+39)
            text_print("61  - Физика",book_pos_x+17,book_pos_y+51)            
            #text_print("97  - Дополнительно",book_pos_x+17,book_pos_y+63)
            
        elif (book_curr_page == 2):
            text_print("     Раздел I",book_pos_x+20,book_pos_y+15)
            text_print("В этом разделе вы",book_pos_x+17,book_pos_y+75)
            text_print("узнайте, как",book_pos_x+17,book_pos_y+87)             
            text_print("управлять программой",book_pos_x+17,book_pos_y+99)

            text_print("        Главы",book_pos_x+162,book_pos_y+15)
            text_print("5  - Входные данные",book_pos_x+165,book_pos_y+39)
            text_print("29 - Моделирование",book_pos_x+165,book_pos_y+51)
            text_print("41 - Просмотр данных",book_pos_x+165,book_pos_y+63)            
            text_print("51 - Сохранения",book_pos_x+165,book_pos_y+75)

        elif (book_curr_page == 3):
            text_print("Глава 1",book_pos_x+20,book_pos_y+15)
            text_print("Входные данные",book_pos_x+20,book_pos_y+27)
            text_print("Есть нескольно",book_pos_x+20,book_pos_y+51)
            text_print("параметров, которые",book_pos_x+20,book_pos_y+63)
            text_print("можно поменять.",book_pos_x+20,book_pos_y+75)

            text_print("Эти параметры",book_pos_x+20,book_pos_y+99)
            text_print("разделяются на",book_pos_x+20,book_pos_y+111)
            text_print("основные и",book_pos_x+20,book_pos_y+123)
            text_print("дополнительные.",book_pos_x+20,book_pos_y+135)

            text_print("Основные параметры:",book_pos_x+165,book_pos_y+15)
            text_print(" - Скорость",book_pos_x+165,book_pos_y+27)
            text_print(" - Угол",book_pos_x+165,book_pos_y+39)            
            text_print(" - Высота",book_pos_x+165,book_pos_y+51)
            text_print(" - Масса",book_pos_x+165,book_pos_y+63)
            text_print(" - Сопротивление",book_pos_x+165,book_pos_y+75)

            text_print("Дополнительные",book_pos_x+165,book_pos_y+87)
            text_print("параметры:",book_pos_x+165,book_pos_y+99)
            text_print(" - Гравитация",book_pos_x+165,book_pos_y+111)
            text_print(" - Плотность вохдуха",book_pos_x+165,book_pos_y+123)            
            text_print(" - Площадь",book_pos_x+165,book_pos_y+135)
            text_print(" - Объём",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 4):
            text_print("Панель ввода",book_pos_x+20,book_pos_y+15)
            text_print("разделена на три",book_pos_x+20,book_pos_y+27)            
            text_print("части. В левой",book_pos_x+20,book_pos_y+39)
            text_print("части можно ввести",book_pos_x+20,book_pos_y+51)
            text_print("угол и скорость.",book_pos_x+20,book_pos_y+63)            
            text_print("чтобы ввести угол",book_pos_x+20,book_pos_y+75)
            text_print("перетащите красный",book_pos_x+20,book_pos_y+87)
            text_print("ползунок на",book_pos_x+20,book_pos_y+99)
            text_print("необходимое значение",book_pos_x+20,book_pos_y+111)
            text_print("Доступны значения",book_pos_x+20,book_pos_y+135)
            text_print("от 0 до 90№.",book_pos_x+20,book_pos_y+147)
            
            text_print("В нижней части",book_pos_x+165,book_pos_y+15)
            text_print("левой панели можно",book_pos_x+165,book_pos_y+27)            
            text_print("ввести скорость.",book_pos_x+165,book_pos_y+39)
            text_print("Чтобы сделать это",book_pos_x+165,book_pos_y+51)
            text_print("нажмите на белое",book_pos_x+165,book_pos_y+63)            
            text_print("окно. Вы можете ",book_pos_x+165,book_pos_y+75)
            text_print("вводить цифры с",book_pos_x+165,book_pos_y+87)
            text_print("клавиатуры.",book_pos_x+165,book_pos_y+99)
            text_print("Доступен ввод чисел",book_pos_x+165,book_pos_y+111)            
            text_print("от 0 до 9. Нажмите",book_pos_x+165,book_pos_y+123)               
            text_print("backspace чтобы",book_pos_x+165,book_pos_y+135)
            text_print("убрать символ и",book_pos_x+165,book_pos_y+147)
            
        elif (book_curr_page == 5):
            text_print("enter чтобы",book_pos_x+20,book_pos_y+15)            
            text_print("завершить ввод.",book_pos_x+20,book_pos_y+27)
            text_print("Cправа от окна",book_pos_x+20,book_pos_y+39)
            text_print("ввода вы можете.",book_pos_x+20,book_pos_y+51)
            text_print("выбрать размерность.",book_pos_x+20,book_pos_y+63)
            text_print("Ввод также можно",book_pos_x+20,book_pos_y+75)            
            text_print("осуществить с",book_pos_x+20,book_pos_y+87)
            text_print("кнопочной панели",book_pos_x+20,book_pos_y+99)
            text_print("(рис.1), однако",book_pos_x+20,book_pos_y+111)
            text_print("для этого всё равно",book_pos_x+20,book_pos_y+123)     
            text_print("необходимо нажать на",book_pos_x+20,book_pos_y+135)
            text_print("поле ввода.",book_pos_x+20,book_pos_y+147)

            text_print("      рисунок 1",book_pos_x+162,book_pos_y+147)

        elif (book_curr_page == 6):
            text_print("Ввод массы",book_pos_x+20,book_pos_y+15)            
            text_print("аналогичен вводу",book_pos_x+20,book_pos_y+27)
            text_print("скорости, за",book_pos_x+20,book_pos_y+39)            
            text_print("исключением того,",book_pos_x+20,book_pos_y+51)
            text_print("что поле ввода",book_pos_x+20,book_pos_y+63)            
            text_print("находится в нижнем",book_pos_x+20,book_pos_y+75)
            text_print("правом углу панели",book_pos_x+20,book_pos_y+87)
            text_print("ввода.",book_pos_x+20,book_pos_y+99)

            text_print("Для того чтобы",book_pos_x+165,book_pos_y+15)
            text_print("задать начальную",book_pos_x+165,book_pos_y+27)
            text_print("высоту, просто",book_pos_x+165,book_pos_y+39)
            text_print("потяните башню на",book_pos_x+165,book_pos_y+51)
            text_print("которой находится",book_pos_x+165,book_pos_y+63)
            text_print("шарик. Для более",book_pos_x+165,book_pos_y+75)
            text_print("точного ввода вы",book_pos_x+165,book_pos_y+87)
            text_print("можете использовать",book_pos_x+165,book_pos_y+99)
            text_print("дисплей в нижнем",book_pos_x+165,book_pos_y+111)           
            text_print("левом углу окна",book_pos_x+165,book_pos_y+123)
            text_print("моделирования.",book_pos_x+165,book_pos_y+135)

        elif (book_curr_page == 7):
            text_print("В верхнем правом",book_pos_x+20,book_pos_y+15)
            text_print("углу панели",book_pos_x+20,book_pos_y+27)
            text_print("ввода можно ввести",book_pos_x+20,book_pos_y+39)
            text_print("аэродинамический",book_pos_x+20,book_pos_y+51)            
            text_print("коэффицент(он же С )",book_pos_x+20,book_pos_y+63)
            text_print("Для того чтобы",book_pos_x+20,book_pos_y+75)            
            text_print("изменить значение",book_pos_x+20,book_pos_y+87)
            text_print("поверните стрелку.",book_pos_x+20,book_pos_y+99)            
            text_print("С помощью обычного",book_pos_x+20,book_pos_y+111)
            text_print("ввода, можно указать",book_pos_x+20,book_pos_y+123)
            text_print("значение от 0 до 1",book_pos_x+20,book_pos_y+135)
            text_print("с точностью до сотых",book_pos_x+20,book_pos_y+147)

            text_print("Если же у вас есть",book_pos_x+165,book_pos_y+15)
            text_print("необходимость",book_pos_x+165,book_pos_y+27)
            text_print("ввести более",book_pos_x+165,book_pos_y+39)
            text_print("точное значение или",book_pos_x+165,book_pos_y+51)
            text_print("значение больше 1,",book_pos_x+165,book_pos_y+63)
            text_print("то в самом правом",book_pos_x+165,book_pos_y+75)
            text_print("верхнем углу панели",book_pos_x+165,book_pos_y+87)
            text_print("ввода можно найти",book_pos_x+165,book_pos_y+99)
            text_print("круглый",book_pos_x+165,book_pos_y+111)
            text_print("переключатель",book_pos_x+165,book_pos_y+123)
            text_print("(рис.2).",book_pos_x+165,book_pos_y+135)

        elif (book_curr_page == 8):
            text_print("      рисунок 2",book_pos_x+17,book_pos_y+147)

            text_print("Повернув",book_pos_x+165,book_pos_y+15)
            text_print("переключатель,",book_pos_x+165,book_pos_y+27)            
            text_print("нажмите на",book_pos_x+165,book_pos_y+39)
            text_print("зелёную панель, где",book_pos_x+165,book_pos_y+51)
            text_print("появляются цифры.",book_pos_x+165,book_pos_y+63)            
            text_print("После этого вы",book_pos_x+165,book_pos_y+75)
            text_print("сможете ввести",book_pos_x+165,book_pos_y+87)
            text_print("своё значение с",book_pos_x+165,book_pos_y+99)            
            text_print("клавиатуры или с",book_pos_x+165,book_pos_y+111)
            text_print("помощью кнопочной",book_pos_x+165,book_pos_y+123)
            text_print("панели.",book_pos_x+165,book_pos_y+135)            

        elif (book_curr_page == 9):
            text_print("Учитите, что первая",book_pos_x+20,book_pos_y+15)    
            text_print("введённая цифра",book_pos_x+20,book_pos_y+27)
            text_print("будет являться",book_pos_x+20,book_pos_y+39)
            text_print("целой частью, в",book_pos_x+20,book_pos_y+51)
            text_print("то время как все",book_pos_x+20,book_pos_y+63)
            text_print("последующие - ",book_pos_x+20,book_pos_y+75)
            text_print("дробной.",book_pos_x+20,book_pos_y+87)
            text_print("Более подробно",book_pos_x+20,book_pos_y+111)
            text_print("ознакомиться с",book_pos_x+20,book_pos_y+123)
            text_print("сопротивлением",book_pos_x+20,book_pos_y+135)            
            text_print("воздуха можно в",book_pos_x+20,book_pos_y+147)

            text_print("2 главе II раздела.",book_pos_x+165,book_pos_y+15)
            text_print("Как уже было описано",book_pos_x+165,book_pos_y+51)            
            text_print("выше, помимо",book_pos_x+165,book_pos_y+63)
            text_print("основных параметов",book_pos_x+165,book_pos_y+75)
            text_print("существуют тагже и",book_pos_x+165,book_pos_y+87)
            text_print("дополнительные",book_pos_x+165,book_pos_y+99)
            text_print("параметры, о",book_pos_x+165,book_pos_y+111)
            text_print("мы расскажем",book_pos_x+165,book_pos_y+123)
            text_print("далее.",book_pos_x+165,book_pos_y+135)

        elif (book_curr_page == 10):
            text_print("В правой верхней",book_pos_x+20,book_pos_y+15)    
            text_print("части панели",book_pos_x+20,book_pos_y+27)
            text_print("ввода, там где",book_pos_x+20,book_pos_y+39)
            text_print("вы вводили",book_pos_x+20,book_pos_y+51)
            text_print("сопротивление,",book_pos_x+20,book_pos_y+63)
            text_print("вы могли заметить",book_pos_x+20,book_pos_y+75)
            text_print("четыры кнопки",book_pos_x+20,book_pos_y+87)
            text_print("разных цветов.",book_pos_x+20,book_pos_y+99)

            text_print("Нажав синию кнопку",book_pos_x+165,book_pos_y+15)
            text_print("с буквой G,",book_pos_x+165,book_pos_y+27)            
            text_print("откроется ",book_pos_x+165,book_pos_y+39)
            text_print("дополнительная",book_pos_x+165,book_pos_y+51)
            text_print("панель, где вы",book_pos_x+165,book_pos_y+63)
            text_print("сможете изменить",book_pos_x+165,book_pos_y+75)            
            text_print("гравитацию.",book_pos_x+165,book_pos_y+87)
            text_print("Чтобы увеличить",book_pos_x+165,book_pos_y+99)                
            text_print("гравитацию, нажмите",book_pos_x+165,book_pos_y+111)           
            text_print("на кнопку с плюсом.",book_pos_x+165,book_pos_y+123)
            text_print("Чтобы уменьшить",book_pos_x+165,book_pos_y+135)           
            text_print("гравитацию, нажмите",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 11):
            text_print("на кнопку с минусом.",book_pos_x+20,book_pos_y+15)    
            text_print("Можно быстро вернуть",book_pos_x+20,book_pos_y+27)
            text_print("изначальное",book_pos_x+20,book_pos_y+39)
            text_print("значение, нажав на",book_pos_x+20,book_pos_y+51)
            text_print("кнопку с единицей.",book_pos_x+20,book_pos_y+63)
            text_print("Можно ввести",book_pos_x+20,book_pos_y+75)
            text_print("значение от 0 до",book_pos_x+20,book_pos_y+87)
            text_print("10 с точностью до",book_pos_x+20,book_pos_y+99)
            text_print("сотых.",book_pos_x+20,book_pos_y+111)

            text_print("Нажав красную кнопку",book_pos_x+165,book_pos_y+15)
            text_print("с буквой A,",book_pos_x+165,book_pos_y+27)            
            text_print("откроется ",book_pos_x+165,book_pos_y+39)
            text_print("дополнительная",book_pos_x+165,book_pos_y+51)
            text_print("панель, где вы",book_pos_x+165,book_pos_y+63)
            text_print("сможете изменить",book_pos_x+165,book_pos_y+75)            
            text_print("угол с точностью до",book_pos_x+165,book_pos_y+87)
            text_print("минут и секунд.",book_pos_x+165,book_pos_y+99)                
            text_print("Чтобы включить панель",book_pos_x+165,book_pos_y+111)           
            text_print("передвинте",book_pos_x+165,book_pos_y+123)
            text_print("переключатель в",book_pos_x+165,book_pos_y+135)           
            text_print("положение ON, затем,",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 12):
            text_print("используя 12 кнопок",book_pos_x+20,book_pos_y+15)
            text_print("справа (рис.3), вы",book_pos_x+20,book_pos_y+27)
            text_print("сможете настроить",book_pos_x+20,book_pos_y+39)
            text_print("нужный вам угол.",book_pos_x+20,book_pos_y+51)
            text_print("Нажав на зелёную",book_pos_x+20,book_pos_y+75)            
            text_print("кнопку с буквой P",book_pos_x+20,book_pos_y+87)
            text_print("откроется ещё одна",book_pos_x+20,book_pos_y+99)
            text_print("панель, где вы",book_pos_x+20,book_pos_y+111)
            text_print("сможете указать",book_pos_x+20,book_pos_y+123)
            text_print("плотность среды,",book_pos_x+20,book_pos_y+135)
            text_print("где происходит",book_pos_x+20,book_pos_y+147)
                                    
            text_print("      рисунок 3",book_pos_x+162,book_pos_y+147)

        elif (book_curr_page == 13):
            text_print("бросок. Ввод данных",book_pos_x+20,book_pos_y+15)
            text_print("на этой панели",book_pos_x+20,book_pos_y+27)
            text_print("аналогичен вводу",book_pos_x+20,book_pos_y+39)
            text_print("данных на панели",book_pos_x+20,book_pos_y+51)
            text_print("гравитации.",book_pos_x+20,book_pos_y+63)            
            text_print("Нажав на жёлтую",book_pos_x+20,book_pos_y+87)
            text_print("кнопку с буквами VS",book_pos_x+20,book_pos_y+99)
            text_print("откроется последняя",book_pos_x+20,book_pos_y+111)
            text_print("панель, где вы",book_pos_x+20,book_pos_y+123)
            text_print("сможете ввести сразу",book_pos_x+20,book_pos_y+135)           
            text_print("два параметра -",book_pos_x+20,book_pos_y+147)

            text_print("плотность и объём.",book_pos_x+165,book_pos_y+15)
            text_print("Синий ползунок",book_pos_x+165,book_pos_y+27)            
            text_print("отвечает за объём,",book_pos_x+165,book_pos_y+39)
            text_print("в то время как",book_pos_x+165,book_pos_y+51)
            text_print("зелёный - за",book_pos_x+165,book_pos_y+63)
            text_print("площадь.",book_pos_x+165,book_pos_y+75)            
            text_print("Потяните ползунок",book_pos_x+165,book_pos_y+87)
            text_print("вверх, чтобы",book_pos_x+165,book_pos_y+99)                
            text_print("увеличить",book_pos_x+165,book_pos_y+111)           
            text_print("параметр и вниз,",book_pos_x+165,book_pos_y+123)
            text_print("чтобы уменьшить.",book_pos_x+165,book_pos_y+135)           
            text_print("В зависимости от",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 14):
            text_print("того, как сильно вы",book_pos_x+20,book_pos_y+15)
            text_print("потянули ползунок,",book_pos_x+20,book_pos_y+27)
            text_print("параметр будет",book_pos_x+20,book_pos_y+39)
            text_print("меняться с",book_pos_x+20,book_pos_y+51)
            text_print("соотвествущей",book_pos_x+20,book_pos_y+63)            
            text_print("скоростью.",book_pos_x+20,book_pos_y+75)
            text_print("Чтобы изменить",book_pos_x+20,book_pos_y+87)
            text_print("значение на",book_pos_x+20,book_pos_y+99)
            text_print("изначальное, нажмите",book_pos_x+20,book_pos_y+111)
            text_print("на кнопку с",book_pos_x+20,book_pos_y+123)
            text_print("изображением",book_pos_x+20,book_pos_y+135)
            text_print("единицы.",book_pos_x+20,book_pos_y+147)
            
            text_print("Учтите, что",book_pos_x+165,book_pos_y+15)
            text_print("дополнительные",book_pos_x+165,book_pos_y+27)            
            text_print("параметры не",book_pos_x+165,book_pos_y+39)
            text_print("учитываются",book_pos_x+165,book_pos_y+51)
            text_print("в сохранениях",book_pos_x+165,book_pos_y+63)
            text_print("или при печати",book_pos_x+165,book_pos_y+75)            
            text_print("чека.",book_pos_x+165,book_pos_y+87)

        elif (book_curr_page == 15):
            text_print("Глава 2",book_pos_x+20,book_pos_y+15)
            text_print("Моделирование",book_pos_x+20,book_pos_y+27)
            text_print("После того как",book_pos_x+20,book_pos_y+51)
            text_print("вы ввели все",book_pos_x+20,book_pos_y+63)
            text_print("необходимые",book_pos_x+20,book_pos_y+75)
            text_print("данные, обратите",book_pos_x+20,book_pos_y+87)
            text_print("внимание на",book_pos_x+20,book_pos_y+99)
            text_print("панель справа от",book_pos_x+20,book_pos_y+111)
            text_print("панели ввода.",book_pos_x+20,book_pos_y+123)
            text_print("Эта панель",book_pos_x+20,book_pos_y+135)
            text_print("называется",book_pos_x+20,book_pos_y+147)
            
            text_print("панелью управления",book_pos_x+165,book_pos_y+15)
            text_print("моделированием",book_pos_x+165,book_pos_y+27)            
            text_print("(в дальнейшем - ПУМ).",book_pos_x+165,book_pos_y+39)
            text_print("Не спешите нажимать",book_pos_x+165,book_pos_y+51)
            text_print("большую зелёную",book_pos_x+165,book_pos_y+63)
            text_print("кнопку: сейчас она",book_pos_x+165,book_pos_y+75)            
            text_print("неактивна. Чтобы",book_pos_x+165,book_pos_y+87)
            text_print("это исправить, вам",book_pos_x+165,book_pos_y+99)
            text_print("необходимо найти",book_pos_x+165,book_pos_y+111)
            text_print("рычак снизу слева от",book_pos_x+165,book_pos_y+123)            
            text_print("зелёной кнопки и",book_pos_x+165,book_pos_y+135)
            text_print("потянуть его вниз.",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 16):
            text_print("Сделав это, вы",book_pos_x+20,book_pos_y+15)
            text_print("передёте в режим",book_pos_x+20,book_pos_y+27)
            text_print("моделирования.",book_pos_x+20,book_pos_y+39)
            text_print("Чтобы вернуться",book_pos_x+20,book_pos_y+51)
            text_print("обратно к режиму",book_pos_x+20,book_pos_y+63)
            text_print("ввода, потяните",book_pos_x+20,book_pos_y+75)
            text_print("рычаг вверх.",book_pos_x+20,book_pos_y+87)
            text_print("В этом режиме",book_pos_x+20,book_pos_y+99)
            text_print("вы наконец сможете",book_pos_x+20,book_pos_y+111)
            text_print("запустить",book_pos_x+20,book_pos_y+123)
            text_print("моделирование, для",book_pos_x+20,book_pos_y+135)
            text_print("этого просто",book_pos_x+20,book_pos_y+147)

            text_print("нажмите на большую",book_pos_x+165,book_pos_y+15)
            text_print("зелёную кнопку и",book_pos_x+165,book_pos_y+27)            
            text_print("наблюдайте, за",book_pos_x+165,book_pos_y+39)
            text_print("полётом объекта.",book_pos_x+165,book_pos_y+51)
            text_print("После того как",book_pos_x+165,book_pos_y+63)
            text_print("шарик призелится,",book_pos_x+165,book_pos_y+75)            
            text_print("на панели ПУМ",book_pos_x+165,book_pos_y+87)
            text_print("появиться красная",book_pos_x+165,book_pos_y+99)
            text_print("кнопка, нажав на",book_pos_x+165,book_pos_y+111)
            text_print("которую вы сможете",book_pos_x+165,book_pos_y+123)            
            text_print("вернуться в",book_pos_x+165,book_pos_y+135)
            text_print("исходное положение.",book_pos_x+165,book_pos_y+147)            

        elif (book_curr_page == 17):
            text_print("Желтая кнопка,",book_pos_x+20,book_pos_y+15)
            text_print("расположенная в",book_pos_x+20,book_pos_y+27)
            text_print("центре ПУМ,",book_pos_x+20,book_pos_y+39)
            text_print("позволяет",book_pos_x+20,book_pos_y+51)
            text_print("распечатать чек.",book_pos_x+20,book_pos_y+63)
            text_print("В чеке можно",book_pos_x+20,book_pos_y+75)
            text_print("увидеть важную",book_pos_x+20,book_pos_y+87)
            text_print("информацию о",book_pos_x+20,book_pos_y+99)
            text_print("результатат броска.",book_pos_x+20,book_pos_y+111)
            text_print("Чеки сохраняются",book_pos_x+20,book_pos_y+123)
            text_print("после нажатия",book_pos_x+20,book_pos_y+135)
            text_print("кнопки возврата.",book_pos_x+20,book_pos_y+147)

            text_print("М.В. в чеке обозачает",book_pos_x+165,book_pos_y+15)
            text_print("максимальную высоту.",book_pos_x+165,book_pos_y+27)            
            text_print("Обратите внимание на",book_pos_x+165,book_pos_y+39)
            text_print("лампу слева от",book_pos_x+165,book_pos_y+51)
            text_print("кнопки. Если она",book_pos_x+165,book_pos_y+63)
            text_print("горит зелёным,",book_pos_x+165,book_pos_y+75)            
            text_print("значит вы можете",book_pos_x+165,book_pos_y+87)
            text_print("распечатать чек.",book_pos_x+165,book_pos_y+99)

        elif (book_curr_page == 18):
            text_print("Под принтером,",book_pos_x+20,book_pos_y+15)
            text_print("справа от жёлтой",book_pos_x+20,book_pos_y+27)
            text_print("кнопки, расположен",book_pos_x+20,book_pos_y+39)
            text_print("регулятор маштаба",book_pos_x+20,book_pos_y+51)
            text_print("окна моделирования.",book_pos_x+20,book_pos_y+63)
            text_print("По умолчанию он",book_pos_x+20,book_pos_y+75)
            text_print("работает в",book_pos_x+20,book_pos_y+87)
            text_print("автоматическом",book_pos_x+20,book_pos_y+99)
            text_print("режиме, но если",book_pos_x+20,book_pos_y+111)
            text_print("переключить тумблер",book_pos_x+20,book_pos_y+123)
            text_print("в ручное положение,",book_pos_x+20,book_pos_y+135)
            text_print("у вас появится",book_pos_x+20,book_pos_y+147)

            text_print("возможность самим",book_pos_x+165,book_pos_y+15)
            text_print("выбирать настраивать",book_pos_x+165,book_pos_y+27)            
            text_print("маштаб. Доступны",book_pos_x+165,book_pos_y+39)
            text_print("следующие маштабы:",book_pos_x+165,book_pos_y+51)
            text_print("1, 2, 4, 8, 16.",book_pos_x+165,book_pos_y+63)
            text_print("Перетените ползунок",book_pos_x+165,book_pos_y+87)
            text_print("на нужное значение",book_pos_x+165,book_pos_y+99)            
            text_print("чтобы настроить",book_pos_x+165,book_pos_y+111)
            text_print("маштаб. Если вы",book_pos_x+165,book_pos_y+123)
            text_print("хотите вернуться в",book_pos_x+165,book_pos_y+135)
            text_print("автоматический режим,",book_pos_x+165,book_pos_y+147)
            
        elif (book_curr_page == 19):
            text_print("нажмите на тумблер",book_pos_x+20,book_pos_y+15)
            text_print("ещё раз.",book_pos_x+20,book_pos_y+27)
            text_print("Под регулятором",book_pos_x+20,book_pos_y+51)
            text_print("маштаба находится",book_pos_x+20,book_pos_y+63)
            text_print("регулятор скорости",book_pos_x+20,book_pos_y+75)
            text_print("моделирования.",book_pos_x+20,book_pos_y+87)
            text_print("Чтобы активировать",book_pos_x+20,book_pos_y+99)
            text_print("его, нажмите на",book_pos_x+20,book_pos_y+111)
            text_print("красную кнопку на",book_pos_x+20,book_pos_y+123)
            text_print("панели слева от",book_pos_x+20,book_pos_y+135)
            text_print("главной стрелки.",book_pos_x+20,book_pos_y+147)

            text_print("Затем поверните",book_pos_x+165,book_pos_y+15)
            text_print("гланую стрелку на",book_pos_x+165,book_pos_y+27)            
            text_print("требуемое значение.",book_pos_x+165,book_pos_y+39)
            text_print("Повернтите стрелку",book_pos_x+165,book_pos_y+51)
            text_print("против часовой до",book_pos_x+165,book_pos_y+63)
            text_print("конца, чтобы",book_pos_x+165,book_pos_y+75)
            text_print("поставить",book_pos_x+165,book_pos_y+87)            
            text_print("моделирование на",book_pos_x+165,book_pos_y+99)
            text_print("паузу. Данный",book_pos_x+165,book_pos_y+111)
            text_print("регулятор способен",book_pos_x+165,book_pos_y+123)
            text_print("замедлить",book_pos_x+165,book_pos_y+135)
            text_print("моделирование",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 20):
            text_print("впоть до остановки",book_pos_x+20,book_pos_y+15)
            text_print("или ускорить его",book_pos_x+20,book_pos_y+27)
            text_print("максимум в 2 раза.",book_pos_x+20,book_pos_y+39)
            text_print("Принимает значения",book_pos_x+20,book_pos_y+51)
            text_print("с точностью до",book_pos_x+20,book_pos_y+63)
            text_print("сотых.",book_pos_x+20,book_pos_y+75)
            text_print("Вы можете также",book_pos_x+20,book_pos_y+87)
            text_print("и вернуть стрелку",book_pos_x+20,book_pos_y+99)
            text_print("на изначальное",book_pos_x+20,book_pos_y+111)
            text_print("положение, нажав",book_pos_x+20,book_pos_y+123)
            text_print("синию кнопку над",book_pos_x+20,book_pos_y+135)            
            text_print("кнопкой включения.",book_pos_x+20,book_pos_y+147)

            text_print("Справа от регулятора",book_pos_x+165,book_pos_y+15)
            text_print("скорости находится",book_pos_x+165,book_pos_y+27)            
            text_print("кнопка авариной",book_pos_x+165,book_pos_y+39)
            text_print("остановки",book_pos_x+165,book_pos_y+51)
            text_print("моделирования.",book_pos_x+165,book_pos_y+63)
            text_print("Чтобы остановить",book_pos_x+165,book_pos_y+75)            
            text_print("моделирование,",book_pos_x+165,book_pos_y+87)
            text_print("нажмите на неё",book_pos_x+165,book_pos_y+99)
            text_print("два раза. Эта",book_pos_x+165,book_pos_y+111)
            text_print("кнопка полезна, если",book_pos_x+165,book_pos_y+123)
            text_print("вы ввели какие-либо",book_pos_x+165,book_pos_y+135)
            text_print("данные неправильно.",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 21):
            text_print("Глава 3",book_pos_x+20,book_pos_y+15)
            text_print("Просмотр данных",book_pos_x+20,book_pos_y+27)
            
            text_print("данные о броске",book_pos_x+20,book_pos_y+51)
            text_print("можно увидеть как",book_pos_x+20,book_pos_y+63)
            text_print("и во время",book_pos_x+20,book_pos_y+75)
            text_print("моделирования, так и",book_pos_x+20,book_pos_y+87)            
            text_print("после. До и во",book_pos_x+20,book_pos_y+99)
            text_print("время моделирования",book_pos_x+20,book_pos_y+111)
            text_print("данные отображаются",book_pos_x+20,book_pos_y+123)            
            text_print("на панели слева.",book_pos_x+20,book_pos_y+135)
            text_print("В самой левой",book_pos_x+20,book_pos_y+147)

            text_print("части панели",book_pos_x+165,book_pos_y+15)
            text_print("находится",book_pos_x+165,book_pos_y+27)            
            text_print("секундомер.",book_pos_x+165,book_pos_y+39)
            text_print("Главная чёрная",book_pos_x+165,book_pos_y+51)
            text_print("стрелка показывает",book_pos_x+165,book_pos_y+63)            
            text_print("секунды, а маленькая",book_pos_x+165,book_pos_y+75)
            text_print("красная - сотые доли",book_pos_x+165,book_pos_y+87)
            text_print("секунды. Правее, в",book_pos_x+165,book_pos_y+99)            
            text_print("центре панели, можно",book_pos_x+165,book_pos_y+111)
            text_print("увидеть ещё данные.",book_pos_x+165,book_pos_y+123)
            text_print("левее и выше от",book_pos_x+165,book_pos_y+135)
            text_print("центра распологаются",book_pos_x+165,book_pos_y+147)
            
        elif (book_curr_page == 22):
            text_print("показатели скорости.",book_pos_x+20,book_pos_y+15)
            
            text_print("X - скорость по",book_pos_x+20,book_pos_y+39)
            text_print("горизонтали",book_pos_x+20,book_pos_y+51)
            text_print("Y - скорость по",book_pos_x+20,book_pos_y+63)
            text_print("вертикали",book_pos_x+20,book_pos_y+75)
            text_print("O - общая скорость",book_pos_x+20,book_pos_y+87)

            text_print("Все скорости",book_pos_x+20,book_pos_y+111)
            text_print("указаны в",book_pos_x+20,book_pos_y+123)
            text_print("метрах в секунду.",book_pos_x+20,book_pos_y+135)

            text_print("правее и выше от",book_pos_x+165,book_pos_y+15)
            text_print("центра находится",book_pos_x+165,book_pos_y+27)            
            text_print("углометр. он",book_pos_x+165,book_pos_y+39)
            text_print("показывает",book_pos_x+165,book_pos_y+51)
            text_print("направление тела",book_pos_x+165,book_pos_y+63)
            text_print("относительно",book_pos_x+165,book_pos_y+75)
            text_print("горизонта.",book_pos_x+165,book_pos_y+87)

        elif (book_curr_page == 23):
            text_print("В нижней центральной",book_pos_x+20,book_pos_y+15)
            text_print("находятся показатели",book_pos_x+20,book_pos_y+27)
            text_print("энергии тела.",book_pos_x+20,book_pos_y+39)

            text_print("Синим цветом",book_pos_x+20,book_pos_y+75)
            text_print("обозначена",book_pos_x+20,book_pos_y+87)
            text_print("потенциальная",book_pos_x+20,book_pos_y+99)
            text_print("энергия",book_pos_x+20,book_pos_y+111)
            
            text_print("Оранжевым цветом",book_pos_x+165,book_pos_y+15)
            text_print("обозначена",book_pos_x+165,book_pos_y+27)
            text_print("кинетическая",book_pos_x+165,book_pos_y+39)
            text_print("энергия",book_pos_x+165,book_pos_y+51)

            text_print("Зелёным цветом",book_pos_x+165,book_pos_y+75)
            text_print("обозначена",book_pos_x+165,book_pos_y+87)
            text_print("потеря энергии от",book_pos_x+165,book_pos_y+99)
            text_print("сопротивления",book_pos_x+165,book_pos_y+111)
            text_print("воздуха.",book_pos_x+165,book_pos_y+123)
            text_print("(если присутствует)",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 24):
            text_print("Энергии представлены",book_pos_x+20,book_pos_y+15)
            text_print("как в числовом виде,",book_pos_x+20,book_pos_y+27)
            text_print("так и в процентном",book_pos_x+20,book_pos_y+39)
            text_print("соотношении.",book_pos_x+20,book_pos_y+51)

            text_print("После завершения",book_pos_x+20,book_pos_y+75)
            text_print("моделирования",book_pos_x+20,book_pos_y+87)
            text_print("данные на панели",book_pos_x+20,book_pos_y+99)
            text_print("перестают работать,",book_pos_x+20,book_pos_y+111)
            text_print("но теперь вы можете",book_pos_x+20,book_pos_y+123)
            text_print("получить информацию",book_pos_x+20,book_pos_y+135)
            text_print("из любой точки",book_pos_x+20,book_pos_y+147)

            text_print("траектории. Для",book_pos_x+165,book_pos_y+15)
            text_print("этого наведите",book_pos_x+165,book_pos_y+27)
            text_print("курсор на желаемую",book_pos_x+165,book_pos_y+39)
            text_print("высоту. Если на",book_pos_x+165,book_pos_y+51)
            text_print("этой высоте линия",book_pos_x+165,book_pos_y+63)
            text_print("вышего курсора",book_pos_x+165,book_pos_y+75)
            text_print("пересекает линию",book_pos_x+165,book_pos_y+87)
            text_print("траектории, то",book_pos_x+165,book_pos_y+99)
            text_print("в правом верхнем",book_pos_x+165,book_pos_y+111)
            text_print("углу окна",book_pos_x+165,book_pos_y+123)
            text_print("моделирования",book_pos_x+165,book_pos_y+135)
            text_print("появится",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 25):
            text_print("информация об",book_pos_x+20,book_pos_y+15)            
            text_print("этой точке",book_pos_x+20,book_pos_y+27)
            text_print("траектории.",book_pos_x+20,book_pos_y+39)
            text_print("Таких точек может",book_pos_x+20,book_pos_y+51)
            text_print("быть и две.",book_pos_x+20,book_pos_y+63)
            text_print("Информация",book_pos_x+20,book_pos_y+75)
            text_print("аналогична той, что",book_pos_x+20,book_pos_y+87)
            text_print("была представлена",book_pos_x+20,book_pos_y+99)
            text_print("на панели, за",book_pos_x+20,book_pos_y+111)
            text_print("исключением ",book_pos_x+20,book_pos_y+123)
            text_print("позиции тела.",book_pos_x+20,book_pos_y+135)

            text_print("Чтобы просмотреть",book_pos_x+165,book_pos_y+15)
            text_print("данные о самой",book_pos_x+165,book_pos_y+27)
            text_print("высокой точке",book_pos_x+165,book_pos_y+39)
            text_print("траектории, поднимите",book_pos_x+165,book_pos_y+51)
            text_print("курсор выше",book_pos_x+165,book_pos_y+63)
            text_print("всей траектории.",book_pos_x+165,book_pos_y+75)

            text_print("Если точка лежит за",book_pos_x+165,book_pos_y+99)
            text_print("пределами окна, то",book_pos_x+165,book_pos_y+111)
            text_print("просмотреть её",book_pos_x+165,book_pos_y+123)
            text_print("данные невозможно.",book_pos_x+165,book_pos_y+135)

        elif (book_curr_page == 26):
            text_print("Глава 4",book_pos_x+20,book_pos_y+15)
            text_print("Сохранения",book_pos_x+20,book_pos_y+27)

            text_print("В этой главе мы",book_pos_x+20,book_pos_y+63)
            text_print("расскажем, как",book_pos_x+20,book_pos_y+75)
            text_print("пользоваться",book_pos_x+20,book_pos_y+87)
            text_print("монитором, сохранять",book_pos_x+20,book_pos_y+99)
            text_print("и загружать файлы.",book_pos_x+20,book_pos_y+111)


            text_print("Монитор находится",book_pos_x+165,book_pos_y+15)
            text_print("справа от вывода",book_pos_x+165,book_pos_y+27)
            text_print("данных. Чтобы",book_pos_x+165,book_pos_y+39)
            text_print("включить его, нажмите",book_pos_x+165,book_pos_y+51)
            text_print("на кнопку включения в",book_pos_x+165,book_pos_y+63)
            text_print("левом нижнем углу",book_pos_x+165,book_pos_y+75)
            text_print("монитора и подождите,",book_pos_x+165,book_pos_y+87)
            text_print("пока закончится",book_pos_x+165,book_pos_y+99)
            text_print("загрузка. Чтобы",book_pos_x+165,book_pos_y+111)
            text_print("выключить монитор,",book_pos_x+165,book_pos_y+123)
            text_print("нажмите на кнопку",book_pos_x+165,book_pos_y+135)
            text_print("включения ещё раз.",book_pos_x+165,book_pos_y+147)            

        elif (book_curr_page == 27):                       
            text_print("В основном меню",book_pos_x+20,book_pos_y+15)
            text_print("находится четыре",book_pos_x+20,book_pos_y+27)
            text_print("опции.",book_pos_x+20,book_pos_y+39)            
            text_print("Самая первая опция -",book_pos_x+20,book_pos_y+51)
            text_print("запоминание",book_pos_x+20,book_pos_y+63)
            text_print("траектории. Вы",book_pos_x+20,book_pos_y+75)
            text_print("можете сохранить до",book_pos_x+20,book_pos_y+87)
            text_print("8 разных траекторий.",book_pos_x+20,book_pos_y+99)
            text_print("После того как",book_pos_x+20,book_pos_y+111)            
            text_print("моделирование",book_pos_x+20,book_pos_y+123)
            text_print("завершится, нажмите",book_pos_x+20,book_pos_y+135)
            text_print("на зелёную стрелку,",book_pos_x+20,book_pos_y+147)

            text_print("чтобы сохранить",book_pos_x+165,book_pos_y+15)
            text_print("траекторию. Она",book_pos_x+165,book_pos_y+27)
            text_print("будет отображаться",book_pos_x+165,book_pos_y+39)
            text_print("даже после нового",book_pos_x+165,book_pos_y+51)
            text_print("запуска. Чтобы",book_pos_x+165,book_pos_y+63)
            text_print("удалить траекторию,",book_pos_x+165,book_pos_y+75)
            text_print("нажмите на красный",book_pos_x+165,book_pos_y+87)
            text_print("крестик. Вы можете",book_pos_x+165,book_pos_y+99)
            text_print("скрыть траекторию,",book_pos_x+165,book_pos_y+111)
            text_print("не удалая её. Чтобы",book_pos_x+165,book_pos_y+123)
            text_print("сделать это, нажмите",book_pos_x+165,book_pos_y+135)
            text_print("на кнопку с глазом.",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 28):
            text_print("Нажмите на кнопку",book_pos_x+20,book_pos_y+15)
            text_print("ещё раз, чтобы",book_pos_x+20,book_pos_y+27)
            text_print("показать траекторию.",book_pos_x+20,book_pos_y+39)
            text_print("Самая правая кнопка",book_pos_x+20,book_pos_y+51)            
            text_print("позволяет изменить",book_pos_x+20,book_pos_y+63)
            text_print("цвет траетории.",book_pos_x+20,book_pos_y+75)

            text_print("Монитор позволяет",book_pos_x+20,book_pos_y+99)            
            text_print("сохранять введённые",book_pos_x+20,book_pos_y+111)
            text_print("параметры. Вы",book_pos_x+20,book_pos_y+123)
            text_print("можете загрузить",book_pos_x+20,book_pos_y+135)
            text_print("сохранёные",book_pos_x+20,book_pos_y+147)

            text_print("параметры даже",book_pos_x+165,book_pos_y+15)
            text_print("после перезагрузки",book_pos_x+165,book_pos_y+27)
            text_print("приложения!",book_pos_x+165,book_pos_y+39)
            
            text_print("Чтобы сохранить",book_pos_x+165,book_pos_y+63)
            text_print("параметры,",book_pos_x+165,book_pos_y+75)
            text_print("выберете в",book_pos_x+165,book_pos_y+87)
            text_print("основном меню",book_pos_x+165,book_pos_y+99)
            text_print("вторую опцию.",book_pos_x+165,book_pos_y+111)
            text_print("затем нажмите на",book_pos_x+165,book_pos_y+123)
            text_print("на то сохранение,",book_pos_x+165,book_pos_y+135)
            text_print("которые вы хотите",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 29):
            text_print("записать. После",book_pos_x+20,book_pos_y+15)
            text_print("этого у вас должен",book_pos_x+20,book_pos_y+27)
            text_print("открыться",book_pos_x+20,book_pos_y+39)
            text_print("предосмотр файла.",book_pos_x+20,book_pos_y+51)            
            text_print("Убедитесь, что вы",book_pos_x+20,book_pos_y+63)
            text_print("ввели все данные",book_pos_x+20,book_pos_y+75)
            text_print("правильно. Вы",book_pos_x+20,book_pos_y+87)
            text_print("можете изменить",book_pos_x+20,book_pos_y+99)            
            text_print("название файла.",book_pos_x+20,book_pos_y+111)
            text_print("Обратите внимание,",book_pos_x+20,book_pos_y+123)
            text_print("что сохраняются",book_pos_x+20,book_pos_y+135)
            text_print("только основыне",book_pos_x+20,book_pos_y+147)

            text_print("параметры.",book_pos_x+165,book_pos_y+15)
            text_print("Дополнительные",book_pos_x+165,book_pos_y+27)
            text_print("параметры",book_pos_x+165,book_pos_y+39)
            text_print("сохранены не",book_pos_x+165,book_pos_y+51)
            text_print("будут!",book_pos_x+165,book_pos_y+63)

            text_print("Чтобы загрузить",book_pos_x+165,book_pos_y+87)
            text_print("ранее сохранёные",book_pos_x+165,book_pos_y+99)
            text_print("файлы, выберете",book_pos_x+165,book_pos_y+111)
            text_print("третию опцию в",book_pos_x+165,book_pos_y+123)
            text_print("основном меню.",book_pos_x+165,book_pos_y+135)
            text_print("затем выберете",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 30):
            text_print("сохранение,",book_pos_x+20,book_pos_y+15)
            text_print("которое вы хотите",book_pos_x+20,book_pos_y+27)
            text_print("загрузить. вы",book_pos_x+20,book_pos_y+39)
            text_print("сможете просмотреть",book_pos_x+20,book_pos_y+51)
            text_print("данные о файле",book_pos_x+20,book_pos_y+63)
            text_print("перед тем как его",book_pos_x+20,book_pos_y+75)
            text_print("загрузить.",book_pos_x+20,book_pos_y+87)
            text_print("Автосохранение",book_pos_x+20,book_pos_y+111)
            text_print("загружается также,",book_pos_x+20,book_pos_y+123)
            text_print("как и другие",book_pos_x+20,book_pos_y+135)
            text_print("сохранения.",book_pos_x+20,book_pos_y+147)

            text_print("Последней опцией в",book_pos_x+165,book_pos_y+15)
            text_print("основном меню",book_pos_x+165,book_pos_y+27)
            text_print("являются настройки.",book_pos_x+165,book_pos_y+39)
            text_print("Здесь вы сможете",book_pos_x+165,book_pos_y+51)
            text_print("настроить",book_pos_x+165,book_pos_y+63)
            text_print("различные свойства",book_pos_x+165,book_pos_y+75)
            text_print("приложения.",book_pos_x+165,book_pos_y+87)

        elif (book_curr_page == 31):
            text_print("     Раздел II",book_pos_x+17,book_pos_y+15)

            text_print("В этом разделе вы",book_pos_x+17,book_pos_y+75)
            text_print("узнайте, как",book_pos_x+17,book_pos_y+87)             
            text_print("работает физика",book_pos_x+17,book_pos_y+99)
            text_print("во время броска",book_pos_x+17,book_pos_y+111)
            text_print("тела.",book_pos_x+17,book_pos_y+123)
            
            text_print("        Главы",book_pos_x+162,book_pos_y+15)
            text_print("63 - Основы броска",book_pos_x+165,book_pos_y+39)
            text_print("75 - Сопротивление",book_pos_x+165,book_pos_y+51)
            text_print("89 - Энергии",book_pos_x+165,book_pos_y+63)

        elif (book_curr_page == 32):
            text_print("Глава 1",book_pos_x+20,book_pos_y+15)
            text_print("Обычный бросок",book_pos_x+20,book_pos_y+27)

            text_print("Прежде чем",book_pos_x+20,book_pos_y+51)
            text_print("рассматривать",book_pos_x+20,book_pos_y+63)
            text_print("сам бросок,",book_pos_x+20,book_pos_y+75)
            text_print("необходимо для",book_pos_x+20,book_pos_y+87)
            text_print("начала определить",book_pos_x+20,book_pos_y+99)
            text_print("систему координат.",book_pos_x+20,book_pos_y+111)
            text_print("Представим, что",book_pos_x+20,book_pos_y+123)
            text_print("ось абцисс будет",book_pos_x+20,book_pos_y+135)
            text_print("расстоянием, а",book_pos_x+20,book_pos_y+147)            

            text_print("ось ординат -",book_pos_x+165,book_pos_y+15)
            text_print("высотой. Тогда наша",book_pos_x+165,book_pos_y+27)
            text_print("система будет",book_pos_x+165,book_pos_y+39)
            text_print("выглядеть так:",book_pos_x+165,book_pos_y+51)

        elif (book_curr_page == 33):
            text_print("Обозначем высоту",book_pos_x+20,book_pos_y+15)
            text_print("как H и расстояние",book_pos_x+20,book_pos_y+27)            
            text_print("как L.",book_pos_x+20,book_pos_y+39)   

            text_print("Теперь мы можем",book_pos_x+20,book_pos_y+63)
            text_print("описать траекторию",book_pos_x+20,book_pos_y+75)
            text_print("в качестве",book_pos_x+20,book_pos_y+87)
            text_print("уравнения.",book_pos_x+20,book_pos_y+99)
            text_print("Если у тела есть",book_pos_x+20,book_pos_y+111)
            text_print("скорость, её нужно",book_pos_x+20,book_pos_y+123)
            text_print("будет разложить на",book_pos_x+20,book_pos_y+135)
            text_print("скорость по",book_pos_x+20,book_pos_y+147)

            text_print("вертикали и",book_pos_x+165,book_pos_y+15)
            text_print("скорость по",book_pos_x+165,book_pos_y+27)
            text_print("горизонтали.",book_pos_x+165,book_pos_y+39)
            text_print("Представим это так:",book_pos_x+165,book_pos_y+51)

        elif (book_curr_page == 34):
            text_print("Общая скорость",book_pos_x+20,book_pos_y+15)
            text_print("разложится на",book_pos_x+20,book_pos_y+27)
            text_print("скорость по",book_pos_x+20,book_pos_y+39)
            text_print("горизонтали",book_pos_x+20,book_pos_y+51)
            text_print("и вертикали",book_pos_x+20,book_pos_y+63)

            text_print("Чтобы узнать",book_pos_x+20,book_pos_y+87)
            text_print("каждую из этих",book_pos_x+20,book_pos_y+99)
            text_print("скоростей, нам",book_pos_x+20,book_pos_y+111)
            text_print("понадовится угол",book_pos_x+20,book_pos_y+123)
            text_print("броска",book_pos_x+20,book_pos_y+135)

            text_print("На схеме вы могли",book_pos_x+165,book_pos_y+15)
            text_print("заметить",book_pos_x+165,book_pos_y+27)
            text_print("прямоугольный",book_pos_x+165,book_pos_y+39)
            text_print("треугольник с",book_pos_x+165,book_pos_y+51)
            text_print("гипотенузой",book_pos_x+165,book_pos_y+63)
            text_print("и катетами ",book_pos_x+165,book_pos_y+75)
            text_print("и",book_pos_x+165,book_pos_y+87)

            text_print("Здесь нам и",book_pos_x+165,book_pos_y+111)            
            text_print("пригодится наш угол:",book_pos_x+165,book_pos_y+123)
            text_print("мы найдём скорости по",book_pos_x+165,book_pos_y+135)
            text_print("следующим уравнениям:",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 35):
            text_print("    скорость по",book_pos_x+20,book_pos_y+51)
            text_print("    горизонтали",book_pos_x+20,book_pos_y+63)
            text_print("    скорость по",book_pos_x+20,book_pos_y+123)
            text_print("     вертикали",book_pos_x+20,book_pos_y+135)

            text_print("Последнее, что нам",book_pos_x+165,book_pos_y+15)
            text_print("стоит учесть - ",book_pos_x+165,book_pos_y+27)
            text_print("ускорение свободного",book_pos_x+165,book_pos_y+39)
            text_print("падения. Будем",book_pos_x+165,book_pos_y+51)
            text_print("принимать его за",book_pos_x+165,book_pos_y+63)
            text_print("9.80665 м/с  Именно",book_pos_x+165,book_pos_y+75)
            text_print("из-за него тело",book_pos_x+165,book_pos_y+87)
            text_print("падает, а не улетает",book_pos_x+165,book_pos_y+99)
            text_print("вверх. Теперь у нас",book_pos_x+165,book_pos_y+111)
            text_print("есть всё, чтобы",book_pos_x+165,book_pos_y+123)
            text_print("построить уравнения.",book_pos_x+165,book_pos_y+135)

        elif (book_curr_page == 36):
            text_print("Так как по",book_pos_x+20,book_pos_y+15)
            text_print("горизонтали на",book_pos_x+20,book_pos_y+27)            
            text_print("тело никакие силы",book_pos_x+20,book_pos_y+39)
            text_print("не действуют,",book_pos_x+20,book_pos_y+51)
            text_print("для описания",book_pos_x+20,book_pos_y+63)
            text_print("координаты X нам",book_pos_x+20,book_pos_y+75)
            text_print("достаточно уравнения",book_pos_x+20,book_pos_y+87)
            text_print("пути:",book_pos_x+20,book_pos_y+99)

            text_print("По вертикали на тело",book_pos_x+165,book_pos_y+15)
            text_print("действует ускорение",book_pos_x+165,book_pos_y+27)
            text_print("ускорение свободного",book_pos_x+165,book_pos_y+39)
            text_print("падения. Так что",book_pos_x+165,book_pos_y+51)
            text_print("нам придётся",book_pos_x+165,book_pos_y+63)
            text_print("использовать",book_pos_x+165,book_pos_y+75)
            text_print("уравнение для",book_pos_x+165,book_pos_y+87)
            text_print("движения с",book_pos_x+165,book_pos_y+99)
            text_print("постоянным",book_pos_x+165,book_pos_y+111)
            text_print("ускорением. Не стоит",book_pos_x+165,book_pos_y+123)
            text_print("также забывать и о",book_pos_x+165,book_pos_y+135)
            text_print("высоте.",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 37):
            text_print("Используя эти две",book_pos_x+165,book_pos_y+15)
            text_print("формулы, вы сможете",book_pos_x+165,book_pos_y+27)
            text_print("получить координаты",book_pos_x+165,book_pos_y+39)
            text_print("тела в любой момент",book_pos_x+165,book_pos_y+51)
            text_print("времени T.",book_pos_x+165,book_pos_y+63)

        elif (book_curr_page == 38):
            text_print("Глава 2",book_pos_x+20,book_pos_y+15)
            text_print("Сопротивление",book_pos_x+20,book_pos_y+27)

            text_print("Бросок с",book_pos_x+20,book_pos_y+51)
            text_print("сопротивлением",book_pos_x+20,book_pos_y+63)
            text_print("воздуха намного,",book_pos_x+20,book_pos_y+75)
            text_print("намного сложнее.",book_pos_x+20,book_pos_y+87)

            text_print("Давайте сначала",book_pos_x+20,book_pos_y+111)
            text_print("посмотрим на",book_pos_x+20,book_pos_y+123)
            text_print("уравнения:",book_pos_x+20,book_pos_y+135)

            text_print("Вы можете узнать об",book_pos_x+165,book_pos_y+111)
            text_print("уравнениях в открытых",book_pos_x+165,book_pos_y+123)
            text_print("источниках. Мы же",book_pos_x+165,book_pos_y+135)
            text_print("орбратим внимание на",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 39):
            text_print("две вещи. Во-первых,",book_pos_x+20,book_pos_y+15)
            text_print("в отличии от обычных",book_pos_x+20,book_pos_y+27)
            text_print("уравнений, здесь нам",book_pos_x+20,book_pos_y+39)
            text_print("важна масса тела.",book_pos_x+20,book_pos_y+51)            
            text_print("Во-вторых, здесь",book_pos_x+20,book_pos_y+63)
            text_print("появляется",book_pos_x+20,book_pos_y+75)
            text_print("коэффициент",book_pos_x+20,book_pos_y+87)
            text_print("сопротивления",book_pos_x+20,book_pos_y+99)
            text_print("воздуха. Его можно",book_pos_x+20,book_pos_y+111)
            text_print("разложить по",book_pos_x+20,book_pos_y+123)
            text_print("следующей формуле:",book_pos_x+20,book_pos_y+135)

            text_print("В данной формуле",book_pos_x+165,book_pos_y+87)
            text_print("участвуют 4",book_pos_x+165,book_pos_y+99)
            text_print("переменные, мы",book_pos_x+165,book_pos_y+111)
            text_print("рассмотрим каждую",book_pos_x+165,book_pos_y+123)
            text_print("из них отдельно.",book_pos_x+165,book_pos_y+135)

        elif (book_curr_page == 40):
            text_print("аэродинамический",book_pos_x+20,book_pos_y+15)
            text_print("коэффицент (C",book_pos_x+20,book_pos_y+27)
            text_print("зависит от формы",book_pos_x+20,book_pos_y+39)
            text_print("тела и его нельзя",book_pos_x+20,book_pos_y+51)
            text_print("вычислить, он",book_pos_x+20,book_pos_y+63)
            text_print("рассчитывается",book_pos_x+20,book_pos_y+75)
            text_print("эксперементально.",book_pos_x+20,book_pos_y+87)
            text_print("В таблице",book_pos_x+20,book_pos_y+99)
            text_print("представленны",book_pos_x+20,book_pos_y+111)
            text_print("некоторые значения.",book_pos_x+20,book_pos_y+123)

        elif (book_curr_page == 41):
            text_print("Следующее, о чём",book_pos_x+20,book_pos_y+15)
            text_print("стоит поговорить,",book_pos_x+20,book_pos_y+27)
            text_print("это плотность",book_pos_x+20,book_pos_y+39)
            text_print("среды. Главной",book_pos_x+20,book_pos_y+51)
            text_print("особенностью здесь",book_pos_x+20,book_pos_y+63)
            text_print("является уменьшение",book_pos_x+20,book_pos_y+75)
            text_print("плотности с ростом",book_pos_x+20,book_pos_y+87)
            text_print("высоты. Уменьшение",book_pos_x+20,book_pos_y+99)
            text_print("зависит от многих",book_pos_x+20,book_pos_y+111)
            text_print("параметров, таких",book_pos_x+20,book_pos_y+123)
            text_print("как температура,",book_pos_x+20,book_pos_y+135)
            text_print("молярная масса и",book_pos_x+20,book_pos_y+147)

            text_print("гравитации. В",book_pos_x+165,book_pos_y+15)        
            text_print("качестве молярной",book_pos_x+165,book_pos_y+27)   
            text_print("используется",book_pos_x+165,book_pos_y+39)        
            text_print("молярная масса",book_pos_x+165,book_pos_y+51)  
            text_print("воздуха.",book_pos_x+165,book_pos_y+63)
            text_print("Температура -",book_pos_x+165,book_pos_y+75)        
            text_print("288.15№k.",book_pos_x+165,book_pos_y+87)   
            text_print("Ускорение свободного",book_pos_x+165,book_pos_y+99)        
            text_print("падения вы можете",book_pos_x+165,book_pos_y+111)  
            text_print("изменить сами. Не",book_pos_x+165,book_pos_y+123)
            text_print("переживайте - вам",book_pos_x+165,book_pos_y+135)
            text_print("достаточно ввести",book_pos_x+165,book_pos_y+147)
            
        elif (book_curr_page == 42):
            text_print("плотность на",book_pos_x+20,book_pos_y+15)
            text_print("уровне моря, и",book_pos_x+20,book_pos_y+27)
            text_print("приложение посчитает",book_pos_x+20,book_pos_y+39)
            text_print("плотность на высоте",book_pos_x+20,book_pos_y+51)
            text_print("за вас.",book_pos_x+20,book_pos_y+63)
            
            text_print("На графике вы можете",book_pos_x+20,book_pos_y+87)
            text_print("видеть зависимость",book_pos_x+20,book_pos_y+99)
            text_print("плотности воздуха",book_pos_x+20,book_pos_y+111)
            text_print("(отношение к",book_pos_x+20,book_pos_y+123)
            text_print("1.2255 кг/м",book_pos_x+20,book_pos_y+136)
            text_print("от высоты (в км).",book_pos_x+20,book_pos_y+147)

        elif (book_curr_page == 43):
            text_print("Объём тела, пожалуй,",book_pos_x+20,book_pos_y+15)
            text_print("является самой",book_pos_x+20,book_pos_y+27)
            text_print("понятной величиной.",book_pos_x+20,book_pos_y+39)
            text_print("Всё, что вам нужно",book_pos_x+20,book_pos_y+51)
            text_print("сделать - это",book_pos_x+20,book_pos_y+63)
            text_print("посчитать объём",book_pos_x+20,book_pos_y+75)
            text_print("запускаемого вами",book_pos_x+20,book_pos_y+87)
            text_print("тела. Здесь вам",book_pos_x+20,book_pos_y+99)
            text_print("поможет уже",book_pos_x+20,book_pos_y+111)
            text_print("геометрия.",book_pos_x+20,book_pos_y+123)

            text_print("С площадью всё",book_pos_x+165,book_pos_y+15) 
            text_print("немного сложнее.",book_pos_x+165,book_pos_y+27)
            text_print("Когда мы говорим",book_pos_x+165,book_pos_y+39)
            text_print("площадь, мы не",book_pos_x+165,book_pos_y+51)
            text_print("имеем в виду",book_pos_x+165,book_pos_y+63)
            text_print("площадь боковой",book_pos_x+165,book_pos_y+75)
            text_print("поверхности - это",book_pos_x+165,book_pos_y+87)
            text_print("заблуждение. Для",book_pos_x+165,book_pos_y+99)
            text_print("каждой фигуры эта",book_pos_x+165,book_pos_y+111)
            text_print("площадь",book_pos_x+165,book_pos_y+123)
            text_print("рассчитывается",book_pos_x+165,book_pos_y+135)
            text_print("по-разному, но в",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 44):
            text_print("большенстве случаев",book_pos_x+20,book_pos_y+15)            
            text_print("площадь определяется",book_pos_x+20,book_pos_y+27)
            text_print("площадью поперечного",book_pos_x+20,book_pos_y+39)
            text_print("сечения фигуры.",book_pos_x+20,book_pos_y+51)
            text_print("В некоторых случаях",book_pos_x+20,book_pos_y+63)
            text_print("площадь определяется",book_pos_x+20,book_pos_y+75)
            text_print("немного по-другому.",book_pos_x+20,book_pos_y+87)
            text_print("Больше информации вы",book_pos_x+20,book_pos_y+99)
            text_print("найдёте в открытых",book_pos_x+20,book_pos_y+111)
            text_print("источниках.",book_pos_x+20,book_pos_y+123)

        elif (book_curr_page == 45):
            text_print("Глава 3",book_pos_x+20,book_pos_y+15)
            text_print("Энергии",book_pos_x+20,book_pos_y+27)

            text_print("В этой главе мы",book_pos_x+20,book_pos_y+63)
            text_print("расскажем, как",book_pos_x+20,book_pos_y+75)
            text_print("рассчитать энергию",book_pos_x+20,book_pos_y+87)
            text_print("тела в любой момент",book_pos_x+20,book_pos_y+99)
            text_print("броска.",book_pos_x+20,book_pos_y+111)

            text_print("Энергию тела",book_pos_x+165,book_pos_y+15)            
            text_print("можно разложить",book_pos_x+165,book_pos_y+27)
            text_print("на кинетическую",book_pos_x+165,book_pos_y+39)
            text_print("и потенциальную",book_pos_x+165,book_pos_y+51)
            text_print("энергию. На",book_pos_x+165,book_pos_y+63)
            text_print("следующей странице",book_pos_x+165,book_pos_y+75)
            text_print("вы можете увидеть",book_pos_x+165,book_pos_y+87)
            text_print("уравнения, по",book_pos_x+165,book_pos_y+99)
            text_print("которым мы можем",book_pos_x+165,book_pos_y+111)
            text_print("найти обе энергии.",book_pos_x+165,book_pos_y+123)

        elif (book_curr_page == 46):
            text_print("Энергии связаны",book_pos_x+165,book_pos_y+15)            
            text_print("друг с другом:",book_pos_x+165,book_pos_y+27)
            text_print("в сумме они всегда",book_pos_x+165,book_pos_y+39)
            text_print("дают одну величину.",book_pos_x+165,book_pos_y+51)
            text_print("Благодаря этому",book_pos_x+165,book_pos_y+63)
            text_print("зная начальное",book_pos_x+165,book_pos_y+75)
            text_print("значение энергии",book_pos_x+165,book_pos_y+87)
            text_print("вы легко найдёте",book_pos_x+165,book_pos_y+99)
            text_print("скорость через высоту",book_pos_x+165,book_pos_y+111)
            text_print("и наоборот в любой",book_pos_x+165,book_pos_y+123)
            text_print("точке траектории.",book_pos_x+165,book_pos_y+135)
            
        elif (book_curr_page == 47):
            text_print("Однако, если мы",book_pos_x+20,book_pos_y+51)
            text_print("будем учитывать",book_pos_x+20,book_pos_y+63)
            text_print("сопротивление",book_pos_x+20,book_pos_y+75)
            text_print("воздуха, то",book_pos_x+20,book_pos_y+87)
            text_print("столкнёмся с тем,",book_pos_x+20,book_pos_y+99)
            text_print("что сумма энергий",book_pos_x+20,book_pos_y+111)
            text_print("не будет давать одну",book_pos_x+20,book_pos_y+123)
            text_print("и туже величину.",book_pos_x+20,book_pos_y+135)

            text_print("Появились потери",book_pos_x+165,book_pos_y+15)
            text_print("в энергии, вызванные",book_pos_x+165,book_pos_y+27)
            text_print("сопротивлением",book_pos_x+165,book_pos_y+39)
            text_print("воздуха. Энергия,",book_pos_x+165,book_pos_y+51)
            text_print("потраченая на",book_pos_x+165,book_pos_y+63)
            text_print("преоодоление",book_pos_x+165,book_pos_y+75)
            text_print("сопротивления",book_pos_x+165,book_pos_y+87)
            text_print("растёт с каждым",book_pos_x+165,book_pos_y+99)
            text_print("моментом броска. В",book_pos_x+165,book_pos_y+111)
            text_print("этом случае нам",book_pos_x+165,book_pos_y+123)
            text_print("нужно изменить наше",book_pos_x+165,book_pos_y+135)
            text_print("уравнение:",book_pos_x+165,book_pos_y+147)

        elif (book_curr_page == 48):
            text_print("Потери в любой",book_pos_x+20,book_pos_y+51)
            text_print("точке траектории",book_pos_x+20,book_pos_y+63)
            text_print("можно рассчитать,",book_pos_x+20,book_pos_y+75)
            text_print("зная начальную",book_pos_x+20,book_pos_y+87)
            text_print("энергию и",book_pos_x+20,book_pos_y+99)
            text_print("энергию в выбраной",book_pos_x+20,book_pos_y+111)
            text_print("точке.",book_pos_x+20,book_pos_y+123)
            
def print_EN(x,y,string):
    if string[0] != ".":
        Window.blit(EN[int(string[0])],(x, y))
        if len(string)-1 > 0:
            print_EN(x+14,y,string[1:])
    else:
        pygame.draw.rect(Window, (39,39,39),(x-3, y+16, 2, 2))
        if len(string)-1 > 0:
            print_EN(x,y,string[1:])

def print_ENP(x,y,string):
        Window.blit(EN[int(string[0])],(x, y))
        if len(string)-1 > 0:
            print_ENP(x+12,y,string[1:])
    
def Energy_update(K,P,S):
    Ekoff = 0
    for i in range(3):
        if K > 10000:
            K = K/1000
            Ekoff += 1

    K = (int(K*100))/100
    K = str(K)
    for i in range(len(K)):
        if K[i] == ".":
            while len(K[i+1:]) < 2: K += "0"
            break
    xadd = (8-(len(K)-1))*14
    print_EN(228+xadd,890+sideshow_pos_y,str(K))

    if Ekoff == 1: Window.blit(EK1,(346, 890+sideshow_pos_y))
    elif Ekoff == 2: Window.blit(EK2,(346, 890+sideshow_pos_y))
    elif Ekoff == 3: Window.blit(EK3,(346, 890+sideshow_pos_y))


    Ekoff = 0
    for i in range(3):
        if P > 10000:
            P = P/1000
            Ekoff += 1

    P = (int(P*100))/100
    P = str(P)
    for i in range(len(P)):
        if P[i] == ".":
            while len(P[i+1:]) < 2: P += "0"
            break
    xadd = (8-(len(P)-1))*14
    print_EN(228+xadd,868+sideshow_pos_y,str(P))

    if Ekoff == 1: Window.blit(EK1,(346, 868+sideshow_pos_y))
    elif Ekoff == 2: Window.blit(EK2,(346, 868+sideshow_pos_y))
    elif Ekoff == 3: Window.blit(EK3,(346, 868+sideshow_pos_y))

    if S < 0: S = 0
    Ekoff = 0
    for i in range(3):
        if S > 10000:
            S = S/1000
            Ekoff += 1

    S = (int(S*100))/100
    S = str(S)
    for i in range(len(S)):
        if S[i] == ".":
            while len(S[i+1:]) < 2: S += "0"
            break
    xadd = (8-(len(S)-1))*14
    print_EN(228+xadd,912+sideshow_pos_y,str(S))

    if Ekoff == 1: Window.blit(EK1,(346, 912+sideshow_pos_y))
    elif Ekoff == 2: Window.blit(EK2,(346, 912+sideshow_pos_y))
    elif Ekoff == 3: Window.blit(EK3,(346, 912+sideshow_pos_y))

def EG_update(K,P,S):
    K = round(K*100)
    P = round(P*100)
    S = round(S*100)

    if (K == 100):
        pygame.draw.rect(Window, (39,39,39),(391, 890+sideshow_pos_y, 2, 18))
        print_ENP(395,890+sideshow_pos_y,"00")
    else:
        xadd = (1-(len(str(K))-1))*12
        print_ENP(395+xadd,890+sideshow_pos_y,str(K))

    if (P == 100):
        pygame.draw.rect(Window, (39,39,39),(391, 868+sideshow_pos_y, 2, 18))
        print_ENP(395,868+sideshow_pos_y,"00")
    else:
        xadd = (1-(len(str(P))-1))*12
        print_ENP(395+xadd,868+sideshow_pos_y,str(P))

    if (S == 100):
        pygame.draw.rect(Window, (39,39,39),(391, 912+sideshow_pos_y, 2, 18))
        print_ENP(395,912+sideshow_pos_y,"00")
    else:
        xadd = (1-(len(str(S))-1))*12
        print_ENP(395+xadd,912+sideshow_pos_y,str(S))

def simspeed_update(angle):
    angle += 180
    if angle > 190:
        if angle < 270: angle = 190
        else:
            if angle > 350: angle -= 360
            else: angle = -10
    angle += 10
    
    Window.blit(simspeed_rotte[(360-angle)%4],(1035,764))

    simrotor_rect = rotor.get_rect(center=(1064,758)) 
    simrotor2, simrotor_p = rot_center(simspeed_rotor, simrotor_rect, 100-angle)
    
    Window.blit(simrotor2,simrotor_p)

    F = angle/100

    return F

def smoke_create(x,y):
    global smoke_count
    smoke_count += 1
    if smoke_count > 31: smoke_count = 0
    smoke_active[smoke_count] = True
    smoke_posx[smoke_count] = x
    smoke_posy[smoke_count] = y
    smoke_a[smoke_count] = 240

def smoke_update(i):
        if smoke_active[i]:
            smoke.set_alpha(smoke_a[i])
            smoke_a[i] -= 10
            smoke_posx[i] += (1-randint(0,2))
            smoke_posy[i] += (-randint(0,4))
            if smoke_a[i] == 0:
                smoke_active[i] = False
                #smoke_create(randint(28,65),randint(708,720))

def sim_num(num):
    num = str(num)
    if len(num) < 4: num = num + "0"
    Window.blit(SSN[int(num[0])],(986,743))
    Window.blit(SSN[int(num[2])],(994,743))
    Window.blit(SSN[int(num[3])],(1000,743))

def find_up():
    global pos_save_y, masch, y_mouse
    for k in range(0,Max_pos-1):
        T = (600-pos_save_y[k])
        M = (600-pos_save_y[k+1])
        R = ((600-y_mouse)*masch)+20
        if (M >= R) and (R > T): return k
    return -1

def find_down():
    global pos_save_y, masch, y_mouse
    for k in range(tick-1,Max_pos+1,-1):
        T = (600-pos_save_y[k])
        M = (600-pos_save_y[k-1])
        R = ((600-y_mouse)*masch)+20
        if (M >= R) and (R > T): return k
    return -1

def showside_speed_num_print(s,posx,posy):
    if s[0] != ".": Window.blit(showside_speed_num[int(s[0])],(posx,posy))
    else: Window.blit(showside_speed_num[10],(posx,posy))
    if len(s)-1 > 0: showside_speed_num_print(s[1:],posx+6,posy)
    
def showside_speed_num_update(x,y,o):
    x = str((int(x*1000))/1000)
    y = str((int(y*1000))/1000)
    o = str((int(o*1000))/1000)
    for i in range(len(x)):
        if x[i] == ".":
            while len(x[i:]) < 4: x = x + "0"
            break
    for i in range(len(y)):
        if y[i] == ".":
            while len(y[i:]) < 4: y = y + "0"
            break
    for i in range(len(o)):
        if o[i] == ".":
            while len(o[i:]) < 4: o = o + "0"
            break
    add = (8-len(x))*6
    showside_speed_num_print(x,215+add,800++sideshow_pos_y)
    add = (8-len(y))*6
    showside_speed_num_print(y,215+add,813++sideshow_pos_y)
    add = (8-len(o))*6
    showside_speed_num_print(o,215+add,826++sideshow_pos_y)

def draw_circle_grafic(p,x,y):
    F1 = int(p[0]*360)
    F2 = int(p[1]*360)
    F3 = int(p[2]*360)
    for angle in range(F3):
        xa = 37*math.cos(math.radians(angle-90))
        ya = 37*math.sin(math.radians(angle-90))
        pygame.draw.line(Window, (87,225,71), [x, y], [x+xa, y+ya],2)
        if angle >= 90 and angle <= 270: pygame.draw.line(Window, (79,204,65), [x+xa, y+ya], [x+xa, y+ya+10],1)
    for angle in range(F3,F3+F2):
        xa = 37*math.cos(math.radians(angle-90))
        ya = 37*math.sin(math.radians(angle-90))
        pygame.draw.line(Window, (255,182,58), [x, y], [x+xa, y+ya],2)
        if angle >= 90 and angle <= 270: pygame.draw.line(Window, (230,165,54), [x+xa, y+ya], [x+xa, y+ya+10],1)
    for angle in range(F3+F2,F3+F2+F1):
        xa = 37*math.cos(math.radians(angle-90))
        ya = 37*math.sin(math.radians(angle-90))
        pygame.draw.line(Window, (58,100,255), [x, y], [x+xa, y+ya],2)
        if angle >= 90 and angle <= 270: pygame.draw.line(Window, (54,91,230), [x+xa, y+ya], [x+xa, y+ya+10],1)

def grafic_procent_update(p,x,y):
    F1 = str(int(p[0]*100))
    F2 = str(int(p[1]*100))
    F3 = str(int(p[2]*100))

    if len(F1) == 1:
        Window.blit(Znumbers[int(F1[0])],(x+24, y))
    elif len(F1) == 2:
        Window.blit(Znumbers[int(F1[1])],(x+24, y))
        Window.blit(Znumbers[int(F1[0])],(x+12, y))
    elif len(F1) == 3:
        Window.blit(Znumbers[int(F1[2])],(x+24, y))
        Window.blit(Znumbers[int(F1[1])],(x+12, y))
        Window.blit(Znumbers[int(F1[0])],(x, y))

    if len(F2) == 1:
        Window.blit(Znumbers[int(F2[0])],(x+24, y+20))
    elif len(F2) == 2:
        Window.blit(Znumbers[int(F2[1])],(x+24, y+20))
        Window.blit(Znumbers[int(F2[0])],(x+12, y+20))
    elif len(F2) == 3:
        Window.blit(Znumbers[int(F2[2])],(x+24, y+20))
        Window.blit(Znumbers[int(F2[1])],(x+12, y+20))
        Window.blit(Znumbers[int(F2[0])],(x, y+20))

    if len(F3) == 1:
        Window.blit(Znumbers[int(F3[0])],(x+24, y+40))
    elif len(F3) == 2:
        Window.blit(Znumbers[int(F3[1])],(x+24, y+40))
        Window.blit(Znumbers[int(F3[0])],(x+12, y+40))
    elif len(F3) == 3:
        Window.blit(Znumbers[int(F3[2])],(x+24, y+40))
        Window.blit(Znumbers[int(F3[1])],(x+12, y+40))
        Window.blit(Znumbers[int(F3[0])],(x, y+40))

def superangle_update(DD,MM,SS):
    D = str(DD)
    if len(D) < 2: D = '0'+D
    M = str(MM)
    if len(M) < 2: M = '0'+M
    S = str(SS)
    if len(S) < 2: S = '0'+S

    Window.blit(superangle_number[int(D[0])],(901, 630))
    Window.blit(superangle_number[int(D[1])],(913, 630))
    Window.blit(superangle_number[int(M[0])],(901, 656))
    Window.blit(superangle_number[int(M[1])],(913, 656))
    Window.blit(superangle_number[int(S[0])],(901, 682))
    Window.blit(superangle_number[int(S[1])],(913, 682))


#Основная функция отрисовки
    
def update():
    global decor_bool,decor_tick,x_pos,y_pos,Dot_count, speed_arrow, x_mouse, y_mouse, start_button_play, Atick, curr_angle_vent, repeat_button_rise_play, repeat_button_up, repeat_button_set_play
    global sideshow_play_up,sideshow_play_down,anim_x_1,anim_y_1,anim_y_2,anim_y_3,Btick,Hinfo_p, numbutton_bool, Atick_printmachine, print_button_play, presser_on, presser_off, presser_play, curr_angle_rotor
    global sideshow_pos_y, sideshow_bool, Dtick, decoran2_up, decoran2_down, decoran2_bool, animballangle, Stick, m16, m8, m4, m2, m1, monitor_bool, monitor_start, MST, monitor_start_load, Ctick, masch
    global RTA_nor, RTA_inv, rotor_ticker_bool, Dtick, rotor_angle, koff_input, koff, koff_word, koff_enable, Etick, book_bool, Ftick, Gtick, Window, HBA, Htick, Ktick, masch_avto_anim, masch_avto_bool
    global masch_avto_curr, hm16,hm8, hm4, hm2, hm32, hm64, hm128, hm256, bgt, gbgt, abt, abort_button_status, ED_tick, ED_subtick, Energy_potencial, Energy_kinetikal, Energy_body, FS_bool, sim_speed
    global simspeed_enable, sim_angle, smoke_tick, smoke_spawntick, simspeed_on, simspeed_set, speed_or, speed_xr, speed_yr, EP_save, filename_subtick, filename_tick, AB_tick, AB_bool, Atick_pmsubtick
    global BS_a, BS_bool, PL_a, PL_bool, loadtick, asbutton_tick, asbutton_play, addsettings_panel_tick, addsettings_panel_subtick, TF, TF_tick, addsettings_panel_closeandopen, addsettings_panel_bool
    global ASP_tick, monitor_LD, monitor_LD_tick, monitor_savetick, superangle_tick, superangle_subtick, addsettings_menu, addsettings_menu_past, array_tick, array_subtick, array_trigger
    global superangle_DD, superangle_MM, superangle_SS, superangle, IT1_a, IT1_bool, gravity_a, G, gravity_up_button_bool, gravity_down_button_bool, array_bool, drlevel, pva, gravity_setbase_button_bool
    global plotnost_up_button_bool, plotnost_down_button_bool, plotnost_setbase_button_bool, plotnost, volume, sqr, pva_lamplist, fps_past_list, dvig_angle, VS_volume_tugger_take, VS_sqr_tugger_take
    global VS_volume_tugger_pos, VS_sqr_tugger_pos, VS_base_button_bool

    DR = ((str(datetime.datetime.now()))[11:19])
    supertime = int(DR[0:2])*3600+int(DR[3:5])*60+int(DR[6:8])

    if (simulator_run) and (not(decoran2_bool)): decoran2_up = True
    if (finish_sim or abort_button_status == "down") and (decoran2_bool): decoran2_down = True
    
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

    gbgt += round_time*60
    if gbgt > 6:
        gbgt -= 6
        bgt += 1
        if bgt > 2: bgt = 0

    if masch == 1: Window.blit(background_1x[bgt],(0,0))
    if masch == 2: Window.blit(background_2x[bgt],(0,0))
    if masch == 4: Window.blit(background_4x[bgt],(0,0))
    if masch == 8: Window.blit(background_8x[bgt],(0,0))
    if masch == 16: Window.blit(background_16x[bgt],(0,0))

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
            if (array_tick[0] == 4): ea = superangle
            else: ea = angle
            forse_arrow_rect = forse_arrow.get_rect(center=(int(60),int(60))) 
            forse_arrow2, forse_arrow_p = rot_center(forse_arrow, forse_arrow_rect, (90-ea))
            forse_arrow3 = pygame.transform.flip(forse_arrow2, True, False)
            Window.blit(forse_arrow3, (forse_arrow_p[0]+20,forse_arrow_p[1]+height-80))
            if (presser_on):
                kof_word1 = float(kof_word)
                if (kof_word1 >= 0) and (kof_word1 < 0.05):
                    ball1_rect = ball1.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball1, ball1_rect, ea)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.05) and (kof_word1 < 0.15):
                    ball1_rect = ball2.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball2, ball1_rect, ea)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.15) and (kof_word1 < 0.25):
                    ball1_rect = ball3.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball3, ball1_rect, ea)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.25) and (kof_word1 < 0.35):
                    ball1_rect = ball4.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball4, ball1_rect, ea)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.35) and (kof_word1 < 0.45):
                    ball1_rect = ball5.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball5, ball1_rect, ea)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.45) and (kof_word1 < 0.55):
                    ball1_rect = ball6.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball6, ball1_rect, ea)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.55) and (kof_word1 < 0.65):
                    ball1_rect = ball7.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball7, ball1_rect, ea)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.65) and (kof_word1 < 0.75):
                    ball1_rect = ball8.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball8, ball1_rect, ea)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.75) and (kof_word1 < 0.85):
                    ball1_rect = ball9.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball9, ball1_rect, ea)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.85) and (kof_word1 < 0.95):
                    ball1_rect = ball10.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball10, ball1_rect, ea)
                    Window.blit(balln,(ball1_p))
                elif (kof_word1 >= 0.95):
                    ball1_rect = ball11.get_rect(center=(125+x_pos, height-20)) 
                    balln, ball1_p = rot_center(ball11, ball1_rect, ea)
                    Window.blit(balln,(ball1_p))
                    
            else: Window.blit(ball6,(105+x_pos, height-40))
        
    Window.blit(height_info,(0, Hinfo_p-13))
    Hinfo_update(str(500-(height-100)))

    Window.blit(base_insidewall,(12, 612))

    Window.blit(showside_base,(12, 760+sideshow_pos_y))

    Window.blit(energy_name,(284, 825+sideshow_pos_y))
    Window.blit(energy_base,(203, 844+sideshow_pos_y))

    HC = False
    if (simulator_run):
        Energy_all = Energy_potencial + Energy_kinetikal
        HC = True
    elif not(finish_sim):
        if (mass_word != '') and (speed_word != ''):
            emass = int(mass_word)
            espeed = int(speed_word)
            
            if (speed_how != "meterspersecond"):
                if (speed_how == "kilometersperhour"): espeed = espeed/3.6
                if (speed_how == "santimeterspersecond"): espeed = espeed/100
            if (mass_how != "kg"):
                if (mass_how == "ton"): emass = emass*1000
                if (mass_how == "gramm"): emass = emass/1000
                
            Energy_potencial = emass*(G*9.80665)*(((600-(height - 40))-40)/10)
            Energy_kinetikal = ((emass*(espeed**2))/2)*10
            Energy_all = Energy_potencial + Energy_kinetikal
            Energy_body = Energy_all
            HC = True

    
    
    else:
        Energy_potencial = 0
        Energy_all = Energy_kinetikal
        HC = True

    if HC:
        if ((presser_on) and (koff != 0)): ES = Energy_body-Energy_all
        else: ES = 0

        Energy_update(Energy_kinetikal,Energy_potencial,ES)
        
        SEG = ES/Energy_body
        NE = 1-SEG
        PEG = (Energy_potencial/Energy_all) * NE
        KEG = (Energy_kinetikal/Energy_all) * NE

        EG_update(KEG,PEG,SEG)
            
        pygame.draw.rect(Window, (58,100,255),(229, 854+sideshow_pos_y, round(200*PEG), 6))
        pygame.draw.rect(Window, (255,182,58),(229+round(200*PEG), 854+sideshow_pos_y, round(200*KEG), 6))
        pygame.draw.rect(Window, (87,225,71),((229+round(200*PEG)+round(200*KEG)), 854+sideshow_pos_y, round(200*SEG)+(200-(round(200*PEG)+round(200*KEG)+round(200*SEG))), 6))

    ED_subtick += 1*sim_speed
    if ED_subtick >= 4:
        ED_subtick -= 4
        ED_tick += 1
        if ED_tick > 5: ED_tick = 0

    filename_subtick += 1
    if filename_subtick > 20:
        filename_subtick = 0
        filename_tick = not filename_tick

    Window.blit(mehatron_under,(279, 788+sideshow_pos_y))
    dvig_angle += 2 * sim_speed
    if dvig_angle > 360: dvig_angle -= 360
    dvig_update(dvig_angle)
    Window.blit(decoran3[ED_tick],(279, 788+sideshow_pos_y))

    TF_tick += 1*sim_speed
    if TF_tick >= 8:
        TF_tick -= 8
        TF += 1 - randint(0,2)
        if TF > 4: TF = 4
        if TF < 0: TF = 0
    
    Window.blit(decoran4[TF],(416,765+sideshow_pos_y))

    Window.blit(showside_speed,(203, 784+sideshow_pos_y))
    if ((simulator_run) or (finish_sim)): showside_speed_num_update(speed_xr,speed_yr,speed_or)
    elif (speed_word != ''): showside_speed_num_update(int(speed_word)*math.cos(math.radians(angle)),int(speed_word)*math.sin(math.radians(angle)),int(speed_word))
    
    Window.blit(anglometr,(399, 784+sideshow_pos_y))
    am_arrow = anglometr_arrow.get_rect(center=(428, 813+sideshow_pos_y)) 
    if ((simulator_run) or (finish_sim)): am_arrowr, am_arrow_p = rot_center(anglometr_arrow, am_arrow, -animballangle)
    else:
        if (array_tick[0] == 4): ea = superangle
        else: ea = angle
        am_arrowr, am_arrow_p = rot_center(anglometr_arrow, am_arrow, ea) 
    Window.blit(am_arrowr,(am_arrow_p))
    Window.blit(anglometr_close,(399, 784+sideshow_pos_y))
    
    Window.blit(monitor_base,(468, 768+sideshow_pos_y))
    Window.blit(podmonitor,(468, 909+sideshow_pos_y))

    if monitor_savetick == 0:
        if monitor_start or monitor_start_load:
            monitor_LD_tick += 1
            if monitor_LD_tick > 3:
                monitor_LD_tick = 0
                if randint(0,5) != 0: FLD1 = True
                else: FLD1 = False
                if randint(0,3) == 0: FLD2 = True
                else: FLD2 = False
                if randint(0,2) == 0: FLD3 = True
                else: FLD3 = False
                if randint(0,9) == 0: FLD4 = True
                else: FLD4 = False 
                monitor_LD = [FLD1,FLD2,FLD3,FLD4]
        elif monitor_bool:
            monitor_LD_tick += 1
            if monitor_LD_tick > 3:
                monitor_LD_tick = 0
                if randint(0,0) == 0: FLD1 = True
                else: FLD1 = False
                if randint(0,8) == 0: FLD2 = True
                else: FLD2 = False
                if randint(0,4) == 0: FLD3 = True
                else: FLD3 = False
                if randint(0,16) == 0: FLD4 = True
                else: FLD4 = False 
                monitor_LD = [FLD1,FLD2,FLD3,FLD4]
        else:
            monitor_LD = [False,False,False,False]
    else:
        monitor_savetick -= 1
        if monitor_bool:
            monitor_LD_tick += 1
            if monitor_LD_tick > 3:
                monitor_LD_tick = 0
                if randint(0,8) != 0: FLD1 = True
                else: FLD1 = False
                if randint(0,4) == 0: FLD2 = True
                else: FLD2 = False
                if randint(0,4) == 0: FLD3 = True
                else: FLD3 = False
                if randint(0,4) == 0: FLD4 = True
                else: FLD4 = False 
                monitor_LD = [FLD1,FLD2,FLD3,FLD4]
        else:
            monitor_savetick = 0
            monitor_LD = [False,False,False,False]
            
    for i in range(4):
        if monitor_LD[i]: Window.blit(monitor_lampdecor,(506+14*i, 925+sideshow_pos_y))            
    
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
    for i in range(15):
        fps_past_list[i] = fps_past_list[i+1]
    fps_past_list[15] = fpc_procent

    fps_summ = 0
    for i in range(16):
        fps_summ += fps_past_list[i]
    fps_summ = fps_summ/16
    
    if (fps_summ > 1): fps_summ = 1
    if (fps_summ < 0): fps_summ = 0
    for i in range (int(fps_summ*100)):
        pygame.draw.rect(Window, (int((i/100)*255),127,255-int((i/100)*255)),(205+i*2, 770+sideshow_pos_y, 2, 10))

    
                                
    Window.blit(button_group_first,(11+anim_x_1, 611+anim_y_1))
    Window.blit(button_group_second,(366, 704+anim_y_2))
    Window.blit(button_group_third,(366, 611+anim_y_3))
    Window.blit(rotor2, (rotor_p[0],rotor_p[1]+anim_y_3))
    Window.blit(rotor_ticker[Ctick],(681, 622+anim_y_3))
    Window.blit(decor2,(366, 591+anim_y_3))

    gravityshow_update(G,anim_x_1,anim_y_1)

    if array_bool[7]:
        array_subtick[7] += 1*sim_speed
        if array_subtick[7] >= 3:
            array_subtick[7] -= 3
            array_tick[7] += 1
            if array_tick[7] >= 20: array_tick[7] = 0

        Window.blit(decoran8[array_tick[7]],(373,707+anim_y_2))
    else:
        array_subtick[8] += 1*sim_speed
        if array_subtick[8] >= 4:
            array_subtick[8] -= 4

            HF = False
            while True:
                choise = randint(0,2)
                if drlevel[choise] > 0:
                    drlevel[choise] -= 1
                    while True:
                        choise2 = randint(0,2)
                        if choise2 != choise and drlevel[choise] < 9:
                            drlevel[choise2] += 1
                            HF = True
                            break
                if HF: break
            
        decorline_update(373,707+anim_y_2,sim_speed)

    array_subtick[1] += 1*sim_speed
    if array_subtick[1] >= 2:
        array_subtick[1] -= 2
        array_tick[1] += 1
        if array_tick[1] > 25: array_tick[1] = 0

    Window.blit(decoran5[array_tick[1]],(551,709+anim_y_2))

    if random_nake == 1: Window.blit(aseprint_nake,(random_nake_x+anim_x_1, random_nake_y+anim_y_1))
    if random_nake == 2: Window.blit(python_nake,(random_nake_x+anim_x_1, random_nake_y+anim_y_1))
    if random_nake == 3: Window.blit(pi_nake,(random_nake_x+anim_x_1, random_nake_y+anim_y_1))

    for i in range(4):
        if (asbutton_play[i]):
            asbutton_subtick[i] += 1
            if asbutton_subtick[i] > 1:
                asbutton_subtick[i] = 0
                asbutton_tick[i] += 1
            if asbutton_tick[i] >= 4:
                asbutton_tick[i] = 0
                asbutton_play[i] = False

    Window.blit(addsettings_button_g[asbutton_tick[0]],(469, 672+anim_y_3))
    Window.blit(addsettings_button_a[asbutton_tick[1]],(496, 672+anim_y_3))
    Window.blit(addsettings_button_p[asbutton_tick[2]],(523, 672+anim_y_3))
    Window.blit(addsettings_button_vs[asbutton_tick[3]],(550, 672+anim_y_3))

    if array_tick[0] == 0:
        for i in range(90-angle):
            pygame.draw.rect(Window, (255,(int(180-((i*2)))),(int(180-((i*2))))),(21+i*3+anim_x_1, 643+anim_y_1, 3, 56))
            
    if  (array_tick[0] == 0): 
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
    else:
        Window.blit(angle_off,(303+anim_x_1,644+anim_y_1))
        
        Window.blit(superangle_angleinfo,(21+anim_x_1, 643+anim_y_1))

        SAD = str(superangle_DD)
        if len(SAD) < 2: SAD = '0'+SAD
        SAM = str(superangle_MM)
        if len(SAM) < 2: SAM = '0'+SAM
        SAS = str(superangle_SS)
        if len(SAS) < 2: SAS = '0'+SAS

        Window.blit(superangle_number[int(SAD[0])],(110+anim_x_1, 662+anim_y_1))
        Window.blit(superangle_number[int(SAD[1])],(122+anim_x_1, 662+anim_y_1))
        Window.blit(superangle_number[int(SAM[0])],(142+anim_x_1, 662+anim_y_1))
        Window.blit(superangle_number[int(SAM[1])],(154+anim_x_1, 662+anim_y_1))
        Window.blit(superangle_number[int(SAS[0])],(174+anim_x_1, 662+anim_y_1))
        Window.blit(superangle_number[int(SAS[1])],(186+anim_x_1, 662+anim_y_1))

    smoke_spawntick += 1*sim_speed
    if smoke_spawntick >= 2:
        smoke_spawntick -= 2
        if randint(0,1): smoke_create(randint(28,61)+anim_x_1,randint(708,716)+anim_y_1)
        else: smoke_create(randint(243,276)+anim_x_1,randint(708,716)+anim_y_1)

    smoke_tick += 1*sim_speed
    if smoke_tick >= 2:
        smoke_tick -= 2
        for i in range(32):
            smoke_update(i)

    for i in range(32):
            smoke.set_alpha(smoke_a[i])
            Window.blit(smoke,(smoke_posx[i],smoke_posy[i]))

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

    decor_tick = decor_tick + sim_speed
    if (decor_tick > 5):
        decor_tick -= 5
        decor_bool = bool(randint(0,1))
    if decor_bool: Window.blit(decoran1_f2,(298+anim_x_1, 688+anim_y_1))
    else: Window.blit(decoran1_f1,(298+anim_x_1, 688+anim_y_1))

    Window.blit(rotor_close,(588, 617+anim_y_3))
    if(presser_on):Window.blit(indicator_on,(689, 655+anim_y_3))
    else:Window.blit(indicator_off,(689, 655+anim_y_3))

    if (presser_on):curr_angle_vent = curr_angle_vent + (angle_speed_vent*(1/(koff+1))) * sim_speed
    else: curr_angle_vent = curr_angle_vent + (angle_speed_vent) * sim_speed
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

    speed_update(speed_word)
    mass_update(mass_word)
    kof_update(kof_word)



    Window.blit(base,(0, 600))

    if masch == 1: Window.blit(sky_background2[bgt],(328, 0))
    if masch == 2: Window.blit(sky_background1[bgt],(328, 0))
    if masch == 4: Window.blit(sky_background[bgt],(328, 0))
    if masch == 8: Window.blit(sky_background3[bgt],(328, 0))
    if masch == 16: Window.blit(sky_background4[bgt],(328, 0))

    airship_update(masch,sim_speed)
    
    oblako_update(masch,sim_speed)

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
        if (finish_sim) and not((presser_on) and (koff != 0)):
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
                    
                    if masch == 1:
                        #pygame.draw.rect(Window, (255,0,0),((pos_save_x[Max_pos]+119)/masch+2,600-(600-(pos_save_y[Max_pos]+15))/masch+2, SX, 3))
                        Window.blit(found_point,((pos_save_x[Max_pos]+119)/masch-1, (600-(600-(pos_save_y[Max_pos]+15))/masch-1)))                        
                    elif masch == 2:
                        #pygame.draw.rect(Window, (255,0,0),((pos_save_x[Max_pos]+119)/masch+1,600-(600-(pos_save_y[Max_pos]+15))/masch+1, SX, 2))
                        Window.blit(found_point2,((pos_save_x[Max_pos]+118)/masch-1, (600-(600-(pos_save_y[Max_pos]+14))/masch-1)))
                    elif masch == 4:
                        #pygame.draw.rect(Window, (255,0,0),((pos_save_x[Max_pos]+119)/masch+0,600-(600-(pos_save_y[Max_pos]+15))/masch+0, SX, 2))
                        Window.blit(found_point3,((pos_save_x[Max_pos]+117)/masch-1, (600-(600-(pos_save_y[Max_pos]+13))/masch-1)))
                    else:
                        #pygame.draw.rect(Window, (255,0,0),((pos_save_x[Max_pos]+119)/masch-1,600-(600-(pos_save_y[Max_pos]+15))/masch-1, SX, 1))
                        Window.blit(found_point4,((pos_save_x[Max_pos]+116)/masch-1, (600-(600-(pos_save_y[Max_pos]+12))/masch-1)))
                        
                    Window.blit(infotable_highpoint,(1118, 10))

                    print_znum('00.0№',1149,79)

                    draw_angle(1118, 10, 0)

                    SX = str(speed_x_save[Max_pos])
                    while len(SX) > 6: SX = SX[:len(SX)-1]
                    print_znum(SX+'#',1140,139)
                    SY = "0.00000"
                    while len(SY) > 6: SY = SY[:len(SY)-1]
                    print_znum(SY+'#',1140,159)
                    SO = str(speed_o_save[Max_pos])
                    while len(SO) > 6: SO = SO[:len(SO)-1]
                    print_znum(SO+'#',1140,179)

                    draw_circle_grafic(EP_save[Max_pos],1277,161)
                    grafic_procent_update(EP_save[Max_pos],1353,135)
                    
                    pos_viev = [11]*5
                        
                    viev_pos_x = str(int(pos_save_x[Max_pos]))
                    while len(viev_pos_x) < 2: viev_pos_x = "0"+viev_pos_x
                    n = len(viev_pos_x)
                    if (n == 1):
                        pos_viev[0] = viev_pos_x[0]
                        pos_viev[1] = 11
                        pos_viev[2] = 11
                        pos_viev[3] = 11
                        pos_viev[4] = 11
                    elif (n == 2):
                        pos_viev[1] = viev_pos_x[0]
                        pos_viev[0] = viev_pos_x[1]
                        pos_viev[2] = 11
                        pos_viev[3] = 11
                        pos_viev[4] = 11
                    elif (n == 3):
                        pos_viev[2] = viev_pos_x[0]
                        pos_viev[1] = viev_pos_x[1]
                        pos_viev[0] = viev_pos_x[2]
                        pos_viev[3] = 11
                        pos_viev[4] = 11
                    elif (n == 4):
                        pos_viev[3] = viev_pos_x[0]
                        pos_viev[2] = viev_pos_x[1]
                        pos_viev[1] = viev_pos_x[2]
                        pos_viev[0] = viev_pos_x[3]
                        pos_viev[4] = 11
                    elif (n == 5):
                        pos_viev[4] = viev_pos_x[0]
                        pos_viev[3] = viev_pos_x[1]
                        pos_viev[2] = viev_pos_x[2]
                        pos_viev[1] = viev_pos_x[3]
                        pos_viev[0] = viev_pos_x[4]

                    for i in range(5):
                        for j in range(10):
                            if (pos_viev[i] == str(j)):
                                if (i == 4) and (j != 11): Window.blit(Znumbers[j],(1331, 35))
                                elif (i == 3) and (j != 11): Window.blit(Znumbers[j],(1343, 35))
                                elif (i == 2) and (j != 11): Window.blit(Znumbers[j],(1355, 35))
                                elif (i == 1) and (j != 11): Window.blit(Znumbers[j],(1367, 35))
                                elif (i == 0) and (j != 11): Window.blit(Znumbers[j],(1383, 35))

                    pos_viev = [11]*6
                        
                    viev_pos_timer = str(int(timer_save[Max_pos]*1000))
                    while len(viev_pos_timer) < 4: viev_pos_timer = "0"+viev_pos_timer
                    n = len(viev_pos_timer)
                    if (n == 1):
                        pos_viev[5] = viev_pos_timer[0]
                        pos_viev[4] = 11
                        pos_viev[3] = 11
                        pos_viev[2] = 11
                        pos_viev[1] = 11
                        pos_viev[0] = 11
                    elif (n == 2):
                        pos_viev[4] = viev_pos_timer[0]
                        pos_viev[5] = viev_pos_timer[1]
                        pos_viev[3] = 11
                        pos_viev[2] = 11
                        pos_viev[1] = 11
                        pos_viev[0] = 11
                    elif (n == 3):
                        pos_viev[3] = viev_pos_timer[0]
                        pos_viev[4] = viev_pos_timer[1]
                        pos_viev[5] = viev_pos_timer[2]
                        pos_viev[2] = 11
                        pos_viev[1] = 11
                        pos_viev[0] = 11
                    elif (n == 4):
                        pos_viev[2] = viev_pos_timer[0]
                        pos_viev[3] = viev_pos_timer[1]
                        pos_viev[4] = viev_pos_timer[2]
                        pos_viev[5] = viev_pos_timer[3]
                        pos_viev[1] = 11
                        pos_viev[0] = 11
                    elif (n == 5):
                        pos_viev[1] = viev_pos_timer[0]
                        pos_viev[2] = viev_pos_timer[1]
                        pos_viev[3] = viev_pos_timer[2]
                        pos_viev[4] = viev_pos_timer[3]
                        pos_viev[5] = viev_pos_timer[4]
                        pos_viev[0] = 11
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
                                if (i == 0) and (j != 11): Window.blit(Znumbers[j],(1315, 79))
                                elif (i == 1) and (j != 11): Window.blit(Znumbers[j],(1327, 79))
                                elif (i == 2) and (j != 11): Window.blit(Znumbers[j],(1339, 79))
                                elif (i == 3) and (j != 11): Window.blit(Znumbers[j],(1355, 79))
                                elif (i == 4) and (j != 11): Window.blit(Znumbers[j],(1367, 79))
                                elif (i == 5) and (j != 11): Window.blit(Znumbers[j],(1379, 79))


                    pos_viev = [11]*5
                        
                    viev_pos_y = str(int(810-(pos_save_y[Max_pos]+250)))
                    while len(viev_pos_y) < 2: viev_pos_y = "0"+viev_pos_y
                    n = len(viev_pos_y)
                    if (n == 1):
                        pos_viev[0] = viev_pos_y[0]
                        pos_viev[1] = 11
                        pos_viev[2] = 11
                        pos_viev[3] = 11
                        pos_viev[4] = 11
                    elif (n == 2):
                        pos_viev[1] = viev_pos_y[0]
                        pos_viev[0] = viev_pos_y[1]
                        pos_viev[2] = 11
                        pos_viev[3] = 11
                        pos_viev[4] = 11
                    elif (n == 3):
                        pos_viev[2] = viev_pos_y[0]
                        pos_viev[1] = viev_pos_y[1]
                        pos_viev[0] = viev_pos_y[2]
                        pos_viev[3] = 11
                        pos_viev[4] = 11
                    elif (n == 4):
                        pos_viev[3] = viev_pos_y[0]
                        pos_viev[2] = viev_pos_y[1]
                        pos_viev[1] = viev_pos_y[2]
                        pos_viev[0] = viev_pos_y[3]
                        pos_viev[4] = 11
                    elif (n == 5):
                        pos_viev[4] = viev_pos_y[0]
                        pos_viev[3] = viev_pos_y[1]
                        pos_viev[2] = viev_pos_y[2]
                        pos_viev[1] = viev_pos_y[3]
                        pos_viev[0] = viev_pos_y[4]
                            
                    for i in range(5):
                        for j in range(10):
                            if (pos_viev[i] == str(j)):
                                if (i == 4) and (j != 11): Window.blit(Znumbers[j],(1331, 15))
                                elif (i == 3) and (j != 11): Window.blit(Znumbers[j],(1343, 15))
                                elif (i == 2) and (j != 11): Window.blit(Znumbers[j],(1355, 15))
                                elif (i == 1) and (j != 11): Window.blit(Znumbers[j],(1367, 15))
                                elif (i == 0) and (j != 11): Window.blit(Znumbers[j],(1383, 15))

            else:
                    S = find_up()
                    if S != -1 and ((600-height+20)/masch<600-y_mouse):
                            first_place_taken = True
                                                        
                            if masch == 1:
                                #pygame.draw.rect(Window, (0,0,255),((pos_save_x[S]+119)/masch+2,600-(600-(pos_save_y[S]+15))/masch+2-SY, 3, SY))
                                #pygame.draw.rect(Window, (255,0,0),((pos_save_x[S]+119)/masch+3,600-(600-(pos_save_y[S]+15))/masch+3, SX, 3))
                                Window.blit(found_point,((pos_save_x[S]+119)/masch-1, (600-(600-(pos_save_y[S]+15))/masch-1)))
                            elif masch == 2:
                                #pygame.draw.rect(Window, (0,0,255),((pos_save_x[S]+119)/masch+1,600-(600-(pos_save_y[S]+15))/masch+1-SY, 2, SY))
                                #pygame.draw.rect(Window, (255,0,0),((pos_save_x[S]+119)/masch+2,600-(600-(pos_save_y[S]+15))/masch+2, SX, 2))
                                Window.blit(found_point2,((pos_save_x[S]+118)/masch-1, (600-(600-(pos_save_y[S]+14))/masch-1)))
                            elif masch == 4:
                                #pygame.draw.rect(Window, (0,0,255),((pos_save_x[S]+119)/masch+0,600-(600-(pos_save_y[S]+15))/masch+0-SY, 2, SY))
                                #pygame.draw.rect(Window, (255,0,0),((pos_save_x[S]+119)/masch+1,600-(600-(pos_save_y[S]+15))/masch+1, SX, 2))
                                Window.blit(found_point3,((pos_save_x[S]+117)/masch-1, (600-(600-(pos_save_y[S]+13))/masch-1)))
                            else:
                                #pygame.draw.rect(Window, (0,0,255),((pos_save_x[S]+119)/masch-1,600-(600-(pos_save_y[S]+15))/masch-1-SY, 1, SY))
                                #pygame.draw.rect(Window, (255,0,0),((pos_save_x[S]+119)/masch+0,600-(600-(pos_save_y[S]+15))/masch+0, SX, 1))
                                Window.blit(found_point4,((pos_save_x[S]+116)/masch-1, (600-(600-(pos_save_y[S]+12))/masch-1)))
                            
                            Window.blit(infotable_up,(1118, 10))

                            H1 = (abs(angle_save[S]))
                            H = (str(abs(angle_save[S])))
                            if H1 < 10: H = '0'+H
                            while len(H) > 4: H = H[:len(H)-1]
                            print_znum(H+'№',1149,79)

                            draw_angle(1118, 10, -(abs(angle_save[S])))
                            
                            SX = str(speed_x_save[S])
                            while len(SX) > 6: SX = SX[:len(SX)-1]
                            print_znum(SX+'#',1140,139)
                            SY = str(speed_y_save[S])
                            while len(SY) > 6: SY = SY[:len(SY)-1]
                            print_znum(SY+'#',1140,159)
                            SO = str(speed_o_save[S])
                            while len(SO) > 6: SO = SO[:len(SO)-1]
                            print_znum(SO+'#',1140,179)

                            draw_circle_grafic(EP_save[S],1277,161)
                            grafic_procent_update(EP_save[S],1353,135)

                            pos_viev = [11]*5
                            
                            viev_pos_x = str(int(pos_save_x[S]))
                            while len(viev_pos_x) < 2: viev_pos_x = "0"+viev_pos_x
                            n = len(viev_pos_x)
                            if (n == 1):
                                pos_viev[0] = viev_pos_x[0]
                                pos_viev[1] = 11
                                pos_viev[2] = 11
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 2):
                                pos_viev[1] = viev_pos_x[0]
                                pos_viev[0] = viev_pos_x[1]
                                pos_viev[2] = 11
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 3):
                                pos_viev[2] = viev_pos_x[0]
                                pos_viev[1] = viev_pos_x[1]
                                pos_viev[0] = viev_pos_x[2]
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 4):
                                pos_viev[3] = viev_pos_x[0]
                                pos_viev[2] = viev_pos_x[1]
                                pos_viev[1] = viev_pos_x[2]
                                pos_viev[0] = viev_pos_x[3]
                                pos_viev[4] = 11
                            elif (n == 5):
                                pos_viev[4] = viev_pos_x[0]
                                pos_viev[3] = viev_pos_x[1]
                                pos_viev[2] = viev_pos_x[2]
                                pos_viev[1] = viev_pos_x[3]
                                pos_viev[0] = viev_pos_x[4]

                            for i in range(5):
                                for j in range(10):
                                    if (pos_viev[i] == str(j)):
                                        if (i == 4) and (j != 11): Window.blit(Znumbers[j],(1331, 35))
                                        elif (i == 3) and (j != 11): Window.blit(Znumbers[j],(1343, 35))
                                        elif (i == 2) and (j != 11): Window.blit(Znumbers[j],(1355, 35))
                                        elif (i == 1) and (j != 11): Window.blit(Znumbers[j],(1367, 35))
                                        elif (i == 0) and (j != 11): Window.blit(Znumbers[j],(1383, 35))

                            pos_viev = [11]*6
                            
                            viev_pos_timer = str(int(timer_save[S]*1000))
                            while len(viev_pos_timer) < 4: viev_pos_timer = "0"+viev_pos_timer
                            n = len(viev_pos_timer)
                            if (n == 1):
                                pos_viev[5] = viev_pos_timer[0]
                                pos_viev[4] = 11
                                pos_viev[3] = 11
                                pos_viev[2] = 11
                                pos_viev[1] = 11
                                pos_viev[0] = 11
                            elif (n == 2):
                                pos_viev[4] = viev_pos_timer[0]
                                pos_viev[5] = viev_pos_timer[1]
                                pos_viev[3] = 11
                                pos_viev[2] = 11
                                pos_viev[1] = 11
                                pos_viev[0] = 11
                            elif (n == 3):
                                pos_viev[3] = viev_pos_timer[0]
                                pos_viev[4] = viev_pos_timer[1]
                                pos_viev[5] = viev_pos_timer[2]
                                pos_viev[2] = 11
                                pos_viev[1] = 11
                                pos_viev[0] = 11
                            elif (n == 4):
                                pos_viev[2] = viev_pos_timer[0]
                                pos_viev[3] = viev_pos_timer[1]
                                pos_viev[4] = viev_pos_timer[2]
                                pos_viev[5] = viev_pos_timer[3]
                                pos_viev[1] = 11
                                pos_viev[0] = 11
                            elif (n == 5):
                                pos_viev[1] = viev_pos_timer[0]
                                pos_viev[2] = viev_pos_timer[1]
                                pos_viev[3] = viev_pos_timer[2]
                                pos_viev[4] = viev_pos_timer[3]
                                pos_viev[5] = viev_pos_timer[4]
                                pos_viev[0] = 11
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
                                        if (i == 0) and (j != 11): Window.blit(Znumbers[j],(1315, 79))
                                        elif (i == 1) and (j != 11): Window.blit(Znumbers[j],(1327, 79))
                                        elif (i == 2) and (j != 11): Window.blit(Znumbers[j],(1339, 79))
                                        elif (i == 3) and (j != 11): Window.blit(Znumbers[j],(1355, 79))
                                        elif (i == 4) and (j != 11): Window.blit(Znumbers[j],(1367, 79))
                                        elif (i == 5) and (j != 11): Window.blit(Znumbers[j],(1379, 79))

                                        

                            pos_viev = [11]*5
                            
                            viev_pos_y = str(int(810-(pos_save_y[S]+250)))
                            while len(viev_pos_y) < 2: viev_pos_y = "0"+viev_pos_y
                            n = len(viev_pos_y)
                            if (n == 1):
                                pos_viev[0] = viev_pos_y[0]
                                pos_viev[1] = 11
                                pos_viev[2] = 11
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 2):
                                pos_viev[1] = viev_pos_y[0]
                                pos_viev[0] = viev_pos_y[1]
                                pos_viev[2] = 11
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 3):
                                pos_viev[2] = viev_pos_y[0]
                                pos_viev[1] = viev_pos_y[1]
                                pos_viev[0] = viev_pos_y[2]
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 4):
                                pos_viev[3] = viev_pos_y[0]
                                pos_viev[2] = viev_pos_y[1]
                                pos_viev[1] = viev_pos_y[2]
                                pos_viev[0] = viev_pos_y[3]
                                pos_viev[4] = 11
                            elif (n == 5):
                                pos_viev[4] = viev_pos_y[0]
                                pos_viev[3] = viev_pos_y[1]
                                pos_viev[2] = viev_pos_y[2]
                                pos_viev[1] = viev_pos_y[3]
                                pos_viev[0] = viev_pos_y[4]
                                
                            for i in range(5):
                                for j in range(10):
                                    if (pos_viev[i] == str(j)):
                                        if (i == 4) and (j != 11): Window.blit(Znumbers[j],(1331, 15))
                                        elif (i == 3) and (j != 11): Window.blit(Znumbers[j],(1343, 15))
                                        elif (i == 2) and (j != 11): Window.blit(Znumbers[j],(1355, 15))
                                        elif (i == 1) and (j != 11): Window.blit(Znumbers[j],(1367, 15))
                                        elif (i == 0) and (j != 11): Window.blit(Znumbers[j],(1383, 15))

                    S = find_down()
                    if S != -1:
                            if not (first_place_taken): FPT = 0
                            else: FPT = 219
                            
                            if masch == 1:
                                #pygame.draw.rect(Window, (0,0,255),((pos_save_x[S]+119)/masch+2,600-(600-(pos_save_y[S]+15))/masch+2, 3, SY))
                                #pygame.draw.rect(Window, (255,0,0),((pos_save_x[S]+119)/masch+3,600-(600-(pos_save_y[S]+15))/masch+3, SX, 3))
                                Window.blit(found_point,((pos_save_x[S]+119)/masch-1, (600-(600-(pos_save_y[S]+15))/masch-1)))
                            elif masch == 2:
                                #pygame.draw.rect(Window, (0,0,255),((pos_save_x[S]+119)/masch+1,600-(600-(pos_save_y[S]+15))/masch+1, 2, SY))
                                #pygame.draw.rect(Window, (255,0,0),((pos_save_x[S]+119)/masch+2,600-(600-(pos_save_y[S]+15))/masch+2, SX, 2))
                                Window.blit(found_point2,((pos_save_x[S]+118)/masch-1, (600-(600-(pos_save_y[S]+14))/masch-1)))
                            elif masch == 4:
                                #pygame.draw.rect(Window, (0,0,255),((pos_save_x[S]+119)/masch+0,600-(600-(pos_save_y[S]+15))/masch+0, 2, SY))
                                #pygame.draw.rect(Window, (255,0,0),((pos_save_x[S]+119)/masch+1,600-(600-(pos_save_y[S]+15))/masch+1, SX, 2))
                                Window.blit(found_point3,((pos_save_x[S]+117)/masch-1, (600-(600-(pos_save_y[S]+13))/masch-1)))
                            else:
                                #pygame.draw.rect(Window, (0,0,255),((pos_save_x[S]+119)/masch-1,600-(600-(pos_save_y[S]+15))/masch-1, 1, SY))
                                #pygame.draw.rect(Window, (255,0,0),((pos_save_x[S]+119)/masch+0,600-(600-(pos_save_y[S]+15))/masch+0, SX, 1))
                                Window.blit(found_point4,((pos_save_x[S]+116)/masch-1, (600-(600-(pos_save_y[S]+12))/masch-1)))
                                
                            Window.blit(infotable_down,(1118, 10+FPT))

                            H1 = abs(angle_save[S])
                            H = str(abs(angle_save[S]))
                            if H1 < 10: H = '0'+H
                            while len(H) > 4: H = H[:len(H)-1]
                            print_znum(H+'№',1149,79+FPT)

                            draw_angle(1118, 10+FPT, (angle_save[S]))

                            SX = str(speed_x_save[S])
                            while len(SX) > 6: SX = SX[:len(SX)-1]
                            print_znum(SX+'#',1140,139+FPT)
                            SY = str(speed_y_save[S])
                            while len(SY) > 6: SY = SY[:len(SY)-1]
                            print_znum(SY+'#',1140,159+FPT)
                            SO = str(speed_o_save[S])
                            while len(SO) > 6: SO = SO[:len(SO)-1]
                            print_znum(SO+'#',1140,179+FPT)

                            draw_circle_grafic(EP_save[S],1277,161+FPT)
                            grafic_procent_update(EP_save[S],1353,135+FPT)
                            
                            pos_viev = [11]*5
                            
                            viev_pos_x = str(int(pos_save_x[S]))
                            while len(viev_pos_x) < 2: viev_pos_x = "0"+viev_pos_x
                            n = len(viev_pos_x)
                            if (n == 1):
                                pos_viev[0] = viev_pos_x[0]
                                pos_viev[1] = 11
                                pos_viev[2] = 11
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 2):
                                pos_viev[1] = viev_pos_x[0]
                                pos_viev[0] = viev_pos_x[1]
                                pos_viev[2] = 11
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 3):
                                pos_viev[2] = viev_pos_x[0]
                                pos_viev[1] = viev_pos_x[1]
                                pos_viev[0] = viev_pos_x[2]
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 4):
                                pos_viev[3] = viev_pos_x[0]
                                pos_viev[2] = viev_pos_x[1]
                                pos_viev[1] = viev_pos_x[2]
                                pos_viev[0] = viev_pos_x[3]
                                pos_viev[4] = 11
                            elif (n == 5):
                                pos_viev[4] = viev_pos_x[0]
                                pos_viev[3] = viev_pos_x[1]
                                pos_viev[2] = viev_pos_x[2]
                                pos_viev[1] = viev_pos_x[3]
                                pos_viev[0] = viev_pos_x[4]

                            for i in range(5):
                                for j in range(10):
                                    if (pos_viev[i] == str(j)):
                                        if (i == 4) and (j != 11): Window.blit(Znumbers[j],(1331, 35+FPT))
                                        elif (i == 3) and (j != 11): Window.blit(Znumbers[j],(1343, 35+FPT))
                                        elif (i == 2) and (j != 11): Window.blit(Znumbers[j],(1355, 35+FPT))
                                        elif (i == 1) and (j != 11): Window.blit(Znumbers[j],(1367, 35+FPT))
                                        elif (i == 0) and (j != 11): Window.blit(Znumbers[j],(1383, 35+FPT))

                            pos_viev = [11]*6
                            
                            viev_pos_timer = str(int(timer_save[S]*1000))
                            while len(viev_pos_timer) < 4: viev_pos_timer = "0"+viev_pos_timer
                            n = len(viev_pos_timer)
                            if (n == 1):
                                pos_viev[5] = viev_pos_timer[0]
                                pos_viev[4] = 11
                                pos_viev[3] = 11
                                pos_viev[2] = 11
                                pos_viev[1] = 11
                                pos_viev[0] = 11
                            elif (n == 2):
                                pos_viev[4] = viev_pos_timer[0]
                                pos_viev[5] = viev_pos_timer[1]
                                pos_viev[3] = 11
                                pos_viev[2] = 11
                                pos_viev[1] = 11
                                pos_viev[0] = 11
                            elif (n == 3):
                                pos_viev[3] = viev_pos_timer[0]
                                pos_viev[4] = viev_pos_timer[1]
                                pos_viev[5] = viev_pos_timer[2]
                                pos_viev[2] = 11
                                pos_viev[1] = 11
                                pos_viev[0] = 11
                            elif (n == 4):
                                pos_viev[2] = viev_pos_timer[0]
                                pos_viev[3] = viev_pos_timer[1]
                                pos_viev[4] = viev_pos_timer[2]
                                pos_viev[5] = viev_pos_timer[3]
                                pos_viev[1] = 11
                                pos_viev[0] = 11
                            elif (n == 5):
                                pos_viev[1] = viev_pos_timer[0]
                                pos_viev[2] = viev_pos_timer[1]
                                pos_viev[3] = viev_pos_timer[2]
                                pos_viev[4] = viev_pos_timer[3]
                                pos_viev[5] = viev_pos_timer[4]
                                pos_viev[0] = 11
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
                                        if (i == 0) and (j != 11): Window.blit(Znumbers[j],(1315, 79+FPT))
                                        elif (i == 1) and (j != 11): Window.blit(Znumbers[j],(1327, 79+FPT))
                                        elif (i == 2) and (j != 11): Window.blit(Znumbers[j],(1339, 79+FPT))
                                        elif (i == 3) and (j != 11): Window.blit(Znumbers[j],(1355, 79+FPT))
                                        elif (i == 4) and (j != 11): Window.blit(Znumbers[j],(1367, 79+FPT))
                                        elif (i == 5) and (j != 11): Window.blit(Znumbers[j],(1379, 79+FPT))

                            pos_viev = [11]*5
                  
                            viev_pos_y = str(int(810-(pos_save_y[S]+250)))
                            while len(viev_pos_y) < 2: viev_pos_y = "0"+viev_pos_y
                            n = len(viev_pos_y)
                            if (n == 1):
                                pos_viev[0] = viev_pos_y[0]
                                pos_viev[1] = 11
                                pos_viev[2] = 11
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 2):
                                pos_viev[1] = viev_pos_y[0]
                                pos_viev[0] = viev_pos_y[1]
                                pos_viev[2] = 11
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 3):
                                pos_viev[2] = viev_pos_y[0]
                                pos_viev[1] = viev_pos_y[1]
                                pos_viev[0] = viev_pos_y[2]
                                pos_viev[3] = 11
                                pos_viev[4] = 11
                            elif (n == 4):
                                pos_viev[3] = viev_pos_y[0]
                                pos_viev[2] = viev_pos_y[1]
                                pos_viev[1] = viev_pos_y[2]
                                pos_viev[0] = viev_pos_y[3]
                                pos_viev[4] = 11
                            elif (n == 5):
                                pos_viev[4] = viev_pos_y[0]
                                pos_viev[3] = viev_pos_y[1]
                                pos_viev[2] = viev_pos_y[2]
                                pos_viev[1] = viev_pos_y[3]
                                pos_viev[0] = viev_pos_y[4]
                                
                            for i in range(5):
                                for j in range(10):
                                    if (pos_viev[i] == str(j)):
                                        if (i == 4) and (j != 11): Window.blit(Znumbers[j],(1331, 15+FPT))
                                        elif (i == 3) and (j != 11): Window.blit(Znumbers[j],(1343, 15+FPT))
                                        elif (i == 2) and (j != 11): Window.blit(Znumbers[j],(1355, 15+FPT))
                                        elif (i == 1) and (j != 11): Window.blit(Znumbers[j],(1367, 15+FPT))
                                        elif (i == 0) and (j != 11): Window.blit(Znumbers[j],(1383, 15+FPT))
                            
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
    Window.blit(decor5,(773,771))
    Window.blit(plotnost_dumout,(1284,737))
    
    if book_bool:   Window.blit(instr2,(823, 611))
    else:   Window.blit(instr1,(823, 611))

    if AB_bool:
        if AB_tick < 90: AB_tick += 1.5
    else:
        if AB_tick > 0:  AB_tick -= 1.5
        if AB_tick > 0:  AB_tick -= 1.5
    
    Window.blit(sppanel,(823,761))
    sparrow_rect = sppanel_arrow.get_rect(center=(859,770)) 
    sparrow2, sparrow_p = rot_center(sppanel_arrow, sparrow_rect, AB_tick)
    Window.blit(sparrow2, (sparrow_p))

    if ASP_tick > 0: ASP_tick -= 1

    if ASP_tick == 0:
        if addsettings_panel_bool:
            if addsettings_panel_tick < 13:
                addsettings_panel_subtick += 1
                if addsettings_panel_subtick > 2:
                    addsettings_panel_subtick = 0
                    addsettings_panel_tick += 1
        else:
            if addsettings_panel_tick > 0:
                addsettings_panel_subtick += 1
                if addsettings_panel_subtick > 2:
                    addsettings_panel_subtick = 0
                    addsettings_panel_tick -= 1
            elif addsettings_panel_closeandopen:
                addsettings_panel_closeandopen = False
                addsettings_panel_bool = True
                ASP_tick = 15
                addsettings_menu = addsettings_menu_past
                addsettings_menu_past = "None"

    superangle_subtick += 1*sim_speed
    if superangle_subtick >= 3:
        superangle_tick += 1
        superangle_subtick -= 3
        if superangle_tick > 3:
            superangle_tick = 0

    array_subtick[3] += 1*sim_speed*G
    
    while array_subtick[3] >= 5:
        array_subtick[3] -= 5
        array_tick[3] += 1
        
        for i in range(4):
            if gravity_a[i] > 0: gravity_a[i] -= 51
        
        if array_tick[3] > 8:
            array_tick[3] = 0
        if array_tick[3] < 4: gravity_a[array_tick[3]] = 255

    for i in range(7):
        gravity_shadow[i].set_alpha(gravity_a[i])

    for i in range(4,7,1):
            if gravity_a[i] > 0: gravity_a[i] -= 51

    if gravity_up_button_bool:
        gravity_a[6] = 255
        array_tick[5] += 1
        if array_trigger[5]:
            if array_tick[5] >= 1:
                array_tick[5] -= 1
                if G < 10:
                    G = (round((G + 0.01)*100))/100
        else:
            if array_tick[5] >= 10:
                array_tick[5] -= 10
                array_trigger[5] = True

    if gravity_down_button_bool:
        gravity_a[5] = 255
        array_tick[5] += 1
        if array_trigger[5]:
            if array_tick[5] >= 1:
                array_tick[5] -= 1
                if G > 0:
                    G = (round((G - 0.01)*100))/100
        else:
            if array_tick[5] >= 10:
                array_tick[5] -= 10
                array_trigger[5] = True

    if gravity_setbase_button_bool:
        if G == 1: gravity_setbase_button_bool = False
        elif G > 1:
                if abs(G - 1) <= 0.05: G = (round((G - 0.01)*100))/100
                else: G = (round((G - 0.05)*100))/100
        else:
                if abs(G - 1) <= 0.05: G = (round((G + 0.01)*100))/100
                else: G = (round((G + 0.05)*100))/100

    if plotnost_up_button_bool:
        pva_addspeed = 5.5

        array_tick[10] += 1*sim_speed
        if array_tick[10] >= 6:
            pva_lamplist = [True,randint(0,13) == 0,False]
            array_tick[10] -= 6
        
        array_tick[9] += 1
        if array_trigger[9]:
            if array_tick[9] >= 1:
                array_tick[9] -= 1
                if plotnost < 10:
                    plotnost = (round((plotnost + 0.01)*100))/100
        else:
            if array_tick[9] >= 10:
                array_tick[9] -= 10
                array_trigger[9] = True
    else:
        pva_addspeed = 1
        array_tick[10] += 1*sim_speed
        if array_tick[10] >= 6:
            pva_lamplist = [False,randint(0,8) == 0,True]
            array_tick[10] -= 6
                
    if plotnost_down_button_bool:
        pva_dumout = True
        array_tick[9] += 1
        if array_trigger[9]:
            if array_tick[9] >= 1:
                array_tick[9] -= 1
                if plotnost > 0:
                    plotnost = (round((plotnost - 0.01)*100))/100
        else:
            if array_tick[9] >= 10:
                array_tick[9] -= 10
                array_trigger[9] = True
    else:
        pva_dumout = False

    if plotnost_setbase_button_bool:
        if plotnost == 1: plotnost_setbase_button_bool = False
        elif plotnost > 1:
                if abs(plotnost - 1) <= 0.05: plotnost = (round((plotnost - 0.01)*100))/100
                else: plotnost = (round((plotnost - 0.05)*100))/100

                pva_dumout = True
        else:
                if abs(plotnost - 1) <= 0.05: plotnost = (round((plotnost + 0.01)*100))/100
                else: plotnost = (round((plotnost + 0.05)*100))/100

                pva_addspeed = 5.5
                pva_lamplist = [True,randint(0,13) == 0,False]

    if VS_base_button_bool:
        if sqr == 1 and volume == 1: VS_base_button_bool = False
        else:

            if sqr != 1:
                if sqr > 1:
                    if abs(sqr - 1) <= 0.10: sqr = (round((sqr - 0.01)*100))/100
                    else: sqr = (round((sqr - 0.10)*100))/100

                else:
                    if abs(sqr - 1) <= 0.10: sqr = (round((sqr + 0.01)*100))/100
                    else: sqr = (round((sqr + 0.10)*100))/100
                    
            if volume != 1:            
                if volume > 1:
                    if abs(volume - 1) <= 0.10: volume = (round((volume - 0.01)*100))/100
                    else: volume = (round((volume - 0.10)*100))/100

                else:
                    if abs(volume - 1) <= 0.10: volume = (round((volume + 0.01)*100))/100
                    else: volume = (round((volume + 0.10)*100))/100                

                
         

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

    Window.blit(colapanel_under,(872,733))
    if (addsettings_menu == "Plotnost"):

        Window.blit(plotnost_input,(879,740))
        
        if pva_lamplist[0]: pygame.draw.rect(Window, (112,255,58),(920,779, 3, 3))
        if pva_lamplist[1]: pygame.draw.rect(Window, (225,222,82),(920,783, 3, 3))
        if pva_lamplist[2]: pygame.draw.rect(Window, (255,88,58),(920,787, 3, 3))

        if pva_dumout:
            pygame.draw.rect(Window, (0,0,0),(934,745, 1, 5))
            pygame.draw.rect(Window, (0,0,0),(932,747, 5, 1))

        pva = pva + (2) * sim_speed * pva_addspeed
        pva_rect = plotnost_vent.get_rect(center=(899,775)) 
        pva2, pva_p = rot_center(plotnost_vent, pva_rect, -pva)

        Window.blit(pva2,pva_p)

        Window.blit(plotnost_up_button[int(plotnost_up_button_bool)],(921,760))
        Window.blit(plotnost_down_button[int(plotnost_down_button_bool)],(932,760))
        Window.blit(plotnost_base_button[int(plotnost_setbase_button_bool)],(943,760))
    
    if (addsettings_menu == "Gravity"):

        for i in range(21):
            ang = i*48-(G)*96
            if (ang < 48 and ang > -48) or 0:
                gravity_wheel_rect = gravity_wheel[i].get_rect(center=(939, 768)) 
                gravity_wheeln, gravity_wheel_p = rot_center(gravity_wheel[i], gravity_wheel_rect, -(ang))
            
                Window.blit(gravity_wheeln,gravity_wheel_p)
        
        Window.blit(gravity_info,(879,740))
        
    if (addsettings_menu == "Superangle"):
        Window.blit(superangle_input,(879,740))
        Window.blit(superangle_tugger[array_tick[0]],(884,752))  
    if array_trigger[0]:
        array_subtick[0] += 1
        if array_subtick[0] > 1:
            if array_tick[0] < 4:
                array_subtick[0] = 0
                array_tick[0] += 1
    else:
        array_subtick[0] += 1
        if array_subtick[0] > 1:
            if array_tick[0] > 0:
                array_subtick[0] = 0
                array_tick[0] -= 1

    if (addsettings_menu == "Sandv"):
        Window.blit(VS_input,(879,740))

        Window.blit(VS_volume_tugger,(884,760+VS_volume_tugger_pos))
        Window.blit(VS_sqr_tugger,(931,760+VS_sqr_tugger_pos))

        Window.blit(VS_base_button[int(VS_base_button_bool)],(906,770))

        if VS_volume_tugger_take and not(VS_base_button_bool):
            if VS_volume_tugger_pos >= -17 and VS_volume_tugger_pos < -12:
                array_tick[12] += 1
                if array_tick[12] >= 0:
                    array_tick[12] -= 0
                    if volume < 1000-0.01: volume = (round((volume + 0.01)*100))/100
                    elif volume < 1000-0: volume = (round((volume + 0.01)*100))/100
            elif VS_volume_tugger_pos >= -12 and VS_volume_tugger_pos < -7:
                array_tick[12] += 1
                if array_tick[12] >= 10:
                    array_tick[12] -= 10
                    if volume < 1000-0.01: volume = (round((volume + 0.01)*100))/100
                    elif volume < 1000-0: volume = (round((volume + 0.01)*100))/100
            elif VS_volume_tugger_pos >= -7 and VS_volume_tugger_pos < -2:
                array_tick[12] += 1
                if array_tick[12] >= 30:
                    array_tick[12] -= 30
                    if volume < 1000-0.01: volume = (round((volume + 0.01)*100))/100
                    elif volume < 1000-0: volume = (round((volume + 0.01)*100))/100
            elif VS_volume_tugger_pos > 2 and VS_volume_tugger_pos <= 7:
                array_tick[12] += 1
                if array_tick[12] >= 30:
                    array_tick[12] -= 30
                    if volume > 0.01: volume = (round((volume - 0.01)*100))/100
                    elif volume > 0: volume = (round((volume - 0.01)*100))/100
            elif VS_volume_tugger_pos > 7 and VS_volume_tugger_pos <= 12:
                array_tick[12] += 1
                if array_tick[12] >= 10:
                    array_tick[12] -= 10
                    if volume > 0.01: volume = (round((volume - 0.01)*100))/100
                    elif volume > 0: volume = (round((volume - 0.01)*100))/100
            elif VS_volume_tugger_pos > 12 and VS_volume_tugger_pos <= 17:
                array_tick[12] += 1
                if array_tick[12] >= 0:
                    array_tick[12] -= 0
                    if volume > 0.01: volume = (round((volume - 0.01)*100))/100
                    elif volume > 0: volume = (round((volume - 0.01)*100))/100

        if VS_sqr_tugger_take and not(VS_base_button_bool):
            if VS_sqr_tugger_pos >= -17 and VS_sqr_tugger_pos < -12:
                array_tick[12] += 1
                if array_tick[12] >= 0:
                    array_tick[12] -= 0
                    if sqr < 1000-0.01: sqr = (round((sqr + 0.01)*100))/100
                    elif sqr < 1000-0: sqr = (round((sqr + 0.01)*100))/100
            elif VS_sqr_tugger_pos >= -12 and VS_sqr_tugger_pos < -7:
                array_tick[12] += 1
                if array_tick[12] >= 10:
                    array_tick[12] -= 10
                    if sqr < 1000-0.01: sqr = (round((sqr + 0.01)*100))/100
                    elif sqr < 1000-0: sqr = (round((sqr + 0.01)*100))/100
            elif VS_sqr_tugger_pos >= -7 and VS_sqr_tugger_pos < -2:
                array_tick[12] += 1
                if array_tick[12] >= 30:
                    array_tick[12] -= 30
                    if sqr < 1000-0.01: sqr = (round((sqr + 0.01)*100))/100
                    elif sqr < 1000-0: sqr = (round((sqr + 0.01)*100))/100
            elif VS_sqr_tugger_pos > 2 and VS_sqr_tugger_pos <= 7:
                array_tick[12] += 1
                if array_tick[12] >= 30:
                    array_tick[12] -= 30
                    if sqr > 0.01: sqr = (round((sqr - 0.01)*100))/100
                    elif sqr > 0: sqr = (round((sqr - 0.01)*100))/100
            elif VS_sqr_tugger_pos > 7 and VS_sqr_tugger_pos <= 12:
                array_tick[12] += 1
                if array_tick[12] >= 10:
                    array_tick[12] -= 10
                    if sqr > 0.01: sqr = (round((sqr - 0.01)*100))/100
                    elif sqr > 0: sqr = (round((sqr - 0.01)*100))/100
            elif VS_sqr_tugger_pos > 12 and VS_sqr_tugger_pos <= 17:
                array_tick[12] += 1
                if array_tick[12] >= 0:
                    array_tick[12] -= 0
                    if sqr > 0.01: sqr = (round((sqr - 0.01)*100))/100
                    elif sqr > 0: sqr = (round((sqr - 0.01)*100))/100
                                
    Window.blit(colapanel[addsettings_panel_tick],(872,733))

    Window.blit(addsettings_under,(872,611))
    if (addsettings_menu == "Plotnost"):
        
        Window.blit(plotnost_info,(879,625))

        plotnost_cast_update(sim_speed)

        if plotnost == 5:
            F1 = 255
            F2 = 255
            F3 = 0
        elif plotnost < 5:
            F1 = 255
            F2 = 255
            F3 = round((1-(plotnost/5))*255)
        else:
            F1 = 255
            F2 = round((1-((plotnost-5)/5))*255)
            F3 = 0

        Window.blit(changColor(plotnost_atm,(F1,F2,F3)),(879,625))

        plotnost_num_print(plotnost,(F1,F2,F3))
        
    if (addsettings_menu == "Gravity"):
        
        Window.blit(gravity_base,(879,625))
        gravity_bit_update(sim_speed)
                
        for i in range(7):
            Window.blit(gravity_shadow[i],(879,625))
        
    if (addsettings_menu == "Superangle"):
        Window.blit(superangle_info[superangle_tick],(879,625))
        if array_tick[0] == 0: Window.blit(superangle_off,(879,625))
        else:
            superangle_update(superangle_DD, superangle_MM, superangle_SS)

    if (addsettings_menu == "Sandv"):
        Window.blit(VS_info,(879,625))

        VS_text_update(volume,sqr)  
        
    Window.blit(addsettings[addsettings_panel_tick],(872,611))

    Window.blit(colapanel_close,(872,803))

    array_subtick[2] += 1*sim_speed
    if array_subtick[2] >= 3:
        array_subtick[2] -= 3
        array_tick[2] += 1
        if array_tick[2] > 0:
            array_tick[2] = 0
            array_trigger[2] = bool(randint(0,1))

    if array_trigger[2]: Window.blit(decor6,(986,714))           

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
            if Atick_printmachine < 27:
                Atick_pmsubtick += 1
                if Atick_pmsubtick > 10:
                    Atick_printmachine += 1
                    if Atick_pmsubtick > 11: Atick_pmsubtick = 0
            else: Atick_printmachine += 1
            
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
                Atick_pmsubtick = 0
        
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

    Window.blit(simspeed_base,(1018, 712))
    if(simspeed_enable and simspeed_on): sim_angle = int(math.degrees(math.atan2(y_mouse-758, x_mouse-1064)))
    sim_speed = simspeed_update(sim_angle)
    if not simspeed_on: sim_speed = 1.00
    Window.blit(simspeed_block,(972, 735))
    sim_num(sim_speed)
    if simspeed_set: Window.blit(simspeed_button_set1,(979, 767))
    else: Window.blit(simspeed_button_set2,(979, 767))
    if simspeed_on: Window.blit(simspeed_button_on1,(979, 781))
    else: Window.blit(simspeed_button_on2,(979, 781))
    

    
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

    if (303+anim_x_1-11 > 0):
        Window = effect_light(Window,303+anim_x_1,693+anim_y_1,10)
        if not decor_bool: Window = effect_light(Window,317+anim_x_1,693+anim_y_1,10)

    if (array_trigger[2]): Window = effect_light(Window,992,720,10)
        
    for i in range (16):
        if (infoprint_status[infoprint_numtaken[15-i]] == "printed"):
            
            #shadow_rect(20,infoprint_pos_x[infoprint_numtaken[15-i]],infoprint_pos_y[infoprint_numtaken[15-i]],infoprint_pos_x[infoprint_numtaken[15-i]]+200,infoprint_pos_y[infoprint_numtaken[15-i]]+300,45,45)
            
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

    #shadow_rect(10,book_pos_x,book_pos_y,book_pos_x+300,book_pos_y+200,45,30)
    
    if book_bool:

        #shadow_rect(20,book_pos_x,book_pos_y,book_pos_x+300,book_pos_y+200,45,45)
        
        Window.blit(book_page[book_curr_page],(book_pos_x, book_pos_y))
        Window.blit(shadow_book,(book_pos_x, book_pos_y))
        
        book_text_update()

        if book_coffee_page == book_curr_page: Window.blit(book_coffee,(book_pos_x, book_pos_y))
        
    if (FS_bool):
        screen = pygame.display.get_surface()
        screen = pygame.transform.scale(screen,(int(1920*(1920/1440)),int(1080*(1080/810))))
        Window.blit(screen, (0, 0), (0,0,1920,1080))

    if loadtick <= 175:
        loadtick += 1
        
        Window.blit(blackscreen,(0,0))
        blackscreen.set_alpha(BS_a)
        if BS_bool:
            if BS_a < 255: BS_a += 4.25
        else:
            if BS_a > 0: BS_a -= 4.25

        Window.blit(python_logo,(580,253))
        python_logo.set_alpha(PL_a)

        Window.blit(intro_text1,(256,169))
        intro_text1.set_alpha(IT1_a)
        
        if loadtick > 115:
            BS_bool = False
        elif loadtick > 100:
            PL_bool = False
        elif loadtick > 70:
            PL_bool = True
        elif loadtick > 55:
            IT1_bool = False
        elif loadtick > 5:
            IT1_bool = True
            
        if PL_bool:
            if PL_a < 255: PL_a += 17
        else:
            if PL_a > 0: PL_a -= 17
        if IT1_bool:
            if IT1_a < 255: IT1_a += 17
        else:
            if IT1_a > 0: IT1_a -= 17

#Конец основной функции отрисовки

print("Время загрузки составило",int((time.perf_counter_ns()-start_time)/1000000)/1000,"секунд")
print()

previous_time = time.perf_counter_ns()

def keypress(event,S): #Считать нажатие клавиш
    global file_namechange
    if (event.type == pygame.KEYDOWN):
        if(event.key == pygame.K_BACKSPACE) and len(S) > 0: S = S[:len(S)-1]
        elif(event.key == pygame.K_RETURN):
            file_namechange = -1
        else:
            K = (str(event.unicode))
            if set_code(K) != "83":
                if len(S) < 24: S = S + K

    return S

#Игровой цикл

Run = True      
while Run: 
    clock.tick(FPS)

    new_time = time.perf_counter_ns()
    fps_count = 1/(((new_time-previous_time)/1000000000))
    previous_time = new_time
    if Real_time_count:
        round_time = ((new_time-previous_time)/1000000000)
        if round_time > (1/FPS): round_time = 1/FPS
    else:
        if sim_speed != 0: round_time = 1/(FPS/sim_speed)
        else: round_time = 0
    
    x_mouse,y_mouse = pygame.mouse.get_pos()
    if (FS_bool):
        x_mouse = int(x_mouse/(1920/1440))
        y_mouse = int(y_mouse/(1080/810))


    #Обработка событий

    for event in pygame.event.get():
        if event.type == pygame.QUIT: Run = False
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE): Run = False
        if not(BS_bool):
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE) and (sideshow_bool) and not(finish_sim) and not(simulator_run) and (file_namechange == -1):
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
                realkoss = koff*(((RPNW(plotnost,(600-height)/10,G))*(volume**2))/2)*sqr
                    
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
                realkoss = koff*(((RPNW(plotnost,(600-height)/10,G))*(volume**2))/2)*sqr

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 1206) and (x_mouse <= 1280) and (y_mouse >= 624) and (y_mouse <= 697) and (not (simulator_run)) and (finish_sim) and (repeat_button_up):
                repeat_button_set_play = True
                simulator_run = False
                finish_sim = False
                Energy_body = Energy_potencial + Energy_kinetikal
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
                hm2 = False
                hm4 = False
                hm8 = False
                hm16 = False
                hm32 = False
                hm64 = False
                hm128 = False
                hm256 = False   

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
                    if book_curr_page < 49: book_curr_page += 1
                else:
                    book_take_x = x_mouse - book_pos_x
                    book_take_y = y_mouse - book_pos_y
                    book_take = True

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 1067) and (x_mouse <= 1082) and (y_mouse >= 668) and (y_mouse <= 699):
                masch_avto_anim = True
                tugger_sound.play()

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 906) and (x_mouse <= 927) and (y_mouse >= 770) and (y_mouse <= 791) and (addsettings_menu == "Sandv") and not(VS_base_button_bool):
                VS_base_button_bool = True

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 830) and (x_mouse <= 864) and (y_mouse >= 766) and (y_mouse <= 797):
                AB_bool = True

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 921) and (x_mouse <= 929) and (y_mouse >= 760) and (y_mouse <= 769) and (addsettings_menu == "Plotnost") and (not(plotnost_setbase_button_bool)):
                plotnost_up_button_bool = True
                if plotnost < 10: plotnost = (round((plotnost + 0.01)*100))/100
                
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 932) and (x_mouse <= 940) and (y_mouse >= 760) and (y_mouse <= 769) and (addsettings_menu == "Plotnost") and (not(plotnost_setbase_button_bool)):
                plotnost_down_button_bool = True
                if plotnost > 0: plotnost = (round((plotnost - 0.01)*100))/100
                
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 943) and (x_mouse <= 951) and (y_mouse >= 760) and (y_mouse <= 769) and (addsettings_menu == "Plotnost") and (not(plotnost_setbase_button_bool)):
                plotnost_setbase_button_bool = True

                
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 882) and (x_mouse <= 897) and (y_mouse >= 629) and (y_mouse <= 644) and (addsettings_menu == "Gravity") and (not(gravity_setbase_button_bool)):
                gravity_a[6] = 255
                gravity_up_button_bool = True
                if G < 10: G = (round((G + 0.01)*100))/100
                
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 882) and (x_mouse <= 897) and (y_mouse >= 648) and (y_mouse <= 663) and (addsettings_menu == "Gravity") and (not(gravity_setbase_button_bool)):
                gravity_a[5] = 255
                gravity_down_button_bool = True
                if G > 0: G = (round((G - 0.01)*100))/100
                
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 882) and (x_mouse <= 897) and (y_mouse >= 667) and (y_mouse <= 682) and (addsettings_menu == "Gravity") and (not(gravity_setbase_button_bool)):
                gravity_a[4] = 255
                gravity_setbase_button_bool = True
                

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 1138) and (x_mouse <= 1169) and (y_mouse >= 764) and (y_mouse <= 795):
                if (abort_button_status == "off") and (simulator_run): abort_button_status = "rise"
                if (abort_button_status == "set"):
                    abort_button_status = "down"
                    simulator_run = False
                    finish_sim = False
                    Energy_body = Energy_potencial + Energy_kinetikal
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
                    hm2 = False
                    hm4 = False
                    hm8 = False
                    hm16 = False
                    hm32 = False
                    hm64 = False
                    hm128 = False
                    hm256 = False

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (addsettings_menu == "Sandv") and (x_mouse >=884) and (x_mouse <=  902) and (y_mouse >= 760+VS_volume_tugger_pos) and (y_mouse <= 771+VS_volume_tugger_pos):
                VS_volume_tugger_take = True
                VS_volume_tugger_postake = y_mouse-VS_volume_tugger_pos

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (addsettings_menu == "Sandv") and (x_mouse >=931) and (x_mouse <=  949) and (y_mouse >= 760+VS_sqr_tugger_pos) and (y_mouse <= 771+VS_sqr_tugger_pos):
                VS_sqr_tugger_take = True
                VS_sqr_tugger_postake = y_mouse-VS_sqr_tugger_pos

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (not(sideshow_bool)) and (x_mouse >=471) and (x_mouse <=  490) and (y_mouse >= 672) and (y_mouse <= 691) and not(True in asbutton_play) and (addsettings_panel_tick == 0 or addsettings_panel_tick == 13) and not(addsettings_panel_closeandopen):
                 asbutton_play[0]= True
                 button_tub.play()
                 if not addsettings_panel_bool:
                     addsettings_panel_bool = True
                     addsettings_menu = "Gravity"
                 else:
                     addsettings_panel_bool = False
                     addsettings_panel_closeandopen = True
                     addsettings_menu_past = "Gravity"
                     
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (not(sideshow_bool)) and (x_mouse >=498) and (x_mouse <=  517) and (y_mouse >= 672) and (y_mouse <= 691) and not(True in asbutton_play) and (addsettings_panel_tick == 0 or addsettings_panel_tick == 13) and not(addsettings_panel_closeandopen):
                 asbutton_play[1]= True
                 button_tub.play()
                 if not addsettings_panel_bool:
                     addsettings_panel_bool = True
                     addsettings_menu = "Superangle"
                 else:
                     addsettings_panel_bool = False
                     addsettings_panel_closeandopen = True
                     addsettings_menu_past = "Superangle"
                     
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (not(sideshow_bool)) and (x_mouse >=525) and (x_mouse <=  544) and (y_mouse >= 672) and (y_mouse <= 691) and not(True in asbutton_play) and (addsettings_panel_tick == 0 or addsettings_panel_tick == 13) and not(addsettings_panel_closeandopen):
                 asbutton_play[2]= True
                 button_tub.play()
                 if not addsettings_panel_bool:
                     addsettings_panel_bool = True
                     addsettings_menu = "Plotnost"
                 else:
                     addsettings_panel_bool = False
                     addsettings_panel_closeandopen = True
                     addsettings_menu_past = "Plotnost"
                 
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (not(sideshow_bool)) and (x_mouse >=552) and (x_mouse <=  571) and (y_mouse >= 672) and (y_mouse <= 691) and not(True in asbutton_play) and (addsettings_panel_tick == 0 or addsettings_panel_tick == 13) and not(addsettings_panel_closeandopen):
                 asbutton_play[3]= True
                 button_tub.play()
                 if not addsettings_panel_bool:
                     addsettings_panel_bool = True
                     addsettings_menu = "Sandv"
                 else:
                     addsettings_panel_bool = False
                     addsettings_panel_closeandopen = True
                     addsettings_menu_past = "Sandv"
                     
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 884) and (x_mouse <=  895) and (y_mouse >= 752) and (y_mouse <= 775) and (array_tick[0] == 0 or array_tick[0] == 4) and (addsettings_menu == "Superangle"):
                array_trigger[0] = not(array_trigger[0])

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 912) and (x_mouse <=  952) and (y_mouse >= 750) and (y_mouse <= 764) and (array_tick[0] == 4) and (addsettings_menu == "Superangle"):
                if (x_mouse >= 912) and (x_mouse <=  917) and (y_mouse >= 750) and (y_mouse <= 756): superangle_DD += 10
                elif (x_mouse >= 912) and (x_mouse <=  917) and (y_mouse >= 758) and (y_mouse <= 764): superangle_DD -= 10
                elif (x_mouse >= 919) and (x_mouse <=  924) and (y_mouse >= 750) and (y_mouse <= 756): superangle_DD += 1
                elif (x_mouse >= 919) and (x_mouse <=  924) and (y_mouse >= 758) and (y_mouse <= 764): superangle_DD -= 1            
                elif (x_mouse >= 926) and (x_mouse <=  931) and (y_mouse >= 750) and (y_mouse <= 756): superangle_MM += 10
                elif (x_mouse >= 926) and (x_mouse <=  931) and (y_mouse >= 758) and (y_mouse <= 764): superangle_MM -= 10
                elif (x_mouse >= 933) and (x_mouse <=  938) and (y_mouse >= 750) and (y_mouse <= 756): superangle_MM += 1
                elif (x_mouse >= 933) and (x_mouse <=  938) and (y_mouse >= 758) and (y_mouse <= 764): superangle_MM -= 1
                elif (x_mouse >= 940) and (x_mouse <=  945) and (y_mouse >= 750) and (y_mouse <= 756): superangle_SS += 10
                elif (x_mouse >= 940) and (x_mouse <=  945) and (y_mouse >= 758) and (y_mouse <= 764): superangle_SS -= 10
                elif (x_mouse >= 947) and (x_mouse <=  952) and (y_mouse >= 750) and (y_mouse <= 756): superangle_SS += 1
                elif (x_mouse >= 947) and (x_mouse <=  952) and (y_mouse >= 758) and (y_mouse <= 764): superangle_SS -= 1

                superangle = superangle_DD + (superangle_MM+(superangle_SS/60))/60
                
                if superangle > 90: superangle_DD = 90; superangle_MM = 0; superangle_SS = 0
                if superangle < 0: superangle_DD = 0; superangle_MM = 0; superangle_SS = 0
                
                if superangle_DD < 90:
                    if superangle_SS >= 60: superangle_MM += 1; superangle_SS -= 60
                    if superangle_MM >= 60: superangle_DD += 1; superangle_MM -= 60

                if superangle_DD > 0:
                    if superangle_SS < 0: superangle_MM -= 1; superangle_SS += 60
                    if superangle_MM < 0: superangle_DD -= 1; superangle_MM += 60

                superangle = superangle_DD + (superangle_MM+(superangle_SS/60))/60
                
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= masch_avto_curr) and (x_mouse <=  masch_avto_curr+7) and (y_mouse >= 693) and (y_mouse <= 704) and not(masch_avto_bool):
                masch_avto_take = True

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 979) and (x_mouse <=  1005) and (y_mouse >= 781) and (y_mouse <= 791):
                simspeed_on = not simspeed_on
                
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 979) and (x_mouse <=  1005) and (y_mouse >= 767) and (y_mouse <= 777) and not(simspeed_set) and (simspeed_on):
                simspeed_set = True
                sim_angle = -90

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 1035) and (x_mouse <=  1094) and (y_mouse >= 729) and (y_mouse <= 788) and not(simspeed_enable):
                simspeed_enable = True
                
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 679) and (x_mouse <= 715) and (y_mouse >= 672) and (y_mouse <= 698) and (not (simulator_run)) and (not (sideshow_bool)) and (not (finish_sim)) and not(presser_play):
                presser_play = True
                koff_tugger.play()
                
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
                        if (array_tick[0] == 4): ea = superangle
                        else: ea = angle
                        infoprint_status[haveused] = "printing"
                        IP_speed[haveused] = speed
                        IP_angle[haveused] = ea
                        IP_height[haveused] = (600-height)/10
                        IP_mass[haveused] = mass
                        if not rotor_ticker_bool: koff, kof_word = rotor_update(rotor_angle)
                        else: koff, kof_word = get_koff_numpad(koff_input)
                        if (presser_on) and ((koff) != 0): IP_koff[haveused] = koff
                        else: IP_koff[haveused] = "/"
                        if (ea != 0) and (speed != 0): IP_max[haveused] = (int(((600-pos_save_y[Max_pos])-40)*100))/1000
                        else: IP_max[haveused] = IP_height[haveused]
                        IP_dis[haveused] = (int(pos_save_x[tick]*100))/1000
                        IP_time_all[haveused] = (int(timer_save[tick]*1000))/1000
                        if (ea != 0) and (speed != 0): IP_time_DMV[haveused] = (int(timer_save[Max_pos]*1000))/1000
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
                        if (ea != 0) and (speed != 0): IP_dis_DMV[haveused] = (int(dis_save[Max_pos]*100))/1000
                        else: IP_dis_DMV[haveused] = "/"
                        IP_dis_PMV[haveused] = (int((dis_save[tick]-dis_save[Max_pos])*100))/1000
                        
                    else: haveused = 15

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 736) and (x_mouse <= 760) and (y_mouse >= 655) and (y_mouse <= 679) and (not (simulator_run)) and (not (finish_sim)) and not(numbutton_bool[0]):
                numbutton_bool[0] = True
                numpud_tub.play()
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
                numpud_tub.play()
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
                numpud_tub.play()
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
                numpud_tub.play()
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
                numpud_tub.play()
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
                numpud_tub.play()
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
                numpud_tub.play()
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
                numpud_tub.play()
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
                numpud_tub.play()
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
                numpud_tub.play()
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
                numpud_tub.play()
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
                numpud_tub.play()
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
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (x_mouse >= 24) and (x_mouse <= 294) and (y_mouse >= 624) and (y_mouse <= 680)and (not(sideshow_bool)) and (not (sideshow_bool)) and (not (simulator_run)) and (not (finish_sim)) and (array_tick[0] == 0): angle_enabled = True
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
                
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (rotor_ticker_bool) and(x_mouse >= 467) and (x_mouse <= 578) and (y_mouse >= 630) and (y_mouse <= 663) and (not(sideshow_bool)) and (not (sideshow_bool)) and (not (simulator_run)) and (not (finish_sim)):
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
                    menu = "main"

            if file_namechange != -1:
                ls = file_namechange
                inputfilename[file_namechange] = keypress(event,inputfilename[file_namechange])
                if inputfilename[file_namechange] == '' and file_namechange == -1: inputfilename[ls] = "без названия"
            
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "main")):
                if (enable_1): menu = "remember"; monitor_tub.play()
                if (enable_4): menu = "settings"; monitor_tub.play()
                if (enable_3): menu = "loadsave"; monitor_tub.play()
                if (enable_2): menu = "filesave"; monitor_tub.play()
                
            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "settings")):
                if (enable_1): menu = "main"; monitor_tub.play()
                if (enable_3):
                    vol += 10
                    if vol > 100: vol = 0

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "remember")):
                if (enable_1): menu = "main"; monitor_tub.play()

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

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "loadsave")):
                if (enable_1): menu = "main"; monitor_tub.play()
                if (enable_3): menu = "load_1"; monitor_tub.play()
                if (enable_4): menu = "load_2"; monitor_tub.play()
                if (enable_5): menu = "load_3"; monitor_tub.play()
                if (enable_6): menu = "load_4"; monitor_tub.play()
                if (enable_8): menu = "load_avto"; monitor_tub.play()

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "filesave")):
                if (enable_1): menu = "main"; monitor_tub.play()
                if (enable_3): menu = "save_1"; monitor_tub.play()
                if (enable_4): menu = "save_2"; monitor_tub.play()
                if (enable_5): menu = "save_3"; monitor_tub.play()
                if (enable_6): menu = "save_4"; monitor_tub.play()

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "load_1")):
                if (enable_1): menu = "loadsave"; monitor_tub.play()
                if (enable_3):
                    if (not (simulator_run)) and (not (finish_sim)):
                        speed_word = str(file_speed[0])
                        ea = (file_angle[0])
                        if str(ea)[0] != "|": angle = ea
                        else:
                            array_trigger[0] = True
                            superangle_DD = int(ea[1:2])*10
                            superangle_MM = int(ea[4:5])*10
                            superangle_SS = int(ea[7:8])*10
                            superangle = superangle_DD + (superangle_MM+(superangle_SS/60))/60
                        height = 600-10*(file_height[0])
                        mass_word = str(file_mass[0])
                        S = str(file_koff[0])
                        if S != "0":
                            for i in range(len(S)):
                                if S[i] == ".":
                                    S = S[:i]+S[i+1:]
                                    break
                            koff_input = S
                            if presser_on == False: presser_play = True
                            if not rotor_ticker_bool: RTA_nor = True; rotor_ticker_bool = False
                        else:
                            if presser_on == True: presser_play = True
                            
            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "load_2")):
                if (enable_1): menu = "loadsave"; monitor_tub.play()
                if (enable_3):
                    if (not (simulator_run)) and (not (finish_sim)):
                        speed_word = str(file_speed[1])
                        ea = (file_angle[1])
                        if str(ea)[0] != "|": angle = ea
                        else:
                            array_trigger[0] = True
                            superangle_DD = int(ea[1:2])*10
                            superangle_MM = int(ea[4:5])*10
                            superangle_SS = int(ea[7:8])*10
                            superangle = superangle_DD + (superangle_MM+(superangle_SS/60))/60
                        height = 600-10*(file_height[1])
                        mass_word = str(file_mass[1])
                        S = str(file_koff[1])
                        if S != "0":
                            for i in range(len(S)):
                                if S[i] == ".":
                                    S = S[:i]+S[i+1:]
                                    break
                            koff_input = S
                            if presser_on == False: presser_play = True
                            if not rotor_ticker_bool: RTA_nor = True; rotor_ticker_bool = False
                        else:
                            if presser_on == True: presser_play = True
                            
            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "load_3")):
                if (enable_1): menu = "loadsave"; monitor_tub.play()
                if (enable_3):
                    if (not (simulator_run)) and (not (finish_sim)):
                        speed_word = str(file_speed[2])
                        ea = (file_angle[2])
                        if str(ea)[0] != "|": angle = ea
                        else:
                            array_trigger[0] = True
                            superangle_DD = int(ea[1:2])*10
                            superangle_MM = int(ea[4:5])*10
                            superangle_SS = int(ea[7:8])*10
                            superangle = superangle_DD + (superangle_MM+(superangle_SS/60))/60
                        height = 600-10*(file_height[2])
                        mass_word = str(file_mass[2])
                        S = str(file_koff[2])
                        if S != "0":
                            for i in range(len(S)):
                                if S[i] == ".":
                                    S = S[:i]+S[i+1:]
                                    break
                            koff_input = S
                            if presser_on == False: presser_play = True
                            if not rotor_ticker_bool: RTA_nor = True; rotor_ticker_bool = False
                        else:
                            if presser_on == True: presser_play = True

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "load_4")):
                if (enable_1): menu = "loadsave"; monitor_tub.play()
                if (enable_3):
                    if (not (simulator_run)) and (not (finish_sim)):
                        speed_word = str(file_speed[3])
                        ea = (file_angle[3])
                        if str(ea)[0] != "|": angle = ea
                        else:
                            array_trigger[0] = True
                            superangle_DD = int(ea[1:2])*10
                            superangle_MM = int(ea[4:5])*10
                            superangle_SS = int(ea[7:8])*10
                            superangle = superangle_DD + (superangle_MM+(superangle_SS/60))/60
                        height = 600-10*(file_height[3])
                        mass_word = str(file_mass[3])
                        S = str(file_koff[3])
                        if S != "0":
                            for i in range(len(S)):
                                if S[i] == ".":
                                    S = S[:i]+S[i+1:]
                                    break
                            koff_input = S
                            if presser_on == False: presser_play = True
                            if not rotor_ticker_bool: RTA_nor = True; rotor_ticker_bool = False
                        else:
                            if presser_on == True: presser_play = True

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "load_avto")):
                if (enable_1): menu = "loadsave"; monitor_tub.play()
                if (enable_3):
                    if (not (simulator_run)) and (not (finish_sim)):
                        speed_word = str(file_speed[4])
                        ea = (file_angle[3])
                        if str(ea)[0] != "|": angle = ea
                        else:
                            array_trigger[0] = True
                            superangle_DD = int(ea[1:2])*10
                            superangle_MM = int(ea[4:5])*10
                            superangle_SS = int(ea[7:8])*10
                            superangle = superangle_DD + (superangle_MM+(superangle_SS/60))/60
                        height = 600-10*(file_height[4])
                        mass_word = str(file_mass[4])
                        S = str(file_koff[4])
                        if S != "0":
                            for i in range(len(S)):
                                if S[i] == ".":
                                    S = S[:i]+S[i+1:]
                                    break
                            koff_input = S
                            if presser_on == False: presser_play = True
                            if not rotor_ticker_bool: RTA_nor = True; rotor_ticker_bool = False
                        else:
                            if presser_on == True: presser_play = True

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "save_1")):
                if (enable_1): menu = "filesave"; file_namechange = -1; monitor_tub.play()
                if (enable_3): save_file(1); load_file(1); monitor_savetick = randint(24,38)
                if (enable_4): file_namechange = 0

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "save_2")):
                if (enable_1): menu = "filesave"; file_namechange = -1; monitor_tub.play()
                if (enable_3): save_file(2); load_file(2); monitor_savetick = randint(24,38)
                if (enable_4): file_namechange = 1

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "save_3")):
                if (enable_1): menu = "filesave"; file_namechange = -1; monitor_tub.play()
                if (enable_3): save_file(3); load_file(3); monitor_savetick = randint(24,38)
                if (enable_4): file_namechange = 2

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((menu == "save_4")):
                if (enable_1): menu = "filesave"; file_namechange = -1; monitor_tub.play()
                if (enable_3): save_file(4); load_file(4); monitor_savetick = randint(24,38)
                if (enable_4): file_namechange = 3

            if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
                AB_bool = False
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
                simspeed_enable = False
                simspeed_set = False
                gravity_up_button_bool = False
                gravity_down_button_bool = False
                plotnost_up_button_bool = False
                plotnost_down_button_bool = False
                array_trigger[5] = False
                array_trigger[9] = False
                array_tick[5] = 0
                array_tick[9] = 0
                VS_volume_tugger_take = False
                VS_sqr_tugger_take = False
                for i in range(16):
                    infoprint_havetaken[i] = False
                if (book_take):
                    if (book_pos_x >= 687) and (book_pos_x <= 707) and (book_pos_y >= 467) and (book_pos_y <= 487): book_bool = False
                book_take = False
            
    for i in range(16):
        if (infoprint_havetaken[i]):
            infoprint_pos_x[i] = x_mouse - infoprint_pointtaken_x[i]
            infoprint_pos_y[i] = y_mouse - infoprint_pointtaken_y[i]

    if (VS_volume_tugger_take):
        VS_volume_tugger_pos = y_mouse - VS_volume_tugger_postake
    elif (VS_volume_tugger_pos != 0):
        if (VS_volume_tugger_pos > 0):
            VS_volume_tugger_pos -= 1
        else:
            VS_volume_tugger_pos += 1

    if (VS_sqr_tugger_take):
        VS_sqr_tugger_pos = y_mouse - VS_sqr_tugger_postake
    elif (VS_sqr_tugger_pos != 0):
        if (VS_sqr_tugger_pos > 0):
            VS_sqr_tugger_pos -= 1
        else:
            VS_sqr_tugger_pos += 1

    if VS_volume_tugger_pos > 17: VS_volume_tugger_pos = 17
    if VS_volume_tugger_pos < -17: VS_volume_tugger_pos = -17  
    if VS_sqr_tugger_pos > 17: VS_sqr_tugger_pos = 17
    if VS_sqr_tugger_pos < -17: VS_sqr_tugger_pos = -17
    
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

    if AB_tick == 90: Run = False
    
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
        addsettings_panel_bool = False
        addsettings_menu = "None"
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
        addsettings_panel_bool = False
        
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

    avtosave_tick += 1
    if avtosave_mode != "ns" and avtosave_mode != "ae":
        if avtosave_mode == "1m":
            if avtosave_tick > FPS*60:
                avtosave_tick = 0
                save_file(5)
                load_file(5)
        if avtosave_mode == "3m":
            if avtosave_tick > FPS*60*3:
                avtosave_tick = 0
                save_file(5)
                load_file(5)
        if avtosave_mode == "5m":
            if avtosave_tick > FPS*60*5:
                avtosave_tick = 0
                save_file(5)
                load_file(5)

    pygame.mixer.music.set_volume(vol/100*0)
                
    if (simulator_run): #Вычисление траектории
        if True:
            stime += round_time
            if (array_tick[0] == 4): ea = superangle
            else: ea = angle
            while stime >= 1/FPS:
                stime -= 1/FPS
                if not rotor_ticker_bool: koff, kof_word = rotor_update(rotor_angle)
                else: koff, kof_word = get_koff_numpad(koff_input)
                if (presser_on) and (realkoss != 0) and (plotnost != 0):  #Если сопротивление воздуха есть
                    if tick > 0: realkoss = koff*(((RPNW(plotnost,(600-(past_y_pos+40))/10,G))*(volume**2))/2)*sqr
                    tick = tick + 1
                    timer = (timer + 1/FPS)
                    x_pos = ((speed*10*math.cos(math.radians(ea)))*(mass/realkoss)*(1-(math.e**(-(realkoss/mass)*timer))))
                    y_pos = -((mass/realkoss)*(((speed*10*math.sin(math.radians(ea)))+((mass*9.80665*G)/realkoss))*(1-(math.e**(-(realkoss/mass)*timer)))-9.80665*G*timer)) + height - 40
                    animballangle = math.degrees(math.atan2(y_pos-past_y_pos,x_pos-past_x_pos))
                    if ea == 90: angle_save[tick] = 90
                    else: angle_save[tick] = animballangle
                    if tick > 0:
                        dis_save[tick] = dis_save[tick-1] + (math.sqrt((x_pos-past_x_pos)**2 + (y_pos-past_y_pos)**2))
                        speed_xr = abs(x_pos-past_x_pos)*6
                        speed_yr = abs(y_pos-past_y_pos)*6
                        speed_or = (math.sqrt((speed_xr)**2 + (speed_yr)**2))
                        speed_x_save[tick] = speed_xr
                        speed_y_save[tick] = speed_yr
                        speed_o_save[tick] = speed_or
                    past_x_pos = x_pos
                    past_y_pos = y_pos
                    pos_save_x[tick] = x_pos
                    pos_save_y[tick] = y_pos
                    timer_save[tick] = timer
                    if (tick%(int(FPS/6)) == 0):
                        Dot_count = Dot_count + 1
                        Dot_spawn_x[Dot_count] = int(x_pos + 17)
                        Dot_spawn_y[Dot_count] = int(y_pos + 17)

                    if (y_pos > 560):
                        break
                    
                else:                                                     #Если сопротивление воздуха нет
                    tick = tick + 1
                    timer = (timer + 1/FPS)
                    x_pos = (((speed*10)))* timer * math.cos(math.radians(ea))
                    y_pos = -((((speed*10))) * timer * math.sin(math.radians(ea)) - ((G*9.80665 * (timer*timer))/2)) + height - 40
                    animballangle = math.degrees(math.atan2(y_pos-past_y_pos,x_pos-past_x_pos))
                    if ea == 90: angle_save[tick] = 90
                    else: angle_save[tick] = animballangle
                    if tick > 0:
                        dis_save[tick] = dis_save[tick-1] + (math.sqrt((x_pos-past_x_pos)**2 + (y_pos-past_y_pos)**2))
                        speed_xr = abs(speed*math.cos(math.radians(ea)))
                        speed_yr = abs(y_pos-past_y_pos)*6
                        speed_or = (math.sqrt((speed_xr)**2 + (speed_yr)**2))
                        speed_x_save[tick] = speed_xr
                        speed_y_save[tick] = speed_yr
                        speed_o_save[tick] = speed_or
                    past_x_pos = x_pos
                    past_y_pos = y_pos
                    pos_save_x[tick] = x_pos
                    pos_save_y[tick] = y_pos
                    timer_save[tick] = timer
                    if (tick%(int(FPS/6)) == 0):
                        Dot_count = Dot_count + 1
                        Dot_spawn_x[Dot_count] = int(x_pos + 17)
                        Dot_spawn_y[Dot_count] = int(y_pos + 17)

                    if (y_pos > 560):
                        break

                RYP = ((600-y_pos)-40)/10
                if RYP < 0: RYP = 0

                Energy_potencial = mass*(G*9.80665)*(RYP)
                Energy_kinetikal = ((mass*(speed_or**2))/2)*10

                if (presser_on) and (koff != 0): EP_save[tick] = (Energy_potencial/Energy_body,Energy_kinetikal/Energy_body,1-(Energy_potencial+Energy_kinetikal)/Energy_body)
                else: EP_save[tick] = (Energy_potencial/(Energy_potencial+Energy_kinetikal),Energy_kinetikal/(Energy_potencial+Energy_kinetikal),0)
                
    update() #Отрисовать
    pygame.display.flip() #Обновить экран

#Сохранение
if avtosave_exitmode: save_file(5)
save_settings()

pygame.quit()
