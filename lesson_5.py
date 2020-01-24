# 1. Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# свидетельствует пустая строка.


# with open('text_lesson_5.txt', 'w') as file:
#     while True:
#         user_text = input('Введите текст: ')
#         if user_text == '':
#             break
#         else:
#             file.write(f'{user_text}\n')


# 2. Создать текстовый файл (не программно), сохранить в нем несколько
# строк, выполнить подсчет количества строк, количества слов в каждой
# строке.


# f = open('the_text.txt')
# lines = f.readlines()
# print(f'Количество строк в фаайле - {len(lines)}:')
# number_line = 1
# for line in lines:
#     print(f'Строка №{number_line} содержит {len(line.split())} слов')
#     number_line +=1


# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
# сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


# answer = {}
# low_user_zp = []
# all_zp = []
# i = 0
#
# # Открываем файл 'cash.txt'
# zp = open('cash.txt')
# file_zp = zp.read().split()
#
# # Создаю славарь где ключ имя, а значение сумма
# while i < len(file_zp):
#     answer[file_zp[i]] = float(file_zp[i + 1])
#     i += 2
#
# # Определяем кто из сотрудников получает меньше 20к и добовляем их в
# # список. Также собираем все ЗП в отдельный список.
# for key, value in answer.items():
#     if value < 20000:
#         low_user_zp.append(key)
#     all_zp.append(value)
#
# # Выполнить подсчет средней величины дохода сотрудников.
# medium_zp = round(sum(all_zp) / len(all_zp), 2)
#
# print(f'Сотрудники имеющие оклад меньше 20000: \n{low_user_zp[0]}\n{low_user_zp[1]}')
# print(f'Средняя ЗП всех сотрудников: {medium_zp}')


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.


# dz_5 = open('dz_5_2.txt', 'w')
#
# with open('dz_5.txt') as file_dz_5:
#     for line in file_dz_5:
#         content = line.split()
#
#         for i in content:
#             if i == 'One':
#                 content.insert(content.index(i), 'Один')
#                 content.remove(i)
#             elif i == 'Two':
#                 content.insert(content.index(i), 'Два')
#                 content.remove(i)
#             elif i == 'Three':
#                 content.insert(content.index(i), 'Три')
#                 content.remove(i)
#             elif i == 'Four':
#                 content.insert(content.index(i), 'Четыре')
#                 content.remove(i)
#         print(' '.join(content), file=dz_5)
# dz_5.close()


# 5. Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделенных пробелами. Программа должна подсчитывать сумму
# чисел в файле и выводить ее на экран.

# import random
# with open('dz_5_5.txt', 'w') as dz_5_5:
#     numbers = []
#     for i in range(1, 11):
#         numbers.append(str(random.randint(1, 101)))
#     dz_5_5.write(" ".join(numbers))
#
# with open('dz_5_5.txt') as dz_5_5:
#     the_answer = dz_5_5.read().split()
#     summa = 0
#     for i in the_answer:
#         summa += int(i)
#     print(f'Сумма чисел в файле = {summa}')
