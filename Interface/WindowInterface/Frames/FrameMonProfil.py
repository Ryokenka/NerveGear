import re
from tkinter import messagebox
import customtkinter as ctk

from Interface.WindowInterface.Frames import FrameConfig
from Interface.WindowInterface.utils import load_selected_options
from Interface.WindowInterface.utils import write_selected_options

class FrameMonProfil(ctk.CTkFrame):
    def create_profile(self):
        pseudo = self.entry_pseudo.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        valid, message = self.check(pseudo, email, password)
        if not valid:
            print(f"Erreur : {message}")
            return

        selected_options = load_selected_options()

        with open("BDD_pseudo.txt", "a") as file:
            file.write(
                f"Pseudo: {pseudo}; Email: {email}; Password: {password}; SelectedOptions: {selected_options}\n")

        print("Profil enregistré dans BDD_pseudo.txt.")
        self.app.frames['FrameConfig'].update_optionmenu()

    def login(self):
        pseudo = self.entry_pseudo.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        with open("BDD_pseudo.txt", "r") as file:
            users = file.readlines()
            # print(users)

        for user in users:
            user_info = user.strip().split("; ")
            user_data = {}

            for info in user_info:
                if ": " in info:
                    key, value = info.split(": ", 1)
                    user_data[key] = value.strip()
                    # print("test",key,"personne : ", user_data[key])

            if user_data.get("Pseudo") == pseudo and user_data.get("Email") == email and user_data.get(
                    "Password") == password:
                messagebox.showinfo("La connexion réussie", f"Bienvenue, {pseudo}!")

                selected_options = user_data.get("SelectedOptions")
                print("Options sélectionnées :", selected_options)
                selected_options = eval(selected_options)

                for i in range(len(selected_options)):
                    write_selected_options(selected_options[i], i)

                print("TEST")
                self.app.frames['FrameConfig'].update_optionmenu()

                    #self.app.frames[FrameConfig].update_optionmenu()

                return

        messagebox.showerror("La connexion a échouée",
                             "Votre profil n'a pas été reconnu, veuillez créer un nouveau profil")

    def check(self, pseudo, email, password):
        # Vérification du pseudo -> pas d'accents
        if re.search(r'[^\x00-\x7F]', pseudo):
            return False, "Le pseudo ne doit pas contenir d'accents."

        # Vérification de l'email
        if "@" not in email:
            return False, "L'email doit contenir le caractère '@'."

        # Vérification du mot de passe
        if len(password) <= 4:
            return False, "Le mot de passe doit contenir plus de 4 caractères."

        return True, ""

    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.labelMain = (ctk.CTkLabel(self, text="Mon profil", font=("Courrier", 25))
                          .grid(row=1, column=0, padx=20, pady=20, sticky="nw"))

        self.label_pseudo = (ctk.CTkLabel(self, text="Pseudo:", font=("Courrier", 15))
                             .grid(row=2, column=0, padx=20, pady=10, sticky="nw"))
        self.entry_pseudo = ctk.CTkEntry(self)
        self.entry_pseudo.grid(row=2, column=1, padx=20, pady=10, sticky="nw")

        self.label_email = (ctk.CTkLabel(self, text="Email:", font=("Courrier", 15))
                            .grid(row=3, column=0, padx=20, pady=10, sticky="nw"))
        self.entry_email = ctk.CTkEntry(self)
        self.entry_email.grid(row=3, column=1, padx=20, pady=10, sticky="nw")

        self.label_password = (ctk.CTkLabel(self, text="Password:", font=("Courrier", 15))
                               .grid(row=4, column=0, padx=20, pady=10, sticky="nw"))
        self.entry_password = ctk.CTkEntry(self, show="*")
        self.entry_password.grid(row=4, column=1, padx=20, pady=10, sticky="nw")

        self.button_create_profile = ctk.CTkButton(self, text="Créer le profil", command=self.create_profile)
        self.button_create_profile.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        self.button_login = ctk.CTkButton(self, text="Se connecter", command=self.login)
        self.button_login.grid(row=5, column=0, padx=20, pady=10, sticky="w")



