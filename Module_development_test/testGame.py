import pygame

pygame.init()
screen = pygame.display.set_mode((1080, 720))
running = True

while running:



    # Events loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


