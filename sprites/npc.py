import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self, pos, patrol_points):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Red for NPC
        self.rect = self.image.get_rect(center=pos)
        self.patrol_points = patrol_points
        self.current_point = 0
        self.speed = 2

    def update(self):
        target = self.patrol_points[self.current_point]
        dx = target[0] - self.rect.x
        dy = target[1] - self.rect.y
        dist = (dx ** 2 + dy ** 2) ** 0.5

        if dist < 5:
            self.current_point = (self.current_point + 1) % len(self.patrol_points)
        else:
            self.rect.x += self.speed if dx > 0 else -self.speed
            self.rect.y += self.speed if dy > 0 else -self.speed

