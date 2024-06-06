import customtkinter as ctk



class FrameBoutons(ctk.CTkFrame):
    def __init__(self, master,app):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.labelMain = (ctk.CTkLabel(self, text="Test Commandes", font=("Courrier", 25))
                          .grid(row=0, padx=20, pady=20, sticky="wn"))

        self.button1 = ctk.CTkButton(self, text="Avancer", command= lambda : MCavancer(MC))
        self.button1.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.button2 = ctk.CTkButton(self, text="Reculer", command= lambda :MCreculer(MC))
        self.button2.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.button3 = ctk.CTkButton(self, text="Gauche", command= lambda :MCgauche(MC))
        self.button3.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.button4 = ctk.CTkButton(self, text="Droite", command= lambda :MCdroite(MC))
        self.button4.grid(row=2, column=2, padx=10, pady=10, sticky="ew")


# # Test des commandes
# def MCavancer(MC):
#     MC.bouger_perso('z', 2, 'avant')
# def MCreculer(MC):
#     MC.bouger_perso('s', 2, 'arrière')
# def MCgauche(MC):
#     MC.bouger_perso('q', 2, 'gauche')
# def MCdroite(MC):
#     MC.bouger_perso('d', 2, 'droit')
# def MCjump(MC):
#     MC.clic_rapide('space')
