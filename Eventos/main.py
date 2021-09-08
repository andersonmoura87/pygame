# event with pygame

import pygame

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Game test")

run = True

while run: # ==> run == True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # r = red --> vermelho --> 255
    # g = green --> verde --> 255
    # b = blue --> azul --> 255
    
    screen.fill([255, 255, 255]) 
    pygame.display.update()

pygame.quit()
