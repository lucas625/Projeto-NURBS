from auxiliars.helpers import getJson 
import auxiliars.vectors as vectors
import cam
import nurbs

entrada = getJson('example.json')#get the input

camIn = entrada['cam']
pointsIn = entrada['control_points']
weightsIn = entrada['weights']
knotsIn = entrada['knots']
degreesIn = entrada['degrees']

workingCam = cam.Cam(camIn)#prepare the cam
pointsIn = workingCam.organizePoints(pointsIn)#the control points after all camera transformation
nurbsVar = nurbs.Nurbs(#create the surface
    degreesIn['Pdegree'], degreesIn['Qdegree'],
    len(pointsIn)-1, len(pointsIn[0])-1,
    pointsIn, knotsIn['P'], knotsIn['Q'], weightsIn
)
print(nurbsVar)