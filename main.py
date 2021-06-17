import tkinter as tk
import sys
from settings import Settings
from appPage import AppPage
from intro import LoginPage
from tkinter import messagebox as msg

class Window(tk.Tk):

    def __init__(self, App):
        self.app = App
        self.settings = App.settings

        super().__init__()
        self.title(self.settings.title)
        self.geometry(self.settings.screen)
        self.resizable(0,0)

        self.create_menus()

        self.create_container()

        self.pages = {}
        self.create_appPage()
        self.create_loginPage()

    def quit(self):
        self.Window.destroy()
        sys.exit()


    def change_page(self, page):
        page = self.pages[page]
        page.tkraise()

    def create_loginPage(self):
        self.pages['loginpage'] = LoginPage(self.container, self)

    def create_menus(self):
        self.menuBar = tk.Menu(self)
        self.configure(menu=self.menuBar)

        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="New Item")
        self.fileMenu.add_command(label="Exit", command=self.exit_program)

        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="About", command=self.show_about_info)

        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.menuBar.add_cascade(label="Help", menu=self.helpMenu)


    def create_container(self):
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)


    def create_appPage(self):
        self.pages["appPage"] = AppPage(self.container, self.app)


    def show_about_info(self):
        msg.showinfo("About Palembang Hamster App", "This apps created by\n1. Katarina Cathleen Yap\n2. Steven Sebastian Chandra\n\nCopyright-2021")

    def exit_program(self):
        respond = msg.askyesnocancel("Exit Program", "Are you sure to close the app ?")
        if respond:
            sys.exit()



class ContactApp:

    def __init__(self):
        self.settings = Settings()
        self.window = Window(self)

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    myContactApp = ContactApp()
    myContactApp.run()