from tkinter import *

from MenuFrame import *

root = Tk()
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
root.title("Gestion de pharmacie")
root.geometry("1200x600")
menuF = MenuFrame(root,200, "red", 3)
menuF.grid(row=0, column=0)

root.mainloop()
