# ASCII SNAKE
*by Sivert Log  
March 2025*


## Dependencies:
- Install keyboard module
    - In terminal enter `pip install keyboard`

### For PyCharm
Two options to run properly in PyCharm:
- Enable 'Emulate terminal in output console'  
  1) Main Menu | Run | Edit Configurations
  2) Edit configuration templates(*bottom left*)
  3) select Python on left pane
  4) click Modify options(*top right*)
  5) select Emulate terminal in output console
  6) select OK to apply  

  ***OR***
- Run in terminal
  - *Open terminal with `ALT F12`, or the button on the
bottom left of the PyCharm window, above Git and Problems*
  - In the terminal enter `python snake.py`

## Notes:
The controls aren't perfect, but at the higher speed
it is harder to notice(I will fix this!) The map is scalable, just change
the `MAP_X` and `MAP_Y` variables in `game_loop()`

I tried my best to only use what we've learned in class
up to this point. I made two exceptions to keep the
game fun. The two exceptions are the keyboard detection
and the `system('cls')` command to clear the terminal.

The keyboard inputs are super easy to understand,
they're in the `game_loop` function.

`system('cls')` and `system('clear')` are for
clearing the screen. It doesn't normally work
in the run window for PyCharm unless you select
'Emulate terminal in output console'. Without this
the program constantly prints new game maps underneath
each other, making the game unplayable. With it
the map appears stationary, so you can
see the snake's movement relative to the map.

Making the map was basically the same as making
the Vigenere square in Lab 7. `snake_location` is
the 'snake'; it is a list of coordinates that is applied
to the map. At the very bottom of `game_loop` there
is a commented line `#print(snake_location)`. If you
uncomment this you can get a good visual of how the
snake list works.

If anyone is interested, I would be more than happy
to add comments to the code explaining everything in
more detail. Just let me know!