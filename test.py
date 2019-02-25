from auxiliars.helpers import getJson 
import auxiliars.vectors as vectors
import cam
import nurbs
import numpy as np
entrada = getJson('example.json')#get the input

camIn = entrada['cam']
pointsIn = entrada['control_points']
weightsIn = entrada['weights']
knotsIn = entrada['knots']
degreesIn = entrada['degrees']

nurbsVar = nurbs.Nurbs(
    degreesIn['Pdegree'], degreesIn['Qdegree'],
    len(pointsIn)-1, len(pointsIn[0])-1,
    pointsIn, knotsIn['P'], knotsIn['Q'], weightsIn
)
"""
ponto = nurbsVar.nurbs_surface(0.2, 0.4)

print(nurbsVar.calculate_Q(nurbsVar.knotsP, 1, nurbsVar.p))
print(nurbsVar.calculate_Q(nurbsVar.knotsQ, 2, nurbsVar.q))
print(ponto)
print(nurbsVar.tangent(0.2,0.4))
print(nurbsVar)
"""
a = [1,2,3,4]
print(a)
print(np.array(a))
print(a)
a = np.array(a)[np.newaxis]
print(a)
print(a.T)
print(a.tolist())