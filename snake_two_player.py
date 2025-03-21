#################
#  ASCII Snake  #
# by Sivert Log #
#   March 2025  #
#################
import keyboard
import time
from os import system, name
import random

def cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def make_snake_map(map_x, map_y, snake_location_1, snake_location_2, f_location, score, players):
    snake_map = []
    for i in range(map_y):
        snake_map.append([])
        for _ in range(map_x):
            snake_map[i].append(' ')
    for i in range(len(snake_location_1)):
        snake_map[snake_location_1[i][0]][snake_location_1[i][1]] = '█'
    for i in range(len(snake_location_2)):
        snake_map[snake_location_2[i][0]][snake_location_2[i][1]] = '░'
    snake_map[f_location[0]][f_location[1]] = '☼'

    display_map(snake_map, map_x, score, players)

def display_map(snake_map, map_x, score, players):
    control_msg = 'Arrow Keys Control Snake'
    exit_msg = '***Press q To End Game***'
    snake_msg = '[ASCII Snake!!]'
    p1_score = '[P1 Score: ' + str(score[0]) + ']'
    if players == 2:
        p2_score = '[P2 Score: ' + str(score[1]) + ']'
    else:
        if score[0] > score[1]: score[1] = score[0]
        p2_score = '[High Score: ' + str(score[1]) + ']'
    score_len = len(p1_score) + len(p2_score)

    print(f"    ╔{'═' * (map_x - len(snake_msg) // 2)}{snake_msg}{'═' * (map_x - len(snake_msg) // 2)}╗")
    print(f"    ╠{p1_score}{'═' * (map_x * 2 + 1 - score_len)}{p2_score}╣")

    for i in snake_map:
        print(f"    ║ {' '.join(i)} ║")

    print(f"    ╠{'═' * (map_x * 2 + 1)}╣")
    print(f"    ║{' ' * (map_x - len(control_msg) // 2)}{control_msg}{' ' * (map_x - len(control_msg) // 2 + 1)}║")
    print(f"    ║{' ' * (map_x - len(exit_msg) // 2)}{exit_msg}{' ' * (map_x - len(exit_msg) // 2)}║")
    print(f"    ╚{'═' * (map_x * 2 + 1)}╝")

def new_fruit_location(map_x, map_y, snake_location):
    while True:
        x = [0, 0]
        x[0] = random.randint(0, map_y - 1)
        x[1] = random.randint(0, map_x - 1)
        if not x in snake_location: return x

def eat_fruit(snake_loc, fruit_loc):
    return snake_loc == fruit_loc

def eat_tail(snake_location):
    if snake_location[0] in snake_location[4:]:
        return True
    return False

def eat_other(snake_1, snake_2):
    if snake_1[0] in snake_2:
        return True
    return False

def move_head(direction, snake_location, map_x, map_y):
    if direction == 'n':
        snake_location[0][0] = (snake_location[0][0] - 1) % map_y
    elif direction == 'e':
        snake_location[0][1] = (snake_location[0][1] + 1) % map_x
    elif direction == 's':
        snake_location[0][0] = (snake_location[0][0] + 1) % map_y
    elif direction == 'w':
        snake_location[0][1] = (snake_location[0][1] - 1) % map_x

def move_body(snake_location):
    for i in range(len(snake_location), 1, -1):
        snake_location[i - 1] = list(snake_location[i - 2])

def grow_snake(snake_location, grow_amount):
    for _ in range(grow_amount):
        snake_location.append(list(snake_location[0]))

def game_loop(players, score):
    MAP_X = 30
    MAP_Y = 20
    SPEED = .15
    GROW_AMOUNT = 10
    SCORE_MULTI = 10
    snake_location_1 = [[0, 0]]
    if players == 2:
        snake_location_2 = [[MAP_Y//2, 0]]
    else:
        snake_location_2 = []
    fruit_location = new_fruit_location(MAP_X, MAP_Y, (snake_location_1 + snake_location_2))
    direction_1 = 'e'
    direction_2 = 'e'

    # input
    while True:
        key_1 = False
        key_2 = False
        timer = time.time()
        while True:
            if not key_1:
                if keyboard.is_pressed('up'):
                    if direction_1 != 's':
                        direction_1 = 'n'
                        key_1 = True
                if keyboard.is_pressed('right'):
                    if direction_1 != 'w':
                        direction_1 = 'e'
                        key_1 = True
                if keyboard.is_pressed('down'):
                    if direction_1 != 'n':
                        direction_1 = 's'
                        key_1 = True
                if keyboard.is_pressed('left'):
                    if direction_1 != 'e':
                        direction_1 = 'w'
                        key_1 = True
            if not key_2:
                if keyboard.is_pressed('w'):
                    if direction_2 != 's':
                        direction_2 = 'n'
                        key_2 = True
                if keyboard.is_pressed('d'):
                    if direction_2 != 'w':
                        direction_2 = 'e'
                        key_2 = True
                if keyboard.is_pressed('s'):
                    if direction_2 != 'n':
                        direction_2 = 's'
                        key_2 = True
                if keyboard.is_pressed('a'):
                    if direction_2 != 'e':
                        direction_2 = 'w'
                        key_2 = True

            if keyboard.is_pressed('q'): return score

            if (time.time() - timer) > SPEED: break

        # logic
        if snake_location_1:
            move_body(snake_location_1)
            move_head(direction_1, snake_location_1, MAP_X, MAP_Y)
            if eat_tail(snake_location_1):
                if players == 2:
                    snake_location_1 = []
                else:
                    return score
        if snake_location_1:
            if eat_fruit(snake_location_1[0], fruit_location):
                grow_snake(snake_location_1, GROW_AMOUNT)
                score[0] += SCORE_MULTI
                fruit_location = new_fruit_location(MAP_X, MAP_Y, (snake_location_1 + snake_location_2))

        if snake_location_2:
            move_body(snake_location_2)
            move_head(direction_2, snake_location_2, MAP_X, MAP_Y)
            if eat_tail(snake_location_2): snake_location_2 = []
        if snake_location_2:
            if eat_fruit(snake_location_2[0], fruit_location):
                grow_snake(snake_location_2, GROW_AMOUNT)
                score[1] += SCORE_MULTI
                fruit_location = new_fruit_location(MAP_X, MAP_Y, (snake_location_1 + snake_location_2))

        if snake_location_1 and snake_location_2:
            if eat_other(snake_location_1, snake_location_2) and eat_other(snake_location_2, snake_location_1):
                return score
            if eat_other(snake_location_1, snake_location_2): snake_location_1 = []
            if eat_other(snake_location_2, snake_location_1): snake_location_2 = []
        if not (snake_location_1 or snake_location_2): return score

        # grafix
        cls()
        make_snake_map(MAP_X, MAP_Y, snake_location_1, snake_location_2, fruit_location, score, players)
        # print(snake_location)

def menu():
    cls()
    print(f'''



        [ASCII]  __  __ ___ ._  ._  _____*                            
          /  _\ /  |/ // - || |/ / |  __/                          
         *_\ \ / /|  // /| ||   \  |  _|                    
          \__//_/ |_//_/ |_||_|\_\ |____\                           
           -------------------*by Sivert


                1) Play Game
                2) Two Player
                2) Exit Game
    ''')
    try:
        select = int(input("                Selection: "))
        if 0 < select < 4:
            return select
    except ValueError:
        return 0

def game_over(score, high_score):
    cls()
    print(f'''



        ***GAME OVER***

    ''')
    if score[0] > high_score:
        print(f'''
        New High Score!''')
    print(f'''

         Score: {score[0]}


    ''')
    input("Press ENTER to continue:")

def game_over_2(score):
    cls()
    print(f'''



        ***GAME OVER***

    ''')
    print(f'''

         P1 Score: {score[0]}
         P2 Score: {score[1]}


    ''')
    input("Press ENTER to continue:")

def main():
    high_score = 0
    while True:
        select = menu()
        if select == 1:
            score = [0, high_score]
            score = game_loop(1, score)
            game_over(score, high_score)
            if score[0] > high_score: high_score = score[0]
        elif select == 2:
            score = [0, 0]
            score = game_loop(2, score)
            game_over_2(score)
        elif select == 3:
            return

if __name__ == '__main__':
    main()