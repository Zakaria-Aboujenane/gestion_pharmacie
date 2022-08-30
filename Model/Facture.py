import pymysql

class Facture:

    def __init__(self,id_facture,montant):
        self.id_facture=id_facture
        self.montant=montant
           

    def addFacture(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="pharmacie")
        cursor=con.cursor()
        req = "insert into facture (montant) values(%s) "
        cursor.execute(req,(float(self.montant)))
        con.commit()
        cursor.close()
        con.close()
    def getLastFacture(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="pharmacie")
        cursor=con.cursor()
        req = "select id_facture from facture order by id_facture desc limit 1 "
        cursor.execute(req)
        res = cursor.fetchone()
        lastFactureId =  res[0]
        con.commit()
        cursor.close()
        con.close()
        return lastFactureId


