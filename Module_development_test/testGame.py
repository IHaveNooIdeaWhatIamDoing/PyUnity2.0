import pygame
import punity
from Module_development_test.punity import Transform2D, Sprite, Input_Manger, Vector2D, Ridigbody

pygame.init()
screen = pygame.display.set_mode((1080, 720))
running = True

# Pictures
player_img_path = "C:/Domenik/Programming2/python-Projects/PyGameTest/Module_development_test/test_pictures/ball.png"

loaded_img = pygame.image.load(player_img_path)
# Create a GameObject
player = punity.GameObject(
                Transform2D(Vector2D(20,30),30, x_scale=0.2, y_scale=0.2),
                Sprite(image_path=player_img_path,layer=1),
                Ridigbody()
                )
punity.add_to_rendering(player)

# For player Movement
speed = 3

def player_movement():
    direction = manage_input()
    player.ridigbody.add_force(Vector2D(speed * direction,0))
    player.ridigbody.update()
    player.physics_update()



def manage_input() -> int:
    direction = 0
    right = int(Input_Manger.get_key_down(key = pygame.K_d))
    left = int(Input_Manger.get_key_down(key = pygame.K_a))
    if right:
        direction = 1
        if left:
            direction = 0
    if left and not right:
        direction = -1
    if not right and not left:
        direction = 0
    return direction



while running:

    # Player Movement
    player_movement()
    punity.main(screen)

    # Events loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False






