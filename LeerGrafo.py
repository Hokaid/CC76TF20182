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

