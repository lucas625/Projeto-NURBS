import auxiliars.vectors as vectors
import ipdb
class Nurbs:

    def __init__(self, p, q, n, m, points, knotsP, knotsQ, weights):
        self.p = p
        self.q = q
        self.n = n
        self.m = m
        self.control_points = points
        self.knotsP = knotsP
        self.knotsQ = knotsQ
        self.weights = weights
        self.iterations = 0


    def __str__(self):
        p = "p: " + str(self.p)
        q = "q: " + str(self.q)
        n = "n: " + str(self.n)
        m = "m: " + str(self.m)
        control_points = "control points: " + str(self.control_points)
        knotsP = "knotsP: " + str(self.knotsP)
        knotsQ = "knotsQ: " + str(self.knotsP)
        weights = "weights: " + str(self.weights)
        return (p + "\n" + q + "\n" + n + "\n" + m +
             "\n" + control_points + "\n" + knotsP + "\n" + knotsQ +
                  "\n" + weights + "\n")

    def set_iterations(self, val):
        #set the total number of iterations
        self.iterations = val

    def checkSpan(self,u1,u2,u):
        # ui <= u < u1+1
        if u1<=u and u<u2:
            return 1
        else:
            return 0

    def bsplineBFunction(self, knots, u, i, p):
        #the B-spline basis function
        """
            knots: list of knots that has a interval that contais u
            u: position
            i: actual interval
            p: degree
        """
        if p==0:
            return self.checkSpan(knots[i], knots[i+1], u)
        N1 = self.bsplineBFunction(knots,u,i,p-1)
        aux1 = 0
        if N1!=0:
            aux1 = (N1*(u-knots[i])) / (knots[i+p]-knots[i])
        N2 = self.bsplineBFunction(knots,u,i+1,p-1)
        aux2 = 0
        if N2!=0:
            aux2 = (N2*(knots[i+p+1] - u)) / (knots[i+p+1] - knots[i+1])
        return aux1 + aux2

    def nurbs_surface(self, knotsP, knotsQ, p, q, n, m, control_points, weights, u, v):
        #computes a point on the surface
        """
            knotsP: list of knots that contains knots relative to p degree
            knotsQ: list of knots that contains knots relative to q degree
            p: first degree
            q: second degree
            control_points: matrix of control_points
            n: points degree(line)
            m: points degree(column)
            weights: matrix of weights
            u: first parameter
            v: second parameter
        """
        downSum = 0
        upperPart = vectors.createEmptyVector(len(control_points[0][0]))
        for i in range(n):
            firstPart = self.bsplineBFunction(knotsP,u,i,p)
            secondPart = 0
            secondPart_with_point = vectors.createEmptyVector(len(control_points[0][0]))
            for j in range(m):
                aux = self.bsplineBFunction(knotsQ,v,j,q)*weights[i][j]
                secondPart = secondPart + aux
                secondPart_with_point = vectors.sumV(secondPart_with_point,vectors.constantMult(control_points[i][j], aux))
            downSum = downSum + (firstPart*secondPart)
            upperPart = vectors.sumV(upperPart, vectors.constantMult(secondPart_with_point, firstPart))
        return vectors.constantMult(upperPart, 1/downSum)
