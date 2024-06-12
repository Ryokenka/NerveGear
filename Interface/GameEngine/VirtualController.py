from time import sleep
import pyautogui as pt
import pygetwindow as gw

class VirtualController:
    def __init__(self, window_name):
        self.window_name = window_name
        self.current_window = None
        print("Init Controller with window:", self.window_name)

    def set_window_name(self, window_name):
        self.window_name = window_name
        self.current_window = None  # Reset current window when the window name is updated
        print("Updating Controller with window:", self.window_name)

    def activate_selected_window(self):
        if self.current_window is None or self.current_window.title != self.window_name:
            windows = gw.getWindowsWithTitle(self.window_name)
            if windows:
                self.current_window = windows[0]
                print(f"Found window: {self.current_window}")
                try:
                    if self.current_window.isMinimized:
                        print("Window is minimized, restoring...")
                        self.current_window.restore()
                        sleep(0.1)

                    print(f"Activating window: {self.window_name}")
                    self.current_window.activate()
                    sleep(0.1)

                    if not self.current_window.isActive:
                        raise Exception("Failed to activate window.")
                    print(f"Activated window: {self.window_name}")

                except Exception as e:
                    print(f"Failed to activate window {self.window_name}: {e}")
            else:
                print(f"Window with title '{self.window_name}' not found.")

    def update_active_window(self):
        self.activate_selected_window()

    def deactivate_all_keys(self):
        # List of keys to deactivate
        keys = ['q', 'd', 'z', 's', 'space', 'ctrl', '&', 'é', '"', "'", '(', '-', 'è', '_', 'ç', 'à']
        for key in keys:
            if key == 'ctrl':
                pt.keyUp('ctrl')
                pt.keyUp('&')
            else:
                pt.keyUp(key)

    def activate_key(self, key_press):
        print("J'active la key:", key_press)
        self.activate_selected_window()
        self.deactivate_all_keys()
        pt.keyDown(key_press)
        print(f"{key_press} is activated")

    def bouger_perso(self, key_press, duration, action):
        print("Bouger Perso")
        self.update_active_window()
        if pt.keyDown(key_press):
            pt.keyUp(key_press)
            print(action + " début")
        else:
            pt.keyDown(key_press)
            print(action + " fin")

    def clic_rapide(self, key_press):
        self.update_active_window()
        pt.hotkey(key_press)

    def clic_long(self, key_press):
        self.update_active_window()
        pt.keyDown(key_press)
        pt.keyUp(key_press)

    def clic_deplacements(self, side):
        self.update_active_window()
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

    def mouvement_av(self):
        self.update_active_window()
        pt.keyDown("z")
        pt.keyUp("s")
        pt.keyUp("d")
        pt.keyUp("q")




    def mouvement_gav(self):
        self.update_active_window()
        pt.keyDown("z")
        pt.keyDown("q")
        pt.keyUp("s")
        pt.keyUp("d")

    def mouvement_dav(self):
        self.update_active_window()
        pt.keyDown("z")
        pt.keyDown("d")
        pt.keyUp("s")
        pt.keyUp("q")

    def mouvement_ar(self):
        self.update_active_window()
        pt.keyDown("s")
        pt.keyUp("z")
        pt.keyUp("d")
        pt.keyUp("q")

    def mouvement_gar(self):
        self.update_active_window()
        pt.keyDown("s")
        pt.keyDown("q")
        pt.keyUp("z")
        pt.keyUp("d")

    def mouvement_dar(self):
        self.update_active_window()
        pt.keyDown("s")
        pt.keyDown("d")
        pt.keyUp("z")
        pt.keyUp("q")

    def mouvement_g(self):
        self.update_active_window()
        pt.keyDown("q")
        pt.keyUp("d")
        pt.keyUp("z")
        pt.keyUp("s")

    def mouvement_d(self):
        self.update_active_window()
        pt.keyDown("d")
        pt.keyUp("q")
        pt.keyUp("z")
        pt.keyUp("s")

    def mouvement_saut(self):
        self.update_active_window()
        pt.keyDown("space")

    def mouvement_stop(self):
        self.update_active_window()
        pt.keyUp("q")
        pt.keyUp("d")
        pt.keyUp("z")
        pt.keyUp("s")
        pt.keyUp("space")

    def clic_parmi_plusieurs_choix(self, number, tab):
        self.update_active_window()
        pt.hotkey(tab[number])

    def mouvement_gauche_droite_cam(self, side):
        self.update_active_window()
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
        self.update_active_window()
        pt.keyDown("space")
        pt.keyUp("space")

    def mouvement_clic_muscle(self):
        self.update_active_window()
        pt.leftClick()

    def changer_barre(self, number):
        self.update_active_window()
        tab = ['&', ')', '"', "'", '(', '-', '=', '_', '$', "*"]
        if number != 0:
            pt.hotkey(tab[number - 1])


# Exemple d'utilisation:
# minecraft_engine = MinecraftEngine("Minecraft")
# minecraft_engine.bouger_perso('z', 2, 'avant')



#duration = 10

#while duration !=0:
#    bouger_perso('z',2,'attack')
#    duration -= 1