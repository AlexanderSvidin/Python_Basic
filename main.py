names_list = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]

day1_names_list = []
for index, name in enumerate(names_list):
    if index % 2 == 0:
        day1_names_list.append(name)

print("Первый день:", day1_names_list)


