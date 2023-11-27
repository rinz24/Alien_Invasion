import sys

import pygame

class Game:
    def __init__ (self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Background")
        self.bg_color = (173,216,230)
        
    def run_game (self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)
    
if __name__ == "__main__":
    game = Game()
    game.run_game()