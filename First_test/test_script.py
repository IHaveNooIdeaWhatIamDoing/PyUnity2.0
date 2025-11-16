import pygame
from pygame.transform import scale

pygame.init()

screen = pygame.display.set_mode((1080, 720))
running = True

# Sprites
ball_img = pygame.image.load("C:/Domenik/Programming2/python-Projects/PyGameTest/First_test/pictures/ball.png").convert_alpha()
ball_img = pygame.transform.scale(ball_img, (ball_img.get_width() *0.1, ball_img.get_height() * 0.1))


font = pygame.font.SysFont("Arial", 20)

clock = pygame.time.Clock()
x=0
delta_time = 0.1
speed = 0
while running:
    screen.fill((255, 255, 255))
    screen.blit(ball_img, (x, 30))


    hitbox = pygame.Rect(x, 30, ball_img.get_width(), ball_img.get_height())

    mpos = pygame.mouse.get_pos()

    target = pygame.Rect(300,0,160,280)
    collision = hitbox.colliderect(target)
    m_collision = target.collidepoint(mpos)
    pygame.draw.rect(screen, (255* collision , 255 *m_collision, 30), target)

    x += speed

    text = font.render(str(speed), True, (255, 255, 255))
    screen.blit(text, (30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                speed = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                speed = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                speed = 0


    pygame.display.flip()
    delta_time = clock.tick(120)
    delta_time = max(0.001,min(0.1,delta_time))
pygame.quit()