num_vd = int(input("Количество видеокарт: "))
vd_list = []

for index in range(1, num_vd + 1):
    print("Видеокарта",  str(index) + ":", end= " ")
    vd = int(input())
    vd_list.append(vd)

new_vd_list = []
for vd in vd_list:
    vd = str(vd)
    if int(vd[2]) <= 7:
        new_vd_list.append(int(vd))

print("\nСтарый список видеокарт:", vd_list)
print("Новый список видеокарт:", new_vd_list)