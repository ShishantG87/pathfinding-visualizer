import pygame
import random
import algorithms
from grid import make_grid, draw, get_clicked_pos
from algorithms import bfs, reconstruct_path, astar, dijkstra

WIDTH = 800
ROWS = 40

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")

FONT = pygame.font.SysFont("arial", 18)


def draw_text(win):
    text = "A=A* | SPACE=BFS | D=Dijkstra | W+Click=Weight | C=Clear | M=Maze | ↑↓ Speed"
    label = FONT.render(text, True, (0, 0, 0))
    win.blit(label, (10, 10))


def generate_maze(grid, density=0.3):
    for row in grid:
        for node in row:
            if random.random() < density:
                node.make_wall()


def main():

    pygame.init()

    grid = make_grid(ROWS, WIDTH)

    start = None
    end = None

    running = True
    while running:

        draw(WIN, grid, ROWS, WIDTH)
        draw_text(WIN)
        pygame.display.update()

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

                elif pygame.key.get_pressed()[pygame.K_w] and node != start and node != end:
                    node.make_weight()

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

            # KEY INPUT
            if event.type == pygame.KEYDOWN:

                # SPEED
                if event.key == pygame.K_UP:
                    if algorithms.SPEED > 1:
                        algorithms.SPEED -= 2

                if event.key == pygame.K_DOWN:
                    algorithms.SPEED += 2

                # A*
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

                # BFS
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

                # Dijkstra
                if event.key == pygame.K_d and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    found, came_from = dijkstra(
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

                # CLEAR
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)

                # MAZE
                if event.key == pygame.K_m:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)
                    generate_maze(grid)

    pygame.quit()


main()