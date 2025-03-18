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

    display_map(snake_map, map_x, snake_location)

def display_map(snake_map, map_x, snake_location):
    score = (len(snake_location) - 1) * 10
    show_score = "[Score: " + str(score) + "]"

    print(f"    ╔{show_score}{'═' * (map_x * 2 + 1 - len(show_score))}╗")

    for i in snake_map:
        print(f"    ║ {' '.join(i)} ║")
    print(f"    ╚{'═' * (map_x * 2 + 1)}╝")

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

def game_loop():
    map_x = 20
    snake_location = [[0, 0]]
    fruit_location = new_fruit_location(map_x, snake_location)
    fruit_exist = True
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
            return len(snake_location) * 10

        time.sleep(.1)

        #logic
        move_body(snake_location)
        move_head(direction, snake_location, map_x)

        if eat_tail(snake_location):
            print("Game Over")
            return len(snake_location) * 10

        if eat_fruit(snake_location[0], fruit_location):
            snake_location.append(list(snake_location[0]))
            fruit_exist = False

        if not fruit_exist:
            fruit_location = new_fruit_location(map_x, snake_location)
            fruit_exist = True

        #grafix
        cls()

        make_snake_map(map_x, snake_location, fruit_location)
        print("Click here, then control snake with arrow keys")
        print(snake_location)

def menu():
    cls()
    print(f'''



        [ASCII]  __  __ ___ ._  ._  _____*                              
          /  _\ /  |/ // - || |/ / |  __/                          
         *_\ \ / /|  // /| ||   \  |  _|                    
          \__//_/ |_//_/ |_||_|\_\ |____\                           

            1) Play Game
            2) Exit''')
    try:
        select = int(input("            Selection: "))
        if 0 < select < 3:
            return select
    except ValueError:
        return 0

def game_over(score):
    cls()
    print(f'''
    
    
    
        ***GAME OVER***
        
        
        
        
         Score: {score}
         
         
''')
    input("Press ENTER to continue:")

def main():
    while True:
        select = menu()
        if select == 1:
            score = game_loop()
            game_over(score)
        elif select == 2:
            return


if __name__ == '__main__':
    main()
