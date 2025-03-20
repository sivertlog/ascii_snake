# ASCII SNAKE
*by Sivert Log  
March 2025*


## Dependencies:
- Install keyboard module
    - In terminal enter `pip install keyboard`

### For PyCharm
- Enable 'Emulate terminal in output console'  
*or*  
- Run in terminal  
  - In terminal enter `python snake.py`

## Notes:

I tried my best to only use what we've learned in class
up to this point. The two exceptions are keyboard input
and the `system('cls')` command to clear the terminal.

The keyboard inputs are super easy to understand,
they're in the `game_loop` function.

`system('cls')` and `system('clear')` are for
clearing the terminal. It doesn't normally work
in the run window for PyCharm unless you select
'Emulate terminal in output console'. Without this
the program constantly prints new game maps underneath
each other, making the game unplayable. With it
the map appears stationary, so you can
see the snake's movement relative to the map.