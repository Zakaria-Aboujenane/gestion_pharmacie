import tkinter
import customtkinter as ctk
from PIL import ImageTk
import PIL.Image
from AjoutProduitFrame import AjoutProduitFrame
from ModifierProduitFrame import ModifierProduitFrame
from ProduitsFrame import *
import customtkinter  # <- import the CustomTkinter module

from VendreFrame import VendreFrame


class MenuFrame(ctk.CTkFrame):

    def __init__(self, master, w, borderC, tick):
        self.ajoutP = AjoutProduitFrame(master, 200,self)
        p= Produit(3, "AZERO", 12, "AZERTOF", 98, 100, "Medicament", "", "3 fois par jours", "", "",
                        "emplacement2-5")
        self.modifP = ModifierProduitFrame(master, 200, self, p)

        self.prodsF = ProduitsFrame(master, 600, self)

        ctk.CTkFrame.__init__(self, master, width=w,fg_color="white")
        self.ourMaster = master

        # search bar :
        self.searchFrame = ctk.CTkFrame(self, self,bg_color="white",fg_color="white")
        pic_bar_rech = ImageTk.PhotoImage(PIL.Image.open("pics/search.png").resize((32, 32)))
        self.btn_bar_recherche = customtkinter.CTkButton(self.searchFrame, text="",
                                                         image=pic_bar_rech, compound="left",
                                                         corner_radius=30,
                                                         bg_color="white",fg_color="white",
                                                         width=40,
                                                         command=self.rechercherProd)
        self.bar_recherche = customtkinter.CTkEntry(self.searchFrame,
                               width=200,
                               height=25,
                               fg_color="#29b57e",
                               text_color="Black",
                               corner_radius=2)
        self.bar_recherche.grid(row=0,column=0,padx=2)
        self.btn_bar_recherche.grid(row=0,column=1)




        # creating images :
        mediamentImg = ImageTk.PhotoImage(PIL.Image.open("pics/pharmacy.png").resize((32, 32)))
        addIMG = ImageTk.PhotoImage(PIL.Image.open("pics/plus.png").resize((32, 32)))
        sell = ImageTk.PhotoImage(PIL.Image.open("pics/online-shopping.png").resize((32, 32)))
        update = ImageTk.PhotoImage(PIL.Image.open("pics/update.png").resize((32, 32)))
        delete = ImageTk.PhotoImage(PIL.Image.open("pics/remove.png").resize((32, 32)))
        Logo = ImageTk.PhotoImage(PIL.Image.open("pics/logoPh.png").resize((40,50)))

        # buttons :
        self.btnLogo = customtkinter.CTkButton(self,text="Pharmacie ZAHM",
                                               text_font=("Proxima Nova", 8, "bold"),
                                               image=Logo,compound="top",
                                               bg_color="white",fg_color="white",hover_color="white")
        self.btn_produitsFrame = customtkinter.CTkButton(self, text="liste des Produits",
                                                         image=mediamentImg, compound="left",
                                                         command=self.afficherListProduitsFrame)
        self.btn_ajoutProduitFrame = customtkinter.CTkButton(self, text="Ajouters",
                                                             image=addIMG,compound="left",
                                                             command=self.afficherAjoutProdFrame)
        self.btn_vendreProduitFrame = customtkinter.CTkButton(self, text="Vendre",
                                                              image=sell,compound="left",
                                                              command=self.afficherVendreProduitsFrame)
        self.btn_modifierProduitFrame = customtkinter.CTkButton(self, text="Modifier",
                                                                image=update,compound="left",
                                                                command=self.afficherModifierProduitsFrame)
        self.btn_supprimerProduitFrame = customtkinter.CTkButton(self, text="Supprimer",
                                                                image=delete,compound="left",
                                                                 command=self.supprimerCeProd)
        allBtns = [self.btn_produitsFrame, self.btn_ajoutProduitFrame,
                   self.btn_vendreProduitFrame,
                   self.btn_modifierProduitFrame,self.btn_supprimerProduitFrame]
        # configure buttons:
        for But in allBtns:
            But.config(height=10, width=35)

        # packing:
        self.btnLogo.grid(row=0,column=0,padx=10,pady=20)
        self.btn_produitsFrame.grid(row=0, column=1, padx=5, pady=10)
        self.btn_ajoutProduitFrame.grid(row=0, column=2, padx=5, pady=10)
        self.btn_vendreProduitFrame.grid(row=0, column=3, padx=5, pady=10)
        self.btn_modifierProduitFrame.grid(row=0, column=4, padx=5, pady=10)
        self.btn_supprimerProduitFrame.grid(row=0, column=5, padx=5, pady=10)
        self.searchFrame.grid(row=0,column=6,padx=5,pady=10)
        # principal frames:

        self.prodsF = ProduitsFrame(self.ourMaster, 200,self)
        ProduitsFrame.myMenu = self
        self.ajoutP = AjoutProduitFrame(self.ourMaster, 200,self)
        self.ajoutP.setMenuFrame()
        self.vendreF = VendreFrame(ProduitsFrame.MasterPage,  ProduitsFrame.listPanier)

        # ProduitsFrame.setMenuF(self)


        # setting frames:
        self.prodsF.grid(row=1, column=0, padx=5, pady=10)
        self.prodsF.isOn = 1

        self.ajoutP.isOn = 0

        self.listFrames = [self.prodsF, self.ajoutP]
        self.setBtnDisabled(self.btn_modifierProduitFrame)
        self.setBtnDisabled(self.btn_vendreProduitFrame)
        self.setBtnDisabled(self.btn_supprimerProduitFrame)
        ProduitsFrame.myMenu = self

    def rechercherProd(self):
        mot_cle = self.bar_recherche.get()
        if mot_cle != "":
            dao = Dao()
            newL = dao.search_prd(mot_cle)
            for l in newL:
                print(l)
            self.prodsF.afficherProduitsDepuis(newL)
        else:
            tkinter.messagebox.showerror(title="recherche vide !", message="vous n avez rien ecrit")



    def afficherListProduitsFrame(self):

        self.destroyAllF()
        self.prodsF = ProduitsFrame(self.ourMaster, 600,self)
        self.prodsF.isOn = 1
        self.prodsF.grid(row=1, column=0, padx=5, pady=10)

    def afficherVendreProduitsFrame(self):
        self.setBtnDisabled(self.btn_modifierProduitFrame)
        self.setBtnDisabled(self.btn_vendreProduitFrame)
        self.setBtnDisabled(self.btn_supprimerProduitFrame)
        if len(ProduitsFrame.listPanier)>0:
            self.destroyAllF()
            self.vendreF = VendreFrame(ProduitsFrame.MasterPage, ProduitsFrame.listPanier)
            print("oui ?")
            self.vendreF.isOn = 1
            self.vendreF.grid(row=1, column=0, padx=5, pady=10)
        else :
            tkinter.messagebox.showerror(title="panier vide", message="le panier est vide")


    def afficherAjoutProdFrame(self):
        self.setBtnDisabled(self.btn_modifierProduitFrame)
        self.setBtnDisabled(self.btn_vendreProduitFrame)
        self.setBtnDisabled(self.btn_supprimerProduitFrame)
        print("ajouter a la list prods")
        self.destroyAllF()
        self.ajoutP = AjoutProduitFrame(self.ourMaster, 600,self)
        self.ajoutP.isOn = 1
        self.ajoutP.grid(row=1, column=0, padx=5, pady=10)
    def afficherModifierProduitsFrame(self):
        self.setBtnDisabled(self.btn_modifierProduitFrame)
        self.setBtnDisabled(self.btn_vendreProduitFrame)
        self.setBtnDisabled(self.btn_supprimerProduitFrame)
        if ProduitsFrame.produitSelected != None:
            print("modifier a la list prods")
            self.destroyAllF()
            self.modifP = ModifierProduitFrame(self.ourMaster, 200, self, ProduitsFrame.produitSelected)
            self.modifP.isOn = 1
            self.modifP.grid(row=1, column=0, padx=5, pady=10)
        else:
            tkinter.messagebox.showerror(title="pas de produits", message="Aucun produit selectionne")

    def supprimerCeProd(self):
        p = ProduitsFrame.produitSelected
        if p !=None:
            MsgBox = tkinter.messagebox.askquestion('Supression du produit ' + str(p.id_produit),
                                                    'Est ce que vous etes sur de supprimer le produit '
                                                    + str(p.designation),
                                                    icon='warning')
            if MsgBox == 'yes':
                dao = Dao()
                dao.delete_prd(p.id_produit)
                self.prodsF.refreshList()
            else:
                tkinter.messagebox.showinfo('retourner', 'Votre produit ne sera pas supprime')
        else :
            tkinter.messagebox.showerror(title="pas de produits", message="Aucun produit selectionne")

    def AllerVersVendre(self):
      ProduitsFrame.AllerVerVendreProds()

    def destroyAllF(self):
        print("pour ajout Prod : " + str(self.ajoutP.isOn))
        print("pour list Prod : " + str(self.prodsF.isOn))
        if self.ajoutP.isOn:
            self.ajoutP.destroy()
            self.ajoutP.isOn = 0
        elif self.prodsF.isOn:
            self.prodsF.destroy()
            self.prodsF.isOn = 0
        elif self.vendreF.isOn:
            self.vendreF.destroy()
            self.vendreF.isOn = 0
        elif self.modifP.isOn:
            self.modifP.destroy()
            self.modifP.isOn=0

    def setBtnDisabled(self,Btn):
        Btn.state=DISABLED
        Btn.bg_color="RED"
        Btn.hover_color="RED"
        Btn.fg_color="RED"

    def setBtnModifyEnabled(self):
        self.EnableButton(self.btn_modifierProduitFrame)
    def setBtnDeleteEnabled(self):
        self.EnableButton(self.btn_supprimerProduitFrame)
    def setBtnVendreEnabled(self):
        self.EnableButton(self.btn_vendreProduitFrame)


    def EnableButton(self,Btn):
        Btn.state = NORMAL
        Btn.bg_color = "white"
        Btn.hover_color = "#29b57e"
        Btn.fg_color = "#29b57e"



