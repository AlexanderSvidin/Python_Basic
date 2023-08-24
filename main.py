nums_list = []
count_elem = int(input('Введите кол-во элементов списка: '))

for index_elem in range(count_elem):
    print("Введите", str(index_elem + 1) + "-й элемент списка:", end=" ")
    elem = int(input())
    nums_list.append(elem)

def even_reverse_nums(array):
    for index_elem in range(len(array) - 1, -1, -1):
        if array[index_elem] % 2 == 0:
            print(array[index_elem], end=" ")

print("\nИзначальный список:", nums_list)
print("Чётные числа в обратном порядке:", end=" ")
even_reverse_nums(nums_list)