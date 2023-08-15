number = int(input("Введите число: "))
odd_nums_list = []

for num in range(1, number + 1):
    if num % 2 != 0:
        odd_nums_list.append(num)

print("Список из нечётных чисел от одного до N:", odd_nums_list)