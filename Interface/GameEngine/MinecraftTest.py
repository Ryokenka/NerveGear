from time import sleep
import pyautogui as pt

class MinecraftEngine : 
    def __init__(self):
        print("Init Minecraft")

    def bouger_perso(self, key_press, duration, action):
        print("Bouger Perso")
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        if pt.keyDown(key_press):
            pt.keyUp(key_press)
            print(action+"début")
        else:
            pt.keyDown(key_press)
            print(action+"fin")



#duration = 10

#while duration !=0:
#    bouger_perso('z',2,'attack')
#    duration -= 1