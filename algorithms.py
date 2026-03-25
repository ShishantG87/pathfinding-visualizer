import pygame
from collections import deque
from queue import PriorityQueue


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# -------- BFS --------
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


# -------- A* --------
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            return True, came_from

        for neighbor in current.neighbors:

            temp_g = g_score[current] + neighbor.weight  # ✅ USE WEIGHT

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


# -------- DIJKSTRA --------
def dijkstra(draw, grid, start, end):

    count = 0
    pq = PriorityQueue()
    pq.put((0, count, start))

    came_from = {}

    dist = {node: float("inf") for row in grid for node in row}
    dist[start] = 0

    visited = set()

    while not pq.empty():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = pq.get()[2]

        if current in visited:
            continue

        visited.add(current)

        if current == end:
            return True, came_from

        for neighbor in current.neighbors:

            new_dist = dist[current] + neighbor.weight  # ✅ USE WEIGHT

            if new_dist < dist[neighbor]:

                dist[neighbor] = new_dist
                came_from[neighbor] = current

                count += 1
                pq.put((dist[neighbor], count, neighbor))

                neighbor.make_visited()

        pygame.time.delay(10)
        draw()

    return False, came_from


# -------- PATH --------
def reconstruct_path(came_from, end, draw):

    current = end

    while current in came_from:

        current = came_from[current]
        current.make_path()
        draw()