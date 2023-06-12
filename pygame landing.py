import pygame
from pygame.locals import*
import time

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
game = True
burn = False
speed_y = 0.0 # y-positive is down
speed_x = 0.0
thrust = 0.15
gravity = 0.1
player_x = 660.0
player_y = 40.0

fuel = 800
crash = False
landing_speed = 0.0
game_height = 980
game_width = 1386
clock = pygame.time.Clock()

#graphics
pygame.init()
size = (game_width, game_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Alienplanet shuttle touchdown")
background = pygame.image.load('images/alienplanetbg.bmp').convert()
player_off = pygame.image.load('images/shuttle_off.bmp').convert()
player_on = pygame.image.load('images/shuttle_on.bmp').convert()
player_crash = pygame.image.load('images/shuttle_crash.bmp').convert()
player_on.set_colorkey(WHITE)
player_off.set_colorkey(WHITE)
player_crash.set_colorkey(WHITE)
screen.blit(background, [0,0])
screen.blit(player_off, [player_x,player_y])
pygame.display.update()

while game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if pygame.key.get_pressed()[K_ESCAPE]:
        game = False
    
    speed_y += gravity
    #player_y += speed_y
    screen.blit(background, [0,0])
    #screen.blit(fuel, [600, 200])
    screen.blit(player_off, [player_x,player_y])
    
    
    
    if pygame.key.get_pressed()[K_SPACE]:
        screen.blit(player_on, [player_x,player_y])
        speed_y -= thrust
        fuel -= 2
        burn = True
        
    player_y += speed_y
    landing_speed = speed_y
        
    if player_y >= 705:
        player_y = 705
        speed_y -= gravity
        
                   
        message = 'Landing Speed: %d m/s' %(landing_speed * 10 - 1)
        font = pygame.font.Font(None, 30)
        text = font.render(message, True, GREEN)
        screen.blit(text, (game_width-240, game_height-80))
        #landing_speed = False
        
        #blit(speed_y)
        
        
        if  landing_speed > 4:
            crash = True
            if crash == True:
                
                screen.blit(player_crash, [player_x - 140,player_y - 50])
                message = 'Crashed!'
                font = pygame.font.Font(None, 50)
                text = font.render(message, True, RED)
                screen.blit(text, (game_width-780, game_height-490))         
        else:
            message = 'Landing succesful!'
            font = pygame.font.Font(None, 50)
            text = font.render(message, True, GREEN)
            screen.blit(text, (game_width-850, game_height-490))
             
            #game = False
            
        
    #if speed_y == 0:
        
          
    message = 'Speed: %d m/s' %(speed_y * 10)
    font = pygame.font.Font(None, 30)
    text = font.render(message, True, GREEN)
    screen.blit(text, (game_width-140, game_height-40))
    
    message = 'Fuel: %d' % fuel
    if fuel < 300:
        text = font.render(message, True, ORANGE)
    else:
        text = font.render(message, True, GREEN)
    if fuel < 100:
        text = font.render(message, True, RED)
    screen.blit(text, (game_width-120, game_height-60))
    #if fuel == 0:
        #text = font.render(message, True, RED)
        #screen.blit(text, (game_width-120, game_height-60))
    
    if fuel <= 0:
        fuel = 0
        thrust = 0
        
        
    pygame.display.update()
    clock.tick(50)
        
    
#time.sleep(10)    
pygame.quit()
        
    
    

