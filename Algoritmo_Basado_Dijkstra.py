import math
import heapq as hq
from LectorDeGrafo import *

def MakeWay(path, t, contador, camino, n):
    if t != -1 and contador < n:
        MakeWay(path, path[t], contador + 1, camino, n)
        camino.append(t)

def dikjstra_modificado(G, s, numero_iteraciones):
    n = len(G)
    dist = [math.inf]*n
    path = [-1]*n
    prof = [0]*n
    visited = [False]*n
    q = []
    profus = []
    hq.heappush(q, (0, s))
    dist[s] = 0
    while len(q) > 0:
        numero_iteraciones[0] = numero_iteraciones[0] + 1
        g, u = hq.heappop(q)
        if not visited[u]:
            visited[u] = True
            if (prof[u] > n-1): break
            for wv in G[u]:
                numero_iteraciones[0] = numero_iteraciones[0] + 1
                if wv != None:
                    w,v = wv
                    f = g + w
                    if not visited[v]:
                        if (prof[u] + 1 == prof[v]):
                            if f < dist[v]:
                                dist[v] = f
                                path[v] = u
                                prof[v] = 1 + prof[u]
                                hq.heappush(profus, (n-prof[v], v))
                                hq.heappush(q, (f, v))
                        elif(prof[u] + 1 > prof[v]):
                            dist[v] = f
                            path[v] = u
                            prof[v] = 1 + prof[u]
                            hq.heappush(profus, (n-prof[v], v))
                            hq.heappush(q, (f, v))
                            
    _,ciudad_final = hq.heappop(profus)
    visit = [False]*n
    weight = [math.inf]*n
    pathi = [-1]*n
    if (path[s] == -1):
        camino_regreso = False
        for w,v in G[ciudad_final]:
            numero_iteraciones[0] = numero_iteraciones[0] + 1
            if (v == s):
                camino_regreso = True
                path[v] = ciudad_final
        if (camino_regreso == False):
            queue = []
            weight[ciudad_final] = 0
            hq.heappush(queue, (0, ciudad_final))
            while len(queue) > 0:
                numero_iteraciones[0] = numero_iteraciones[0] + 1
                g, u = hq.heappop(queue)
                if visit[u]: continue
                visit[u] = True
                if (u == s): break
                for h,v in G[u]:
                    numero_iteraciones[0] = numero_iteraciones[0] + 1
                    f = g + h
                    if f < weight[v]:
                        weight[v] = f
                        pathi[v] = u
                        hq.heappush(queue, (f, v))
                        
    return path, pathi, dist, weight, ciudad_final

def Ejecutar_Alg_Basado_Dikjstra(G,s,ciudad,peso,solup,iters):
    numero_iteraciones = [0]
    path, pathi, dist, weight, ciudad_final = dikjstra_modificado(G,s,numero_iteraciones)
    camino = []
    if (pathi == [-1]*len(G)):
        MakeWay(path, s, 0, camino, len(G))
    else:
        MakeWay(path, path[ciudad_final], 0, camino, len(G))
        MakeWay(pathi, s, 0, camino, len(G))
    for u in range(len(G)):
        SoyPadre = False
        Phato = path + pathi
        for i in Phato:
            if (u == i):
                SoyPadre = True
        if (SoyPadre == False):
            cou = 0
            for c in camino:
                if (path[u] == c):
                    caminAux1 = camino[:cou+1]
                    caminAux2 = camino[cou+1:]
                    caminAux1.append(u)
                    caminAux1.append(path[u])
                    camino = caminAux1 + caminAux2
                    break
                cou = cou + 1
    print("...Resultado en Consola:...")
    print("El camino(solución) encontrado sigue la siguiente estructura:")
    lugares_visitados = []
    distancia_acumulada = 0
    anterior = s
    counter = 0
    print(str(s) + "(0)",end="->")
    for i in camino:
        Ya_encontrado = False
        for j in lugares_visitados:
            if (i == j):
                Ya_encontrado = True
        if (Ya_encontrado == False):
            lugares_visitados.append(i)
        for wv in G[anterior]:
            if wv != None:
                w,v = wv
                if v == i:
                    distancia_acumulada = distancia_acumulada + w
                    if (counter == len(camino)-1):
                        print(str(v)+"("+str(distancia_acumulada)+")")
                    else:
                        print(str(v)+"("+str(distancia_acumulada)+")",end="->")
                    anterior = i
                    break
        counter = counter + 1
    print("Distancia recorrida en el camino es(Km): " + str(distancia_acumulada))
    ciudad.set(str(len(lugares_visitados)))
    solup.set(str(float((100/len(G))*len(lugares_visitados))) + "%")
    peso.set(str(distancia_acumulada))
    iters.set(str(numero_iteraciones[0]))
    print()









