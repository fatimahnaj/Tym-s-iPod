import pygame
from songs_list import *
from buttons import *

pygame.init()
pygame.mixer.init()

# set up the display
screen_size = (390,600) # give screen size
screen = pygame.display.set_mode(screen_size) # opens up a window 
pygame.display.set_caption("Tym's iPod") # window name
pygame_icon = pygame.image.load('play_status.png')
pygame.display.set_icon(pygame_icon)


#initialise variable
current_playlist = 2
current_p1_song = 1
current_p2_song = 1
current_p3_song = 1
current_p4_song = 1
current_p5_song = 1
playing = False

#colors
black = (57, 55, 57)
grey = (203, 202, 197)
white = (225, 226, 228)

#popup any image
def popup_image(image_link,x,y):
    image = pygame.image.load(image_link)
    screen.blit(image, (x,y))

class IMAGE:
    def __init__(self, image_link,x,y):
        self.image_link = image_link
        self.x = x
        self.y = y

    def popup_image(self):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (self.x,self.y))

    def update_image(self, new_image_link):
        self.image_link = new_image_link
        image = pygame.image.load(self.image_link)
        screen.blit(image, (self.x,self.y))

    def hover_image(self, hover_image_link):
        image = pygame.image.load(self.image_link)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if image.collidepoint(mouse_x, mouse_y):
            self.image_link = hover_image_link
            image = pygame.image.load(self.image_link)
        screen.blit(image, (self.x,self.y))

menu_button = IMAGE('menu_text.png',196-22,221+122)

#insert text
def insert_text(text,size,color,x,y):
    font = pygame.font.Font("retro_gaming.ttf",size)
    set_text = font.render(text, True, color)
    rect_text = set_text.get_rect(center=(x,y))
    screen.blit(set_text, rect_text)
    
#box (will act as background for text)
def draw_box(coordinate, width, height, color):
    x = coordinate[0]
    y = coordinate[1]
    set_box = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, set_box)

# p1_songs = [p1_song1, p1_song2, p1_song3, p1_song4]
# p2_songs = [p2_song1, p2_song2, p2_song3, p2_song4, p2_song5]
# p3_songs = [p3_song1, p3_song2, p3_song3, p3_song4]
# p4_songs = [p4_song1, p4_song2, p4_song3, p4_song4, p4_song5]
# p5_songs = [p5_song1, p5_song2, p5_song3]
# playlists = [playlist_1, playlist_2, playlist_3, playlist_4, playlist_5]

#queue
currently_playing = [A_Better_Tomorrow]

def play_new_song(song_title):
    global playing
    if not playing:
        print("Currently playing: " )
        currently_playing.append(song_title)
        currently_playing.pop(0)
        currently_playing[0].play_music()

def iPod_interface():
    screen.fill(white)
    draw_box((41,68),308,216,grey) #screen
    popup_image('controller.png',94-22,203+122) #ipod controller
    # popup_image('menu_text.png',196-22,221+122) #menu button
    menu_button.popup_image()
    popup_image('next_song_icon.png',302-22,310+122) #next song button
    popup_image('prev_song_icon.png',98-22, 310+122) #prev song button
    popup_image('play_pause_icon.png',203-22,410+122) #play/pause button

def homescreen():
    iPod_interface()
    popup_image('music_icon.png',311,73)
    popup_image('pause_status.png',58,79)
    insert_text("Tym's iPod",16,black,185,85)
    #display all the available playlist
    for playlist in playlists:
        playlist.insert_button()
    pygame.display.flip()

def create_playlist_screen(playlist_name, playlist_songlist):
    iPod_interface()
    popup_image('music_icon.png',311,73)
    popup_image('pause_status.png',58,79)
    insert_text(playlist_name,16,black,185,85)
    for song in playlist_songlist:
        song.insert_button()
    pygame.display.flip()

def playlist1_screen():
    iPod_interface()
    create_playlist_screen("Study Jazz", p1_songs)
    pygame.display.flip()

def playlist2_screen():
    iPod_interface()
    create_playlist_screen("White Roses", p2_songs)
    pygame.display.flip()

def playlist3_screen():
    iPod_interface()
    create_playlist_screen("Adulting", p3_songs)
    pygame.display.flip()

def playlist4_screen():
    iPod_interface()
    create_playlist_screen("Synthwave", p4_songs)
    pygame.display.flip()

def playlist5_screen():
    iPod_interface()
    create_playlist_screen("Noise", p5_songs)
    pygame.display.flip()

page = "homescreen" #initialise first screen
homescreen() #call homescreen

####################################################################
#main loop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #check if any button is clicked
        if event.type == pygame.KEYDOWN:
            #up arrow is clicked
            if event.key == pygame.K_UP:
                # playing = False
                if page == "homescreen":
                    if current_playlist <= len(playlists):
                        if current_playlist == 1:
                            current_playlist = 1
                            print("Current playlist = " + str(current_playlist))
                        else:
                            current_playlist -= 1
                            print("Current playlist = " + str(current_playlist))
                            playlists[current_playlist-1].hover_button()
                            playlists[current_playlist].not_hover_button()
                        homescreen() #redraw the screen
                elif page == "playlist_1":
                    if current_p1_song <= len(p1_songs):
                        if current_p1_song == 1:
                            current_p1_song = 1
                            print("Current song (in playlist 1): song " + str(current_p1_song) )
                        else:
                            current_p1_song -= 1
                            print("Current song (in playlist 1): song " + str(current_p1_song) )
                            p1_songs[current_p1_song-1].hover_button()
                            p1_songs[current_p1_song].not_hover_button()
                        playlist1_screen()
                elif page == "playlist_2":
                    if current_p2_song <= len(p2_songs):
                        if current_p2_song == 1:
                            current_p2_song = 1
                            print("Current song (in playlist 2): song " + str(current_p2_song) )
                        else:
                            current_p2_song -= 1
                            print("Current song (in playlist 2): song " + str(current_p2_song) )
                            p2_songs[current_p2_song-1].hover_button()
                            p2_songs[current_p2_song].not_hover_button()
                        playlist2_screen()
                elif page == "playlist_3":
                    if current_p3_song <= len(p3_songs):
                        if current_p3_song == 1:
                            current_p3_song = 1
                            print("Current song (in playlist 3): song " + str(current_p3_song) )
                        else:
                            current_p3_song -= 1
                            print("Current song (in playlist 3): song " + str(current_p3_song) )
                            p3_songs[current_p3_song-1].hover_button()
                            p3_songs[current_p3_song].not_hover_button()
                        playlist3_screen()

                elif page == "playlist_4":
                    if current_p4_song <= len(p4_songs):
                        if current_p4_song == 1:
                            current_p4_song = 1
                            print("Current song (in playlist 4): song " + str(current_p4_song) )
                        else:
                            current_p4_song -= 1
                            print("Current song (in playlist 4): song " + str(current_p4_song) )
                            p4_songs[current_p4_song-1].hover_button()
                            p4_songs[current_p4_song].not_hover_button()
                        playlist4_screen()

                elif page == "playlist_5":
                    if current_p5_song <= len(p5_songs):
                        if current_p5_song == 1:
                            current_p5_song = 1
                            print("Current song (in playlist 5): song " + str(current_p5_song) )
                        else:
                            current_p5_song -= 1
                            print("Current song (in playlist 5): song " + str(current_p5_song) )
                            p5_songs[current_p5_song-1].hover_button()
                            p5_songs[current_p5_song].not_hover_button()
                        playlist5_screen()

            #down arrow is clicked
            elif event.key == pygame.K_DOWN:
                # playing = False
                if page == "homescreen":
                    if current_playlist <= len(playlists):
                        if current_playlist != len(playlists): #max number of playlist available
                            current_playlist += 1 #move to the next playlist (below it)
                            print("Current playlist = " + str(current_playlist))
                            playlists[current_playlist-1].hover_button()
                            playlists[current_playlist-2].not_hover_button()
                        else:
                            current_playlist = current_playlist #if reach the last playlist, go back to top
                            print("Current playlist = " + str(current_playlist))
                        homescreen() #redraw the screen
                elif page == "playlist_1":
                    if current_p1_song <= len(p1_songs):
                        if current_p1_song != len(p1_songs):
                            current_p1_song += 1
                            print("Current song (in playlist 1): song " + str(current_p1_song) )
                            p1_songs[current_p1_song-1].hover_button()
                            p1_songs[current_p1_song-2].not_hover_button()
                        else:
                            current_p1_song = current_p1_song
                            print("Current song (in playlist 1): song " + str(current_p1_song) )
                        playlist1_screen()
                elif page == "playlist_2":
                    if current_p2_song <= len(p2_songs):
                        if current_p2_song != len(p2_songs):
                            current_p2_song += 1
                            print("Current song (in playlist 2): song " + str(current_p2_song) )
                            p2_songs[current_p2_song-1].hover_button()
                            p2_songs[current_p2_song-2].not_hover_button()
                        else:
                            current_p2_song = current_p2_song
                            print("Current song (in playlist 2): song " + str(current_p2_song) )
                        playlist2_screen()

                elif page == "playlist_3":
                    if current_p3_song <= len(p3_songs):
                        if current_p3_song != len(p3_songs):
                            current_p3_song += 1
                            print("Current song (in playlist 3): song " + str(current_p3_song) )
                            p3_songs[current_p3_song-1].hover_button()
                            p3_songs[current_p3_song-2].not_hover_button()
                        else:
                            current_p3_song = current_p3_song
                            print("Current song (in playlist 3): song " + str(current_p3_song) )
                        playlist3_screen()

                elif page == "playlist_4":
                    if current_p4_song <= len(p4_songs):
                        if current_p4_song != len(p4_songs):
                            current_p4_song += 1
                            print("Current song (in playlist 4): song " + str(current_p4_song) )
                            p4_songs[current_p4_song-1].hover_button()
                            p4_songs[current_p4_song-2].not_hover_button()
                        else:
                            current_p4_song = current_p4_song
                            print("Current song (in playlist 4): song " + str(current_p4_song) )
                        playlist4_screen()

                elif page == "playlist_5":
                    if current_p5_song <= len(p5_songs):
                        if current_p5_song != len(p5_songs):
                            current_p5_song += 1
                            print("Current song (in playlist 5): song " + str(current_p5_song) )
                            p5_songs[current_p5_song-1].hover_button()
                            p5_songs[current_p5_song-2].not_hover_button()
                        else:
                            current_p5_song = current_p5_song
                            print("Current song (in playlist 5): song " + str(current_p5_song) )
                        playlist5_screen()


            elif event.key == pygame.K_RETURN:
                #changing screen to the selected playlist
                if page == "homescreen":
                    if current_playlist == 1:
                        playlist1_screen()
                        page = "playlist_1"
                        print("Changing to screen " + page + " ...")
                    elif current_playlist == 2:
                        playlist2_screen()
                        page = "playlist_2"
                        print("Changing to screen " + page + " ...")
                    elif current_playlist == 3:
                        playlist3_screen()
                        page = "playlist_3"
                        print("Changing to screen " + page + " ...")
                    elif current_playlist == 4:
                        playlist4_screen()
                        page = "playlist_4"
                        print("Changing to screen " + page + " ...")
                    elif current_playlist == 5:
                        playlist5_screen()
                        page = "playlist_5"
                        print("Changing to screen " + page + " ...")
                #play selected song from playlist_1
                elif page == "playlist_1":
                    if current_p1_song == 1:
                        play_new_song(A_Better_Tomorrow)
                    elif current_p1_song == 2:
                        play_new_song(Amazing_Things)
                    elif current_p1_song == 3:
                        play_new_song(Meet_You_Halfway)
                    elif current_p1_song == 4:
                        play_new_song(Moments_of_Good_Time)
                #play selected song from playlist_2
                elif page == "playlist_2":
                    if current_p2_song == 1:
                        play_new_song(If_its_not_you)
                    elif current_p2_song == 2:
                        play_new_song(penjaga_hati)
                    elif current_p2_song == 3:
                        play_new_song(Take_My_Half)
                    elif current_p2_song == 4:
                        play_new_song(The_Only_Exception)
                    elif current_p2_song == 5:
                        play_new_song(Youre_here_thats_the_thing)
                elif page == "playlist_3":
                    if current_p3_song == 1:
                        play_new_song(Its_Not_The_Same_Anymore)
                    elif current_p3_song == 2:
                        play_new_song(Kembali_Pulang)
                    elif current_p3_song == 3:
                        play_new_song(No_One_Noticed)
                    elif current_p3_song == 4:
                        play_new_song(Runtuh)

                elif page == "playlist_4":
                    if current_p4_song == 1:
                        play_new_song(Departure)
                    elif current_p4_song == 2:
                        play_new_song(late_hrs)
                    elif current_p4_song == 3:
                        play_new_song(No_Surprises)
                    elif current_p4_song == 4:
                        play_new_song(Skybeam)
                    elif current_p4_song == 5:
                        play_new_song(Space_Things)

                elif page == "playlist_5":
                    if current_p5_song == 1:
                        play_new_song(SLAY)
                    elif current_p5_song == 2:
                        play_new_song(They_Think_Im_Hiding)
                    elif current_p5_song == 3:
                        play_new_song(You_Monster)

            #pause/unpause the song
            elif event.key == pygame.K_SPACE:
                #if a song is playing, we will pause. else,(song is pause. therefore,) we will unpause.
                if not playing:
                    currently_playing[0].pause_music()
                    playing = not playing
                else:
                    currently_playing[0].unpause_music()
                    playing = not playing
                #create an array to store the currently playing song. 
                # when i play the song, append the song into the array (works like a queue)
                # when i switch (if current song != song inside array) -> chg the currently playing song
                # when i pause, pause the current song in the array

            elif event.key == pygame.K_ESCAPE:
                page = "homescreen"
                homescreen()

    pygame.display.flip() #updates the display

pygame.quit() #quit pygame