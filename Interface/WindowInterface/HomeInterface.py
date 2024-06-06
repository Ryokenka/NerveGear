from tkinter import *
from typing import Dict, List, Any

import pygetwindow as gw
from multiprocessing import Pool, cpu_count
from Interface.CapteursEngine.AccelerometreEngine import AccelerometreTracking
from Interface.CapteursEngine.BitalinoEngine import MuscleTracking
from Interface.CapteursEngine.TestCameraRecognition import HeadAndHandTracking
from Interface.GameEngine.VirtualController import VirtualController
from Interface.WindowInterface.Frames import FrameGuideCapteurs
from Interface.WindowInterface.Frames import FrameConfig
from Interface.WindowInterface.Frames import FrameBoutons
from Interface.WindowInterface.Frames import FrameNervegear
from Interface.WindowInterface.Frames import FrameMonProfil
from Interface.WindowInterface.Frames import FrameConfigAdvance
from Interface.WindowInterface.Frames import FrameNavig

import customtkinter as ctk
import csv

from Interface.WindowInterface.utils import load_selected_options


def load_config(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        config = []
        for row in reader:
            action = row[0]
            options = row[1:]
            config.append([action, options])
        return config
    
# Fonction pour sélectionner la fenêtre
def get_active_windows():
    # Retrieve all windows
    windows = gw.getAllTitles()
    # Filter out empty titles and ensure all entries are strings
    return [win for win in windows if isinstance(win, str) and win]

#l'interface
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1080x720')
        self.title("Interface Test")
        self.iconbitmap("../Image/LOGO_NVG.ico")



        self.selected_window = StringVar(value="Choisir fenêtre")
        self.window_list = get_active_windows()
        self.MC = VirtualController("")
        self.update_minecraft_window(self)

        # Print the window list to debug
        print("Window List:", self.window_list)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.total_rows = total_rows # Example shared variable
        self.lst = lst  # Example shared variable
        self.lst_selected = lst_selected  # Example shared variable

        self.frame_navig = FrameNavig(self)
        self.frame_navig.grid(row=0, column=0, padx=20, pady=20, sticky="ns")

        self.mainframe = ctk.CTkFrame(self)

        self.labelMain = ctk.CTkLabel(self.mainframe, text="Interface de configuration", font=("Courrier", 25, "bold"))
        self.labelMain.grid(row=0, padx=20, pady=10)

        self.mainframe.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_rowconfigure(0, weight=1)

        self.frames = {}
        self.create_frames()

        # self.frames[FrameGuideCapteurs] = FrameGuideCapteurs(self.mainframe)
        #
        #
        # for F in (FrameConfig,FrameConfigAdvance, FrameBoutons, FrameMonProfil, FrameNervegear):
        #     self.frames[F] = F(self.mainframe)
        #     self.frames[F].grid(row=0, column=0, sticky="nsew")
        # self.show_frame(FrameConfig)

        self.dropdown = ctk.CTkOptionMenu(self.frames["FrameConfig"], values=self.window_list, variable=self.selected_window, command=self.update_minecraft_window)
        self.dropdown.grid(row=1, padx=20, pady=20 , sticky = "ne")

        self.dropdown = ctk.CTkOptionMenu(self.frames["FrameConfigAdvance"], values=self.window_list,
                                          variable=self.selected_window, command=self.update_minecraft_window)
        self.dropdown.grid(row=1, padx=20, pady=20, sticky = "ne")

        self.dropdown = ctk.CTkOptionMenu(self.frames["FrameBoutons"], values=self.window_list,
                                          variable=self.selected_window, command=self.update_minecraft_window)
        self.dropdown.grid(row=1, padx=20, pady=20, sticky="ne")

    def create_frames(self):
        self.frames["FrameGuideCapteurs"] = FrameGuideCapteurs(self.mainframe)
        self.frames["FrameConfig"] = FrameConfig(self.mainframe, self)
        self.frames["FrameConfigAdvance"] = FrameConfigAdvance(self.mainframe, self)
        self.frames["FrameBoutons"] = FrameBoutons(self.mainframe, self)
        self.frames["FrameMonProfil"] = FrameMonProfil(self.mainframe)
        self.frames["FrameNervegear"] = FrameNervegear(self.mainframe)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("FrameConfig")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        
    def update_minecraft_window(self, *args):
        selected_window = self.selected_window.get()
        self.MC.set_window_name(selected_window)
        print(f"Updated Minecraft window to: {selected_window}")

    def get_selected_window(self):
        return self.selected_window.get()




def write_selected_options(choice, i):
    print("write")
    with open('../ConfigEngine/selected_options.txt', 'r') as f:
        lines = f.readlines()
    with open('../ConfigEngine/selected_options.txt', 'w') as f:
        for j, line in enumerate(lines):
            if j == i:
                f.write(f'{choice}\n')
            else:
                f.write(line)


#definition du mapping
if __name__ == "__main__":
    # appeler fichiers ds capteurs selon la configuration

    lst =load_config('../ConfigEngine/config.csv')
    lst_selected = load_selected_options()
    total_rows = len(lst)
    print("row1:" + str(total_rows))

    app = App()
    app.lst = lst
    app.lst_selected = lst_selected
    app.total_rows = total_rows
    print("row2:" + str(app.total_rows))

    app.mainloop()