import sys

import pygame

def keys():
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Keys")
    font = pygame.font.Font(None, 30)

    text = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                text += key_name
                print(text)

        screen.fill((255, 255, 255))
        text_surface = font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (20, 20))
        pygame.display.flip()

if __name__ == "__main__":
    keys()