from tkinter import *
import sys
class popupWindow(object):
    def __init__(self,master,value,name):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Veuillez specifier la quantite a vendre du produit "+str(name)+" (! ne depassez pas "+str(value)+")")
        self.l.pack()
        self.e=Entry(top)
        self.value=0
        self.e.pack(pady=20,padx=20)
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master,value,name):
        self.n = name
        self.v = value
        self.master=master
        self.popup()

    def popup(self):
        self.w=popupWindow(self.master,self.v,self.n)

        self.master.wait_window(self.w.top)


    def entryValue(self):
        return self.w.value