import random

grid_x_count = 4
grid_y_count = 4

def move(direction):
    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if grid[y][x] == grid_x_count * grid_y_count:
                empty_x = x
                empty_y = y

    new_empty_y = empty_y
    new_empty_x = empty_x

    if direction == 'down':
        new_empty_y -= 1
    elif direction == 'up':
        new_empty_y += 1
    elif direction == 'right':
        new_empty_x -= 1
    elif direction == 'left':
        new_empty_x += 1

    if (
        0 <= new_empty_y < grid_y_count and
        0 <= new_empty_x < grid_x_count
    ):
        changed = (grid[empty_y][empty_x], grid[new_empty_y][new_empty_x])
        grid[new_empty_y][new_empty_x], grid[empty_y][empty_x] = changed

def get_initial_value(x, y):
    return y * grid_x_count + x + 1

def is_complete():
    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if grid[y][x] != get_initial_value(x, y):
                return False

    return True

def reset():
    global grid

    grid = []

    for y in range(grid_y_count):
        grid.append([])
        for x in range(grid_x_count):
            grid[y].append(get_initial_value(x, y))

    while True:
        for move_number in range(1000):
            move(random.choice(('down', 'up', 'right', 'left')))

        for move_number in range(grid_x_count - 1):
            move('left')

        for move_number in range(grid_y_count - 1):
            move('up')

        if not is_complete():
            break

reset()

def on_key_down(key):
    if key == keys.DOWN:
        move('down')
    elif key == keys.UP:
        move('up')
    elif key == keys.RIGHT:
        move('right')
    elif key == keys.LEFT:
        move('left')
    elif key == keys.R:
        reset()

    if is_complete():
        reset()

def draw():
    screen.fill((0, 0, 0))

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            if grid[y][x] == grid_x_count * grid_y_count:
                continue

            piece_size = 100
            piece_draw_size = piece_size - 1

            screen.draw.filled_rect(
                Rect(
                    x * piece_size, y * piece_size,
                    piece_draw_size, piece_draw_size
                ),
                color=(100, 20, 150)
            )

            screen.draw.text(
                str(grid[y][x]),
                (x * piece_size, y * piece_size),
                fontsize=60
            )

WIDTH = 100 * 4
HEIGHT = 100 * 4
