import pygame
from grid import make_grid, draw, get_clicked_pos

WIDTH = 800
ROWS = 40

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")


def main():

    pygame.init()

    grid = make_grid(ROWS, WIDTH)

    start = None
    end = None

    running = True
    while running:

        draw(WIN, grid, ROWS, WIDTH)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # LEFT CLICK
            if pygame.mouse.get_pressed()[0]:

                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)

                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != start and node != end:
                    node.make_wall()

            # RIGHT CLICK
            if pygame.mouse.get_pressed()[2]:

                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)

                node = grid[row][col]
                node.reset()

                if node == start:
                    start = None

                if node == end:
                    end = None

    pygame.quit()


main()