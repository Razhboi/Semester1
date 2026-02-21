import pygame
import os

pygame.init()
WIDHT, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Hagman Game!")

#load images
images =[]
for i in range (7):
    image = pygame.image.load("hangman"+ str(i)+".png")
    images.append(image)

#variable game
hangman_status = 0

#setup game loop

FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick()
    
    win.fill((255,182,193))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()