import math
import heapq as hq
from LeerGrafo import *

def prim(G, s):
    def MakeWay(path, t, contador, camino):
        if t != -1 and contador < len(G):
            MakeWay(path, path[t], contador + 1, camino)
            camino.append(t)
    def dikjstra_modificado(G, s):
        n = len(G)
        dist = [math.inf]*n
        path = [-1]*n
        prof = [0]*n
        visited = [False]*n
        q = []
        hq.heappush(q, (0, s))
        dist[0] = 0
        while len(q) > 0:
            g, u = hq.heappop(q)
            q.clear()
            if not visited[u]:
                visited[u] = True
                if (prof[u] > n-1): break
                for wv in G[u]:
                    if wv != None:
                        w,v = wv
                        f = g + w
                        if not visited[v]:
                            if (prof[u] + 1 == prof[v]):
                                if f < dist[v]:
                                    dist[v] = f
                                    path[v] = u
                                    prof[v] = 1 + prof[u]
                                    hq.heappush(q, (f, v))
                            elif(prof[u] + 1 > prof[v]):
                                dist[v] = f
                                path[v] = u
                                prof[v] = 1 + prof[u]
                                hq.heappush(q, (f, v))
        ciudad_final = u
        visit = [False]*n
        weight = [math.inf]*n
        pathi = [-1]*n
        if (path[s] == -1):
            camino_regreso = False
            for w,v in G[u]:
                if (v == s):
                    camino_regreso = True
                    path[v] = u
            if (camino_regreso == False):
                queue = []
                weight[u] = 0
                hq.heappush(queue, (0, u))
                while len(queue) > 0:
                    g, u = hq.heappop(queue)
                    if visit[u]: continue
                    visit[u] = True
                    if (u == s): break
                    for h,v in G[u]:
                        f = g + h
                        if f < weight[v]:
                            weight[v] = f
                            pathi[v] = u
                            hq.heappush(queue, (f, v))
                            
        return path, pathi, dist, weight, ciudad_final
    
    path, pathi, dist, weight, ciudad_final = dikjstra_modificado(G,s)
    camino = []
    if (pathi == [-1]*len(G)):
        MakeWay(path, s, 0, camino)
    else:
        MakeWay(path, path[ciudad_final], 0, camino)
        MakeWay(pathi, s, 0, camino)
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
    return path, pathi, dist, weight, camino


"""
G = [[(1, 2), (2, 3), (4, 6)],
     [(0, 2), (4, 2), (5, 3)],
     [(0, 3), (4, 1), (3, 5)],
     [(2, 5), (4, 5), (5, 6)],
     [(0, 6), (1, 2), (2, 1), (3, 5), (5, 4)],
     [(1, 3), (3, 6), (4, 4)]]
"""
G = [[(7,1),(8,2),(9,3)],[(7,0),(10,3),(4,2)],[(4,1),(8,0),(15,3)],[(10,1),(15,2),(9,0)]]
#G = LeeGrafo("Grafo_25_Capitales_Regionales.txt")
path, pathi, dist, weight, camino = prim(G, 0)

distancia_acumulada = 0
anterior = 0
for i in camino:
    for w,v in G[anterior]:
        if v == i:
            distancia_acumulada = distancia_acumulada + w
    anterior = i

print(distancia_acumulada)








