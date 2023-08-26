# Задание 4. Вечеринка

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    status_party = input('Гость пришёл или ушёл? ')

    if status_party.casefold() == 'Пора спать'.casefold():
        print('Вечеринка закончилась, все легли спать.')
        break

    else:
        name_new_guest = input('Имя гостя: ')

        if status_party.casefold() == 'пришёл'.casefold() and len(guests) < 6:
            print('Привет,', name_new_guest + '!')
            guests.append(name_new_guest)

        elif status_party.casefold() == 'ушёл'.casefold():
            print('Пока,', name_new_guest + '!')
            guests.remove(name_new_guest)

        else:
            print('Прости,', name_new_guest + ', но мест нет.')

