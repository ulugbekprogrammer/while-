# 1
# my_list = ['salom', 'qandesan', 'hello']
# n = (input('Birirnima kiriting: '))
# i = 0
# has_word = False
# while i < len(my_list):
#     if my_list[i] == n:
#         has_word = True
#         break
#     i += 1
# print(has_word)


# 2
# i = 100
# while i < 1000:
#     summa = 0
#     for x in str(i):
#         summa += int(x)
#     if summa > 5 and summa < 8:
#         print(i)
#     i += 1


# 3
# n = int(input('Son kiriting: '))
# counter = 0
# if n < 0:
#     n *= -1
# while n > 0:
#     n //= 10
#     counter += 1
# print(counter)

# 4
# i = 0
# summa = 0
# while i < 5:
#     n = int(input('Son kiriting: '))
#     summa += n
#     i += 1
# print(summa)


# 5
# i = 0
# get_max = 0
# while i < 8:
#     n = int(input('Son kiriting: '))
#     if n > get_max:
#         get_max = n
#     i += 1
# print(get_max)


# 6
# i = 1
# get_min = int(input("1-sonni kiriting: "))
# while i < 8:
#     n = int(input(f'{i+1}-son kiriting: '))
#     if n < get_min:
#         get_min = n
#     i += 1
# print(get_min)
#

# 7
# my_list = [21, 43, 12, 54]
# i = 0
# while i < len(my_list):
#     print(my_list[i]*2)
#     i += 1

# 8
# n = int(input('Son kiriting: '))
# summa = 0
# i = 1
# while i < n:
#     if n % i == 0:
#         summa += i
#     i += 1
#
# if summa == n:
#     print(f'{n} mukammal son')
# else:
#     print(f'{n} mukammal son emas')


# 9
# n = int(input('Son kiriting: '))
# i = 2
# isPower2 = False
# while i < n:
#     i *= 2
#     if i == n:
#         isPower2 = True
# print(isPower2)
#

# 10
# n = int(input('Son kiriting: '))
# i = 2
# k = 1
# while i < n:
#     i *= 2
#     k += 1
# if i != n:
#     k = "2 ning darajasi emas"
# print(k)


# 11
# n = int(input('Son kiriting: '))
# faktorial = 1
# i = 1
# while i <= n:
#     faktorial *= i
#     i += 1
# print(faktorial)


# 12
# x = [1,23,10,45,-41,56,78,13]
# juft_list = []
# toq_list = []
# i = 0
# while i < len(x):
#     if x[i] % 2 == 0:
#         juft_list.append(x[i])
#     if x[i] % 2 == 1:
#         toq_list.append(x[i])
#     i += 1
#
# print(juft_list)
# print(toq_list)


# 13
# n = int(input('Son kiriting: '))
# i = 1
# while i <= 10:
#     print(f'{n} * {i} = {n*i}')
#     i += 1


# 14
# cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"]
# i = 0
# get_max_len = cars[0]
# while i < len(cars):
#     if len(cars[i]) > len(get_max_len):
#         get_max_len = cars[i]
#     i += 1
#
# print(get_max_len)


# 15
# cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"]
# i = 0
# while i < len(cars):
#     if cars[i].endswith('a'):
#         print(cars[i])
#     i += 1


# cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"]
# i = 0
# while i < len(cars):
#     s = cars[i]
#     if s[len(s) -1] == 'a':
#         print(s)
#     i += 1

# uy ishi
# n = int(input('Son kiriting: '))
# num = n
# k = 0
# while n < 2 * num:
#     n += 0.1
#     k += 1
# print(k)

# n = int(input('Son kiriting: '))
# i = n
# k = 0
# while i < 2 * n:
#     i += 0.1 * i
#     k += 1
# print(k)