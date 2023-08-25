# Задание 2. Уникальное объединение списков

def merge_sorted_lists(array_1, array_2):
    merge_array = array_1 + array_2
    merge_array.sort()

    for index in range(len(merge_array) - 2):
        if merge_array[index] == merge_array[index + 1]:
            merge_array.pop(index)

    return merge_array


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)