# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
calendar = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
if 1 <= month <= 12:
    print('Вы ввели', month)
    print('Количество дней в данном месяце -', calendar[month])
else:
    print("Номер месяца некорректен")


