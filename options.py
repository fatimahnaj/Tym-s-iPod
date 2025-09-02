import pygame

pygame.init()
# set up the display
screen_size = (390,600) # give screen size
screen = pygame.display.set_mode(screen_size) # opens up a window 

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
light_grey = (134, 134, 134)
pure_white = (255, 255, 255)

#insert text
def insert_text(text,size,color,x,y):
    font = pygame.font.Font("retro_gaming.ttf",size)
    set_text = font.render(text, True, color)
    rect_text = set_text.get_rect(center=(x,y))
    screen.blit(set_text, rect_text)
    
class OPTION:
    def __init__(self, x, y, width, height, bg_color, text, font_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.text = text
        self.font_color = font_color
        self.triggered = False
        self.starting_time = 0
        self.max_duration = 3000

    #display playlist/song
    def insert_option(self):
        set_option = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.bg_color, set_option)
        font = pygame.font.Font("retro_gaming.ttf",16)
        set_text = font.render(self.text, True, self.font_color)
        set_text_rect = pygame.Rect(self.x+19, self.y+8, self.width, self.height)
        screen.blit(set_text, set_text_rect)
    
    def hover_option(self):
        self.bg_color = black
        self.font_color = grey

    def not_hover_option(self):
        self.bg_color = grey
        self.font_color = black

    def option_triggered(self): #used when requirements are met
        self.triggered = True 
        self.starting_time = pygame.time.get_ticks()

    def option_clicked(self):
            # global switch
        #if self.triggered: #make sure the option has been triggered
            self.triggered = True 
            self.starting_time = pygame.time.get_ticks()
            print("self.starting_time = " + str(self.starting_time))
            #limit the button to only show changes for a period of a time
            # if self.starting_time < self.max_duration:
                # chg the option color
            self.bg_color = light_grey
            self.font_color = pure_white
            # else:
            #     self.triggered = False #if dh terlebih masa, reset option tu jadi non triggered
            #     switch = True

    def return_option(self):
        global switch
        current_time = pygame.time.get_ticks()
        if current_time >= self.starting_time+100:
            switch = True
    
class IMGBUTTON:
    def __init__(self, x, y, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.center_x = self.x - self.width // 2
        self.center_y = self.y - self.height // 2
        self.click_sound = pygame.mixer.Sound('Button.mp3') #if want
        self.start_time = 0
        self.max_duration = 3000
        self.is_triggered = False
    
    def show_button(self,image_link):
            image = pygame.image.load(image_link)
            screen.blit(image, (self.x,self.y))

    def check_if_clicked(self):
            cursor_pos = pygame.mouse.get_pos()
            rect = pygame.Rect(self.x, self.y, self.width, self.height)
            if cursor_pos[0] in range(rect.left, rect.right) and cursor_pos[1] in range(rect.top, rect.bottom):
                self.click_sound.play()
                self.is_triggered = True
                return True
            else :
                self.is_triggered = False
                return False
            
    def is_selected(self):
        self.click_sound.play()
        self.is_triggered = True
        return True
    
    def button_clicked(self,new_image_link):
        if self.is_triggered:
            new_image = pygame.image.load(new_image_link)
            screen.blit(new_image, (self.x,self.y))

#box (will act as background for text)
def draw_box(coordinate, width, height, color):
    x = coordinate[0]
    y = coordinate[1]
    set_box = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, set_box)

p1_song1 = OPTION(41,104,308,36, black, "A Better Tomorrow", grey)
p1_song2 = OPTION(41,140,308,36, grey, "Amazing Things", black)
p1_song3 = OPTION(41,176,308,36, grey, "Meet You Halfway", black)
p1_song4 = OPTION(41,212,308,36, grey, "Moments of Good Time", black)
p1_songs = [p1_song1, p1_song2, p1_song3, p1_song4]

p2_song1 = OPTION(41,104,308,36, black, "if its not you", grey)
p2_song2 = OPTION(41,140,308,36, grey, "penjaga hati", black)
p2_song3 = OPTION(41,176,308,36, grey, "Take My Half", black)
p2_song4 = OPTION(41,212,308,36, grey, "The Only Exception", black)
p2_song5 = OPTION(41,248,308,36, grey, "Youre here thats the thing", black)
p2_songs = [p2_song1, p2_song2, p2_song3, p2_song4, p2_song5]

p3_song1 = OPTION(41,104,308,36, black, "Its Not The Same Anymore", grey)
p3_song2 = OPTION(41,140,308,36, grey, "Kembali Pulang", black)
p3_song3 = OPTION(41,176,308,36, grey, "No One Noticed", black)
p3_song4 = OPTION(41,212,308,36, grey, "Runtuh", black)
p3_songs = [p3_song1, p3_song2, p3_song3, p3_song4]

p4_song1 = OPTION(41,104,308,36, black, "Departure", grey)
p4_song2 = OPTION(41,140,308,36, grey, "late hrs", black)
p4_song3 = OPTION(41,176,308,36, grey, "No Surprises", black)
p4_song4 = OPTION(41,212,308,36, grey, "Skybeam", black)
p4_song5 = OPTION(41,248,308,36, grey, "Space Things", black)
p4_songs = [p4_song1, p4_song2, p4_song3, p4_song4, p4_song5]

p5_song1 = OPTION(41,104,308,36, black, "SLAY!", grey)
p5_song2 = OPTION(41,140,308,36, grey, "Shadows", black)
p5_song3 = OPTION(41,176,308,36, grey, "Monster", black)
p5_songs = [p5_song1, p5_song2, p5_song3]

playlist_1 = OPTION(41,104,308,36, grey, "Study Jazz", black)
playlist_2 = OPTION(41,140,308,36, black, "White Roses", grey)
playlist_3 = OPTION(41,176,308,36, grey, "Adulting", black)
playlist_4 = OPTION(41,212,308,36, grey, "Synthwave", black)
playlist_5 = OPTION(41,248,308,36, grey, "Noise", black)

playlists = [playlist_1, playlist_2, playlist_3, playlist_4, playlist_5]