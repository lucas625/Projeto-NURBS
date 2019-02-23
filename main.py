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
    degreesIn['Ndegree'], degreesIn['Mdegree'],
    pointsIn, knotsIn['P'], knotsIn['Q'], weightsIn
)
print(nurbsVar)