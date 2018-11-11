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
    return Capitales

def Leer_Cordenadas(filename):
    filec = open(filename)
    CordX = []
    CordY = []
    for line in filec:
        r = 0
        for j in line.split('-'):
            if (is_float(j)):
                pr = float(j)*(-1)
                if (r == 0):
                    CordX.append(pr)
                else:
                    CordY.append(pr)
                r = r + 1
    return CordX, CordY

def Leer_Cordenadas_Criterio(filename, Capitales, Criterio):
    filec = open(filename)
    CordX = []
    CordY = []
    k = 0
    for line in filec:
        r = 0
        for j in line.split('-'):
            if (is_float(j)):
                if Capitales[k] == Criterio:
                    pr = float(j)*(-1)
                    if (r == 0):
                        CordX.append(pr)
                    else:
                        CordY.append(pr)
                r = r + 1
                if (r == 2):
                    k = k + 1
    return CordX, CordY

def Retorna_Cords_Criterio(crit):
    if crit >= 1 and crit <= 3:
        return Leer_Cordenadas_Criterio("Cordenadas_de_CentrosPoblados_Obtenido_del_Dataset.txt",
                             LeerCapital("AtributoCapital_de_CentrosPoblados_Obtenido_del_Dataset.txt",145225),crit)
    elif crit == 0:
        return Leer_Cordenadas("Cordenadas_de_CentrosPoblados_Obtenido_del_Dataset.txt")
    elif crit == 4:
        return Leer_Cordenadas("Cordenadas_de_CentrosEducativos_Obtenido_del_Dataset.txt")





