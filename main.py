# Задание 6. Ролики

num_rollerblade = int(input('Количество роликов: '))
size_rollerblade_list = []

for i_rollerblade in range(1, num_rollerblade + 1):
    print('Размер пары', str(i_rollerblade) + ':', end=' ')
    size_rollerblade = int(input())
    size_rollerblade_list.append(size_rollerblade)


num_people = int(input('\nКоличество людей: '))
foot_size_list = []

for i_person in range(1, num_people + 1):
    print('Размер ноги человека', str(i_person) + ':', end=' ')
    foot_size = int(input())
    foot_size_list.append(foot_size)


count_succesful = 0 # количество людей, которые могут взять ролики
for foot_size in foot_size_list:
    if size_rollerblade_list.count(foot_size) > 0:
        count_succesful += 1
        size_rollerblade_list.remove(foot_size)

print('Наибольшее количество людей, которые могут взять ролики:', count_succesful)


