import sys

import pygame

class game_character:
    def __init__ (self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Game Character")
        self.bg_color = (173,216,230)

        self.character_image = pygame.image.load("./image/character.png")
        self.character_rect = self.screen.get_rect().center
        
    def run_game (self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.screen.blit(self.character_image, self.character_rect)
            pygame.display.flip()
            self.clock.tick(60)
    
if __name__ == "__main__":
    game = game_character()
    game.run_game()