import tkinter as tk
from tkinter import *
from tkinter import ttk
from Model.dao import *

import customtkinter
import customtkinter as ctk

from Model.Produit import Produit
from ProduitsFrame import ProduitsFrame


class ModifierProduitFrame(tk.Frame):
    def __init__(self, master, w,menuF,produit):
        ProduitsFrame.produitSelected = None
        tk.Frame.__init__(self, master, width=1000)
        ModifierProduitFrame.menuFrame = menuF
        self.isOn = 0

        self.ourMaster = master
        # self.labelForTest = tk.Label(self, text="Ajouter un produit", font=("Helvetica", 20))
        # self.labelForTest.grid(row=0,column=0)




        designation = customtkinter.CTkLabel(self,
                                             text="designation du produit :",
                                             width=200,
                                             height=25,
                                             corner_radius=8)
        self.designationInput = customtkinter.CTkEntry(self,
                                                       width=200,
                                                       height=25,
                                                       fg_color="#29b57e",
                                                       text_color="Black",
                                                       corner_radius=2)

        type = customtkinter.CTkLabel(self,
                                      text="Type du produit :",
                                      width=200,
                                      height=25,
                                      corner_radius=8)
        self.typeInput = customtkinter.CTkEntry(self,
                                                width=200,
                                                height=25,
                                                fg_color="#29b57e",
                                                text_color="Black",
                                                corner_radius=2)

        societe = customtkinter.CTkLabel(self,
                                         text="Nom de la societe :",
                                         width=200,
                                         height=25,
                                         corner_radius=8)
        self.societeInput = customtkinter.CTkEntry(self,
                                                   width=200,
                                                   height=25,
                                                   fg_color="#29b57e",
                                                   text_color="Black",
                                                   corner_radius=2)

        prix = customtkinter.CTkLabel(self,
                                      text="prix du produit :",
                                      width=200,
                                      height=25,
                                      corner_radius=8)
        self.prixInput = customtkinter.CTkEntry(self,
                                                width=200,
                                                height=25,
                                                fg_color="#29b57e",
                                                text_color="Black",
                                                corner_radius=2)
        dosage = customtkinter.CTkLabel(self,
                                        text="Dosage :",
                                        width=200,
                                        height=25,
                                        corner_radius=8)
        self.dosageInput = customtkinter.CTkEntry(self,
                                                  width=200,
                                                  height=25,
                                                  fg_color="#29b57e",
                                                  text_color="Black",
                                                  corner_radius=2)
        qte = customtkinter.CTkLabel(self,
                                     text="Quantite du produit :",
                                     width=200,
                                     height=25,
                                     corner_radius=8)
        self.qteInput = customtkinter.CTkEntry(self,
                                               width=200,
                                               height=25,
                                               fg_color="#29b57e",
                                               text_color="Black",
                                               corner_radius=2)
        uses = customtkinter.CTkLabel(self,
                                      text="utilisation du produit :",
                                      width=200,
                                      height=25,
                                      corner_radius=8)
        self.usesInput = customtkinter.CTkEntry(self,
                                                width=200,
                                                height=50,
                                                fg_color="#29b57e",
                                                text_color="Black",
                                                corner_radius=2)

        sideEffects = customtkinter.CTkLabel(self,
                                             text="side effects du produit :",
                                             width=200,
                                             height=25,
                                             corner_radius=8)
        self.sideEffectsInput = customtkinter.CTkEntry(self,
                                                       width=200,
                                                       height=50,
                                                       fg_color="#29b57e",
                                                       text_color="Black",
                                                       corner_radius=2)
        warnings = customtkinter.CTkLabel(self,
                                          text="Remarques sur produit :",
                                          width=200,
                                          height=25,
                                          corner_radius=8)
        self.warningsInput = customtkinter.CTkEntry(self,
                                                    width=200,
                                                    height=50,
                                                    fg_color="#29b57e",
                                                    text_color="Black",
                                                    corner_radius=2)
        lotNum = customtkinter.CTkLabel(self,
                                        text="Emplacement physique du produit :",
                                        width=300,
                                        height=25,
                                        corner_radius=8)
        self.lotNumInput = customtkinter.CTkEntry(self,
                                                  width=200,
                                                  height=25,
                                                  fg_color="#29b57e",
                                                  text_color="Black",
                                                  corner_radius=2)

        Description = customtkinter.CTkLabel(self,
                                             text="Description du produit :",
                                             width=200,
                                             height=25,
                                             corner_radius=8)
        self.descriptionInput = customtkinter.CTkEntry(self,
                                                       width=300,
                                                       height=100,
                                                       fg_color="#29b57e",
                                                       text_color="Black",
                                                       corner_radius=2)

        designation.grid(row=0, column=0, padx=0, pady=5)
        self.designationInput.grid(row=0, column=1, padx=0, pady=5)

        lotNum.grid(row=0, column=2, padx=0, pady=5)
        self.lotNumInput.grid(row=0, column=3, padx=0, pady=5)

        type.grid(row=1, column=0, padx=0, pady=5)
        self.typeInput.grid(row=1, column=1, padx=0, pady=5)

        societe.grid(row=1, column=2, padx=0, pady=5)
        self.societeInput.grid(row=1, column=3, padx=0, pady=5)

        qte.grid(row=2, column=0, padx=0, pady=5)
        self.qteInput.grid(row=2, column=1, padx=0, pady=5)

        prix.grid(row=2, column=2, padx=0, pady=5)
        self.prixInput.grid(row=2, column=3, padx=0, pady=5)

        dosage.grid(row=3, column=0, padx=0, pady=5)
        self.dosageInput.grid(row=3, column=1, padx=0, pady=5)

        sideEffects.grid(row=3, column=2, padx=0, pady=5)
        self.sideEffectsInput.grid(row=3, column=3, padx=0, pady=5)

        uses.grid(row=4, column=0, padx=0, pady=5)
        self.usesInput.grid(row=4, column=1, padx=0, pady=5)

        Description.grid(row=4, column=2, padx=0, pady=5)
        self.descriptionInput.grid(row=4, column=3, padx=0, pady=5)

        warnings.grid(row=5, column=0, padx=0, pady=5)
        self.warningsInput.grid(row=5, column=1, padx=0, pady=5)

        # setting data :
        self.set_text(self.designationInput,produit.designation)
        self.set_text(self.typeInput,produit.type)
        self.set_text(self.prixInput,produit.prix)
        self.set_text(self.dosageInput,produit.dosage)
        self.set_text(self.qteInput,produit.quantite)
        self.set_text(self.descriptionInput,produit.description)
        self.set_text(self.lotNumInput,produit.lot_num)
        self.set_text(self.warningsInput,produit.warnings)
        self.set_text(self.sideEffectsInput,produit.side_effects)
        self.set_text(self.usesInput,produit.uses)
        self.set_text(self.societeInput,produit.societe)
        self.idPC = produit.id_produit



        #

        self.buttonAdd = customtkinter.CTkButton(self, text="Modifier Le Produit",
                                                 command=self.gotoList)
        self.buttonAdd.grid(row=6, column=1, columnspan=2, pady=10)

    def setMenuFrame(menuF):
        ModifierProduitFrame.menuFrame = menuF
        print("obj :")
    def set_text(self,e,text):
        e.delete(0, END)
        e.insert(0, text)
        return

    def gotoList(self):

        des = self.designationInput.get()
        type = self.typeInput.get()
        prix = float(self.prixInput.get())

        qte = int(self.qteInput.get())
        dosage = self.dosageInput.get()
        lot = int(self.lotNumInput.get())
        uses = self.usesInput.get()
        desc = self.descriptionInput.get()
        soc = self.societeInput.get()
        w = self.warningsInput.get()
        s_e = self.sideEffectsInput.get()

        p = Produit(self.idPC, des, prix, soc, dosage, qte, type, desc, uses, w, s_e, lot)
        dao = Dao()
        dao.modifier_prd(p)
        ModifierProduitFrame.menuFrame.afficherListProduitsFrame()