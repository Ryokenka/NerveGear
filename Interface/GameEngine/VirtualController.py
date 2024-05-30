from time import sleep
import pyautogui as pt

class VirtualController:
    def __init__(self, window_name):
        self.window_name = window_name
        print("Init Controller with window:", self.window_name)

    def set_window_name(self, window_name):
        self.window_name = window_name
        print("Updating Controller with window:", self.window_name)

    def activate_selected_window(self):
        Minecraft = pt.getWindowsWithTitle(self.window_name)[0]
        Minecraft.activate()

    def bouger_perso(self, key_press, duration, action):
        print("Bouger Perso")
        self.activate_selected_window()
        if pt.keyDown(key_press):
            pt.keyUp(key_press)
            print(action + " début")
        else:
            pt.keyDown(key_press)
            print(action + " fin")

    def clic_rapide(self, key_press):
        self.activate_selected_window()
        pt.hotkey(key_press)

    def clic_long(self, key_press):
        self.activate_selected_window()
        pt.keyDown(key_press)
        pt.keyUp(key_press)

    def clic_deplacements(self, side):
        self.activate_selected_window()
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

    def clic_parmi_plusieurs_choix(self, number, tab):
        self.activate_selected_window()
        pt.hotkey(tab[number])

    def mouvement_gauche_droite_cam(self, side):
        self.activate_selected_window()
        if side == "gauche":
            print("je vais a gauche")
            pt.keyDown("q")
        elif side == "droite":
            print("je vais a droite")
            pt.keyDown("d")
        elif side == "milieu":
            print("je vais tt droit")
        else:
            pt.keyUp("q")
            pt.keyUp("d")
            pt.keyUp("z")

    def mouvement_saut_muscle(self):
        self.activate_selected_window()
        pt.keyDown("space")
        pt.keyUp("space")

    def mouvement_clic_muscle(self):
        self.activate_selected_window()
        if not pt.leftClick():
            pt.leftClick()

    def changer_barre(self, number):
        self.activate_selected_window()
        tab = ['&', ')', '"', "'", '(', '-', '=', '_', '$',"*"]
        if number != 0:
            pt.hotkey(tab[number - 1])

# Exemple d'utilisation:
# minecraft_engine = MinecraftEngine("Minecraft")
# minecraft_engine.bouger_perso('z', 2, 'avant')



#duration = 10

#while duration !=0:
#    bouger_perso('z',2,'attack')
#    duration -= 1