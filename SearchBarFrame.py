import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk


class ProduitsFrame(ctk.CTkFrame):
    def __init__(self, master, w):
        ctk.CTkFrame.__init__(self, master, width=w, highlightbackground="red", highlightthickness=3)
        self.ourMaster = master
        self.labelForTest = tk.Label(self, text="Liste des Produits", font=("Helvetica", 20))
        self.labelForTest.pack()
        self.isOn = 0