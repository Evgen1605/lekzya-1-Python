# Управляющие конструкции: while и вариация while -else

# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i = i + 1
# else:
#     print('Пожалуй хватит')
# print(i)


n = 423
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
else:
    print('Пожалуй')
    print('хватит )')
print(summa)

# На замену break отлично подходит метод флажка.

# Задача: Пользователь вводит число, необходимо найти минимальный делитель данного числа

n = int(input('Введите число: '))
flag = True
i = 2
while flag:
  if n % i == 0:  # если остаток при делении числа n на i равен 0
    flag = False
    print(i)
  elif i > n // 2:  # делить числа не может превышать введенное число, деленное на 2
    print(n)
    flag = False
i += 1
