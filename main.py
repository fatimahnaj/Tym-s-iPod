import pygame

pygame.init()

# set up the display
screen_size = (390,600) # give screen size
screen = pygame.display.set_mode(screen_size) # opens up a window 
pygame.display.set_caption("Tym's iPod") # window name

#initialise variable
current_playlist = 1

#colors
black = (57, 55, 57)
grey = (203, 202, 197)
white = (225, 226, 228)

#popup any image
def popup_image(image_link,x,y):
    image = pygame.image.load(image_link)
    screen.blit(image, (x-22, y+112))

#insert text
def insert_text(text,size,color,x,y):
    font = pygame.font.Font("retro_gaming.ttf",size)
    set_text = font.render(text, True, color)
    rect_text = set_text.get_rect(center=(x,y))
    screen.blit(set_text, rect_text)
    
#display playlist/song
def draw_button(x, y, width, height, bg_color, text, font_color):
    set_button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, bg_color, set_button)
    font = pygame.font.Font("retro_gaming.ttf",16)
    set_text = font.render(text, True, font_color)
    set_text_rect = pygame.Rect(x+19, y+8, width, height)
    screen.blit(set_text, set_text_rect)
    
#box (will act as background for text)
def draw_box(coordinate, width, height, color):
    x = coordinate[0]
    y = coordinate[1]
    set_box = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, set_box)


def homescreen():
    run = True
    screen.fill(white)
    draw_box((41,68),308,216,grey) #screen
    popup_image('controller.png',94,203) #ipod controller
    popup_image('menu_text.png',196,221) #menu button
    popup_image('next_song_icon.png',302,310) #next song button
    popup_image('prev_song_icon.png',98, 310) #prev song button
    popup_image('play_pause_icon.png',203,410) #play/pause button
    insert_text("Tym's iPod",16,black,185,85)
    playlist_1 = draw_button(41,104,308,36, black, "Playlist 1", grey)
    playlist_2 = draw_button(41,140,308,36, grey, "Playlist 2", black)
    playlist_3 = draw_button(41,176,308,36, grey, "Playlist 3", black)
    playlist_4 = draw_button(41,212,308,36, grey, "Playlist 4", black)
    
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if current_playlist == 1:
                        current_playlist = 1
                        print("Current playlist = " + str(current_playlist))
                    else:
                        current_playlist -= 1
                        print("Current playlist = " + str(current_playlist))
            if event.key == pygame.K_DOWN:
                if current_playlist != 5: #max number of playlist available
                    current_playlist += 1 #move to the next playlist (below it)
                    print("Current playlist = " + str(current_playlist))
                else:
                    current_playlist = 1 #if reach the last playlist, go back to top
                    print("Current playlist = " + str(current_playlist))

    
    homescreen()

    pygame.display.flip() #updates the display

pygame.quit() #quit pygame

homescreen()