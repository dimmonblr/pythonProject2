# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random

sd.resolution = (1200, 600)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.



def smile(x, y, color):
    point = sd.get_point(x, y)
    coord_1_eye = sd.get_point(x - 30, y)
    coord_2_eye = sd.get_point(x - 10, y + 20)
    coord_3_eye = sd.get_point(x + 10, y)
    coord_4_eye = sd.get_point(x + 30, y + 20)
    face = sd.circle(point, color=color, width=4)
    eye1 = sd.ellipse(coord_1_eye, coord_2_eye, color=color)
    eye2 = sd.ellipse(coord_3_eye, coord_4_eye, color=color)
    s1 = sd.get_point(x - 25, y - 20)
    s2 = sd.get_point(x - 10, y - 35)
    s3 = sd.get_point(x + 10, y - 35)
    s4 = sd.get_point(x + 25, y - 20)
    smile_list = [s1, s2, s3, s4]
    sd.lines(point_list=smile_list, width=4, color=color)


#smile (100,500,sd.COLOR_GREEN)
for _ in range(10):
    x = random.randint(0, 1200)
    y = random.randint(0, 600)
    smile(x, y, sd.COLOR_GREEN)
sd.pause()