import sys

import pygame

class Rocket:
    def __init__ (self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket")
        self.bg_color = (173,216,230)

        self.character_image = pygame.image.load("./image/rocket.png")
        self.character_rect = self.character_image.get_rect(center=self.screen.get_rect().center)
        self.speed = 8
        
    def run_game (self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.character_rect.x += self.speed
                    elif event.key == pygame.K_LEFT:
                        self.character_rect.x -= self.speed
                    elif event.key == pygame.K_UP:
                        self.character_rect.y -= self.speed
                    elif event.key == pygame.K_DOWN:
                        self.character_rect.y += self.speed
                    elif event.key == pygame.K_q:
                        sys.exit()
                
            self.character_rect.x = max(0, min(self.character_rect.x, 1200 - self.character_rect.width))
            self.character_rect.y = max(0, min(self.character_rect.y, 800 - self.character_rect.height))
                        
            self.screen.fill(self.bg_color)
            self.screen.blit(self.character_image, self.character_rect)
            pygame.display.flip()
            self.clock.tick(60)

    
if __name__ == "__main__":
    game = Rocket()
    game.run_game()