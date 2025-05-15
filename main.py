import pygame
import sys
from characters import characters_screen
##pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dooble Jump Menu")
clock = pygame.time.Clock()
fps=90
# back button colors
BROWN = (60, 40, 20)
font_button = pygame.font.SysFont("comicsansms", 32)
font_game = pygame.font.SysFont("comicsansms", 40)
buttonsound= pygame.mixer.Sound('sound/buttonsound.mp3')
bgmusic= pygame.mixer.Sound('sound/Bensound - Cute.mp3')
bgmusic.set_volume(0.5)

daymode=pygame.transform.scale(pygame.image.load("mainmenumaps/daymode.png"),(50,50))
nightmode=pygame.transform.scale(pygame.image.load("mainmenumaps/nightmode.png"),(50,50))
# dark mode photos
menu_day = pygame.image.load('mainmenumaps/menuday.jpg')
menu_day = pygame.transform.scale(menu_day, (WIDTH, HEIGHT))
menu_night = pygame.image.load("mainmenumaps/menunight.jpg")
menu_night = pygame.transform.scale(menu_night, (WIDTH, HEIGHT))


dark_button = pygame.Rect(10, 10, 40, 40)

def draw_button_text(rect, text):
    label = font_button.render(text, True, BROWN)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)


def map_select_screen(dark,charplayer):
    global WIDTH,HEIGHT
    maps_img = pygame.image.load('mainmenumaps/mapsday.jpg')
    maps_img = pygame.transform.scale(maps_img, (WIDTH, HEIGHT))
    maps_night=pygame.transform.scale(pygame.image.load('mainmenumaps/mapsnight.jpg'), (WIDTH, HEIGHT))
    
    d=0
    if dark:
       d=70

    map1_rect = pygame.Rect(WIDTH//2 - 60, 200+d, 120, 120)
    map2_rect = pygame.Rect(WIDTH//2 - 60, 340+d, 120, 120)
    map3_rect = pygame.Rect(WIDTH//2 - 60, 480+d, 120, 120)

    back_button = pygame.Rect(WIDTH//2 - 80+d//2, HEIGHT - 70+d/1.8, 160-d, 50)

    while True:
        if dark:
           screen.blit(maps_night, (0, 0))
        else:
           screen.blit(maps_img, (0, 0))   

        pygame.draw.rect(screen, (200, 200, 200), back_button, border_radius=10)
        pygame.draw.rect(screen, BROWN, back_button, 2, border_radius=10)
        back_text = font_button.render("Back", True, BROWN)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if event.button == 1:  
               

               if map1_rect.collidepoint(event.pos):
                  buttonsound.play()
                  bgmusic.stop()
                  import spacemodee
                  spacemodee.salem(dark,charplayer)




               elif map2_rect.collidepoint(event.pos):
                  buttonsound.play()
                  bgmusic.stop()
                  import icemode
                  icemode.salem(dark,charplayer)
               elif map3_rect.collidepoint(event.pos):
                  bgmusic.stop()
                  buttonsound.play()
                  import forestmod
                  forestmod.main(dark,charplayer)
               elif back_button.collidepoint(event.pos):
                  buttonsound.play()
                  main_menu()
                  #return

            

        pygame.display.update()
        clock.tick(fps)


darkmod=False
def cheakdarkmode(a):
    if not a:
        screen.fill((227, 189, 28), pygame.Rect(0, 0, 50, 50))
        screen.blit(daymode,(0,0))
    else:
        screen.fill((185, 129, 56), pygame.Rect(0, 0, 50, 50))
        screen.blit(nightmode,(0,0))   
# main menu
def main_menu():
    global darkmod
    d=0
    charplayer='none'
    channel = pygame.mixer.find_channel()
    channel.play(bgmusic)
    while True:
       
        if not darkmod:
            d=50
            screen.blit(menu_day, (0, 0))
        else :
           d=0
           screen.blit(menu_night, (0, 0))
        start_button = pygame.Rect(135, 205+d, 220, 60)
        score_button = pygame.Rect(135, 300+d, 220, 60)
        
        cheakdarkmode(darkmod)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if start_button.collidepoint(event.pos):
                    buttonsound.play()
                    map_select_screen(darkmod,charplayer)
                elif score_button.collidepoint(event.pos):
                    buttonsound.play()
                    charplayer= characters_screen(screen, clock, WIDTH, HEIGHT, font_button,BROWN)
                    print(charplayer)


                elif dark_button.collidepoint(event.pos):
                    buttonsound.play()
                    if not darkmod:
                      darkmod=True  
                    else :
                      darkmod=False 
                    

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main_menu()
