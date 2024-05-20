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

    def clic_long(self, key_press):
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        pt.keyDown(key_press)
        pt.keyUp(key_press)

    def clic_deplacements(self,side):
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        if side == "gauche":
            pt.keyDown("q")
            pt.keyUp("d")
        elif side == "droite":
            pt.keyDown("d")
            pt.keyUp("q")
        elif side == "avant":
            pt.keyDown("z")
            pt.keyUp("s")
        elif side == "arriere":
            pt.keyDown("s")
            pt.keyUp("z")
        else:
            pt.keyUp("q")
            pt.keyUp("d")
            pt.keyUp("z")
            pt.keyUp("s")


    def clic_parmi_plusieurs_choix(self,number,tab):
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        pt.hotkey(tab[number])

    def mouvement_gauche_droite_cam(self, side):
        Minecraft = pt.getWindowsWithTitle("Minecraft")[0]
        Minecraft.activate()
        if side == "gauche":
            print("je vais a gauche")
            pt.keyDown("q")
        elif side == "droite":
            print("je vais a droite")
            pt.keyDown("d")
        elif side == "milieu":
            print("je vais tt droit")
            #pt.keyDown("z")
        else :
            pt.keyUp("q")
            pt.keyUp("d")
            pt.keyUp("z")

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
        if number != 0:
            pt.hotkey(tab[number-1])



#duration = 10

#while duration !=0:
#    bouger_perso('z',2,'attack')
#    duration -= 1