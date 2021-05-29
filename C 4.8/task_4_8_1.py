import random  # модуль, с помощью которого перемешиваем массив

# пусть имеем массив всего лишь из 9 элементов
array =  [1, 2, 4, 3, 5, 6, 7, 8, 9]

is_sort = False  # станет True, если отсортирован
count = 0  # счетчик количества перестановок

while not is_sort:  # пока не отсортирован
    count += 1  # прибавляем 1 к счетчику

    random.shuffle(array)  # перемешиваем массив

    # проверяем отсортирован ли
    is_sort = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            is_sort = False
            break

print(array)

print(count)

n = [i for i in range(1, 101)]
count = 1
for i in n:
    count *= i

print(len(str(count)))