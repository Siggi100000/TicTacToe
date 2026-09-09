import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

while True:
    screen.fill((random, random, random))
    pygame.display.flip()
    clock.tick(60)