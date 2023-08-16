count_containers = int(input("Количество контейнеров: "))
containers_list = []

for _ in range(count_containers):
    mass_container = int(input("Введите вес контейнера: "))

    while mass_container >= 200: # Контроль ввода
        print("Ошибка! Масса контейнера не должна превышать 200.")
        mass_container = int(input("Попробуйте ещё раз: "))

    containers_list.append(mass_container)

mass_new_container = int(input("Введите вес нового контейнера: "))
index_new_container = 0

while containers_list[index_new_container] >= mass_new_container:
    index_new_container += 1

print("Номер, который получит новый контейнер:", index_new_container + 1)


