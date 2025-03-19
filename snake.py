#################
#  ASCII Snake  #
# by Sivert Log #
#   March 2025  #
#################
import keyboard
import time
from os import system, name
import random

def make_snake_map(map_x, snake_location, f_location, high_score):
    snake_map = []
    for i in range(map_x):
        snake_map.append([])
        for j in range(map_x):
            snake_map[i].append('░')
    for i in range(len(snake_location)):
        snake_map[snake_location[i][0]][snake_location[i][1]] = '█'
    snake_map[f_location[0]][f_location[1]] = '☼'

    display_map(snake_map, map_x, snake_location, high_score)

def display_map(snake_map, map_x, snake_location, high_score):
    control_msg = 'Arrow Keys Control Snake'
    exit_msg = '***Press q To End Game***'
    snake_msg = '[ASCII Snake!!]'
    score = (len(snake_location) - 1) * 10
    if score > high_score: high_score = score
    show_score = '[Score: ' + str(score) + ']'
    show_high = '[High: ' + str(high_score) + ']'
    score_len = len(show_score) + len(show_high)

    print(f"    ╔{'═' * (map_x - len(snake_msg)//2)}{snake_msg}{'═' * (map_x - len(snake_msg)//2)}╗")
    print(f"    ╠{show_score}{'═' * (map_x * 2 + 1 - score_len)}{show_high}╣")

    for i in snake_map:
        print(f"    ║ {' '.join(i)} ║")

    print(f"    ╠{'═' * (map_x * 2 + 1)}╣")
    print(f"    ║{' ' * (map_x - len(control_msg)//2)}{control_msg}{' ' * (map_x - len(control_msg)//2 + 1)}║")
    print(f"    ║{' ' * (map_x - len(exit_msg)//2)}{exit_msg}{' ' * (map_x - len(exit_msg)//2)}║")
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

def game_loop(high_score):
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
        elif keyboard.is_pressed('q'):
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
        make_snake_map(map_x, snake_location, fruit_location, high_score)

def menu():
    cls()
    print(f'''



        [ASCII]  __  __ ___ ._  ._  _____*                            
          /  _\ /  |/ // - || |/ / |  __/                          
         *_\ \ / /|  // /| ||   \  |  _|                    
          \__//_/ |_//_/ |_||_|\_\ |____\                           
           --------------------*by Sivert


                1) Play Game
                2) Exit
''')
    try:
        select = int(input("            Selection: "))
        if 0 < select < 3:
            return select
    except ValueError:
        return 0

def game_over(score, high_score):
    cls()
    print(f'''
    
    
    
        ***GAME OVER***
        
    ''')
    if score > high_score:
        print(f'''
        New High Score!''')
    print(f'''
    
         Score: {score}
         
         
    ''')
    input("Press ENTER to continue:")

def main():
    high_score = 0
    while True:
        select = menu()
        if select == 1:
            score = game_loop(high_score)
            game_over(score, high_score)
            if score > high_score: high_score = score
        elif select == 2:
            return


if __name__ == '__main__':
    main()
