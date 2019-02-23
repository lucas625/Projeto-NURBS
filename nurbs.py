import auxiliars.vectors as vectors
import ipdb

def checkSpan(u1,u2,u):
    # ui <= u < u1+1
    if u1<=u and u<u2:
        return 1
    else:
        return 0

def initializeN(n):
    #inicializa o vetor N com n listas
    N = []
    for a in range(0,n+1):
        N.append([])
    return N

def bsplineBFunction(knots, u, i, p):
    #the B-spline basis function
    if p==0:
        return checkSpan(knots[i], knots[i+1], u)
    N1 = bsplineBFunction(knots,u,i,p-1)
    aux1 = 0
    if N1!=0:
        aux1 = (N1*(u-knots[i])) / (knots[i+p]-knots[i])
    N2 = bsplineBFunction(knots,u,i+1,p-1)
    aux2 = 0
    if N2!=0:
        aux2 = (N2*(knots[i+p+1] - u)) / (knots[i+p+1] - knots[i+1])
    return aux1 + aux2

def bSplineP(points,knots, u, n, k):
    #returns a point on a bspline curve
    PCurve = vectors.createEmptyVector(len(points[0]))
    for a in range(n+1):
        PCurve = vectors.sumV(PCurve, vectors.constantMult(points[a],bsplineBFunction(knots, u, a, k)))
    return PCurve
    


knots = [0 , 0.25, 0.5, 0.75, 1]
points = [
    [1,1,1],
    [0,2,3],
    [3,2,4]
]
u = 0
n = 2
k = 1
print(bSplineP(points, knots, u, n, k))
