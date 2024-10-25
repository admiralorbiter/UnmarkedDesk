import pygame
import os
from settings import PLAYER_SPEED
from PIL import Image

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.load_animations()
        self.image = self.animations['idle_down'][0]
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_SPEED
        self.current_animation = 'idle_down'
        self.animation_index = 0
        self.animation_speed = 0.1
        self.last_update = pygame.time.get_ticks()

    def load_animations(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(base_dir, 'images')
        self.animations = {
            'idle_down': self.load_gif_frames(os.path.join(images_dir, 'down-standing.gif')),
            'idle_up': self.load_gif_frames(os.path.join(images_dir, 'up-standing.gif')),
            'idle_left': self.load_gif_frames(os.path.join(images_dir, 'left-standing.gif')),
            'idle_right': self.load_gif_frames(os.path.join(images_dir, 'right-standing.gif')),
            'run_down': self.load_gif_frames(os.path.join(images_dir, 'down-running.gif')),
            'run_up': self.load_gif_frames(os.path.join(images_dir, 'up-running.gif')),
            'run_left': self.load_gif_frames(os.path.join(images_dir, 'left-running.gif')),
            'run_right': self.load_gif_frames(os.path.join(images_dir, 'right-running.gif')),
        }

    def load_gif_frames(self, gif_path):
        frames = []
        with Image.open(gif_path) as img:
            for frame in range(img.n_frames):
                img.seek(frame)
                frame_surface = pygame.image.fromstring(img.convert("RGBA").tobytes(), img.size, "RGBA")
                frames.append(frame_surface)
        return frames

    def update(self):
        self.move()
        self.animate()

    def move(self):
        keys = pygame.key.get_pressed()
        self.direction.x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.direction.y = keys[pygame.K_DOWN] - keys[pygame.K_UP]

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * self.speed

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:  # Convert to milliseconds
            self.last_update = now
            self.animation_index = (self.animation_index + 1) % len(self.animations[self.current_animation])
            self.image = self.animations[self.current_animation][self.animation_index]

        if self.direction.magnitude() == 0:
            if 'run' in self.current_animation:
                self.current_animation = f'idle_{self.current_animation.split("_")[1]}'
        else:
            if self.direction.x > 0:
                self.current_animation = 'run_right'
            elif self.direction.x < 0:
                self.current_animation = 'run_left'
            elif self.direction.y > 0:
                self.current_animation = 'run_down'
            elif self.direction.y < 0:
                self.current_animation = 'run_up'
