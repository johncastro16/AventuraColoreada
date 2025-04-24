# main.py
import pygame
from settings import WIDTH, HEIGHT, FPS, TITLE
from utils import draw_text, show_menu, load_highscores, save_highscores, show_game_over_screen 
from player import Player
from enemy import WalkingEnemy, FlyingEnemy
from powerup import PowerUp
from levels import generate_level


def game_loop():
    pygame.init() # Inicializa Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Crea la ventana
    pygame.display.set_caption(TITLE) # Cambia el título de la ventana
    clock = pygame.time.Clock() # Crea el reloj para controlar FPS

    all_sprites = pygame.sprite.Group()    # Grupo de todos los sprites
    enemies = pygame.sprite.Group()       # Grupo de enemigos
    powerups = pygame.sprite.Group()      # Grupo de powerups

    player = Player() # Crea el jugador
    all_sprites.add(player) # Añade el jugador al grupo de sprites
    # Genera el primer nivel

    level = 1
    generate_level(level, all_sprites, enemies, powerups)

    highscores = load_highscores() 
    # Pantalla de inicio
    running = True 
    while running:  
        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        all_sprites.update()
        # Colisiones
        for gem in pygame.sprite.spritecollide(player, powerups, False):
            gem.apply(player)
        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            player.take_damage()
            if player.health <= 0:
                running = False
        # Avanzar nivel si no hay enemigos
        if not enemies:
            level += 1
            generate_level(level, all_sprites, enemies, powerups)
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        draw_text(screen, f"Vida: {player.health}", 24, 60, 10)
        draw_text(screen, f"Nivel: {level}", 24, WIDTH/2, 10)
        draw_text(screen, f"Puntaje: {player.score}", 24, WIDTH-80, 10)
        pygame.display.flip()

    # Game over y guardar récord
    if player.score > highscores['highscore']:
        highscores['highscore'] = player.score
        save_highscores(highscores)
    
    if player.health <= 0:
        draw_text(screen, "Game Over", 64, WIDTH/2, HEIGHT/2)
        pygame.display.flip()
        pygame.time.delay(2000)

def main():
    while True:
        game_loop()  # Este corre una partida
        if not show_game_over_screen():
            break  # El jugador no quiere continuar
    pygame.quit()

if __name__ == "__main__":
    main()