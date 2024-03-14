from time import sleep
import pyautogui as pt




def bouger_perso(key_press,duration,action='walking'):
    pt.keyDown(key_press)
    if action == 'walking':
        print('walking')
    elif action=='attack':
        pt.keyDown('x')
    
    sleep(duration)
    pt.keyUp('x')
    pt.keyUp(key_press)


duration = 10

while duration !=0:
    bouger_perso('z',2,'attack')
    duration -= 1