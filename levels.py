# levels.py
from enemy import WalkingEnemy, FlyingEnemy
from powerup import PowerUp
import random

def generate_level(level_num, all_sprites, enemies, powerups):
    # Genera enemigos crecientes
    for _ in range(level_num * 2):
        we = WalkingEnemy()
        all_sprites.add(we); enemies.add(we)
    for _ in range(level_num):
        fe = FlyingEnemy()
        all_sprites.add(fe); enemies.add(fe)
    if random.random() < 0.3:
        pu = PowerUp('shield')
        all_sprites.add(pu); powerups.add(pu)