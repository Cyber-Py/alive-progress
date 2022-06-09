from alive_progress import alive_bar, config_handler
from time import sleep
from random import randint
import os
def clear():
  os.system('clear')


def InitColor(red = 0, green = 0, blue = 0, bold = False, dim = False, italic = False, underlined = False, swap_foreground_and_bg_colors = False, hidden = False, reset = False,reset_all = False):
  '''
  ```
  red, green, and blue: color to use throughout the code unless changed
  the rest of the parameters are for customization of the text
  reset: resets the attributes (Does not include the colors)
  reset_all: resets all of the attributes (Including colors)
  
  `\033[0m` - Resets all color and formats
  `\033[1m` - Creates bold text
  `\033[2m` - Creates dim text
  `\033[3m` - Creates italic text
  `\033[4m` - Creates underlined text
  `\033[7m` - Swaps foreground and background colors
  `\033[8m` - Hides text
  -----------------------
  \033[38;2;{RED};{GREEN};{BLUE}m
  ```
  '''
  if red > 255 or green > 255 or blue > 255 or red < 0 or green < 0 or blue < 0:
    print(f'Try again; Your inputs were{red}{green}{blue}.\n One of them was too high or too low.')
  else:
    print(f'\033[38;2;{red};{green};{blue}m')
  os.system('clear')
  for i in range(1):
    if bold == True:
      print('\033[1m'); clear()
      break
    elif dim == True:
      print('\033[2m'); clear()
      break
    elif italic == True:
      print('\033[3m'); clear()
      break
    elif underlined == True:
      print('\033[4m'); clear()
      break
    elif swap_foreground_and_bg_colors == True:
      print('\033[7m'); clear()
      break
    elif hidden == True:
      print('\033[8m'); clear()
      break
    elif reset == True:
      print('\033[0m'); clear()
      print(f'\033[38;2;{red};{green};{blue}m'); clear()
      break
    elif reset_all == True:
      print('\033[0m'); clear()
      break
    

def terminated():
  InitColor(red = 255, green = 0, blue = 0, bold = True)
  print ('PROGRAM CRASHED\nPLEASE RESTART PROGRAM\nSESSION TERMINATED')
  exit()
  
def chance():
  InitColor(red = 255, green = 0, blue = 0)
  r = randint(1, 1000)
  if r == 392:
    terminated()
    exit()
  else:
    print('We ran into an internal error... Please Wait')
    sleep(randint(1, 5))
    print('Error Fixed.')
    sleep(1.5)
    clear()


def bar(amount = 1000, starting_string = 'Initializing...', bar = 'bubbles', spinner = 'dots_reverse'):
  '''
  ```
  amount: the amount needed to end the progress bar\n
  startin_string: the string that is going to be printed out on 0\n
  bar: the type of bar that will used in the progress bar\n
  spinner: the tpye of spinner that will be used in the progress bar
  ```
  '''
  config_handler.set_global(bar = bar, spinner = spinner)
  count = 0
  with alive_bar(amount) as Bar:
    for i in range(amount):
      if count == 0:
        print(starting_string)
        sleep(1)
        clear()
        count += 1
        InitColor(red = 0, green = 255, blue = 0)
      elif i % randint(100, 700) == count - 1 and count != 0:
        chance()
        InitColor(red = 0, green = 255, blue = 0, reset = True)
        InitColor(red = 0, green = 255, blue = 0)
      sleep(0.01)
      Bar()
    
InitColor(red = 0, green = 255, blue = 0)
bar()
