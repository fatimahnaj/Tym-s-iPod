import pygame

pygame.init()
pygame.mixer.init()

class MUSIC:
    def __init__(self, song_title):
        self.song_title = song_title

    def play_music(self):
        global playing
        pygame.mixer.music.load(self.song_title)
        pygame.mixer.music.play()
        playing = True

    def pause_music(self):
        global playing
        pygame.mixer.music.pause()
        playing = False

    def unpause_music(self):
        global playing
        pygame.mixer.music.unpause()
        playing = True

    def loop_music(self):
        global playing
        pygame.mixer.music.play(-1) #-1 means loop forever
        playing = True

A_Better_Tomorrow = MUSIC('playlist_1/A Better Tomorrow.mp3')
Amazing_Things = MUSIC('playlist_1/Amazing Things.mp3')
Meet_You_Halfway = MUSIC('playlist_1/Meet You Halfway.mp3')
Moments_of_Good_Time = MUSIC('playlist_1/Moments of Good Time.mp3')

If_its_not_you = MUSIC('playlist_2/if its not you.mp3')
penjaga_hati = MUSIC('playlist_2/penjaga hati.mp3')
Take_My_Half = MUSIC('playlist_2/Take My Half.mp3')
The_Only_Exception = MUSIC('playlist_2/The Only Exception.mp3')
Youre_here_thats_the_thing = MUSIC('playlist_2/Youre here thats the thing.mp3')

Its_Not_The_Same_Anymore = MUSIC('playlist_3/Its Not The Same Anymore.mp3')
Kembali_Pulang = MUSIC('playlist_3/Kembali Pulang.mp3')
No_One_Noticed = MUSIC('playlist_3/No One Noticed.mp3')
Runtuh = MUSIC('playlist_3/Runtuh.mp3')

Departure = MUSIC('playlist_4/Departure.mp3')
late_hrs = MUSIC('playlist_4/late hrs.mp3')
No_Surprises = MUSIC('playlist_4/No Surprises.mp3')
Skybeam = MUSIC('playlist_4/Skybeam.mp3')
Space_Things = MUSIC('playlist_4/Space Things.mp3')

SLAY = MUSIC('playlist_5/SLAY!.mp3')
They_Think_Im_Hiding = MUSIC('playlist_5/They Think Im Hiding in the Shadows... but I Am the Shadows.mp3')
You_Monster = MUSIC('playlist_5/You Will Always Be a Monster (Slowed).mp3')