films = [
    "Крепкий орешек",
    "Назад в будущее",
    "Таксист",
    "Леон",
    "Богемская рапсодия",
    "Город грехов",
    "Мементо",
    "Отступники",
    "Деревня",
]

favorite_films = []

count_user_films = int(input("Сколько фильмов хотите добавить? "))
status = False
for _ in range(count_user_films):
    user_name_film = input("Введите название фильма: ")

    for name_film in films:
        if user_name_film.casefold() == name_film.casefold():
            favorite_films.append(user_name_film)
            status = True
            break
        else:
            status = False

    if status == False:
        print("Ошибка: фильма", user_name_film, "у нас нет :(")


print("\nВаш список любимых фильмов:", end=" ")
for index, favorite_user_film in enumerate(favorite_films):
    if index == len(favorite_films) - 1:
        print(favorite_user_film)
    else:
        print(favorite_user_film, end=", ")




