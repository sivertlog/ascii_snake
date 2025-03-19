import keyboard
import time
from os import system, name
import random

#     ░   █   ☼   ☻
# maybe try keyboard listeners
# maybe try threads


def make_snake_map(map_x, s_location, f_location):
    snake_map = []
    for i in range(map_x):
        snake_map.append([])
        for j in range(map_x):
            snake_map[i].append('░')
    snake_map[s_location[0]][s_location[1]] = '█'
    snake_map[f_location[0]][f_location[1]] = '☼'

    for i in snake_map:
        print(' '.join(i))

def new_fruit_location(map_x):
    x = [0, 0]
    x[0] = random.randint(0, map_x-1)
    x[1] = random.randint(0, map_x-1)
    return x

def eat_fruit(snake_loc, fruit_loc):
    return snake_loc == fruit_loc

def move_head(direction, snake_location, map_x):
    if direction == 'n':
        snake_location[0] = (snake_location[0] - 1) % map_x
    elif direction == 'e':
        snake_location[1] = (snake_location[1] + 1) % map_x
    elif direction == 's':
        snake_location[0] = (snake_location[0] + 1) % map_x
    elif direction == 'w':
        snake_location[1] = (snake_location[1] - 1) % map_x

def move_body(last_location, snake_body):
    pass

def cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    snake_map=[]
    map_x = 20
    snake_location = [0, 0]
    last_location = []
    snake_body = []
    fruit_exist = False
    fruit_location = []
    direction = 'e'

    while True:
        #input
        if keyboard.is_pressed('up'):
            if direction != 's': direction = 'n'
        elif keyboard.is_pressed('right'):
            if direction != 'w': direction = 'e'
        elif keyboard.is_pressed('down'):
            if direction != 'n': direction = 's'
        elif keyboard.is_pressed('left'):
            if direction != 'e': direction = 'w'
        elif keyboard.is_pressed('esc'):
            break

        time.sleep(.1)

        #logic
        last_location = list(snake_location)
        move_head(direction, snake_location, map_x)
        move_body(last_location, snake_body)

        if eat_fruit(snake_location, fruit_location):
            snake_body.insert(0, list(last_location))
            fruit_exist = False

        if fruit_exist == False:
            fruit_location = new_fruit_location(map_x)
            fruit_exist = True

        #grafix
        cls()

        make_snake_map(map_x, snake_location, fruit_location)
        print("Click here, then control snake with arrow keys")
        print("esc to quit")

if __name__ == '__main__':
    main()
