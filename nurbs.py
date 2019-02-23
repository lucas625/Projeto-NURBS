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

    def find_interval(self, knots, value):
        for i in range(len(knots)):
            if ( knots[i] <= value and value < knots[i+1] ):
                return i
        else:
            raise("value is not inside any knot span", value)

    def bsplineP(self, knots, u, k, control_points, n):
        """
        knots: a list with knot positions
        u: value between a knot span
        k: degree of the curve
        control_points: a list with control points
        n: len(control_points), the number of control points
        """
        p_curve = vectors.createEmptyVector(len(control_points[0]))
        interval = self.find_interval(knots,u)
        for i in range(n+1):
            p_curve = vectors.sumV(p_curve, vectors.constantMult(control_points[i], self.bsplineBFunction(knots, u, i, k)))
        print(p_curve)
        return p_curve


valor = 0
knots = [0, 0, 0, 1, 2, 3, 3, 4, 4, 4]
ka = 2
points = [[0,1], [1,1],[3, 4], [4, 2], [5, 3], [6, 4], [7, 3]]
Nub = Nurbs(2,0,1,0,points,knots,[],[])
Nub.bsplineP(knots, valor, ka, points, len(points)-1)