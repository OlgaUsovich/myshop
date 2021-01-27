# ДЗ8 07.12.2020 Усович Ольга гр. 07.10.2020

# Задача 51. В данном массиве найдите два наименьших элемента.
# from random import randint
#
# n = int(input('Задайте количество элементов массива: '))
# m = [randint(-100, 100) for i in range(n)]
# mins = [min(m)]
# m.remove(min(m))
# mins.append(min(m))
# print(f'Два наименьших элемента массива: {mins[0]} и {mins[1]}')


# Задача 52. Определите, есть ли в массиве повторяющиеся элементы.
# from random import randint
#
# n = int(input('Задайте количество элементов массива: '))
# m = [randint(-20, 20) for i in range(n)]
# repeats = []
# for i in m:
#     if m.count(i) > 1 and i not in repeats:
#         repeats.append(i)
# for i in repeats:
#     print(f'Число {i} повторилось в массиве {m.count(i)} раз(а)')


# Задача 53. В данном массиве найдите наибольшую серию подряд идущих элементов, расположенных по возрастанию.

# m = [7, 1, 2, 3, 8, 17, 16, 15, 40, 41, 42, 43, 11, 44, 45, 12, 13, 14, 15, 16, 52, 55, 60, 88, 17, 18, 1, 2, 3, 4]
#
# main_list = []
# sequence = []
# for i in range(len(m)):
#     if i != len(m)-1 and m[i + 1] > m[i]:
#         sequence.append(m[i])
#     elif m[i] > m[i-1]:
#         sequence.append(m[i])
#         main_list.append(sequence)
#         sequence = []
#
# max_sequence = []
# for i in range(1, len(main_list)):
#     if len(main_list[i]) > len(max_sequence):
#         max_sequence = main_list[i]
#
# print(f'Наибольшая серия подряд идущих элементов: {max_sequence}. Ее длина равна: {len(max_sequence)}')


# Задача 54. В массиве найдите количество серий из четверок подряд идущих попарно различных элементов.

# m = [7, 1, 1, 2, 2, 3, 3, 4, 8, 17, 16, 16, 15, 14, 13, 40, 41, 42, 43, 11, 11, 44, 45, 12, 13, 14,
#      15, 16, 17, 17, 18, 19, 20, 20, 1, 2, 3, 4]
#
# fours = []
# four = []
# with_overlap = []
#
# i = 0
#
# # for i in range(len(m)):      # без пересечения
# #     if len(four) == 4:
# #         fours.append(four)
# #         four = []
# #     if i == len(m)-1 and m[i] != m[i - 1]:
# #         four.append(m[i])
# #     elif m[i] == m[i + 1] and len(four) != 3:
# #         four = []
# #     else:
# #         four.append(m[i])
# #
# # print('Найденные последовательности:', fours)
# # print('Количество серий из четверок подряд идущих попарно различных элементов равно:', len(fours))
#
# for i in range(len(m)):     # c пересечением
#     if i == len(m)-1 and m[i] != m[i - 1]:
#         with_overlap.append(m[i])
#     elif m[i] == m[i + 1] and len(four) != 3:
#         fours.append(with_overlap)
#         with_overlap = []
#     else:
#         with_overlap.append(m[i])
#
# print(fours)
# count = 0
# for i in fours:
#     if len(i) >= 4:
#         lenth = len(i) - 4
#         count += 1 + lenth
# print('Количество серий из четверок подряд идущих попарно различных элементов равно:', count)


# Задача 55. Определите, можно ли вычеркнуть из данного массива одно число так, чтобы оставшиеся числа
# оказались упорядоченными по возрастанию.

# m = [-1, 1, 2, 3, 4, 4, 20, 5, 6, 7, 8, 9]
#
# count = 0
# num = 0
# for i in range(len(m)):
#     if i == 0:
#         if m[i] > m[i+1]:
#             num = m[i]
#             count += 1
#             break
#     elif i == len(m)-1:
#         if m[i] < m[i-1]:
#             num = m[i]
#             count += 1
#             break
#     elif (m[i + 1] < m[i] > m[i-1] and m[i + 1] >= m[i-1]) or m[i + 1] > m[i] < m[i-1]:
#         num = m[i]
#         count += 1
#         break
#
# if num:
#     m.remove(num)
#     for i in range(len(m)):
#         if i == 0:
#             if m[i] > m[i + 1]:
#                 num = m[i]
#                 count += 1
#                 break
#         elif i == len(m) - 1:
#             if m[i] < m[i - 1]:
#                 num = m[i]
#                 count += 1
#                 break
#         elif (m[i + 1] < m[i] > m[i-1] and m[i + 1] >= m[i-1]) or m[i + 1] > m[i] < m[i - 1]:
#             num = m[i]
#             count += 1
#             break
# if count == 1:
#     print('Из данного массива МОЖНО вычеркнуть одно число так, чтобы оставшиеся числа оказались\n'
#           'упорядоченными по возрастанию.')
# else:
#     print('Из данного массива НЕЛЬЗЯ вычеркнуть одно число так, чтобы оставшиеся числа оказались\n'
#           'упорядоченными по возрастанию.')

# Задача 56. В массиве заменить все числа, большие данного числа, на среднее арифметическое всех чисел массива.
# from random import randint
#
# m = [randint(-20, 20) for i in range(randint(5, 20))]
# print('Исходный массив:', m)
# n = int(input('Введите число: '))
# aver = round(sum(m)/len(m), 2)
# for i in range(len(m)):
#     if m[i] > n:
#         m[i] = aver
# print('Преобразованный массив:', m)

# Задача 57. Дан массив. Заменить все числа, меньшие последнего элемента массива, на первый элемент.
# from random import randint
#
# m = [randint(-20, 20) for i in range(randint(5, 20))]
# print('Исходный массив:', m)
# for i in range(len(m)):
#     if m[i] < m[-1]:
#         m[i] = m[0]
# print('Преобразованный массив:', m)

# Задача 58. Поменять местами наибольший и наименьший элементы массива.
# from random import randint
#
# m = [randint(-20, 20) for i in range(randint(5, 20))]
# print('Исходный массив:', m)
# max_m = max(m)
# min_m = min(m)
# for i in range(len(m)):
#     if m[i] == max_m:
#         m[i] = min_m
#     elif m[i] == min_m:
#         m[i] = max_m
# print('Преобразованный массив:', m)

# Задача 59. Найти наибольший четный элемент массива и поменять его местами с наименьшим нечетным элементом.
# Если одного из таких элементов нет, то всем элементам массива присвоить значение, равное нулю.

# from random import randint
#
# m = [randint(-20, 20) for i in range(randint(5, 20))]
# print('Исходный массив:', m)
#
# evens = []
# notevens = []
# for i in m:
#     if i % 2 == 0:
#         evens.append(i)
#     else:
#         notevens.append(i)
# for i in range(len(m)):
#     if not evens or not notevens:
#         m[i] = 0
#     else:
#         if m[i] == max(evens):
#             m[i] = min(notevens)
#         elif m[i] == min(notevens):
#             m[i] = max(evens)
# print('Преобразованный массив:', m)

# Задача 60. Заменить каждый элемент массива с четным номером на соседний слева элемент.

# from random import randint
#
# m = [randint(-20, 20) for i in range(randint(5, 20))]
# print('Исходный массив:', m)
#
# for i in range(len(m)):
#     if i % 2 != 0:   # с четным номером = с нечетным индексом
#         m[i] = m[i-1]
# print('Преобразованный массив:', m)






