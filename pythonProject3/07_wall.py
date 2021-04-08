# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

def brick(x,y):
    point1= sd.get_point(0+x,0+y)
    point2= sd.get_point(100+x,50+y)
    sd.rectangle(left_bottom=point1, right_top=point2, width = 3, color=sd.COLOR_ORANGE)

for x in range(0,1000,100):             #нечетные слои кирпичей
    for y in range(0,600,100):
        brick(x, y)
for x in range(-50,1000,100):           #четные слои кирпичей
    for y in range(50,600,100):
        brick(x, y)
sd.pause()
