import pygame
import os

pygame.init()
LEBAR, TINGGI = 800, 500
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Permainan Hangman!")

FPS = 60
jam = pygame.time.Clock()
jalankan = True

while jalankan:
    jam.tick(FPS)  # Memastikan kecepatan frame per detik
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalankan = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            posisi = pygame.mouse.get_pos()
            print(posisi)

pygame.quit()
