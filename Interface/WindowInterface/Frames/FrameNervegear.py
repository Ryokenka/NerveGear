
import customtkinter as ctk


class FrameNervegear(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(1, weight=1)
        self.labelMain = (ctk.CTkLabel(self, text="Nervegear", font=("Courrier", 25))
                          .grid(row=0, padx=20, pady=10, sticky="nw"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="Qui nous sommes?",
                                       font=("Courrier", 20), justify="left", wraplength=980)
                          .grid(row=1, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="Nervegear révolutionne l'expérience de jeu avec sa technologie de capteurs innovante. Jouez à vos jeux préférés d'une toute nouvelle manière, plus immersive et plus amusante que jamais !",
                                       font=("Courrier", 15), justify="left", wraplength=980)
                          .grid(row=2, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="Nos valeurs :",
                                       font=("Courrier", 20), justify="left")
                          .grid(row=3, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="L'innovation : Nous vous proposons un large choix de capteurs pour une expérience de jeu inédite.\n"
                                            "L'intégrité : Nous sommes soucieux de l'intégrité de nos produits et nous nous engageons à fournir des solutions open source.\n"
                                            "L'adaptabilité : Notre objectif est de vous offrir une expérience personnalisable, adaptée à vos besoins et à vos contraintes.",
                                       font=("Courrier", 15), justify="left", wraplength=980)
                          .grid(row=4, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="Notre produit :",
                                       font=("Courrier", 20), justify="left")
                          .grid(row=5, padx=20, pady=10, sticky="w"))
        self.labelText = (ctk.CTkLabel(self,
                                       text="Nous vous proposons cette interface de jeu qui vient bouleverser votre manière de jouer. Grâce à une combinaison de différents capteurs (EEG, EMG, caméra, etc.), notre technologie permet aux utilisateurs de jouer à leurs jeux préférés (Mario, Minecraft, et bien d'autres!) de manière totalement inédite.\n\nImaginez pouvoir contrôler votre personnage en tournant simplement la tête, ou en levant un certain nombre de doigts. Imaginez pouvoir utiliser vos ondes cérébrales pour déclencher des actions dans le jeu. C'est désormais possible avec Nervegear !\nEnregistrez votre compte dès maintenant afin de sauvegarder votre configuration. Cela garantit une expérience de jeu personnalisée, confortable et précise.",
                                       font=("Courrier", 15), justify="left", wraplength=980)
                                        .grid(row=6, padx=20, pady=10, sticky="w"))

        self.labelText = (ctk.CTkLabel(self,
                                            text = "Contactez-nous :",
                                            font = ("Courrier", 20), justify = "left")
                                            .grid(row=7, padx=20, pady=10, sticky="w"))
        self.labelText = (ctk.CTkLabel(self,
                                       text="Si vous êtes intéressé par nos produits ou si vous avez des questions, n'hésitez pas à nous contacter. Nous serons ravis de vous aider et de vous fournir toutes les informations dont vous avez besoin.\n\nEmail : contact@nervegear.com\nTéléphone : +33 1 22 33 44 55\nAdresse : 123 rue de l'innovation, 75012 Paris",
                                       font=("Courrier", 15), justify="left", wraplength=980)
                                        .grid(row=8, padx=20, pady=10, sticky="w"))
