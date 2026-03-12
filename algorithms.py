from collections import deque

def bfs(draw, grid, start, end):

    queue = deque([start])
    came_from = {}

    visited = {start}

    while queue:

        current = queue.popleft()

        if current == end:
            return True, came_from

        for neighbor in current.neighbors:

            if neighbor not in visited:

                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

                neighbor.make_visited()

        draw()

    return False, came_from

    
def reconstruct_path(came_from, end, draw):

    current = end

    while current in came_from:

        current = came_from[current]
        current.make_path()
        draw()