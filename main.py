import pygame
from grid import make_grid, draw, get_clicked_pos
from algorithms import bfs, reconstruct_path, astar

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

                if row >= ROWS or col >= ROWS:
                    continue

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

                if row >= ROWS or col >= ROWS:
                    continue

                node = grid[row][col]
                node.reset()

                if node == start:
                    start = None

                if node == end:
                    end = None

            # RUN BFS
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and start and end:

                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    found, came_from = astar(
                        lambda: draw(WIN, grid, ROWS, WIDTH),
                        grid,
                        start,
                        end
                    )

                    if found:
                        reconstruct_path(
                            came_from,
                            end,
                            lambda: draw(WIN, grid, ROWS, WIDTH)
                        )

                if event.key == pygame.K_SPACE and start and end:

                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    found, came_from = bfs(
                        lambda: draw(WIN, grid, ROWS, WIDTH),
                        grid,
                        start,
                        end
                    )

                    if found:
                        reconstruct_path(
                            came_from,
                            end,
                            lambda: draw(WIN, grid, ROWS, WIDTH)
                        )
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)

    pygame.quit()


main()