violator_songs = [

['World in My Eyes', 4.86],

['Sweetest Perfection', 4.43],

['Personal Jesus', 4.56],

['Halo', 4.9],

['Waiting for the Night', 6.07],

['Enjoy the Silence', 4.20],

['Policy of Truth', 4.76],

['Blue Dress', 4.29],

['Clean', 5.83]

]

def time_song(song_title):
    time = 0

    for song in violator_songs:
        if song[0].casefold() == song_title.casefold():
            time += song[1]
            return time

    print('Песни', song_title, 'нет в списке песен.')
    return 0

count_songs = int(input('Сколько песен выбрать? '))
time_songs = 0

for index_song in range(1, count_songs + 1):
    print('Название', str(index_song) + '-й песни:', end=" ")
    song_title = input()
    time_songs += time_song(song_title)

print('Общее время звучания песен —', round(time_songs, 2), 'минуты')


