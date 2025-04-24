# player.py
import pygame
from settings import IMG_DIR, WIDTH, HEIGHT
from utils import load_image

def clamp(val, min_val, max_val): return max(min(val, max_val), min_val)

class Player(pygame.sprite.Sprite):   # Clase del jugador
    def __init__(self):
        super().__init__()
        self.image = load_image(f"{IMG_DIR}/player.png") # Cambia la ruta a la imagen del jugador
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT-50))
        self.speed = 5
        self.health = 10
        self.score = 0

    def update(self): # Actualiza la posición del jugador
        keys = pygame.key.get_pressed() # Obtiene las teclas presionadas
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.speed
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * self.speed
        self.rect.x = clamp(self.rect.x + dx, 0, WIDTH - self.rect.width)
        self.rect.y = clamp(self.rect.y + dy, 0, HEIGHT - self.rect.height)

    def take_damage(self): # Método para recibir daño
        self.health -= 1

    def add_score(self, points):
        self.score += points