import random

def add_to_sequence():
    sequence.append(random.randint(1, 4))

def reset():
    global sequence
    global current
    global timer
    global state
    global flashing

    sequence = []
    add_to_sequence()
    current = 0
    timer = 0
    state = 'watch' # 'watch', 'repeat', 'gameover'
    flashing = False

reset()

def update(dt):
    global timer
    global current
    global state
    global flashing

    if state == 'watch':
        timer += dt
        if timer >= 0.5:
            timer = 0
            flashing = not flashing
            if not flashing:
                current += 1
                if current == len(sequence):
                    state = 'repeat'
                    current = 0

def on_key_down(key):
    global current
    global state

    if state == 'repeat':
        if key in (keys.K_1, keys.K_2, keys.K_3, keys.K_4):
            if key == keys.K_1:
                number = 1
            elif key == keys.K_2:
                number = 2
            elif key == keys.K_3:
                number = 3
            elif key == keys.K_4:
                number = 4

            if number == sequence[current]:
                current += 1
                if current == len(sequence):
                    current = 0
                    add_to_sequence()
                    state = 'watch'
            else:
                state = 'gameover'
    elif state == 'gameover':
        reset()

def draw():
    screen.fill((0, 0, 0))

    def draw_square(number, color, color_flashing):

        if state == 'watch' and flashing and number == sequence[current]:
            square_color = color_flashing
        else:
            square_color = color

        square_size = 50
        screen.draw.filled_rect(
            Rect(square_size * (number - 1), 0, square_size, square_size),
            color=square_color
        )
        screen.draw.text(str(number), (square_size * (number - 1) + 21, 18))

    draw_square(1, (50, 0, 0), (255, 0, 0))
    draw_square(2, (0, 50, 0), (0, 255, 0))
    draw_square(3, (0, 0, 50), (0, 0, 255))
    draw_square(4, (50, 50, 0), (255, 255, 0))

    if state == 'repeat':
        screen.draw.text(str(current + 1) + '/' + str(len(sequence)), (20, 60))
    elif state == 'gameover':
        screen.draw.text('Game over!', (20, 60))

WIDTH = 530
HEIGHT = 400
