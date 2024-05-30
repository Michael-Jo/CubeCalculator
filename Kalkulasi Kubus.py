import tkinter as tk
import ttkbootstrap as tb
import math
# Penghitung kubus
class Kubus:
    def __init__(self, master):
        self.master = master
        master.maxsize(2000, 1000)
        
        self.kiriFramee  =  tb.Frame(master,  width=200,  height=  400)
        self.kiriFramee.pack(side='left',  fill='both',  padx=10,  pady=5,  expand=True)

        self.kananFramee  =  tb.Frame(master,  width=800,  height=400)
        self.kananFramee.pack(side='right',  fill='both',  padx=10,  pady=5,  expand=True)

        self.kiriFm = tb.Label(self.kiriFramee,  text="Mini Image", font=("arial", 20))
        self.kiriFm.pack(side='top',  padx=5,  pady=5)
        self.images  =  tb.PhotoImage(file=r"image/kubus.png")
        self.miniImg  =  self.images.subsample(3,3)
        self.imgKiri = tb.Label(self.kiriFramee,  image=self.miniImg)
        self.imgKiri.pack(fill='both',  padx=5,  pady=5)

        self.imgKanan = tb.Label(self.kananFramee, image=self.images)
        self.imgKanan.pack(fill='both',  padx=5,  pady=5)

        self.menus  =  tb.Frame(self.kiriFramee,  width=400,  height=185)
        self.menus.pack(side='left',  fill='both',  padx=5,  pady=5)

        self.filter_menus  =  tb.Frame(self.kiriFramee,  width=90,  height=185)
        self.filter_menus.pack(side='left',  fill='both',  padx=5,  pady=5,  expand=True)

        #input = sisi
        self.sisi = tb.IntVar()

        LABELluas = tb.Label(self.menus,  text="Mencari Luas Permukaan dan Volume", font=("arial", 10, 'bold'))
        LABELluas.pack(anchor='w',  padx=5,  pady=3,  ipadx=10)

        LABELsisi = tb.Label(self.filter_menus,  text="Sisi Kubus", font=("arial", 10, 'bold'))
        # LABELpanjang = tb.Label(self.menus,  text="PANJANG", font=("arial", 10, 'italic'))
        LABELsisi.pack(padx=5,  pady=5)
        FORMsisi = tb.Entry(self.filter_menus,  textvariable= self.sisi)
        FORMsisi.pack(padx=5,  pady=5)

        # LABELlebar = tb.Label(self.menus,  text="LEBAR", font=("arial", 10, 'italic'))
        # LABELlebar.pack(padx=5,  pady=5)
        # FORMlebar = tb.Entry(self.filter_menus,  textvariable= self.lebar)
        # FORMlebar.pack(padx=5,  pady=5)


        tb.Button(self.menus,  text="Cari Luas Permukaan",  command=self.CariLP).pack(anchor='e',  padx=5,  pady=58,  ipadx=10)
        tb.Button(self.menus,  text="Cari Volume",  command=self.CariVolume).pack(anchor='e', padx=5,  pady=10)
        tb.Button(self.filter_menus,  text="Cari Diagonal Sisi",  command=self.CariDS).pack(anchor='w', padx=5,  pady=10)
        tb.Button(self.filter_menus,  text="Cari Disagonal Ruang",  command=self.CariDR).pack(anchor='w', padx=5,  pady=58)
    def CariLP(self):
        self.imgKanan.config(image='', text=f"Hasil Luas Permukaan ({self.sisi.get()}) = {self.sisi.get() * self.sisi.get() * 6}", font=("arial", 25), foreground="white")
    def CariVolume(self):
        self.imgKanan.config(image='', text=f"Hasil Volume ({self.sisi.get()}) = {self.sisi.get() * self.sisi.get()* self.sisi.get()}", font=("arial", 25), foreground="white")
    def CariDS(self):
        self.imgKanan.config(image='', text=f"Hasil Diagonal Sisi ({self.sisi.get()}) = {self.sisi.get() * math.sqrt(2)}", font=("arial", 25), foreground="white")
    def CariDR(self):
        self.imgKanan.config(image='', text=f"Hasil Diagonal Ruang ({self.sisi.get()}) = {self.sisi.get() * math.sqrt(3)}", font=("arial", 25), foreground="white")

if __name__ == "__main__":
    root  =  tb.Window(themename="superhero")
    Kubus(root)

    root.mainloop()