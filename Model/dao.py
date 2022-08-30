from Model.Facture import Facture
from Model.Produit import *


class Dao:
    def __init__(self):
        self.con = pymysql.connect(host="localhost",user="root",password="",database="pharmacie")

    def produits(self):
        cursor=self.con.cursor()
        req = "select * from produit"
        cursor.execute(req)
        res = cursor.fetchall()
        liste = []
        for ligne in res:
            p=Produit(ligne[0],ligne[1],ligne[4],ligne[3],ligne[5],ligne[6],ligne[7],ligne[2],ligne[8],ligne[9],ligne[10],ligne[11])
            liste.append(p)
        self.con.commit()
        cursor.close()   
        return liste

    def get_prod_by_id(self, id):
        cursor = self.con.cursor()
        req = "select * from produit WHERE product_id=" + str(id)
        cursor.execute(req)
        ligne = cursor.fetchone()
        p = Produit(ligne[0], ligne[1], ligne[4], ligne[3], ligne[5], ligne[6], ligne[7], ligne[2], ligne[8],
                    ligne[9], ligne[10], ligne[11])
        self.con.commit()
        cursor.close()
        return p

    def modifier_prd(self,prd):
        cursor=self.con.cursor()
        req = "UPDATE `produit` SET `designation`=%s,`description`=%s,`societe`=%s,`prix`=%s,`dosage`=%s,`quantite`=%s,`type`=%s,`uses`=%s,`side_effects`=%s,`warnings`=%s,`lot_num`=%s WHERE `product_id`=%s"
        cursor.execute(req,(prd.designation,prd.description,prd.societe,float(prd.prix),prd.dosage,int(prd.quantite),prd.type,prd.uses,prd.side_effects,prd.warnings,int(prd.lot_num),int(prd.id_produit)))
        self.con.commit()
        cursor.close()
    def delete_prd(self,prd_id):
        cursor=self.con.cursor()
        req = "DELETE FROM `produit`  WHERE `product_id`=%s"
        cursor.execute(req,(int(prd_id)))
        self.con.commit()
        cursor.close()
    def search_prd(self,value):
        cursor=self.con.cursor()
        req = "select * from produit where product_id LIKE '%" + value + "%' " \
                                                                        "or designation LIKE '%" + value + "%' or societe LIKE '%" + value + "%'"
        print(req)
        cursor.execute(req)
        res = cursor.fetchall()
        liste = []
        for ligne in res:
            p=Produit(ligne[0],ligne[1],ligne[4],ligne[3],ligne[5],ligne[6],ligne[7],ligne[2],ligne[8],ligne[9],ligne[10],ligne[11])
            liste.append(p)
        self.con.commit()
        cursor.close()   
        return liste
        
    def addVente(self,listp):
        cursor=self.con.cursor()
        req = "insert into produit_facture values (%s,%s,%s)"
        montant = 0
        for ligne in listp:
            print("on a qte a vendre : "+str(ligne.qteAvendre))
            print("du produit : "+str(ligne.id_produit))
            montant = montant + float(ligne.prix)*int(ligne.qteAvendre)
        f = Facture(1,montant)
        f.addFacture()
        Facture_id=f.getLastFacture()
        for ligne in listp:
            cursor.execute(req,(ligne.id_produit,Facture_id,ligne.qteAvendre))
            self.con.commit
        cursor.close



# p =  Produit(1,'test','test','test',252,'10M',100,'test','yesy','yesy','ee',56)
# p =  Produit(3,'test','test','test',252,'10M',100,'test','yesy','yesy','ee',56)
#
# p.addProduct()
# d = Dao()
# d.modifier_prd(p)
# d.delete_prd(1)
# listp = d.search_prd('test')
# for ligne in listp:
#     print(ligne.designation ,ligne.id_produit)
