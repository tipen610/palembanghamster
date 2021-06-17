import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class LoginPage(tk.Frame):

            def __init__(self, parent, App):
                  self.app = App
                  self.settings = App.settings

                  super().__init__(parent) #parent = window.container
                  self.grid(row=0, column=0, sticky="nsew")

                  parent.grid_rowconfigure(0, weight=1)
                  parent.grid_columnconfigure(0, weight=1)

                  self.create_mainframe()
                  self.create_intro()

            def create_mainframe(self):

                  self.mainframe = tk.Frame(self, height=self.settings.side, width=self.settings.side, bg="white")
                  self.mainframe.pack(expand=True)

            def create_intro(self):

                  image = Image.open(self.settings.logo)
                  image_w, image_h = image.size
                  ratio = image_w/self.settings.width
                  image = image.resize((int(image_w//ratio/5), int(image_h//ratio/5)))

                  self.logo = ImageTk.PhotoImage(image)
                  self.label_logo = tk.Label(self.mainframe, image=self.logo)
                  self.label_logo.pack(pady=5)

                  self.title = tk.Label(self.mainframe, text="      PALEMBANG HAMSTER           ", font=("Arial", 18, "bold"), bg="white", fg="black")
                  self.title.pack(pady=5)

                  self.username = tk.Label(self.mainframe, text="Enter Username", font=("Arial", 16, "bold"), bg="white", fg="black")
                  self.username.pack(pady=5)

                  self.entry_username = ttk.Combobox(self.mainframe, font=("Arial", 14, "bold"))
                  self.entry_username['values'] = ("Katarina C Yap", "Steven S Chandra", "(Custom)")
                  self.entry_username.current(0)
                  self.entry_username.pack(pady=5)

                  self.password = tk.Label(self.mainframe, text="Enter Password", font=("Arial", 14, "bold"), bg="white", fg="black")
                  self.password.pack(pady=5)

                  self.entry_password = tk.Entry(self.mainframe, font=("Arial", 14, "bold"), show="*")
                  self.entry_password.pack(pady=5)

                  self.btn_login = tk.Button(self.mainframe, text="Enter", font=("Arial", 16, "bold"), command=lambda:self.app.change_page("appPage"))
                  self.btn_login.pack(pady=5)