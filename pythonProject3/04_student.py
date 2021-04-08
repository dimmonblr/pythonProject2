# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expences = 10000, 12000

# Расходы и доходы за первый месяц
total_grant = educational_grant     #стипендия
month_expences = expences           #траты за месяц
total_expences = month_expences     #общие траты

# Расходы и доходы за оставшиеся 9 месяцев
period = 9
while period > 0:
    period -= 1
    total_grant += educational_grant
    month_expences = month_expences + 0.03 * month_expences
    total_expences += month_expences
diff = total_expences - total_grant
print("Студенту надо попросить ", round(diff,2), " руб.")