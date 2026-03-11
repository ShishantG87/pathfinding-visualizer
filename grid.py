import pygame

WHITE = (255,255,255)
GREY = (200,200,200)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)


class Node:

    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * width
        self.color = WHITE
        self.width = width
        
    def is_start(self):
        return self.color == GREEN

    def is_end(self):
        return self.color == RED

    def is_wall(self):
        return self.color == BLACK

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = GREEN

    def make_end(self):
        self.color = RED

    def make_wall(self):
        self.color = BLACK

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))


def make_grid(rows, width):

    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap)
            grid[i].append(node)

    return grid


def draw_grid(win, rows, width):

    gap = width // rows

    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, width))


def draw(win, grid, rows, width):

    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):

    gap = width // rows
    x, y = pos

    row = y // gap
    col = x // gap

    return row, col