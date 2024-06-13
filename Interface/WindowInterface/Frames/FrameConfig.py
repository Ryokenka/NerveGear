import customtkinter as ctk

from Interface.WindowInterface.HomeInterface import write_selected_options


from Interface.WindowInterface.HomeInterface import load_selected_options


class FrameConfig(ctk.CTkFrame):
    def __init__(self, master,app):
        super().__init__(master)
        self.app = app

        ctk.CTkFrame.__init__(self, master)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        list = ctk.CTkScrollableFrame(self)
        list.grid(row=2, column=0, sticky="nsew")

        self.error_label = ctk.CTkLabel(self, text="", font=("Courrier", 12), text_color="Red")
        self.error_label.grid(row=1,column=0, padx=250, pady=0, sticky="nw")


        self.labelMain = (ctk.CTkLabel(self, text="Associer les capteurs aux actions souhaitées", font=("Courrier", 25))
                          .grid(row=0, column=0, padx=20, pady=20, sticky="nw"))

        self.switch_var = ctk.BooleanVar(value=False)
        self.buttonActivate = ctk.CTkSwitch(master=self, text="Activer",
                                            variable=self.switch_var,
                                            command = lambda: self.toggle_sync(),

                                            onvalue=True, offvalue=False)
        self.buttonActivate.grid(row=0, column=0, padx=20, pady=20, sticky="ne")

        print("INIT bout : " + str(self.switch_var.get()))

        self.optionmenu_vars = []
        print("row:"+str(self.app.total_rows))
        for i in range(self.app.total_rows):
            for j in range(2):
                if j == 0:
                    list.e = ctk.CTkLabel(list, text=self.app.lst[i][0])
                else:
                    #print("liste selected app  AP: "+str(self.app.lst_selected))

                    #print("liste selected AV : "+str(self.app.lst_selected))
                    #self.testselct = load_selected_options()

                    #self.app.lst_selected =load_selected_options()

                    #print("liste selected  AP: "+str(self.app.lst_selected))
                    optionmenu_var = ctk.StringVar(value=self.app.lst_selected[i])
                    self.optionmenu_vars.append(optionmenu_var)

                    list.e = ctk.CTkOptionMenu(list, values=self.app.lst[i][1],
                                               command=lambda choice, nb=i: write_selected_options(choice, nb),
                                               variable=optionmenu_var)

                list.e.grid(row=i + 1, column=j, padx=20, pady=10, sticky="w")


    def show_error(self, message):
        self.error_label.configure(text=message)
        self.error_label.lift()

    def toggle_sync(self):

        if self.switch_var.get() == False:
            self.buttonActivate.deselect()
            self.app.frames["FrameConfigAdvance"].buttonActivate.select()
        else:
            self.buttonActivate.select()
            self.app.frames["FrameConfigAdvance"].buttonActivate.deselect()

    def update_optionmenu(self):
        self.app.lst_selected = load_selected_options()
        print("liste selected  ds func: "+str(self.app.lst_selected))

        for i, optionmenu_var in enumerate(self.optionmenu_vars):
            optionmenu_var.set(self.app.lst_selected[i])


