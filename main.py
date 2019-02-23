from auxiliars.helpers import getJson 
import auxiliars.vectors as vectors
import cam
import nurbs

entrada = getJson('example.json')#get the input

camIn = entrada['cam']
pointsIn = entrada['points']
weightsIn = entrada['weights']
knotsIn = entrada['knots']
degreesIn = entrada['degrees']

workingCam = cam.organizeCam(camIn)
nurbsVar = nurbs.Nurbs(
    degreesIn['Pdegree'], degreesIn['Qdegree'],
    len(pointsIn)-1, len(pointsIn[0])-1,
    pointsIn, knotsIn['P'], knotsIn['Q'], weightsIn
)

ponto = nurbsVar.nurbs_surface(nurbsVar.knotsP, nurbsVar.knotsQ, nurbsVar.p, nurbsVar.q, nurbsVar.n, nurbsVar.m,
 nurbsVar.control_points, nurbsVar.weights, 0.1, 0.5)
print(ponto)