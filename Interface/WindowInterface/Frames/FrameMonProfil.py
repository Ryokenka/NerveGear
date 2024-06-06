import customtkinter as ctk



class FrameMonProfil(ctk.CTkFrame):
    def create_profile(self):
        pseudo = self.entry_pseudo.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        with open("BDD_pseudo.txt", "a") as file:
            file.write(f"Pseudo: {pseudo}, Email: {email}, Password: {password}\n")

        print("Profil enregistré dans BDD_pseudo.txt.")

    def login(self):
        pseudo = self.entry_pseudo.get()
        password = self.entry_password.get()

    def __init__(self, master):
        super().__init__(master)

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



