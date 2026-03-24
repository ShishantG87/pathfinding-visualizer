import pygame
from collections import deque
from queue import PriorityQueue


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def bfs(draw, grid, start, end):

    queue = deque([start])
    came_from = {}

    visited = {start}

    while queue:

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.popleft()

        if current == end:
            return True, came_from

        for neighbor in current.neighbors:

            if neighbor not in visited:

                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

                neighbor.make_visited()

        pygame.time.delay(10)
        draw()

    return False, came_from


def astar(draw, grid, start, end):

    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    came_from = {}

    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h((start.row, start.col), (end.row, end.col))

    open_set_hash = {start}

    while not open_set.empty():

        # allow window to close during algorithm
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            return True, came_from

        for neighbor in current.neighbors:

            temp_g = g_score[current] + 1

            if temp_g < g_score[neighbor]:

                came_from[neighbor] = current
                g_score[neighbor] = temp_g

                f_score[neighbor] = temp_g + h(
                    (neighbor.row, neighbor.col),
                    (end.row, end.col)
                )

                if neighbor not in open_set_hash:

                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)

                    neighbor.make_visited()

        pygame.time.delay(10)
        draw()

    return False, came_from


def reconstruct_path(came_from, end, draw):

    current = end

    while current in came_from:

        current = came_from[current]
        current.make_path()
        draw()