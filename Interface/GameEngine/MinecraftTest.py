from time import sleep
import pyautogui as pt

class MinecraftEngine : 
    def __init__(self):
        print("Init Minecraft")

    def bouger_perso(self, key_press, duration, action='walking'):
        print("Bouger Perso")
        sleep(2)
        pt.keyDown(key_press)
        if action == 'walking':
            print('walking')
        elif action == 'attack':
            pt.keyDown('x')

        sleep(duration)
        pt.keyUp('x')
        pt.keyUp(key_press)


#duration = 10

#while duration !=0:
#    bouger_perso('z',2,'attack')
#    duration -= 1