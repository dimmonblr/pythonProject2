#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

# РЕШЕНИЕ
# сократим ссылки на координаты

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

# вычислим расстояния между городами

moscow_london = ((moscow[0] - london[0])**2 + (moscow[1] - london[1])**2)**0.5
moscow_paris = ((moscow[0] - paris[0])**2 + (moscow[1] - paris[1])**2)**0.5

london_moscow = moscow_london
london_paris = ((london[0] - paris[0])**2 + (london[1] - paris[1])**2)**0.5

paris_moscow = moscow_paris
paris_london = london_paris

distances = {'Moscow' : {'London' : moscow_london, 'Paris' : moscow_paris},
             'London' : {'Moscow' : london_moscow, 'Paris' : london_paris},
             'Paris' : {'Moscow' : paris_moscow, 'London' : paris_london}
             }

#print(distances['Moscow']["London"])
#print(distances['Moscow']["Paris"])



pprint(distances)




