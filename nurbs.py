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

def bsplineBFunction(knots, u, i, p, ar):
    if p==0:
        auxS = 'N'+str(i)+str(p)
        ar[auxS] = checkSpan(knots[i], knots[i+1], u)
        return checkSpan(knots[n], knots[i+1], u)
    aux1 = bsplineBFunction(knots,u,i,p-1, ar)*((u-knots[i]) / (knots[i+p]-knots[i]))
    aux2 = bsplineBFunction(knots,u,i+1,p-1, ar)*((knots[i+p+1] - u) / (knots[i+p+1] - knots[i+1]))
    auxS = 'N'+str(i)+str(p)
    ar[auxS] = aux1 + aux2
    return aux1 + aux2

def bSpline(points,knots, u, n, k):
    ar = {

    }
    for a in range(n+1):
        bsplineBFunction(knots, u, a, k, ar)
    print(ar)


knots = [0,0.25,0.5,0.75,1]
points = []
u = 0.1
n = 2
k = 1
bSpline(points, knots, u, n, k)
