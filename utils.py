# utils.py
import pygame
from settings import WIDTH, HEIGHT, WHITE
import json

def load_image(name):   # Carga una imagen y la convierte a un formato adecuado
    return pygame.image.load(name).convert_alpha()

# Menú simple
def show_menu(start_func):  # Muestra el menú principal
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Aventura Coloreada")   # Cambia el título de la ventana
    clock = pygame.time.Clock()
    selecting = True
    while selecting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                selecting = False
        screen.fill((40, 40, 40))
        draw_text(screen, "Aventura Coloreada", 64, WIDTH/2, HEIGHT/4)
        draw_text(screen, "Presiona cualquier tecla para jugar", 24, WIDTH/2, HEIGHT/2)
        pygame.display.flip()
    start_func()

# Textos
def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont("arial", size)
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surf, text_rect)

# Récords
def load_highscores():
    try:
        with open('highscore.json', 'r') as f:
            data = f.read().strip()
            if not data:
                return {'highscore': 0}
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'highscore': 0}


def save_highscores(data):
    with open('highscore.json', 'w') as f:
        json.dump(data, f)

def show_game_over_screen():
    screen = pygame.display.get_surface()  # obtiene la pantalla actual
    screen.fill((0, 0, 0))
    draw_text(screen, "GAME OVER", 64, WIDTH // 2, HEIGHT // 3)
    draw_text(screen, "Presiona cualquier tecla para reiniciar", 22, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Cerrar juego
            if event.type == pygame.KEYUP:
                return True   # Reiniciar juego