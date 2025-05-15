import pygame
from random import randint
import main 
import sys
blocks=[]
game_over=False
score=0
sss=0
superjump=2
def salem(dark,char):
    global game_over
    fps=90
    white = (255,255,255)
    bg_photo='ice/icemap.jpg'
    gmover_photo='ice/icegameover.jpg'
    playercharacter='ice/iceplayer.png'
    platform_img = pygame.image.load("ice/icestep.png")

    if char!='none':
        playercharacter=char

    gameoversound= pygame.mixer.Sound('sound/gameoverarcade.mp3')
    jumpsound= pygame.mixer.Sound('sound/bubblejump.mp3')
    buttonsounds= pygame.mixer.Sound('sound/buttonsound.mp3')

    width=500;height=700
    replay=pygame.Rect(width//2 - 60, 500, 270, 160)

    gameoverphoto = pygame.transform.scale(pygame.image.load(gmover_photo),(width,height))
    bg=pygame.transform.scale(pygame.image.load(bg_photo),(width,height))
    player=pygame.transform.scale(pygame.image.load(playercharacter),(90,90))
    player1=player
   
    
    font = pygame.font.Font('FreeSansBold.ttf',15)
    timer= pygame.time.Clock()

    #player positions
    player_x = 30
    player_y = 500

    #steps platforms positions
    PLATFORMS=[[30,670,120,25],[230,540,90,30],[400,420,100,27],[220,300,100,30],[50,180,70,26],[200,60,70,23]]
    platbackub=PLATFORMS.copy()
    bol=[30,230,400,220,50,200]
    #game varibles
    jump=False
    y_change = 0
    player_speed=4.5

    #CREATE SCREEN
    screen= pygame.display.set_mode((width,height))
    pygame.display.set_caption("Jump game")
    
    # update player y position
    def update_player(p_y):
        nonlocal jump
        nonlocal y_change
        jump_heghit = 10.0+sss
        gravity=.3
        if jump:
            jumpsound.play()
            y_change = -jump_heghit
            jump =False
        y_change+=gravity     
        p_y+=y_change
        return p_y
   
    # update steps  platforms
    def update_paltforms(plat,y_pos,change):
        global score,sss
        if y_pos<300 and change<0:
            for i in range(len(plat)):
                if plat[i][1] < 700:
                    plat[i][1]-= (change-sss)
        else :
            pass
        
        flag=1
        
        for i in range(len(plat)):
            if plat[i][1]>660 and y_pos<300 :
                plat[i]=[randint(370,1000)%440,randint(-60,-20),randint(40,130),randint(26,30)] 
                score+=1
                sss+=0.01
                 
        return plat         

            
    
    #chaeak jump collision in bloacks
    def cheak_jump(lst,a):
        nonlocal player_x
        nonlocal player_y
        nonlocal y_change
        for i in range(len(lst)):
            if lst[i].colliderect([player_x+40,player_y+50,40,20]) and jump==False and y_change>0:
                
                a=True
        return a     

    #cheak for game over
    def gameoverchaek(y_p,x_p):
        if y_p>750:
            return True
        return False

    def gameoverfun():
        global game_over,superjump,score
        superjump=2
        score=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if replay.collidepoint(event.pos):
                    buttonsounds.play()
                    game_over=0
                    PLATFORMS=platbackub.copy()
                    main.map_select_screen(dark,char)
        pygame.display.update()
        timer.tick(20)            

    running = True
    
    x_change=0
    yy_change=0
    flag=True
    while running==True:
        global blocks,superjump,score
        score_text=font.render("Score: "+str(score),True,white)
        superJUMPtext=font.render("Super Jump: "+str(superjump),True,white)
        
        if game_over:
             if flag:
              gameoversound.play()
              flag=False
             screen.blit(gameoverphoto, (0, 0))
             
             pygame.display.flip()
             gameoverfun()

        else :
            screen.blit(bg, (0, 0)) 
            screen.blit(score_text, (0, 0))
            screen.blit(superJUMPtext, (0, 15))
            screen.blit(player,(player_x,player_y))
            blocks = []
            for plat in PLATFORMS:
# Resize the image to match platform size
                scaled_img = pygame.transform.scale(platform_img, (plat[2], plat[3]))
                screen.blit(scaled_img, (plat[0], plat[1]))  # Draw the image
                block = pygame.Rect(plat[0], plat[1], plat[2], plat[3])  # For collision
                blocks.append(block)

            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                      x_change = -player_speed
                    elif event.key == pygame.K_RIGHT: 
                      x_change = player_speed
                    if event.key == pygame.K_UP:
                      yy_change = -6
                    elif event.key == pygame.K_SPACE and superjump>0: 
                      y_change = -15
                      jumpsound.play()
                      superjump-=1   
            
                 if event.type == pygame.KEYUP: 
                    if event.key == pygame.K_LEFT:
                     x_change = 0
                    elif event.key == pygame.K_RIGHT: 
                     x_change = 0
                    if event.key == pygame.K_UP:
                     yy_change = 0
                    elif event.key == pygame.K_DOWN: 
                     yy_change = 0   
            player_x+=x_change
            player_y+=yy_change
            player_y= update_player(player_y)
            update_paltforms(PLATFORMS,player_y,y_change)
            jump=cheak_jump(blocks,jump)
            timer.tick(fps)
            game_over = gameoverchaek(player_y,player_x)
            pygame.display.flip()

            if x_change>0:
              player=pygame.transform.flip(player1,1,0)
            elif x_change <0:
              player = player1 
            if player_x>500:
               player_x=player_x%500
            if player_x < -1:
               player_x=500     

            if (score+1)%50==0 and score>100:
               score+=1
               superjump+=1                
   

    pygame.quit()

if __name__ == "__main__":
    salem(0,'none')
