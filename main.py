# Алгоритм быстрой сортировки Хоара

import random


def QuickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = random.choice(array)
        less = [elem for elem in array if elem < pivot]
        equal = [elem for elem in array if elem == pivot]
        greater = [elem for elem in array if elem > pivot]

        return QuickSort(less) + equal + QuickSort(greater)


nums_list = [1, 4, -3, 0, 10]
print("Изначальный список:", nums_list)
print("Отсортированный список:", QuickSort(nums_list))