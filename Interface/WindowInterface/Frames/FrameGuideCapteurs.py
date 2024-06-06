import customtkinter as ctk

class FrameGuideCapteurs(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(1, weight=1)

        self.labelMain = (ctk.CTkLabel(self, text="Guide des capteurs", font=("Courrier", 25))
                          .grid(row=0, padx=20, pady=20, sticky="wn"))
        self.labelText = (ctk.CTkLabel(self,
                                       text="Accéléromètre",
                                       font=("Courrier", 20), justify="left", wraplength=980)
                          .grid(row=1, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="Placez le sur votre tête, main, ou pied",
                                       font=("Courrier", 15), justify="left", wraplength=980)
                          .grid(row=2, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="EEG",
                                       font=("Courrier", 20), justify="left", wraplength=980)
                          .grid(row=3, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="blabla de l'EEG",
                                       font=("Courrier", 15), justify="left", wraplength=980)
                          .grid(row=4, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="EMG",
                                       font=("Courrier", 20), justify="left", wraplength=980)
                          .grid(row=5, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="Placez les électrodes rouge et noire sur votre muscle, à quelques centimètres d'écart. Placez le fil blanc sur votre coude comme référence. Connectez les électrodes, le capteur EMG, et le bitalino",
                                       font=("Courrier", 15), justify="left", wraplength=980)
                          .grid(row=6, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="ECG",
                                       font=("Courrier", 20), justify="left", wraplength=980)
                          .grid(row=7, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="blabla de l'ECG",
                                       font=("Courrier", 15), justify="left", wraplength=980)
                          .grid(row=8, padx=20, pady=10, sticky="w"))

