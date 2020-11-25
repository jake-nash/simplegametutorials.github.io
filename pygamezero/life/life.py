import pygame
import math

cell_size = 5

grid_x_count = 70
grid_y_count = 50

grid = []

for y in range(grid_y_count):
    grid.append([])
    for x in range(grid_x_count):
        grid[y].append(False)

def update():
    global selected_x
    global selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = min(math.floor(mouse_x / cell_size), grid_x_count - 1)
    selected_y = min(math.floor(mouse_y / cell_size), grid_y_count - 1)

    if pygame.mouse.get_pressed()[0]:
        grid[selected_y][selected_x] = True
    elif pygame.mouse.get_pressed()[2]:
        grid[selected_y][selected_x] = False

def on_key_down():
    global grid

    next_grid = []

    for y in range(grid_y_count):
        next_grid.append([])
        for x in range(grid_x_count):
            neighbor_count = 0

            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (not (dy == 0 and dx == 0)
                        and (y + dy) < len(grid)
                        and (x + dx) < len(grid[y + dy])
                        and grid[y + dy][x + dx]):

                        neighbor_count += 1

            next_grid[y].append(
                neighbor_count == 3 or
                (grid[y][x] and neighbor_count == 2)
            )

    grid = next_grid

def draw():
    screen.fill((255, 255, 255))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            cell_draw_size = cell_size - 1

            if x == selected_x and y == selected_y:
                color = (0, 255, 255)
            elif grid[y][x]:
                color = (255, 0, 255)
            else:
                color = (220, 220, 220)

            screen.draw.filled_rect(
                Rect(
                    (x * cell_size, y * cell_size),
                    (cell_draw_size, cell_draw_size)
                ),
                color=color
            )

WIDTH = 5 * 70
HEIGHT = 5 * 50
