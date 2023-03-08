import os


def add_songs(*songs):
    song_title = {}

    for song in songs:
        if song[0] not in song_title.keys():
            song_title[song[0]] = []

        song_title[song[0]] = song[1]
    print_result = []
    for song1, text in song_title.items():
        print_result.append("- " + song1)
        if text:
            print_result.extend(text)
    return os.linesep.join(print_result)


