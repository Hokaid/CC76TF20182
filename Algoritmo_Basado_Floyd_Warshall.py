import math
import heapq as hq
import copy
from LeerGrafo import *

def PathXWarshall(G, s):
    d = [[math.inf]*len(G) for i in range(len(G))]
    p = [[None]*len(G) for i in range(len(G))]
    for u in range(len(G)):
        d[u][u] = 0
        for w,v in G[u]:
            d[u][v] = w
            p[u][v] = u
    cont = 0
    for k in range(len(G)):
        cont = cont + 1
        print(cont)
        for u in range(len(G)):
            for v in range(len(G)):
                f = d[u][k] + d[k][v]
                if f < d[u][v]:
                    d[u][v] = f
                    p[u][v] = p[k][v]

    def FormarPath(st, way, v, Way, contador):
        if (p[st][way] == st):
            v[way] = True
            Way.append(way)
            contador[0] = contador[0] + 1
        else:
            v[way] = True
            Way.append(way)
            contador[0] = contador[0] + 1
            FormarPath(st, p[st][way], v, Way, contador)
        
    def Path_X_Wharsall(st, v, camino, dista_acu, contador):
        v[st] = True
        minv = []
        minw = []
        print(contador[0])
        if (contador[0] >= len(G)-1):
            hayWR = False
            for w,u in G[st]:
                if u == s:
                    camino.append(s)
                    dista_acu[0] = dista_acu[0] + w
                    hayWR = True
            if (hayWR == False):
                dista_acu[0] = dista_acu[0] + d[st][s]
                Way = []
                FormarPath(st, s, v, Way, contador)
                for i in range(len(Way)):
                    camino.append(Way[len(Way)-1-i])
        u = 0
        for i in d[st]:
            if v[u] == False:
                if p[st][u] == st:
                    hq.heappush(minv, (i, u))
                else:
                    hq.heappush(minw, (i, u))  
            u = u + 1
        if (len(minw) == 0 and len(minv) > 0):
            w,u = hq.heappop(minv)
            camino.append(u)
            v[u] = True
            dista_acu[0] = dista_acu[0] + w
            contador[0] = contador[0] + 1
            Path_X_Wharsall(u, v, camino, dista_acu, contador)
        elif(len(minw) > 0):
            w,u = hq.heappop(minw)
            dista_acu[0] = dista_acu[0] + w
            Way = []
            FormarPath(st, u, v, Way, contador)
            for i in range(len(Way)):
                camino.append(Way[len(Way)-1-i])
            Path_X_Wharsall(u, v, camino, dista_acu, contador)
            
        return dista_acu
            
    camino = [s]
    v = [False for i in range(len(G))]
    dista_acu = [0]
    contador = [0]
    Path_X_Wharsall(s, v, camino, dista_acu, contador)
    return camino, dista_acu


#G = [[(7,1),(8,2)],[(7,0),(10,3),(4,2)],[(4,1),(8,0),(15,3)],[(10,1),(15,2)]]
G = LeeGrafo("Grafo_171_Capitales_Provinciales.txt")

print(PathXWarshall(G, 0))

