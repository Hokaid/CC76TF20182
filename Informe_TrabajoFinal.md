# Introducción
El problema que se plantea resolver en este proyecto es El problema del vendedor viajero. Este problema se puede definir de la siguiente manera: “Dado un conjunto finito de ciudades, y costos de viaje entre todos los pares de ciudades, encontrar la forma más barata de visitar todas las ciudades exactamente una vez, y volver al punto de partida” (Espinoza, 2006). Este es un problema NP-Hard (tiempo polinomial no determinista-difícil) dentro en la optimización combinatoria, muy importante en la investigación de operaciones y en la ciencia de la computación. La motivación para el desarrollo de este proyecto radica en poner en práctica el uso de los algoritmos y estrategias de solución vistas en clase tales como Dijkstra, Conjuntos disjuntos, programación dinámica, greedy, entre otros. Además, también se cuenta con la motivación de determinar una solución eficiente para un problema difícil e importante, cuya solución no solo podría traer muchos beneficios al mundo de la informática, sino también a la sociedad en general. Esto es así, ya que una solución eficiente para este problema podría tener aplicación en muchas situaciones de la vida real, por ejemplo, la ruta más óptima para realizar un viaje alrededor del mundo. El objetivo del presente informe es la propuesta de 2 algoritmos como solución para el problema mencionado. Dichos algoritmos serán explicados y analizados posteriormente. 

# Objetivos del Proyecto

A. Generar soluciones que estén acorde con los datos respectivos del problema, a partir de un análisis adecuado de los mismos, los cuales son representados bajo diversas formas tales como tablas y gráficos.

B. Desarrollar soluciones para el problema dado basadas en la utilización de números y términos matemáticos.

C. Utilizar técnicas y herramientas modernas en la elaboración de la solución del problema planteado.

D. Aplicar las técnicas y algoritmos de solución vistas a lo largo del curso en el desarrollo de las soluciones para el problema dado.

E. Elaborar un marco teórico explicando detalladamente cada una de las estrategias usadas para dar solución al problema planteado.

F. Determinar la complejidad algorítmica, haciendo uso de la notación Big O, de cada uno de los algoritmos desarrollados.

G. Encontrar soluciones óptimas para el problema planteado (Problema del vendedor viajero).

H. Generar una adecuada visualización de resultados de acuerdo a la solución encontrada, mostrando datos relevantes de la misma.

# Marco Teórico:

Antes de continuar, se debe resaltar que la representación de los datos correspondientes al problema del vendedor viajero se realiza a través de un grafo no dirigido. En el cual, los nodos son los lugares por visitar, y las aristas con sus respectivos pesos son las conexiones entre dichos lugares con sus respectivas distancias asociadas. En ambos algoritmos propuestos se utiliza esta representación para dar solución al problema. Ahora bien, se va a desarrollar el marco teórico correspondiente a cada uno de los algoritmos planteados:

## Marco Teórico del algoritmo basado en Dijkstra:

En primer lugar, se debe definir adecuadamente de qué se trata el algoritmo de Dijkstra. Según Arias (2012), “el algoritmo de dijkstra determina la ruta más corta desde un nodo origen hacia los demás nodos para ello es requerido como entrada un grafo cuyas aristas posean pesos”. Ahora bien, también se debe describir apropiadamente cómo funciona el algoritmo de Dijkstra. A continuación, procederá a brindar una descripción del procedimiento que sigue dicho algoritmo:

   Primero marcamos todos los vértices como no utilizados. El algoritmo parte de un vértice origen que será ingresado, a partir de          ese vértice evaluaremos sus adyacentes, como dijkstra usa una técnica greedy – La técnica greedy utiliza el principio de que para        que un camino sea óptimo, todos los caminos que contiene también deben ser óptimos- entre todos los vértices adyacentes, buscamos        el que esté más cerca de nuestro punto origen, lo tomamos como punto intermedio y vemos si podemos llegar más rápido a través de        este vértice a los demás. Después escogemos al siguiente más cercano (con las distancias ya actualizadas) y repetimos el proceso.        Esto lo hacemos hasta que el vértice no utilizado más cercano sea nuestro destino. Al proceso de actualizar las distancias tomando      como punto intermedio al nuevo vértice se le conoce como relajación. (Arias, 2012) 

En la cita anterior, se ha dado una descripción del procedimiento que sigue el algoritmo de Dijkstra para determinar el camino más corto de un nodo a otro. Asimismo, es importante tener en cuenta que si se utiliza, en la implementación de este algoritmo, una cola de prioridad, la complejidad del mismo se reduce en gran medida (Arias, 2012). En ese sentido, según Arias (2012), es importante mencionar que en dicha cola, los nodos que ingresen adquirirán su respectiva prioridad de acuerdo a lo cercanos que estén al nodo de partida, siendo más prioritarios si están más cerca. A continuación, siguiendo lo dicho por Arias (2012), el pseudocódigo correspondiente al algoritmo de Dijkstra descrito anteriormente está dado por lo siguiente:

```
1  método Dijkstra(Grafo,origen):
2      creamos una cola de prioridad Q
3      agregamos origen a la cola de prioridad Q
4      mientras Q no este vacío:
5          sacamos un elemento de la cola Q llamado u
6          si u ya fue visitado continuo sacando elementos de Q    
7          marcamos como visitado u
8          para cada vértice v adyacente a u en el Grafo:
9              sea w el peso entre vértices ( u , v )  
10             si v no ah sido visitado:
11                Relajacion( u , v , w )

1  método Relajacion( actual , adyacente , peso ):
2      si distancia[ actual ] + peso < distancia[ adyacente ]
3         distancia[ adyacente ] = distancia[ actual ] + peso
4         agregamos adyacente a la cola de prioridad Q
```

Ahora bien, se pasara a explicar en qué consiste el algoritmo planteado, el cual se basa en Dijkstra. Se trata de un Dijkstra modificado. Dicha modificación radica únicamente en agregarle un arreglo adicional al algoritmo. En dicho arreglo, se almacenan las profundidades de cada nodo asociado. Con profundidad se hace referencia a la cantidad de nodos que deben de ser recorridos desde el nodo origen para llegar al nodo en cuestión. Asimismo, también se está haciendo uso de otra cola de prioridad, donde se almacenan los nodos con sus respectivas profundidades, siendo el de mayor profundidad, el más prioritario. Dicha cola adquiere utilidad cuando se debe de seleccionar el nodo más profundo recorrido. Llegados a este punto, se procederá a explicar el algoritmo propuesto paso a paso para un entendimiento adecuado del mismo:

### Pasó a Paso del algoritmo Propuesto
#### Paso 1: 

Inicializar las profundidades de todos los nodos con el valor de 0 en el arreglo “prof” respectivo. Además, análogamente a como se realiza en el algoritmo de Dijkstra, inicializar los arreglos de distancias y paternidad con los valores en infinito y -1 (el -1 significa que no tiene nodo padre) respectivamente. No olvidar el arreglo de visitados que también debe estar inicializado correspondientemente con todos sus valores en “False”. Luego de esto, agregar el nodo de origen a la cola de prioridad y actualizar la información del mismo en los arreglos mencionados anteriormente. A continuación, se muestra la parte del código correspondiente a lo mencionado:

```python
    n = len(G)
    dist = [math.inf]*n
    path = [-1]*n
    prof = [0]*n
    visited = [False]*n
    q = []
    profus = []
    hq.heappush(q, (0, s))
    dist[s] = 0
 ```
#### Paso 2: 

Sacar de la cola de prioridad el nodo más cercano al nodo de origen. Tener en cuenta que en un primer caso se seleccionara el nodo de origen, ya que este será el único en la cola. Luego de sacar dicho nodo, verificar si esta visitado. Si esta visitado, se procederá con el siguiente nodo en la cola. De no estar visitado, se pasara a realizar el análisis de dicho nodo. Hasta ahora el algoritmo es casi idéntico a Dijkstra, no obstante, la variación propuesta se presentara en el siguiente paso. En ese sentido, el código correspondiente a este paso es el siguiente:

```python
while len(q) > 0:
        g, u = hq.heappop(q)
        if not visited[u]:
            visited[u] = True
```
#### Paso 3: 

En este paso, se procede con el análisis del nodo seleccionado. Para ello, se continúa con la evaluación de todos los nodos adyacentes al mismo en el grafo dado. Si el nodo adyacente ya ha sido visitado, se pasa a analizar el siguiente nodo adyacente. De no haber sido visitado, se pregunta si la profundidad de dicho nodo es menor o igual que la profundidad, aumentada en una unidad, del nodo seleccionado, es decir, la profundidad del nodo que se acaba de sacar de la cola más uno. A continuación, se explicara cual es el proceso que se debe seguir para cada posible caso a presentarse dada la condición anterior:

-	Si son iguales, se calcula el valor de la suma entre el peso de la arista que conecta el nodo adyacente con el nodo seleccionado y la distancia acumulada desde el origen al nodo seleccionado. Luego se compara si dicha suma posee un valor menor a la distancia desde el origen asociada al nodo adyacente, la cual en un primer caso puede tener valor infinito. 

1. Si dicho valor es menor, entonces se actualiza la profundidad, la distancia asociada y el parentesco correspondiente al nodo adyacente en los arreglos respectivos. La actualización se realiza de tal forma que en el camino que se pretende formar, el nodo seleccionado debe ser padre del nodo adyacente. Además, se agrega el nuevo nodo descubierto a la primera cola de prioridad con su distancia acumulada respectiva. Asimismo, también se agrega dicho nodo a la segunda cola de prioridad, la cual ordena por profundidad, con su profundidad respectiva.⋅⋅

2. De ser la suma calculada mayor o igual a dicha distancia, entonces no se realiza ninguna operación.⋅⋅

-	Si es menor, entonces se actualiza la profundidad del nodo adyacente, aumentándola en una unidad. Se establece como padre del nodo adyacente al nodo seleccionado. Asimismo, se actualiza la distancia acumulada desde el origen hasta dicho nodo. Las tres operaciones anteriores se realizan en los arreglos respectivos. Igualmente, se debe agregar este nodo adyacente a la primera cola de prioridad, la cual se ordena por pesos acumulados. Por su parte, también es importante agrega dicho nodo a la segunda cola de prioridad con su profundidad respectiva

-	Si es mayor, se procede a analizar el siguiente nodo adyacente, sin realizar ninguna operación adicional.

El código asociado a este paso se muestra a continuación.

```python
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
```

#### Paso 4:

Los pasos 2 y 3 se realizan hasta que la primera cola de prioridad, la cual ordena de acuerdo a distancia, desde el origen, asociada a cada nodo, quede completamente vacía. Esto se implementa agregando una estructura repetitiva “while”, con la condición de que realice las operaciones propuestas en los pasos anteriores hasta que la cola se quede vacía. Una vez vaciada la cola, se procede con el siguiente paso.

#### Paso 5: 

Se procede a seleccionar el elemento más prioritario de la segunda cola de prioridad, en la cual los nodos con la mayor profundidad son los que poseen mayor prioridad. Debido a la naturaleza de esta cola, se obtiene fácilmente el nodo recorrido con la mayor profundidad. Luego de esto, se procede a revisar si existe alguna arista que conecte directamente el nodo obtenido con el nodo de origen. Llegados a este punto, se pasara a explicar los procedimientos a seguir para cada posible resultado de la revisión anterior:

-	 Si existe dicha arista, se procede a realizar la conexión respectiva. De esta manera, se construye el camino solución partiendo desde el nodo de origen hasta el nodo más profundo obtenido, para luego volver al nodo de origen. 

-	 De no existir dicha arista, se procede a construir el camino de regreso haciendo uso del algoritmo de Dijkstra. No obstante, esta vez no es un Dijkstra modificado, sino el clásico. El algoritmo se ejecuta estableciendo como nodo de destino al nodo de origen. En ese sentido, se encuentra el camino más corto de regreso al nodo de origen. En consecuencia, se construye el camino solución partiendo del nodo de origen hasta el nada más profundo alcanzable, para luego regresar al nodo de origen utilizando la ruta más corta. 
Como se puede apreciar, en cualquiera de los dos casos propuestos anteriormente se termina volviendo al nodo de origen. Por lo tanto, se termina construyendo una posible solución al problema del vendedor viajero. Dicha solución parte y vuelve al nodo de origen. No obstante, no hay seguridad de que recorra todos los nodos del grafo. Asimismo, para el segundo caso, es muy probable que en el camino de regreso al nodo de origen, se vuelvan a visitar varios nodos previamente visitados. Por ello, tampoco hay seguridad de que se visita cada nodo (lugar) una sola vez en la solución dada. El código correspondiente a esta parte del algoritmo se muestra a continuación:

```python
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
                        
    return path, pathi, ciudad_final
```
### ¿Qué tan bueno es el algoritmo y que tanto se acerca a solucionar el problema?

Sustentación: Al agregar una nueva estructura que defina la profundidad de cada vértice del grafo, el algoritmo de Dijkstra modificado logra realizar un recorrido más profundo atreves de sus nodos. Esto se logra, porque se prioriza la profundidad de los nodos sobre la distancia para llegar a ellos. Por esta razón, cuando se analizan los nodos adyacentes para agregarlos a la cola, se revisa primero si la profundidad de dicho nodo adyacente es menor a la profundidad que podría adquirir si es elegido como hijo del último nodo visitado. De ser así, sin importar que la distancia acumulada desde el origen hasta dicho nodo adyacente aumente, se registra dicho nodo como hijo del último nodo sacado de la cola, aumentando la profundidad del camino (solución) por construir. Sin embargo, el orden en el que los nodos son visitados aun es con respecto a su distancia al nodo de origen, es decir, la cola de prioridad principal no pierde su utilidad. Por ello, la variación propuesta solo afecta al momento de seleccionar que nodos se agregan a la primera cola de prioridad. En efecto, se debe de tener en cuenta que cuando se agrega un nuevo nodo a la cola de prioridad, también se ve afectado la profundidad, el parentesco, y la distancia acumulada de dicho nodo. Por ende, cuando se visite dicho nodo y se evalúe la visita de sus nodos adyacentes, la profundidad de sus nodos adyacentes solo será mayor. Esto es posible, porque se prioriza la profundidad de los nodos sobre la distancia para llegar a ellos cada vez que se evalúan los nodos adyacentes. En ese sentido, se termina definiendo caminos más profundos a través del grafo para llegar a todos los nodos del mismo de los que se definirían si se usara un Dijkstra clásico. El algoritmo propuesto selecciona el camino recorrido más profundo de todos los demás, es decir, el camino que visita mayor cantidad de nodos. Luego de esto se trata de construir un ciclo que incluya todos los vértices de ese camino. Para esto, se selecciona el último vértice visitado de ese camino, el más profundo, para tratar de conectarlo con el nodo de origen. Dependiendo del grafo, esto se realiza a través de una única arista de manera óptima o  construyendo el camino más corto posible de regreso al nodo de origen. Cabe mencionar que dicho camino se construye aplicando el Dijkstra clásico. Como se puede apreciar, este algoritmo no garantiza que se visiten todos los nodos (lugares) del grafo, ni tampoco que se visite cada nodo una sola vez. Aun así, brinda una solución parcial en un tiempo significativamente corto. La complejidad de este algoritmo se analizara en la siguiente parte. 

### Mejoras adicionales del algoritmo

Cuando se realiza la ejecución del algoritmo propuesto basado en Dijkstra, en el arreglo de parentescos se detallan muchos nodos que son hijos de algunos nodos que participan (son visitados) en el camino (solución) encontrado. No obstante, estos nodos no participan en el camino que se propone como solución, ya que si bien es fácil desviarse del camino (solución) a través de ellos, no hay posibilidad de volver. Por este motivo, una mejora aplicable es agregar dichos nodos al camino. El propósito de hacer esto es aumentar el número de nodos recorridos en el camino. Para ello, se crea una ruta en la solución que permita volver de dichos nodos al camino. Dicha ruta solo se comprende de una arista, y es aquella que permite ir desde dichos nodos hasta su respectivo padre, el cual si pertenece al camino propuesto. Lo anterior se realiza para todos los nodos que cumplan con las características correspondientes. A continuación se presenta el código, en el cual se realizan las operaciones especificadas:

```python
path, pathi, ciudad_final = dikjstra_modificado(G,s,numero_iteraciones)
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
 ```
 
 ## Marco Teórico del algoritmo basado en Greedy:
El algoritmo GREEDY es un algoritmo de tipo voraz. Se basa en la lógica de buscar el vecino más cercano al nodo que esta en proceso, teniendo en cuenta que dichi vecino no haya sido visitado.

A continuacion se mostra un ejemplo de este algoritmo:

 ```python
 def Greedy(Grafo, NodosVisitados):

    MenorPeso = 10000000000
    N = None
    
    for Peso, Nodo in Grafo:
        if Peso < MenorPeso and not NodosVisitados[Nodo]:
            MenorPeso = Peso
            N = Nodo

    return MenorPeso, N
```
Como se puede apreciar es un algoritmo sencillo de entender y de programar. Ahora bien, al aplicar este algoritmo al problema del vendedor viajero la historia es diferente. Como ya se explicó en la introducción, el objetivo del problema del vendedor viajero es determinar el camino más coto entre un determinado número de nodos, pasando una vez obligatoriamente por cada nodo. La dificultad de aplicar el algoritmo GREEDY a este problema es que no se podrá garantizar que se cumpla tal condición. Al determinar el vecino más próximo al nodo procesado siempre, quedaran nodos que en ninguna de las iteraciones del algoritmo sean escogidos como los vecinos más cercanos, por lo tanto, quedaran excluidos de la solución.

La solución propuesta a esta dificultada es juntar el algoritmo GREEDY con uno de BACKTRAKING. Ver algoritmo en la imagen siguiente.

```python
def BackTraking(Grafo, NroNodos, NodoInicial, Nodo, NodosVisitados, Profundidad):
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
    for u, v in Nodos:
        # -- Verificar si ya se alcanzó el nodo inicial (Posible solucion)
        if (NodoInicial == v):
            if (Profundidad == NroNodos-1):
                return u, [v]
        # -- si no se alcanzó una solución, procesar Nodo  
        else:       
            if not NodosVisitadosAux[v]:
                Peso, NodosCamino = BackTraking(Grafo, NroNodos, NodoInicial, v, NodosVisitadosAux, Profundidad + 1)
                if (Peso >= 0) and (Peso + u < MenorPeso):
                    MenorCamino = [v] + NodosCamino;
                    MenorPeso = u + Peso
                    MenorNodo = [u, v]                
                
    # -- Si encontró un menor camino, agregar a NodosCamino el menor camino
    if len(MenorCamino) > 0:
        return MenorPeso , MenorCamino
    else:
        return -1, []
```

La forma en la que estos dos algoritmos se deben de juntar estará descrita en los siguientes pasos:

#### Paso 1:
Implementar una función que determine si el numero de nodos visitados es igual al numero de nodos del grafo, de esta forma se podrá saber si todos los nodos del grafo ya fueron visitados.

```python
 def Greedy(Grafo, NodosVisitados):

    MenorPeso = 10000000000
    N = None
    
    for Peso, Nodo in Grafo:
        if Peso < MenorPeso and not NodosVisitados[Nodo]:
            MenorPeso = Peso
            N = Nodo

    return MenorPeso, N
```
#### Paso 2:
Cambiar el ‘for’ que recoge el Nodo y el Peso del nodo anterior y que recorre todos los nodos del grafo por el algorito GREEDY que se encarga de determinar el Vecino más cercano, Nodo y Peso.

```python
 for u, v in Nodos:
```
cambiar por:
```python
 u, v = Greedy(Nodos, NodosVisitadosAux)
```
#### Paso 3: 
Verificar si ya se recorrieron todos los nodos. De ser así, marcar al 'NodoInicial' como no visitado para poder completar el ciclo. Al finalizar este paso, la parte recursiva del algoritmo tendrá una condición de parada, con lo cual podrá dejar de ejecutar el algoritmo y dar la repuesta requerida.

```python
 NodosVisitadosAux[NodoInicial] = DeterminarNodosRecorridos(Grafo, NodosVisitadosAux)
```

De esta forma se solucionara la dificultad planteada, ya que cada vez que no se incluyan los todos los nodos, el algoritmo volverá en la recursividad para probar con otro nodo, hasta que haya un camino que satisfaga la condición.

El algoritmo quedará de la siguiente forma:
```python
 def Greedy(Grafo, NodosVisitados):

    MenorPeso = 10000000000
    N = None
    
    for Peso, Nodo in Grafo:
        if Peso < MenorPeso and not NodosVisitados[Nodo]:
            MenorPeso = Peso
            N = Nodo

    return MenorPeso, N


def BackTraking(Grafo, NroNodos, NodoInicial, Nodo, NodosVisitados, Profundidad):
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
    u, v = Greedy(Nodos, NodosVisitadosAux)
    print(v)

    # -- Verificar si ya se recorrieron todos los nodos. De ser así, marcar al 'NodoInicial' como no visitado para poder completar el ciclo
    NodosVisitadosAux[NodoInicial] = DeterminarNodosRecorridos(Grafo, NodosVisitadosAux)

    # -- Verificar si ya se alcanzó el nodo inicial (Posible solucion)
    if (NodoInicial == v):
            if (Profundidad == NroNodos-1):
                return u, [v]
    # -- si no se alcanzó una solución, procesar Nodo  
    else:
        if not NodosVisitadosAux[v]:
            Peso, NodosCamino = BackTraking(Grafo, NroNodos, NodoInicial, v, NodosVisitadosAux, Profundidad + 1)
            if (Peso >= 0) and (Peso + u < MenorPeso):
                MenorCamino = [v] + NodosCamino;
                MenorPeso = u + Peso
                MenorNodo = [u, v]
   
    # -- Si encontró un menor camino, agregar a NodosCamino el menor camino
    if len(MenorCamino) > 0:
        return MenorPeso , MenorCamino
    else:
        return -1, []

```
 
# Analisis de Complejidada Algoritmica

## Análisis de la Complejidad del algoritmo basado en Dijkstra

En esta parte, se procederá a realizar el análisis respectivo del algoritmo propuesto, el cual está basado en Dijkstra. Sin embargo, antes es importante realizar el análisis respectivo del algoritmo de Dijkstra. 

### Complejidad del Algoritmo de Dijkstra:

En esta parte, se procederá a realizar el análisis respectivo del algoritmo basado en Dijkstra. Es importante reconocer que el algoritmo de Dijkstra es considerado una especialización de la búsqueda de costo uniforme (“Algoritmo de Dijkstra”, s.f). Asimismo, la búsqueda de costo uniforme se basa en el algoritmo de BFS (Búsqueda en anchura). Con la representación de lista de adyacencia del grafo, la cual es la representación usada para este proyecto, la complejidad asociada a recorrer todos los nodos del grafo, en el algoritmo de Dijkstra, está dada por la siguiente expresión:

                                                  Notación Big O: O(|V| + |E|) 
                                                  
                                           |V| = número de vértices (nodos) del grafo.
                                           |E| = número de aristas del grafo. 
      
La mencionado anteriormente es correcto, porque cada nodo es visitado una vez y su lista de adyacencia es recorrida una vez también (“Dijkstra’s Algorithm for Adjacency List Representation”, s.f). Además, se utiliza una cola de prioridad para determinar el nodo más cercano del conjunto de vértices (nodos) aun no visitados. En ese sentido, la complejidad de cada operación de agregación y expulsión de cada nodo de dicha cola de prioridad corresponde a O(Log(|V|)) (“Dijkstra’s Algorithm for Adjacency List Representation”, s.f). Incluso, es factible considerar que por cada iteración del algoritmo de Dijkstra, analizando el peor caso, se realiza una operación de agregación y/o eliminación de un nodo de la cola de prioridad. Lo dicho anteriormente, sucede porque cada nodo visitado es expulsado de la cola de prioridad antes de ser visitado, y asimismo, cuando se recorre la lista de adyacencia de cada nodo, en el peor de los casos, por cada iteración se realizara una operación de agregación de un nodo a la cola de prioridad (“Dijkstra’s Algorithm for Adjacency List Representation”, s.f). Por ello, de acuerdo a lo dicho por Alarcón (2013), la complejidad del algoritmo de Dijkstra, utilizando cola de prioridad, está dada por la expresión que se muestra a continuación: 

                                                   Notación Big O: O((|V|+|E|) Log(|V|))
                                                   
                                            |V| = número de vértices (nodos) del grafo.
                                            |E| = número de aristas del grafo. 

### Análisis de la Complejidad del algoritmo propuesto (basado en Dijkstra):

Para determinar la complejidad de este algoritmo, se realizara a través del análisis del mismo, realizando el conteo de cada iteración respectiva. A continuación, se muestra el código del algoritmo propuesto basado en Dijkstra con análisis de tiempo respectivo por cada instrucción: 

```python
    n = len(G)  #.........................................................................tiempo: 1
    dist = [math.inf]*n  #…………………………………...tiempo: n
    path = [-1]*n #………………………………………... tiempo: n
    prof = [0]*n #………………………………………….tiempo: n
    visited = [False]*n #……………………………………tiempo: n
    q = [] #………………………………………………….tiempo: 1
    profus = [] #…………………………………………… tiempo: 1
    hq.heappush(q, (0, s)) #…………………………………tiempo: 1
    dist[s] = 0 #……………………………………………..tiempo: 2
    while len(q) > 0: #……………………………………… tiempo: n
        g, u = hq.heappop(q) #………………………………...tiempo: Log(|q|)
        if not visited[u]: #……………………………………..tiempo: 2
            visited[u] = True #………………………………… tiempo: 2
            for wv in G[u]: #……………………………………tiempo: número de nodos adyacentes a u.
                if wv != None: #…………………………………tiempo: 1
                    w,v = wv #…………………………………tiempo: 1
                    f = g + w #…………………………………tiempo: 2
                    if not visited[v]: #…………………………………tiempo: 2
                        if (prof[u] + 1 == prof[v]): #…………………………………tiempo: 4
                            if f < dist[v]: #…………………………………tiempo: 2
                                dist[v] = f #…………………………………tiempo: 2
                                path[v] = u #…………………………………tiempo: 2
                                prof[v] = 1 + prof[u] #…………………………………tiempo: 4
                                hq.heappush(profus, (n-prof[v], v)) #…………tiempo: Log(|profus|)
                                hq.heappush(q, (f, v)) #…………………………...tiempo: Log(|q|)
                        elif(prof[u] + 1 > prof[v]): #……………………….tiempo: 4
                            dist[v] = f #…………………………………….tiempo: 2
                            path[v] = u #…………………………………tiempo: 2
                            prof[v] = 1 + prof[u] #…………………………tiempo: 4
                            hq.heappush(profus, (n-prof[v], v)) )) #…………tiempo: Log(|profus|)
                           hq.heappush(q, (f, v)) #…………………………...tiempo: Log(|q|)
```

Antes de proceder con el análisis matemático, se debe especificar que la repetitiva “while” del código anterior puede llegar a realizar más iteraciones de las especificadas. Es decir, no necesariamente el número de iteraciones coincide con n (número de nodos). Sin embargo, la segunda repetitiva, es decir, el “for” que se encuentra dentro de dicho “while” solo se va a ejecutar n veces. Esto sucede, porque si se analiza bien el código, se puede observar que en cada iteración, se verifica que el nodo a analizar dentro del “while” no haya sido visitado, y de no estarlo, pues se le marca como visitado, inmediatamente, en el arreglo “visited”. De esta manera, el análisis de los nodos adyacentes a cada vértice (nodo) solo se realiza una sola vez. Por esta razón, casi todo el código que está dentro del “while” solo se ejecuta n veces. En ese sentido, por motivos de cálculo y simplificación, se considerara que dicha repetitiva “while” solo realiza n llamadas.

Ahora bien, si realizamos la suma respectiva de los tiempos determinados anteriormente, de acuerdo a las reglas que se deben de tener en cuenta para el análisis de este tipo de algoritmos, se obtiene lo siguiente:

              6+4n+n*(Log(|q|)+4+|número de nodos adyacentes a u|*(20+Log(|profus|)+Log(|q|)))
                      
       Excluyendo los valores constantes y aplicando propiedad distributiva:
                  
              4n+n*(Log(|q|)) + n*|número de nodos adyacentes a u|*(Log(|profus|)+Log(|q|))
              4n + n*(Log(|q|)) + n*|número de nodos adyacentes a u|*(Log(|q|))+ n*|número de nodos adyacentes a u|*(Log(|profus|) 
              4n + n*(Log(|q|))*(1+|número de nodos adyacentes a u|) + n*|número de nodos adyacentes a u|*(Log(|profus|)
            
       Excluyendo nuevamente los valores constantes:
                  
              4n + n*(Log(|q|))*(|número de nodos adyacentes a u|) + n*|número de nodos adyacentes a u|*(Log(|profus|)
              4n + n*|número de nodos adyacentes a u|*(Log(|profus|)+Log(|q|))
              n*(4+|número de nodos adyacentes a u|*(Log(|profus|)+Log(|q|)))
              
       Excluyendo una vez más los valores constantes:
       
              n*|número de nodos adyacentes a u|*(Log(|profus|)+Log(|q|))
              
              n: número de nodos del grafo
              u: cualquier vértice perteneciente al grafo
              
Llegados a este punto, se debe reconocer que la expresión “n*|número de nodos adyacentes a u|” coincide con la suma entre la cantidad de nodos y el número de aristas. A continuación se demostrara lo propuesto anteriormente con un ejemplo:

![alt text](https://github.com/Hokaid/CC76TF20182/blob/master/grafo.png "grafo")

Supongamos que se tiene el grafo no dirigido anterior, son 4 vértices, por lo que la expresión sería “4*|número de nodos adyacentes a u|”. Son 4 aristas, entonces, después del análisis, se debe obtener que son 8 iteraciones en total para la expresión “4*|número de nodos adyacentes a u|” dado este grafo. 

                            1 iteración (u=1)………... |número de nodos adyacentes a u| = 2
                            2 iteración (u=2)………... |número de nodos adyacentes a u| = 3
                            3 iteración (u=3)………... |número de nodos adyacentes a u| = 2
                            4 iteración (u=4)………... |número de nodos adyacentes a u| = 1
                                                                              Total:   8

Como se puede observar en el ejemplo anterior, la fórmula propuesta si es generalizable. No obstante, no se cumple exactamente para todos los casos, pero se aproxima bastante al resultado que debería dar. Por lo tanto, para realizar este análisis, se considerara la formula propuesta. En ese sentido, si remplazamos la expresión “n*|número de nodos adyacentes a u|” por “(n+|a|)”, se obtendría lo siguiente en la expresión matemática correspondiente al análisis de la complejidad de este algoritmo:
 
                                                 (n+|a|)*(Log(|profus|)+Log(|q|))
                                                   
                                                 n: número de nodos
                                                 |a|: cantidad de aristas del grafo
                                                 
Se debe tener en cuenta que expresiones como |q| y |profus| son de longitud variable, ya que representan la longitud de las colas de prioridad “q” y “profus” respectivamente en cada momento. Dichas longitudes variaran constantemente, por lo que, como se está realizando el análisis del peor caso, se considerara la máxima longitud que puedan llegar a obtener dichas colas de prioridad. En el caso de q, la máxima longitud que puede llegar a adquirir coincide con el número de nodos. Se debe tener en cuenta que cada iteración de la repetitiva “while” del código anterior, se libera un elemento de la cola, mientras que cuando se analizan los nodos adyacentes a un nodo, solo se agregan nodos a dicha cola. Por lo tanto, se pueden dar el caso de que un nodo sea adyacente a todos los demás nodos, por lo que se podrían agregar todos ellos a la cola de prioridad “q”. De esta manera, se justifica considerar que la máxima longitud de dicha cola coincida aproximadamente con el número de nodos. Si remplazamos lo dicho anteriormente en la expresión, se obtiene:

                                                (n+|a|)*(Log(|profus|)+Log(n))
                                                
                                                n: número de nodos
                                                |a|: cantidad de aristas del grafo

Algo similar sucede con la cola |profus|, solo que para este caso, en ninguna parte del código mostrado, se expulsan nodos de dicha cola. En esta cola, como ya se explica en la parte teórica, se almacenan los nodos con sus respectivas profundidades en cada momento del recorrido. Asimismo, sirve para determinar el nodo más profundo recorrido, lo cual será útil en la segunda parte del algoritmo. Ahora bien, siguiendo la expresión matemática dada anteriormente, se puede observar que la operación de agregar nodos a la cola de prioridad se lleva a cabo unas “(n+|a|)” veces. Por ello, la longitud máxima que puede alcanzar dicha cola de prioridad es coincide con el valor de dicha expresión: “(n+|a|)”. Considerando lo mencionado en la expresión, se reconoce lo siguiente:

                                                (n+|a|)*(Log(n+|a|)+Log(n))
                                                
                             Aplicando la propiedad de suma de logaritmos:
                             
                                                (n+|a|)*(Log((n+|a|)*n))
                                                
                                                n: número de nodos
                                                |a|: cantidad de aristas del grafo
                                                
Continuando con el asunto, para complementar lo propuesto hasta ahora, se procederá a analizar la segunda parte del algoritmo. En esta segunda parte, a partir de la cola de prioridad “profus”, se determina el nodo más profundo recorrido la primera parte. Luego de ello, se verifica si existe alguna arista que conecte directamente dicho nodo seleccionado con el nodo de origen. De existir dicha arista, como se explicó en la parte teórica, se realiza la conexión respectiva y se retorna el camino (solución) encontrado. Para este primer caso, se debe tener en cuenta que el tiempo de ejecución para encontrar dicha arista y realizar la conexión es despreciable. Por esta razón, para este caso, la complejidad del algoritmo en notación Big O coincidiría con la última expresión matemática dada:

                                           Notación Big O: O((n+|a|)*(Log((n+|a|)*n)))
                                           
                                           n: número de nodos
                                           |a|: cantidad de aristas del grafo
                                           
No obstante, es pertinente analizar el peor caso posible. Esto se da cuando no existe la arista que conecte directamente el nodo más profundo recorrido con el nodo de origen. Para este segundo caso, se intentara buscar el camino más corto para volver al nodo de origen usando el algoritmo clásico de Dijkstra, sin ninguna modificación. En ese sentido, se sumara a la expresión matemática determina la complejidad del algoritmo de Dijkstra:

                           (n+|a|)*(Log((n+|a|)*n)) + ((n+|a|)*Log(n))
                           (n+|a|)*(Log(n+|a|)+Log(n)) + ((n+|a|)*Log(n))
                           
            Realizando la suma respectiva, se obtiene:
                           
                           2*((n+|a|)*Log(n))+ ((n+|a|)*Log(n+|a|))
                           (n+|a|)*(2*Log(n) + Log(n+|a|))
                           
            Simplificando los valores constantes, de acuerdo a la notación Big O:
            
                           (n+|a|)*(Log(n+|a|)+Log(n))
                           (n+|a|)*(Log((n+|a|)*n))
                           
Por lo tanto, la complejidad para este caso, en notación Big O, será idéntica a como se determinó para el primer caso:

                                 Notación Big O: O((n+|a|)*(Log((n+|a|)*n)))

La representación dada anteriormente representa la complejidad, en notación Big O, del algoritmo propuesto basado en Dijkstra.

## Análisis de la Complejidad del algoritmo basado en Greedy:
 Hacer lo Tuyo Javier, also
 
# Conclusiones
En conclusión, se cumplieron los objetivos propuestos satisfactoriamente. Se desarrollo soluciones basadas en el problema dado haciendo uso de herramientas y técnicas (Algoritmos) aprendidas a lo largo del curso. Los algoritmos usados para dicha solución son: El algoritmo de Dijkstra y el algoritmo Greedy relacionaso con backtraking. De la misma forma, se evidencio la aplicación de las competencias generales y específicas, siendo estas las de Razonamiento Cuantitativo y, Planificación y Conducción de Experimentos respectivamente. Esto se ve reflejado en el uso de técnicas matemáticas (Teorema Maestro) para hallar la complejidad de los algoritmos implementados y la exhaustiva investigación de algoritmos que den una solución adecuada al problema planteado. Ademas, es necesario enmarcar que se lograron mejores soluciones generales en comparacion al trabajo parcial, ya que los rangos y los tiempos de solucion son mejores. Para finalizar, el presente trabajo satisface los objetivos planteados. A continuación, se plantarán las conclusiones acorde con los objetivos dados:
A. Se realizó un análisis adecuado de los datos del problema, los cuales estaban representados mediante tablas, para llegar a una solución satisfactoria.

B. Se desarrollo soluciónes para el problema usando tecnicas matemáticas.

C. En la investigacion correspondiente se encontro herramientas modernas para derle solución al problema.

D. Todas las tecnicas implementadas para dar solución al problema se basan en algoritmos trabajados en clase.

E. Se Elaboro un marco teorico acorde a la solución del problema

F. Se determino y se explico la complejidad de cada algoritmo de forma detallada

G. Por la misma naturaleza del problema, no se pudo encontrar una solucion optima con los algoritmos vistos en clase

H. Se priorizo en la visualización de datos relevantes en la demostración del problema

# Bibliografía 

- Algortimo de Dijkstra. (s.f). Recuperado de http://oer2go.org/mods/es-wikipedia-static/content/a/algoritmo_de_dijkstra.html [Consulta: 15 de Noviembre de 2018]

- Arias, J. G. (19 de marzo de 2012). Camino más corto: Algoritmo de Dijkstra. Recuperado de https://jariasf.wordpress.com/2012/03/19/camino-mas-corto-algoritmo-de-dijkstra/ [Consulta: 15 de Noviembre de 2018]

- Dijkstra’s Algorithm for Adjacency List Representation. (s.f). Recuperado de https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/ [Consulta: 15 de Noviembre de 2018]

- Espinoza, D. (24 de julio de 2016). EL Problema del Vendedor Viajero (TSP) y
Programación Entera (IP) [Presentación de Power Point]. Universidad de Chile. Recuperado de http://www.dii.uchile.cl/~daespino/PApers/TSP_and_IP_chile_050820.pdf 
https://jariasf.wordpress.com/2012/03/19/camino-mas-corto-algoritmo-de-dijkstra/ [Consulta: 15 de Noviembre de 2018]








