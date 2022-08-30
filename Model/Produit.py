import pymysql

class Produit:
    def __init__(self,id_produit,designation,prix,societe,dosage,quantite,type,description,uses,warnings,side_effects,lot_num):
        self.id_produit=id_produit 
        self.designation=designation
        self.prix=prix
        self.societe=societe
        self.dosage=dosage
        self.quantite=quantite
        self.type=type
        self.description=description
        self.uses=uses
        self.warnings=warnings
        self.side_effects=side_effects
        self.lot_num=lot_num



    def addProduct(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="pharmacie")
        cursor=con.cursor()
        req = "insert into produit (designation,prix,societe,dosage,quantite,type,description,uses,warnings,side_effects,lot_num) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        cursor.execute(req,(self.designation,float(self.prix),self.societe,self.dosage,int(self.quantite),self.type,self.description,self.uses,self.warnings,self.side_effects,int(self.lot_num)))
        con.commit()
        cursor.close()
        con.close()
    
