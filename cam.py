import auxiliars.vectors as vectors
import numpy as np
import ipdb

class Cam:
    def __init__(self, cam):
        self.matrix = self.organizeCam(cam)#matrix with homogeneous coordinates
        self.matrix = np.array(self.matrix)
        self.hx = cam['screen']['hx']
        self.hy = cam['screen']['hy']
        self.d = cam['screen']['d']

    def __str__(self):
        stringP = "matrix: " + str(self.matrix) + "\n" + "hx: " + str(self.hx) + "\n" + "hy: " + str(self.hy) + "\n" + "d: " + str(self.d)
        stringP = str(stringP)
        return (stringP)

    def normalizaBase(self, base):
        # normalizes every vector of a base
        baseAux = {}
        for i in base:
            aux = vectors.cloneV(base[i])
            aux = vectors.normalize(aux)
            baseAux[i] = aux
        return baseAux

    def organizeVectors(self, N, V, translation):
        # set the vectors of the camera to the desired model
        newBase = {
            'U': [],
            'V': [],
            'N': []
        }
        newBase['V'] = vectors.ortogonalize(N, V)
        newBase['U'] = vectors.crossProduct(N,newBase['V'])
        newBase['N'] = N
        newBase = self.normalizaBase(newBase)
        BaseCam = []
        newBase['U'].append(translation[0])
        newBase['V'].append(translation[1])
        newBase['N'].append(translation[2])
        BaseCam.append(newBase['U'])
        BaseCam.append(newBase['V'])
        BaseCam.append(newBase['N'])
        BaseCam.append([0,0,0,1])
        return BaseCam

    def organizeCam(self, cam):
        #do all camera transformation and return its matrix
        camAux = []
        if(len(cam['N'])==0 or len(cam['V'])==0):
            raise('please use non empty cam vectors')
        translation = vectors.constantMult(cam['C'],-1)
        camAux = self.organizeVectors(cam['N'], cam['V'], translation)
        camAux = np.array(camAux)
        camAux = camAux.T
        camAux = camAux.tolist()
        return camAux

    def organize_single_point(self, point):
        vaux = vectors.cloneV(point)
        vaux.append(1)
        aux = np.array(vaux)[np.newaxis]
        aux = aux.T
        aux = np.matmul(self.matrix, aux)
        aux = aux.T
        aux = aux.tolist()
        newP = []
        for i in range(len(aux[0])-1):
            newP.append(aux[0][i])
        return newP

    def organizePoints(self, points):
        for i in range(len(points)):
            for j in range(len(points[i])):
                points[i][j] = self.organize_single_point(points[i][j])
        return points
                

    def find_position_p(self, point, width, height):
        #find point position on screen given width and height
        a=(-1)*point[2]
        if point[2] == 0:
            a = -1
        a = a*self.d
        x1 = (point[0]) / a #x1 = x*d / z
        y1 = (point[1]) / a #y1 = y*d / z
        pNDCX = (x1 + self.hx) / (2 * self.hx)
        pNDCY = (y1 + self.hy) / (2*self.hy)
        newX = (pNDCX * width)
        newY = ((1-pNDCY) * height)
        #since we are using math plot lib ins#tead of drawing by ourselves, we do not need to care about the screen height or width
        pixelX = int(newX // 1)
        pixelY = int(newY // 1)
        #we are using floor just to make sure that the newX and newY division wont place them between a non integer
        position = [pixelX, pixelY]
        return position

    def find_control_screen(self, control_points, width, height):
        points = []
        for i in range(len(control_points)):
            points.append([])
            for j in range(len(control_points[i])):
                aux = self.organize_single_point(control_points[i][j])
                aux = self.find_position_p(aux, width, height)
                points[i].append(aux)
        return points