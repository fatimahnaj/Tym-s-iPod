import pygame

pygame.init()
pygame.mixer.init()

# set up the display
screen_size = (390,600) # give screen size
screen = pygame.display.set_mode(screen_size) # opens up a window 
pygame.display.set_caption("Tym's iPod") # window name

#initialise variable
current_playlist = 2
current_p1_song = 1
playing = False

#colors
black = (57, 55, 57)
grey = (203, 202, 197)
white = (225, 226, 228)

#popup any image
def popup_image(image_link,x,y):
    image = pygame.image.load(image_link)
    screen.blit(image, (x,y))

#insert text
def insert_text(text,size,color,x,y):
    font = pygame.font.Font("retro_gaming.ttf",size)
    set_text = font.render(text, True, color)
    rect_text = set_text.get_rect(center=(x,y))
    screen.blit(set_text, rect_text)
    
class BUTTON:
    def __init__(self, x, y, width, height, bg_color, text, font_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.text = text
        self.font_color = font_color

    #display playlist/song
    def insert_button(self):
        set_button = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.bg_color, set_button)
        font = pygame.font.Font("retro_gaming.ttf",16)
        set_text = font.render(self.text, True, self.font_color)
        set_text_rect = pygame.Rect(self.x+19, self.y+8, self.width, self.height)
        screen.blit(set_text, set_text_rect)
    
    def hover_button(self):
        self.bg_color = black
        self.font_color = grey

    def not_hover_button(self):
        self.bg_color = grey
        self.font_color = black
    
#box (will act as background for text)
def draw_box(coordinate, width, height, color):
    x = coordinate[0]
    y = coordinate[1]
    set_box = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, set_box)

p1_song1 = BUTTON(41,104,308,36, black, "A Better Tomorrow", grey)
p1_song2 = BUTTON(41,140,308,36, grey, "Amazing Things", black)
p1_song3 = BUTTON(41,176,308,36, grey, "Meet You Halfway", black)
p1_song4 = BUTTON(41,212,308,36, grey, "Moments of Good Time", black)

p1_songs = [p1_song1, p1_song2, p1_song3, p1_song4]

playlist_1 = BUTTON(41,104,308,36, grey, "Study Jazz", black)
playlist_2 = BUTTON(41,140,308,36, black, "Playlist 2", grey)
playlist_3 = BUTTON(41,176,308,36, grey, "Playlist 3", black)
playlist_4 = BUTTON(41,212,308,36, grey, "Playlist 4", black)

playlists = [playlist_1, playlist_2, playlist_3, playlist_4]

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
StudyJazz_playlist = [A_Better_Tomorrow, Amazing_Things, Meet_You_Halfway, Moments_of_Good_Time]

def iPod_interface():
    screen.fill(white)
    draw_box((41,68),308,216,grey) #screen
    popup_image('controller.png',94-22,203+122) #ipod controller
    popup_image('menu_text.png',196-22,221+122) #menu button
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

def playlist1_screen():
    screen.fill(black)
    iPod_interface()
    popup_image('music_icon.png',311,73)
    popup_image('pause_status.png',58,79)
    insert_text("Study Jazz",16,black,185,85)
    for song in p1_songs:
        song.insert_button()
    pygame.display.flip()

page = "homescreen"
homescreen()

####################################################################
#main loop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            #up arrow is clicked
            if event.key == pygame.K_UP:
                playing = False
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

            #down arrow is clicked
            elif event.key == pygame.K_DOWN:
                playing = False
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


            elif event.key == pygame.K_RETURN:
                if page == "homescreen":
                    if current_playlist == 1:
                        playlist1_screen()
                        page = "playlist_1"
                        print("Changing to screen " + page + " ...")
                elif page == "playlist_1":
                    if current_p1_song == 1:
                        if not playing:
                            print("Selecting 1st song..")
                            StudyJazz_playlist[0].play_music()
                        else:
                            StudyJazz_playlist[0].pause_music()
                    if current_p1_song == 2:
                        if not playing:
                            print("Selecting 2nd song..")
                            StudyJazz_playlist[1].play_music()
                        else:
                            StudyJazz_playlist[1].pause_music()
                    if current_p1_song == 3:
                        if not playing:
                            print("Selecting 3rd song..")
                            StudyJazz_playlist[2].play_music()
                        else:
                            StudyJazz_playlist[2].pause_music()
                    if current_p1_song == 4:
                        if not playing:
                            print("Selecting 4th song..")
                            StudyJazz_playlist[3].play_music()
                        else:
                            StudyJazz_playlist[3].pause_music()
                    playlist1_screen()

    pygame.display.flip() #updates the display

pygame.quit() #quit pygame