from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox
import numpy

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

TAM = 200
  
class Application:
    def __init__(self, master=None):
        self.master = master
        # Configuracoes padrao
        self.fontePadrao = ("Arial", "10")
        # Configuracoes padrao
    
        # Containeres Principais
        # sidebar
        self.sidebar = tkinter.Frame(master, bg='#CCC', height=520, relief='sunken', borderwidth=2)
        self.sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

        # main content area
        self.mainarea = tkinter.Frame(master, bg='white', width=460, height=520)
        self.mainarea.pack(expand=True, fill='both', side='right')        
        # /Containeres Principais
    
        # self.load = Image.open("problema.jpeg")
        # self.load = self.load.resize((390,199), Image.ANTIALIAS)
        
        aspect_ratio = 0.7
        img = Image.open('./problema.png')
        width, height = img.size
        img = img.resize((int(width*aspect_ratio), int(height*aspect_ratio)))

        self.render = ImageTk.PhotoImage(img)
        # self.render.subsample(10, 10)
        self.img = tkinter.Label(self.mainarea, image=self.render, height=300)
        self.img.image = self.render
        self.img.place(x=15, y=0)


        #### Campo 'gama Fluido'    
        self.containergamaFLuido = tkinter.Frame(self.sidebar)
        self.containergamaFLuido["width"] = 200
        self.containergamaFLuido.pack() 

        self.gamaFLuidoLabel = tkinter.Label(self.containergamaFLuido, width=23, text="yFluido (Kn/m3)", font=self.fontePadrao)
        self.gamaFLuidoLabel.pack(side=tkinter.LEFT)

        self.gamaFLuido = tkinter.Entry(self.containergamaFLuido, width=10)
        self.gamaFLuido["font"] = self.fontePadrao
        self.gamaFLuido.pack(side=tkinter.LEFT)
        #### /Campo 'gama Fluido'  


        #### Campo 'Altura da Barragem'    
        self.containerAlturaBarragem = tkinter.Frame(self.sidebar)
        self.containerAlturaBarragem["width"] = 200
        self.containerAlturaBarragem.pack() 

        self.AlturaBarragemLabel = tkinter.Label(self.containerAlturaBarragem, width=23, text="Altura (h)", font=self.fontePadrao)
        self.AlturaBarragemLabel.pack(side=tkinter.LEFT)

        self.AlturaBarragem = tkinter.Entry(self.containerAlturaBarragem, width=10)
        self.AlturaBarragem["font"] = self.fontePadrao
        self.AlturaBarragem.pack(side=tkinter.LEFT)
        #### /Campo 'Altura da Barragem'  



        #### Campo 'Comprimento da Barragem'    
        self.containerComprimentoBarragem = tkinter.Frame(self.sidebar)
        self.containerComprimentoBarragem["width"] = 200
        self.containerComprimentoBarragem.pack() 

        self.ComprimentoBarragemLabel = tkinter.Label(self.containerComprimentoBarragem, width=23, text="Comprimento (L)", font=self.fontePadrao)
        self.ComprimentoBarragemLabel.pack(side=tkinter.LEFT)

        self.ComprimentoBarragem = tkinter.Entry(self.containerComprimentoBarragem, width=10)
        self.ComprimentoBarragem["font"] = self.fontePadrao
        self.ComprimentoBarragem.pack(side=tkinter.LEFT)
        #### /Campo 'Comprimento da Barragem'  
       



        #### Botao calcular
        self.containerCalcular = tkinter.Frame(self.sidebar)
        self.containerCalcular.pack() 

        self.calcular = tkinter.Button(self.containerCalcular)
        self.calcular["text"] = "Calcular"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.calcularValores
        self.calcular.pack()
        #### /Botao calcular

        #### Label LabelX
        self.LabelX = tkinter.Label(master, text="? metros", width=12, height=1)
        self.LabelX.place(x=508, y=17)
        #### /Label LabelX

        #### Label LabelF
        self.LabelF = tkinter.Label(master, text="= ?", width=12, height=1)
        self.LabelF.place(x=414, y=182)
        #### /Label LabelF

        #### Label labelEqF01
        self.LabelEqF01 = tkinter.Label(master, text="F = (y * h2 * L) * 0.5", width=26, height=2)
        self.LabelEqF01.place(x=260, y=310)
        #### /Label labelEqF01

        #### Label labelEqX01 ((gamaFluido / 72) * altura ) ** (1/2)  
        self.LabelEqX01 = tkinter.Label(master, text="x = RAIZ( y * 72.000 * h )", width=26, height=2)
        self.LabelEqX01.place(x=485, y=310)
        #### /Label labelEqX01
     

        messagebox.showinfo("Bem-vindo","Preencha os campos do lado esquerdo e clique em calcular para rodar o programa!")
   
    def calcularValores (self):
        try:
            gamaFluido = float(self.gamaFLuido.get())
            altura = float(self.AlturaBarragem.get())
            comprimento = float(self.ComprimentoBarragem.get())
        except:
            messagebox.showerror("Erro!", "Digite Corretamente os campos")
            return
          
        forcaAgua = round((gamaFluido * (altura**2) * comprimento) / 2, 3)

        x = round(((gamaFluido / 72) * altura ) ** (1/2), 3)      

       
        self.LabelF['text'] = "= "+str(forcaAgua/1000) + "KN"
        self.LabelX['text'] = str(x) + " metros"

        #### Label labelEqF02 F = (y * h2 * L) * 0.5
        try:
            self.LabelEqF02['text'] = "F = ({} * {}^2 * {}) * 0.5".format(gamaFluido, altura, comprimento)
        except:
            self.LabelEqF02 = tkinter.Label(self.master, text="F = ({} * {}^2 * {}) * 0.5".format(gamaFluido, altura, comprimento), width=26, height=2)
            self.LabelEqF02.place(x=260, y=355)


        #### Label labelEqF03
        try:
            self.LabelEqF03['text'] = "F = {}".format(forcaAgua)
        except:
            self.LabelEqF03 = tkinter.Label(self.master, text="F = {}".format(forcaAgua), width=26, height=2)
            self.LabelEqF03.place(x=260, y=400) 
        #### /Label labelEqF02


        #### Label labelEqX02 ((gamaFluido / 72) * altura ) ** (1/2) 
        try:
            self.LabelEqX03['text'] = "x = RAIZ( {} * 72.000 * {} )".format(gamaFluido, altura)
        except:
            self.LabelEqX02 = tkinter.Label(self.master, text="x = RAIZ( {} * 72.000 * {} )".format(gamaFluido, altura), width=26, height=2)
            self.LabelEqX02.place(x=485, y=355)
        #### /Label labelEqX02


        #### Label labelEqX03 ((gamaFluido / 72) * altura ) ** (1/2) 
        try:
            self.LabelEqX03['text'] = "x = {}".format(x)
        except:
            self.LabelEqX03 = tkinter.Label(self.master, text="x = {}".format(x), width=26, height=2)
            self.LabelEqX03.place(x=485, y=400)
        #### /Label labelEqX03 

root = tkinter.Tk()
Application(root)
root.mainloop()
