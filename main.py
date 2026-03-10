import pygame
from grid import make_grid, draw

WIDTH = 800
ROWS = 40

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")


def main():
    pygame.init()

    grid = make_grid(ROWS, WIDTH)

    running = True
    while running:
        draw(WIN, grid, ROWS, WIDTH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


main()