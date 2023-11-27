import sys
import pygame
from random import randint

pygame.init()

screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Better Stars")

star_image = pygame.image.load("images/stars.png")
star_rect = star_image.get_rect()

num_of_stars = 20

star_positions = [(randint(0, screen_width - star_rect.width), randint(0, screen_height - star_rect.height)) for _ in range(num_of_stars)]

def update_stars():
    global star_positions
    star_speed = 1 

    for i in range(len(star_positions)):
        x, y = star_positions[i]
        y += star_speed
        if y > screen_height:
            y = 0
            x = randint(0, screen_width - star_rect.width)

        star_positions[i] = (x, y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update_stars()

    screen.fill((0, 0, 0))

    for x, y in star_positions:
        screen.blit(star_image, (x, y))

    pygame.display.flip()
