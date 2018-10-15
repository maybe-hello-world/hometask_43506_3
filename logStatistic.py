from collections import Counter
file = open('DhcpSrvLog-Thu.log')  # открываем файл

a = []  # создаем списки
b = []
for line in file: # построчно считываем файл
    if line.startswith('30'):  # берем только те строки, которые начинаются с 30(т.к.я выбрала id=30)
     b = line.split(',')  # разделяем строку на список элементов, разделитель - запятая
     new_element = str(b[4:5])  # записываем в элемент нового массива только ip(ip - 4 элемент списка)
     a.append(new_element)

print ('Количество событий: ', len(a)-1 , 'Статистика: ', Counter(a))