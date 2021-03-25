money = float(input("введите сумму: "))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

ТКБ = float(per_cent['ТКБ'])*(money/100)
СКБ = float(per_cent['СКБ'])*(money/100)
ВТБ = float(per_cent['ВТБ'])*(money/100)
СБЕР = float(per_cent['СБЕР'])*(money/100)

print ('ТКБ =', ТКБ)
print ('СКБ =', СКБ)
print ('ВТБ =', ВТБ)
print ('СБЕР =', СБЕР)

deposit = [ТКБ, СКБ, ВТБ, СБЕР]
print('Deposit =', deposit)

maximum = max(deposit)
print('Максимальная сумма, которую вы можете заработать = ', maximum)