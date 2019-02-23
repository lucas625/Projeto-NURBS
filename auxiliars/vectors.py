# main functions for work with vectors

def checkELen(vector1, vector2):
    # check if the vectors have the same len
    if len(vector1) != len(vector2):
        raise "invalid combination of vectors for vector operation"

def cloneV(vector1):
    # avoid changing the original vector
    vectorC = []
    for i in range(0, len(vector1)):
        vectorC.append(vector1[i])
    return vectorC

def dotProduct(vector1, vector2):
    # u.v
    checkELen(vector1, vector2)
    sAll = 0
    for i in range(0, len(vector1)):
        aux = vector1[i] * vector2[i]
        sAll = sAll + aux
    return sAll

def sumV(vector1, vector2):
    # u + v
    checkELen(vector1, vector2)
    vectorC = cloneV(vector1)
    for i in range(0, len(vectorC)):
        vectorC[i] = vector1[i] + vector2[i]
    return vectorC

def subV(vector1, vector2):
    # u - v
    checkELen(vector1, vector2)
    vectorC = cloneV(vector1)
    for i in range(0, len(vectorC)):
        vectorC[i] = vectorC[i] - vector2[i]
    return vectorC

def vLen(vector1):
    # ||v||
    lenV = dotProduct(vector1, vector1)
    return (lenV ** 0.5)

def constantMult(vector1, k):
    # 3 * u
    vectorAux = cloneV(vector1)
    for i in range(0, len(vectorAux)):
        vectorAux[i] = vector1[i] * k
    return vectorAux

def projection(vector1, vector2):
    #proj u v
    checkELen(vector1, vector2)
    aux1 = dotProduct(vector1, vector2)
    aux2 = dotProduct(vector2, vector2)
    aux = aux1 / aux2
    return constantMult(vector2, aux)

def ortogonalize(vector1, vector2):
    # u - proj u v
    checkELen(vector1, vector2)
    proj = projection(vector1, vector2)
    ort = subV(vector1, proj)
    return ort

def crossProduct(vector1, vector2):
    # u X v
    checkELen(vector1, vector2)
    if(len(vector1)>3 or len(vector1)<2):
        raise("invalid vector len for crossProduct")
    aux = []
    if(len(vector1)==3):
        aux.append((vector1[1]*vector2[2]) - (vector1[2]*vector2[1]))
        aux.append((vector1[2]*vector2[0]) - (vector1[0]*vector2[2]))
        aux.append((vector1[0]*vector2[1]) - (vector1[1]*vector2[0]))
    elif(len(vector1)==2):
        aux.append((vector1[0]*vector2[1]) - (vector1[1]*vector2[0])) 
    return aux

def normalize(vector1):
    # normalizes a vector
    aux = cloneV(vector1)
    helper = 1 / (vLen(vector1))
    aux = constantMult(aux, helper)
    return aux

def createEmptyVector(n):
    #create an empty vector of len n
    v = []
    for i in range(n):
        v.append(0)
    return(v)
