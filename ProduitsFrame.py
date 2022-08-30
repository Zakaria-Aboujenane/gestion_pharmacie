import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import PIL
from PIL import Image,ImageTk
from Model.Produit import *
from popupWindow import *
from Model.dao import *

import customtkinter as ctk

from VendreFrame import VendreFrame


class ProduitsFrame(ctk.CTkFrame):
    MasterPage = None
    myMenu = None
    produitSelected=None

    def __init__(self, master, w,menuF):
        ProduitsFrame.myMenu = menuF
        ProduitsFrame.listPanier = []
        ProduitsFrame.selectedProds = 0
        ctk.CTkFrame.__init__(self, master, width=w,fg_color="#29b57e",corner_radius=10)
        self.frameNotif = ctk.CTkFrame(self, self, width=w, bg_color="#29b57e", fg_color="#29b57e", corner_radius=10)
        self.frameNotif.grid(row=0, column=0)
        ProduitsFrame.MasterPage = master

        self.ourMaster = master

        self.isOn = 0
        ProduitsFrame.value=10

        self.creerListe()
        self.afficherProduitsDepuisBD()

        self.labelSelected = tk.Label(self.frameNotif, text="Produits Selectionnes : ")
        self.statusbar = tk.Label(self.frameNotif, text="0")
        self.labelSelected.grid(row=0, column=1)
        self.statusbar.grid(row=0, column=2)

        ProduitsFrame.mylist = self.list

        # btn=Button(self,text="hello",command=self.getMultipleSelectedItems)
        # btn.grid(row=3,column=0)
        panier = ImageTk.PhotoImage(PIL.Image.open("pics/shop.png").resize((40, 40)))
        self.btn_ajouter_panier = ctk.CTkButton(self.frameNotif,text="Ajouter au panier",
                                                         image=panier, compound="bottom",
                                                        text_font=("Proxima Nova", 8, "bold"),
                                                         command=self.ajouterAuPanier)
        self.btn_ajouter_panier.grid(row=0,column=0)

    def afficherProduitsDepuisBD(self):
        # prod1 = Produit(2, "AZIX", 80.9, "AZERTOF", 60, 100, "Medicament", "", "3 fois par jours", "", "",
        #                 "emplacement2-5")
        # prod2 = Produit(3, "AZERO", 12, "AZERTOF", 98, 100, "Medicament", "", "3 fois par jours", "", "",
        #                 "emplacement2-5")
        # prod3 = Produit(4, "EBEHA", 123, "AZERTOF", 620, 100, "Medicament", "", "3 fois par jours", "", "",
        #                 "emplacement2-5")
        # prod4 = Produit(5, "ADTIMO", 811, "AZERTOF", 360, 100, "Medicament", "", "3 fois par jours", "", "",
        #                 "emplacement2-5")
        dao = Dao()

        listprods =dao.produits()
        self.setList(listprods)
        ProduitsFrame.mylist = self.list
    def afficherProduitsDepuis(self,listprods):
        self.list.destroy()
        self.creerListe()
        ProduitsFrame.mylist = self.list
        self.setList(listprods)
    def setList(self,listprods):
        for p in listprods:

            mylist = [p.id_produit, p.designation, p.type, p.prix, p.quantite,p.dosage, p.lot_num, p.uses]
            self.list.insert("", "end", values=mylist)
    def refreshList(self):
        self.list.destroy()
        self.creerListe()
        self.afficherProduitsDepuisBD()
    def creerListe(self):
        self.list = ttk.Treeview(self, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height=10)
        style = ttk.Style(self.list)
        style.configure('Treeview', rowheight=30)
        self.list.grid(row=2, column=0)
        self.list.heading('#0', text="")
        self.list.column("#0", minwidth=100, width=100, stretch=NO)
        self.list.heading('#1', text="ID")
        self.list.column("#1", minwidth=0, width=60, stretch=NO)
        self.list.heading('#2', text="Designation")
        self.list.column("#2", minwidth=0, width=150, stretch=NO)
        self.list.heading('#3', text="Type")
        self.list.column("#3", minwidth=0, width=150, stretch=NO)
        self.list.heading('#4', text="Prix")
        self.list.column("#4", minwidth=0, width=60, stretch=NO)
        self.list.heading('#5', text="qte")
        self.list.column("#5", minwidth=0, width=60, stretch=NO)
        self.list.heading('#6', text="dosage")
        self.list.column("#6", minwidth=0, width=80, stretch=NO)
        self.list.heading('#7', text="Emplacement")
        self.list.column("#7", minwidth=0, width=120, stretch=NO)
        self.list.heading('#8', text="utilisation")
        self.list.column("#8", minwidth=0, width=200, stretch=NO)
        self.list.bind('<ButtonRelease-1>', self.selectItem)

    #     create searchbar frame:

    def ajouterAuPanier(self):
        tupleE = ProduitsFrame.mylist.selection()

        if len(tupleE)>0:
            ProduitsFrame.myMenu.setBtnVendreEnabled()
            curItem = ProduitsFrame.mylist.focus()
            string = ProduitsFrame.mylist.item(curItem)
            idProd = string["values"][0]
            v = string["values"]
            qte = v[4]
            des = v[1]
            ok = 0
            qteAv=0
            if int(qte) >0:
                while ok == 0:
                    m = mainWindow(self.ourMaster, qte, des)
                    qteAv = m.entryValue()
                    if int(qteAv) > int(qte):
                        ok = 0
                        tk.messagebox.showerror(title="Attention !", message="veuillez ne pas depasser "
                                                                             "la qte maximale :" + str(qte))
                    else:
                        ok = 1

                if not self.verifierExistance(idProd, ProduitsFrame.listPanier):

                    id = v[0]
                    des = v[1]
                    type = v[2]
                    prix = v[3]

                    qte = v[4]
                    dosage = v[5]
                    lot = v[6]
                    uses = v[7]
                    desc = ""
                    soc = ""
                    prod = Produit(id, des, prix, soc, dosage, qte, type, desc, uses, "", "", lot)
                    prod.qteAvendre = qteAv
                    ProduitsFrame.listPanier.append(prod)
                    ProduitsFrame.selectedProds += 1
                    self.statusbar.destroy()
                    self.statusbar = tk.Label(self.frameNotif, text="" + str(ProduitsFrame.selectedProds))
                    self.statusbar.grid(row=0, column=2)
                else:
                    tk.messagebox.showerror(title="Attention !", message="Ce produit est deja ajoute dans le panier")
            else :
                tk.messagebox.showerror(title="Attention !", message="Ce produit n'est plus disponible sur le stock !")

        else :
            tk.messagebox.showerror(title="Attention !", message="Veuillez selectionner un produit")

    def verifierExistance(self,id,list):
        for i in list:
            if i.id_produit == id:
                return 1
        return 0


    def selectItem(event1=None,event2=None):
        ProduitsFrame.myMenu.setBtnModifyEnabled()
        ProduitsFrame.myMenu.setBtnDeleteEnabled()

        curItem =  ProduitsFrame.mylist.focus()
        string =  ProduitsFrame.mylist.item(curItem)
        v = string["values"]
        if len(v)>0:
            id = v[0]
            print(id)
            dao = Dao()
            p = dao.get_prod_by_id(int(id))
            ProduitsFrame.produitSelected = p
            print(p.designation)


    def getMultipleSelectedItems(event1=None,event2=None):
        tupleE= ProduitsFrame.mylist.selection()
        print("valeures selectionnees: "+str(len(tupleE)))
        for i in tupleE:
            print(ProduitsFrame.mylist.item(i))

    # def callDelete(self):
    def AllerVerVendreProds(list=None):
        ProduitsFrame.myMenu.afficherVendreProduitsFrame()
        x=10
        print(x)

