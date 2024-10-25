# main.py

import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE
from sprites.npc import NPC
from sprites.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("School Espionage Game")
        self.clock = pygame.time.Clock()
        self.running = True

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.all_sprites.add(self.player)
        self.npcs = pygame.sprite.Group()
        npc = NPC(pos=(100, 100), patrol_points=[(100, 100), (200, 100), (200, 200), (100, 200)])
        self.all_sprites.add(npc)
        self.npcs.add(npc)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()
        # Check for collisions between player and NPCs
        if pygame.sprite.spritecollideany(self.player, self.npcs):
            print("Caught by an NPC!")
            # Handle the event (e.g., reset player position)

    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
