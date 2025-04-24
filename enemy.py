# enemy.py
import pygame, random
from settings import IMG_DIR, WIDTH, HEIGHT  # Importa HEIGHT para límites verticales
from utils import load_image  # Importa load_image correctamente

class WalkingEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image(f"{IMG_DIR}/enemy_walk.png")
        self.rect = self.image.get_rect(x=random.randint(0, WIDTH), y=0)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

class FlyingEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image(f"{IMG_DIR}/enemy_fly.png")
        # Usar entero para el límite de randint
        max_y = HEIGHT // 2
        self.rect = self.image.get_rect(x=0, y=random.randint(0, max_y))
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.kill()