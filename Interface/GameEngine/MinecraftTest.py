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

    def clic_rapide(self, key_press):
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        pt.hotkey(key_press)

    def clic_toggle(self, key_press):
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        if pt.keyDown(key_press):
            pt.keyUp(key_press)
        else:
            pt.keyDown(key_press)

    def clic_parmi_plusieurs_choix(self,number,tab):
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        pt.hotkey(tab[number])

    def mouvement_gauche_droite_cam(self, side):
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        if side == "gauche":
            pt.keyDown("q")
        elif side == "droite":
            pt.keyDown("d")
        else :
            pt.keyUp("q")
            pt.keyUp("d")

    def mouvement_saut_muscle(self):
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        pt.keyDown("space")
        pt.keyUp("space")

    def mouvement_clic_muscle(self):
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        if not pt.leftClick():
            pt.leftClick()

    def changer_barre(self,number):
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        tab = ["&","é",'"',"'","(","-","è","_","ç"]
        pt.hotkey(tab[number])



#duration = 10

#while duration !=0:
#    bouger_perso('z',2,'attack')
#    duration -= 1