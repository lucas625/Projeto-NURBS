from auxiliars.helpers import getJson 
import auxiliars.vectors as vectors
import cam

entrada = getJson('entrada.json')#get the input

camIn = entrada['cam']
pointsIn = entrada['points']
weightsIn = entrada['weights']
knotsIn = entrada['knots']
degreesIn = entrada['degrees']

workingCam = cam.organizeCam(camIn)