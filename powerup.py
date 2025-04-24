# powerup.py
import random
from settings import IMG_DIR, WIDTH, HEIGHT
from utils import load_image
import pygame

class PowerUp(pygame.sprite.Sprite):    # Clase para los power-ups
    def __init__(self, kind):
        super().__init__()
        self.kind = kind # Tipo de power-up
        self.image = load_image(f"{IMG_DIR}/powerup_shield.png") # Cambia la ruta a la imagen del power-up
        self.rect = self.image.get_rect(x=random.randint(0, WIDTH), y=random.randint(0, HEIGHT))

    def apply(self, player):    # Método para aplicar el power-up al jugador
        if self.kind == 'shield':
            player.health += 1
        self.kill()