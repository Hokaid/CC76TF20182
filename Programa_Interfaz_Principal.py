from LectorDeGrafo import *
from tkinter import *
from tkinter import messagebox
from Algoritmo_Basado_Dijkstra import *

def is_file(value):
  try:
    file = open(value)
    return True
  except:
    return False

def abrir_ventana2():
    ventanap.withdraw()
    ventana = Toplevel()
    ventana.geometry("800x400")
    imagen = PhotoImage(file="Imagenes\\mape.gif")
    ventana.title("Algorithms_TSP")
    fondo = Label(ventana, image=imagen).place(x=0,y=0)
    boton = Button(ventana,text="Iniciar ejecución",command=Ir_A_Algoritmo).place(x=280,y=330)
    etiquetaTitulo = Label(ventana, text="TRAVEL SALESMAN PROBLEM (ALGORITMOS DE SOLUCIÓN)",bg="#FF4500",fg="#FFF",borderwidth=5).place(x=250, y= 30)
    etiCiudad = Label(ventana, text="Cantidad de ciudades visistadas:",bg="#FFFF00",fg="#000000").place(x=450,y=130)
    cCiudad=Entry(ventana,textvariable=ciudad).place(x=450,y=160)
    etiPeso = Label(ventana, text="Distancia recorrida en la solución encontrada(Km):",bg="#00FFFF",fg="#000").place(x=450,y=190)
    cPeso=Entry(ventana,textvariable=peso).place(x=450,y=220)
    etiSoluP = Label(ventana, text="Porcentaje de la solución:",bg="purple",fg="#FFF").place(x=450,y=250)
    cSoluP = Entry(ventana,textvariable=solup).place(x=450,y=280)
    etiNiter = Label(ventana, text="Numero de iteraciónes realizadas aprox (tiempo):",bg="#00FF66",fg="#000").place(x=450,y=310)
    cNiter = Entry(ventana,textvariable=iters).place(x=450,y=340)
    ArchivoT = Label(ventana, text="Indique el nombre y/o dirección del archivo: ",bg="#009900",fg="#FFF").place(x=50,y=130)
    ArchivoT = Spinbox(ventana, values=("Grafo_25_Capitales_Regionales.txt","Grafo_171_Capitales_Provinciales.txt"
                                        ,"Grafo_1678_Capitales_Distritales.txt","Grafo_145225_CentrosPoblados.txt"
                                        ,"Grafo_Pequeño_Prueva.txt"),textvariable=archivot,width=35).place(x=50,y=160)
    origenes = Label(ventana, text="Ingrese el codigo del lugar en el que desee iniciar el viaje: ",bg="#DC143C",fg="#FFF").place(x=50,y=190)
    origenes =Spinbox(ventana, from_=0,to=145225,textvariable=originNode).place(x=50,y=220)
    cMetodo = Label(ventana, text="Por favor seleccióne el algoritmo a utilizar:  ",bg="#4169E1",fg="#FFF").place(x=50,y=250)
    metodo = Spinbox(ventana, values=("Alg. Basado en Dijkstra","Alg. Basado en Greedy"), textvariable = estrategia,width=22).place(x=50,y=280)
    EtiInput = Label(ventana, text="INGRESO DE DATOS",bg="#40E0D0",fg="#000").place(x=120,y=85)
    EtiOutput = Label(ventana, text="VISUALIZACIÓN DE RESULTADOS",bg="#66FF00",fg="#000").place(x=500,y=85)
    for i in range(14):
      EtiInput = Label(ventana, text="",bg="#2F4F4F").place(x=400,y=90 + (i*20))
    ventana.mainloop()

def Ir_A_Algoritmo():
    if (is_file(archivot.get())):
        messagebox.showwarning
        G = LeeGrafo(archivot.get())
        if (originNode.get() < len(G)):
            if (estrategia.get() == "Alg. Basado en Dijkstra"):
              Ejecutar_Alg_Basado_Dikjstra(G,originNode.get(),ciudad,peso,solup,iters)
            elif (estrategia.get() == "Alg. Basado en Greedy"):
              print("ptmre")
            else:
              messagebox.showwarning("Algoritmo Inadecuada","Por favor indique un algoritmo a ejecutar valido")
        else:
            messagebox.showwarning("Codigo Incorrecto","Por favor indique un codigo de lugar valido")
    else:
        messagebox.showwarning("Archivo Incorrecto","Por favor ingrese el nombre de un archivo valido")

ventanap = Tk()
ciudad = StringVar()
peso = StringVar()
solup = StringVar()
archivot = StringVar()
estrategia = StringVar()
iters = StringVar()
originNode = IntVar()
archivot.set("Grafo_25_Capitales_Regionales.txt")
ventanap.geometry("500x300")
ventanap.title("Program_TSP")
imagen1 = PhotoImage(file="Imagenes\\mapi.gif")
fondo1 = Label(ventanap, image=imagen1).place(x=0,y=0)
Titulo = Label(ventanap, text="TRAVEL SALESMAN PROBLEM (Posibles soluciones)",
                 bg="#ADFF2F",fg="#000066",borderwidth=10).place(x=100,y=100)
Option = Label(ventanap, text="Seleccione el siguiente botón para comenzar :",
                 fg="#CCCCFF",bg="#990099").place(x=130,y=170)
botonA1 = Button(ventanap,text="Iniciar Prueva de los algoritmos",command=abrir_ventana2).place(x=156,y=200)
ventanap.mainloop()
