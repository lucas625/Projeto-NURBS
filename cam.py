import auxiliars.vectors as vectors

def normalizaBase(base):
    # normalizes every vector of a base
    baseAux = {}
    for i in base:
        aux = vectors.cloneV(base[i])
        aux = vectors.normalize(aux)
        baseAux[i] = aux
    return baseAux

def organizeVectors(N, V):
    # set the vectors of the camera to the desired model
    newBase = {
        'U': [],
        'V': [],
        'N': []
    }
    newBase['V'] = vectors.ortogonalize(V, N)
    newBase['U'] = vectors.crossProduct(N,newBase['V'])
    newBase['N'] = N
    return normalizaBase(newBase)

def organizeCam(cam):
    camAux = {
        'C': [],
        'vectors': []
    }
    print(cam['N'])
    if(len(cam['N'])==0 or len(cam['V'])==0):
        raise('please use non empty cam vectors')
    camAux['vectors'] = organizeVectors(cam['N'], cam['V'])
    return camAux