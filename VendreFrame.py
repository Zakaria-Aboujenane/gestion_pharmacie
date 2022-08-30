import os
import tkinter as tk
import subprocess
import webbrowser
from Model.dao import *
import PIL
import customtkinter
from PIL import ImageTk,Image

from pdfCreator import *

from Model.Produit import  *
import customtkinter as ctk


class VendreFrame(ctk.CTkFrame):
    def __init__(self,master,listDesProduits):
        self.listPanier = listDesProduits
        ctk.CTkFrame.__init__(self, master,fg_color="white")
        self.ourMaster = master
        self.labelForTest = tk.Label(self, text="Vendre les produits", font=("Helvetica", 20))
        self.labelForTest.pack()
        self.isOn = 0
        # affichage des produits a vendre + prix total
        mydic = {}
        fames = []
        prixTotal = 0
        self.listProds = []
        for i in listDesProduits:

            frame = ctk.CTkFrame(self, self,pady=3)
            labelProdText = tk.Label(frame, text="produit :")
            textInLabel = i.designation + " -- "+str(i.prix)+" DH"
            totalSingle = float(i.prix)*int(i.qteAvendre)
            txtToFacture = textInLabel +" x"+str(i.qteAvendre)+" = "+str(totalSingle) +"DH"
            newStock = int(i.quantite) - int(i.qteAvendre)
            i.newS = int(newStock)
            self.listProds.append(txtToFacture)
            labelProd = tk.Label(frame,text=textInLabel)
            labelqte = tk.Label(frame, text="quantite :")
            qteInput = customtkinter.CTkLabel(frame,
                                              text=i.qteAvendre,
                                                 width=120,
                                                 height=25,
                                                 fg_color="#29b57e",
                                                 text_color="Black",
                                                 corner_radius=2)
            labelLimitQte = tk.Label(frame, text=" / quantite disponible : "+str(i.quantite))
            labelProdText.grid(row=0,column=0)
            labelProd.grid(row=0,column=1,padx=10)
            labelqte.grid(row=0,column=2)
            qteInput.grid(row=0,column=3)
            labelLimitQte.grid(row=0,column=4)
            frame.pack()
            prixTotal += (float(i.prix)*int(i.qteAvendre))
        frame = ctk.CTkFrame(self, self,pady=20)
        totalPLabel = customtkinter.CTkLabel(frame,
                                          text="Prix total : ",
                                          width=120,
                                          height=25,
                                          fg_color="#29b57e",
                                          text_color="RED",text_font=("Proxima Nova", 16, "bold"),
                                          corner_radius=2)
        self.prixRounded  = round(prixTotal, 2)
        total = customtkinter.CTkLabel(frame,
                                             text=str(self.prixRounded)+" DH",
                                             width=300,
                                             height=25,
                                             fg_color="black",
                                             text_color="RED", text_font=("Proxima Nova", 20, "bold"),
                                             corner_radius=2)
        totalPLabel.grid(row=0,column=0)
        total.grid(row=0,column=1)
        frame.pack()
        pic_imprimer = ImageTk.PhotoImage(PIL.Image.open("pics/printer.png").resize((32, 32)))
        self.btn_bar_recherche = customtkinter.CTkButton(self, text="Imprimer la facture ",
                                                         image=pic_imprimer, compound="left",
                                                         corner_radius=30,
                                                         bg_color="white", fg_color="white",
                                                         width=40,
                                                         command=self.imprimer)
        self.btn_bar_recherche.pack()


    def imprimer(self):
        facture = PdfCreator("Facture.pdf", self.listProds, self.prixRounded)
        dao = Dao()
        dao.addVente(self.listPanier)
        for p in self.listPanier:
            p.quantite = p.newS
            dao.modifier_prd(p)
        path = 'Facture.pdf'
        os.system(path)







