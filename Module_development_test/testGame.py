import pygame
import punity
from Module_development_test.punity import Transform2D, Sprite

pygame.init()
screen = pygame.display.set_mode((1080, 720))
running = True

# Pictures
player_img_path = "C:/Domenik/Programming2/python-Projects/PyGameTest/Module_development_test/test_pictures/ball.png"

loaded_img = pygame.image.load(player_img_path)
# Create a GameObject
player = punity.GameObject(
                Transform2D(20,30, x_scale=0.2, y_scale=0.2),
                Sprite(image_path=player_img_path,layer=1),
                )
punity.add_to_rendering(player)



while running:

    # Testing
    punity.main(screen)
    #screen.blit(loaded_img, (10, 10))

    # Events loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


