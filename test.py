import auxiliars.vectors as vectors
def deBoor(k, x, t, c, p):
    """
    Evaluates S(x).

    Args
    ----
    k: index of knot interval that contains x
    x: position
    t: array of knot positions, needs to be padded as described above
    c: array of control points
    p: degree of B-spline
    """
    d = [c[j + k - p] for j in range(0, p+1)]
    for r in range(1, p+1):
        for j in range(p, r-1, -1):
            print(j,k,p)
            alpha = (x - t[j+k-p]) / (t[j+1+k-r] - t[j+k-p])
            d[j] = vectors.sumV(vectors.constantMult(d[j-1], (1.0 - alpha)), vectors.constantMult(d[j], alpha))
    return d[p]

#

def find_interval(knots, value):
    for i in range(len(knots)):
        if ( knots[i] <= value and value < knots[i+1] ):
            return i
    else:
        raise("value is not inside any knot span", value)

def find_alpha(valor, knots, degree, i, r):
    return (valor - knots[i]) / (knots[i+1+degree-r] - knots[i])

def de_boor(value, knots, points, degree):
    k = find_interval(knots, value)#finding the interval
    d = [c[j + k - degree] for j in range(degree+1)]#starting the temp ctrl points
    for r in range(1, p+1):
        for i in range(k-degree+r, degree+1):
            alpha = find_alpha(value,knots,degree,i,r)
            d[i] = (1.0 - alpha) * d[i-1] + alpha * d[i]



valor = 0.9
knots = [0,0.25,0.5,0.75,1]
ka = 2
n = 1
points = [(1,1,1), (1,3,4), (2,2,5), (0,2,4)]
interval = find_interval(knots, valor)
print(deBoor(interval, valor, knots, points, ka))