# -*- coding: utf-8 -*-
print("hello world")

def make_album(singer_name,song_album,total_number = ''):
    if total_number:
        info_album = singer_name + ', ' + song_album + ',' + total_number
    else:
        info_album = singer_name + ', ' + song_album
    return make_album

while True:
    print('please enter the album information:')
    s_name = input("singer's name:")
    s_album = input("album's name:")
    t_number = input("total numbers:")

    final_album = make_album(s_name,s_album,t_number)
    print(final_album)