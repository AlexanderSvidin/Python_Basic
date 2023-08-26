# Задание 7. Считалка

num_people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке?: '))
print('Значит, выбывает каждый', str(number) + '-й человек')

circle_list = list(range(1, num_people + 1))
count = 0

while len(circle_list) > 1:
    print('\nТекущий круг людей: ', circle_list)
    print('Начало счёта с номера:', circle_list[count])

    count = (count + number - 1) % len(circle_list)

    if circle_list[count] == circle_list[-1]:
        print('Выбывает человек под номером:', circle_list.pop(count))
        count = 0

    else:
        print('Выбывает человек под номером:', circle_list.pop(count))

print('\nОстался человек под номером:', circle_list[0])