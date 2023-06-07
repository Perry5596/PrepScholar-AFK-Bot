import pyautogui as pag
import random
import time

curr_cords = pag.position()
afk_counter = 0
switch_counter = 0
changing_x = 0

# Changeable Vars
# ( All of these are set for 2560x1440, and on the primary monitor)

a = 125 # Update based on resolution
b = 150 # Update based on resolution
b2 = 385 # Update based on resolution
speed = .5 
change_factor = 230 # Update this number based on resolutions

while True:
    if pag.position() == curr_cords:
        afk_counter += 1
        switch_counter += 1
    else:
        switch_counter = 0
        afk_counter = 0
        curr_cords = pag.position()
        
    if afk_counter > 5:
        x = random.randint(1, 2560) # Update this value for different resolutions
        y = random.randint(200, 1240) # Update this value for different resolutions (leave some wiggle room for the top and bottom)
        pag.moveTo(x, y, 0.5)

        n = random.randint(0, 1)
        if n == 0:
            pag.scroll(x, y, 0.5)
        else:
            pag.scroll(-x, -y, 0.5)
            
        curr_cords = pag.position()

    if switch_counter == 1800:
        pag.moveTo(a, b, speed)
        pag.leftClick()
        time.sleep(3)

        pag.moveTo(changing_x + a, b2, speed)
        pag.leftClick()
        time.sleep(3)

        changing_x += change_factor
        curr_cords = pag.position()

    elif switch_counter == 3600:
        pag.moveTo(a, b, speed)
        pag.leftClick()
        time.sleep(3)

        pag.moveTo(changing_x + a, b2, speed)
        pag.leftClick()
        time.sleep(3)

        changing_x += change_factor
        curr_cords = pag.position()

    elif switch_counter == 5400:
        pag.moveTo(a, b, speed)
        pag.leftClick()
        time.sleep(3)

        pag.moveTo(changing_x + a, b2, speed)
        pag.leftClick()
        time.sleep(3)

        changing_x += change_factor
        curr_cords = pag.position()

    elif switch_counter == 7200:
        pag.moveTo(a, b, speed)
        pag.leftClick()
        time.sleep(3)

        pag.moveTo(changing_x + a, b2, speed)
        pag.leftClick()
        time.sleep(3)

        changing_x += change_factor
        curr_cords = pag.position()

    print(f'AFK Counter: {afk_counter}')
    time.sleep(2)
