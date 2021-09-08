# how draw with pygame
import pygame

try: 
    pygame.display.init()

except:
    print("Erro ao iniciar o Game")
    exit()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Game Test")

pos_x = 100
pos_y = 100


run = True

while run: #==> (run == True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    screen.fill([255, 255, 255])
    #                  x   y   width height
    ret = pygame.Rect(pos_x, pos_y, 50, 50)

    if keys[pygame.K_RIGHT]:
        pos_x += 0.5
    if keys[pygame.K_LEFT]:
        pos_x += 0.5
    if keys[pygame.K_UP]:
        pos_y += 0.3 
    if keys[pygame.K_DOWN]:
        pos_y += 0.3 

    pygame.draw.rect(screen, [0, 0, 255, 255], ret)
    
    pygame.display.update()

pygame.quit()            
