# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
"""step = 0
for color in rainbow_colors:
    point1 = sd.get_point(50 + step, 50)
    point2 = sd.get_point(350 + step, 450)
    sd.line(start_point=point1, end_point=point2, color=color, width=4)
    step +=5"""

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

step = 0
for color in rainbow_colors:
    point1 = sd.get_point(500, 0)
    sd.circle(center_position=point1, radius = 500 +step, color = color, width=10)
    step +=10

sd.pause()
