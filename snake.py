import keyboard
import time
from os import system, name
import random

#     ░   █   ☼   ☻
# maybe try keyboard listeners
# maybe try threads


def make_snake_map(map_x, snake_location, f_location):
    snake_map = []
    for i in range(map_x):
        snake_map.append([])
        for j in range(map_x):
            snake_map[i].append('░')
    for i in range(len(snake_location)):
        snake_map[snake_location[i][0]][snake_location[i][1]] = '█'
    snake_map[f_location[0]][f_location[1]] = '☼'

    for i in snake_map:
        print(' '.join(i))

def new_fruit_location(map_x, snake_location):
    while True:
        x = [0, 0]
        x[0] = random.randint(0, map_x-1)
        x[1] = random.randint(0, map_x-1)
        if not x in snake_location: return x

def eat_fruit(snake_loc, fruit_loc):
    return snake_loc == fruit_loc

def eat_tail(snake_location):
    if snake_location[0] in snake_location[3:]:
        return True
    return False

def move_head(direction, snake_location, map_x):
    if direction == 'n':
        snake_location[0][0] = (snake_location[0][0] - 1) % map_x
    elif direction == 'e':
        snake_location[0][1] = (snake_location[0][1] + 1) % map_x
    elif direction == 's':
        snake_location[0][0] = (snake_location[0][0] + 1) % map_x
    elif direction == 'w':
        snake_location[0][1] = (snake_location[0][1] - 1) % map_x

def move_body(snake_location):
    for i in range(len(snake_location), 1, -1):
        snake_location[i-1] = list(snake_location[i-2])

def cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    snake_map=[]
    map_x = 20
    snake_location = [[0, 0]]
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
        move_body(snake_location)
        move_head(direction, snake_location, map_x)

        if eat_tail(snake_location):
            print("Game Over")
            break

        if eat_fruit(snake_location[0], fruit_location):
            snake_location.append(list(snake_location[0]))
            fruit_exist = False

        if fruit_exist == False:
            fruit_location = new_fruit_location(map_x, snake_location)
            fruit_exist = True

        #grafix
        cls()

        make_snake_map(map_x, snake_location, fruit_location)
        print("Click here, then control snake with arrow keys")
        print(snake_location)

if __name__ == '__main__':
    main()
