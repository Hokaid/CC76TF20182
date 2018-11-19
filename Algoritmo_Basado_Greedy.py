import math
import copy

def HayCamino(Grafo, NodosVisitados):
    for d, K in Grafo:
        if not NodosVisitados[K]:
            return True
        
    return False

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def str2pair(x):
    nums = x.split(',')
    if (is_float(nums[0])):
        peso = float(nums[0])
        llegada = int(nums[1])
        return peso, llegada

def LeeGrafo(filename):
    G = []
    file = open(filename)
    for line in file:
        G.append([str2pair(x) for x in line.split(' ')])
        
    return G

def DeterminarNodosRecorridos(Grafo, NodosVisitados):
    
    Contador = 0
    
    for K in range(len(Grafo) - 1):
        if not NodosVisitados[K]:
            Contador += 1
            
    if Contador == 0:
         return False
    else:
        return True
         

def Greedy(Grafo, NodosVisitados, numero_de_iteraciones):

    MenorPeso = 10000000000
    N = 0
    for Peso, Nodo in Grafo:
        numero_de_iteraciones[0] = numero_de_iteraciones[0] + 1
        if Peso < MenorPeso and not NodosVisitados[Nodo]:
            MenorPeso = Peso
            N = Nodo

    if MenorPeso == 10000000000:
        MenorPeso = 0
    
    return MenorPeso, N



def BackTraking(Grafo, NroNodos, NodoInicial, Nodo, NodosVisitados, Profundidad, numero_de_iteraciones):
    if 1000 >= len(Grafo):
        # -- Crear copia de nodos visitidos
        NodosVisitadosAux = copy.copy(NodosVisitados)

        # -- Marcar Nodo de proceso como visitado
        NodosVisitadosAux[Nodo] = True
      
        # -- Iniciar proceso de recorrido de nodos
        Nodos = Grafo[Nodo]    
        # -- Crear un diccionario para llevar el control de nodos recorridos    
        MenorPeso = math.inf
        MenorCamino = []
        MenorNodo = []

        # -- Determinar el vecino mas cercano al 'Nodo' y su respectivo peso
        u, v = Greedy(Nodos, NodosVisitadosAux, numero_de_iteraciones)


        # -- Verificar si ya se recorrieron todos los nodos. De ser así, marcar al 'NodoInicial' como no visitado para poder completar el ciclo
        NodosVisitadosAux[NodoInicial] = DeterminarNodosRecorridos(Grafo, NodosVisitadosAux)
        
        # -- Verificar si ya se alcanzó el nodo inicial (Posible solucion)
        if (NodoInicial == v):
                if (Profundidad == NroNodos-1):
                    return u, [v]
        # -- si no se alcanzó una solución, procesar Nodo  
        else:
            if not NodosVisitadosAux[v]:# and HayCamino(Grafo[v], NodosVisitadosAux):
                numero_de_iteraciones[0] = numero_de_iteraciones[0] + 1
                Peso, NodosCamino = BackTraking(Grafo, NroNodos, NodoInicial, v, NodosVisitadosAux, Profundidad + 1, numero_de_iteraciones)
                if (Peso >= 0) and (Peso + u < MenorPeso):
                    MenorCamino = [v] + NodosCamino;
                    MenorPeso = u + Peso
                    MenorNodo = [u, v]
            
        # -- Si encontró un menor camino, agregar a NodosCamino el menor camino
        if len(MenorCamino) > 0:
            #return MenorPeso , MenorCamino
            return MenorPeso , MenorCamino
            
        else:
            return -1, []
    else:
        return -1, []


def TSP_BackTraking(Grafo, NodoInicial, numero_de_iteraciones,ciudad,peso,solup,iters):

    NroNodos = len(Grafo)
    # -- Generar lista para llevar el control de nodos visitados
    NodosVisitados = [False] * NroNodos
    Camino = [] 

    # -- Efectuar proceso de busqueda     
    Peso, NodosCamino = BackTraking(Grafo, NroNodos, NodoInicial, NodoInicial, NodosVisitados, 0, numero_de_iteraciones)  

    PesoAux = 0
    C = 0
    if Peso == -1:
        for K in range(NroNodos):
            numero_de_iteraciones[0] = numero_de_iteraciones[0] + 1
            if C != 2:
                P, N = Greedy(Grafo[K], NodosVisitados, numero_de_iteraciones)
                NodosVisitados[K] = True
                PesoAux = PesoAux + P
                Camino.append(N)
                if N == 0:
                    C = C +1
        ciudad.set(str(len(Camino)))
        solup.set(str(float((100/len(Grafo))*(len(Camino)+1))) + "%")
        peso.set(str(PesoAux))
        iters.set(str(numero_de_iteraciones[0]))
        return Camino
    
    ciudad.set(str(len(NodosCamino)))
    solup.set(str(float((100/len(Grafo))*(len(NodosCamino)+1))) + "%")
    peso.set(str(Peso))
    iters.set(str(numero_de_iteraciones[0]))
    
    return [NodoInicial] + NodosCamino
