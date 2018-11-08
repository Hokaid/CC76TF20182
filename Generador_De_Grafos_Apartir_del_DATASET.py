import random
import math

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def LeerCapital(filename, numero_nodos):
    Capitales = [0]*numero_nodos
    file = open(filename)
    k = 0
    i = 0
    for line in file:
        if (k == 0):
            k = k + 1
        else:
            if (is_float(line)):
                Capitales[i] = int(line)
                i = i + 1
                print("estoy en capita: " + str(i))
    return Capitales

def LeerPosiciones_Criterio(filename, numero_nodos, Capitales, Criterio):
    Posiciones = [0]*2*numero_nodos
    pr = 0
    file = open(filename)
    i = 0
    k = 0
    for line in file:
        r = 0
        for j in line.split('-'):
            if (is_float(j)):
                if Capitales[k] == Criterio:
                    pr = float(j)
                    Posiciones[i] = pr
                    i = i + 1
                    print("estoy en posiciones: " + str(i))
                r = r + 1
                if (r == 2):
                    k = k + 1
    return Posiciones

def LeerPosiciones(filename, numero_nodos):
    Posiciones = [0]*2*numero_nodos
    pr = 0
    file = open(filename)
    i = 0
    for line in file:
        for j in line.split('-'):
            if (is_float(j)):
                pr = float(j)
                Posiciones[i] = pr
                i = i + 1
        print(i)
    return Posiciones

                            

def Isin(Arr, k):
  for x in Arr:
    if(k==x):
      return True
  return False

def CrearGrafo(Posiciones, numero_nodos):
  G = [[]]*numero_nodos
  Y = [0]*2
  for i in range(numero_nodos):
    A = [(0,0)]*2
    for j in range(2):
      u = random.randint(0,numero_nodos-1)
      while Isin(Y,u):
        u = random.randint(0,numero_nodos-1)
      w = math.sqrt(((Posiciones[2*u+1]-Posiciones[2*i+1])**2)+((Posiciones[2*u]-Posiciones[2*i])**2))
      if (u != i):
          Y[j] = u
          A[j] = (w,u)
    T = []
    for e in range(len(A)):
        if (A[e] != (0,0)):
            T.append(A[e])
    G[i] = T
    print("Estoy en crear grafo: " + str(i))
  return G

def ISin(Arr, b):
    (w,u) = b
    for k in range(len(Arr)):
        (x,y) = Arr[k]
        if(w==x)and(u==y):
            return False
        elif(u==y)and(x!=0):
            Arr.pop(k)
    return True

def Convertir_A_Grafo_No_Dirigido(G):
  u = 0
  for V in G:
    for w, v in V:
        if ((w,v) != (0,0)) and ISin(G[v],(w,u)):
            G[v].append((w,u))
    u += 1
    print("Estoy en Convertir a grafo no dirigido: " + str(u))
  return G

def EscribirGrafo(G, newfilename):
    f = open(newfilename, "w")
    for V in G:
        i = 0
        for v,w in V:
            if (i == len(V)-1):
                f.write(str(v) + "," + str(w))
            else:
                f.write(str(v) + "," + str(w) + " ")
            i = i + 1
        f.write("\n")

                                                                                                                                                                                      
def GenerarGrafo_conCriterio(filename, filecapita, numero_nodos, numero_capita, criterio, newfilename): #Esta función permite generar los grafos de regiones capitales regionales, provinciales y distritales
    EscribirGrafo(Convertir_A_Grafo_No_Dirigido(CrearGrafo(LeerPosiciones_Criterio(filename, numero_nodos,
                                                                                   LeerCapital(filecapita, numero_capita), criterio),numero_nodos)), newfilename)
def GenerarGrafoCompletoCP(filename, numero_nodos, newfilename): #Esta función permite generar el grafo completo con todos los centros poblados
    EscribirGrafo(Convertir_A_Grafo_No_Dirigido(CrearGrafo(LeerPosiciones(filename, numero_nodos),numero_nodos)), newfilename)
#GenerarGrafoCompletoCP("Prueva.txt", 14, "Ray2.txt")
#GenerarGrafo_conCriterio("Prueva.txt", "Prueva2.txt", 5, 14, 1, "Ray.txt")                                                                                                                                             



#!IMPORTANTE!: Descomente el siguiente codigo si desea probar como se genera el grafo de 25 capitales regionales a partir del Dataset, tomara unos 2 minutos
"""
GenerarGrafo_conCriterio("Cordenadas_de_CentrosPoblados_Obtenido_del_Dataset.txt","AtributoCapital_de_CentrosPoblados_Obtenido_del_Dataset.txt", 25, 145225, 1, "Grafo_25_Capitales_Regionales.txt")
"""

#!IMPORTANTE!: Descomente el siguiente codigo si desea probar como se genera el grafo de 171 capitales provinciales a partir del Dataset, tomara unos 5 minutos
"""
GenerarGrafo_conCriterio("Cordenadas_de_CentrosPoblados_Obtenido_del_Dataset.txt","AtributoCapital_de_CentrosPoblados_Obtenido_del_Dataset.txt", 171, 145225, 2, "Grafo_171_Capitales_Provinciales.txt")
"""

#!IMPORTANTE!: Descomente el siguiente codigo si desea probar como se genera el grafo de 1678 capitales distritales a partir del Dataset, tomara unos 10 minutos
"""
GenerarGrafo_conCriterio("Cordenadas_de_CentrosPoblados_Obtenido_del_Dataset.txt","AtributoCapital_de_CentrosPoblados_Obtenido_del_Dataset.txt",1678, 145225, 3, "Grafo_1678_Capitales_Distritales.txt")
"""

#!IMPORTANTE!: Descomente el siguiente codigo si desea probar como se genera el grafo completo con los 145225 centros poblados del Dataset, tomara unos 20 minutos
"""
GenerarGrafoCompletoCP("Cordenadas_de_CentrosPoblados_Obtenido_del_Dataset.txt",145225,"Grafo_145225_CentrosPoblados.txt")
"""

#!IMPORTANTE!: Descomente el siguiente codigo si desea probar como se genera el grafo de 75512 centros educativos, tomara unos 13 minutos
"""
GenerarGrafoCompletoCP("Cordenadas_de_CentrosEducativos_Obtenido_del_Dataset.txt",75512,"Grafo_75512_CentrosEducativos.txt")
"""







    
    
