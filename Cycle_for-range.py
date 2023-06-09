# В Python цикл for в основном используется для перебора значений
# ● Range выдает значения из диапазона с шагом 1.
# ● Если указано только одно число — от 0 до заданного числа.
# ● Если нужен другой шаг, третьим аргументов можно задать приращение.

r = range(5) # 0 1 2 3 4 
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ---------
r = range(1, 10, 2) # 1 3 5 7 9
r = range(100, 0, -20) # 100 80 60 40 20
for i in r:
    print(i)

# Можно использовать цикл for () и со строками, так как у строк есть нумерация, такая же как и у массивов, начинается с 0:
for i in 'qwerty':
    print(i)

# Можно использовать вложенные циклы:
line = ''
for i in range(5):
    line = ''
    for j in range(5):
        line += '*'
    print(line)