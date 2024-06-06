import csv

import customtkinter as ctk

class FrameConfigAdvance(ctk.CTkFrame):
    def __init__(self, master,app):
        super().__init__(master)
        self.app = app

        ctk.CTkFrame.__init__(self, master)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        list_frame = ctk.CTkScrollableFrame(self)
        list_frame.grid(row=2, column=0, sticky="nsew")

        self.error_label = ctk.CTkLabel(self, text="", font=("Courrier", 12), text_color="Red")
        self.error_label.grid(row=1,column=0,padx=20, pady=20 , sticky="nw")

        self.switch_var = ctk.BooleanVar(value=False)
        self.buttonActivate = ctk.CTkSwitch(master=self, text="Activer",
                                            variable=self.switch_var,
                                            command = lambda: self.toggle_sync(),

                                            onvalue=True, offvalue=False)
        self.buttonActivate.grid(row=0, column=0, padx=20, pady=20, sticky="ne")

        self.labelMain = (ctk.CTkLabel(self, text="Configuration avancée", font=("Courrier", 25))
                          .grid(row=0, column=0, padx=20, pady=20, sticky="nw"))


        list_frame.labelTouches = ctk.CTkLabel(list_frame, text="Touches", font=("Courrier", 18))
        list_frame.labelTouches.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        list_frame.labelCapteurs = ctk.CTkLabel(list_frame, text="Capteurs", font=("Courrier", 18))
        list_frame.labelCapteurs.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        capteurs_list = []
        with open('../ConfigEngine/capteurs_list.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            capteurs_list = [row[0] for row in reader]

        total_rows_advance = len(capteurs_list)
        self.lstTouchesJoueur = [''] * total_rows_advance # Liste pour stocker les touches claviers écrites
        self.capteurs_choice = [''] * total_rows_advance  # Liste pour stocker les capteurs sélectionnés
        self.capteurs_choice = [capteurs_list[0]] * total_rows_advance

        for i in range(total_rows_advance):

            entry_var = ctk.StringVar()
            entry = ctk.CTkEntry(list_frame, textvariable=entry_var)
            entry.grid(row=i + 1, column=0, padx=20, pady=10, sticky="w")


            def update_lstTouchesJoueur(event, row=i, var=entry_var):
                self.lstTouchesJoueur[row] = var.get()

            entry.bind('<KeyRelease>', update_lstTouchesJoueur)


            optionmenu_var = ctk.StringVar(value=capteurs_list[0])
            option_menu = ctk.CTkOptionMenu(list_frame, values=capteurs_list,
                                             command=lambda choice, nb=i: self.write_selected_options(choice,                                                    nb),
                                             variable=optionmenu_var)

            option_menu.grid(row=i + 1, column=1, padx=20, pady=10, sticky="w")


    def show_error(self, message):
        self.error_label.configure(text=message)
        self.error_label.lift()

    def write_selected_options(self, choice, nb):
        self.capteurs_choice[nb] = choice

    def get_touches_and_capteurs(self):
        # Retourne une liste de paires (touche, capteur)
        print("totale : "+str(list(zip(self.lstTouchesJoueur, self.capteurs_choice))))
        return list(zip(self.lstTouchesJoueur, self.capteurs_choice))

    def toggle_sync(self):

        if self.switch_var.get() == False:
            self.buttonActivate.deselect()
            self.app.frames["FrameConfig"].buttonActivate.select()
        else:
            self.buttonActivate.select()
            self.app.frames["FrameConfig"].buttonActivate.deselect()


