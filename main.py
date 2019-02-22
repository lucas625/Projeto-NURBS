from auxiliars.helpers import getJson 
import auxiliars.vectors as vectors


entrada = getJson('entrada.json')#get the input

cam = entrada['cam']
points = entrada['points']
weights = entrada['weights']
knots = entrada['knots']
degrees = entrada['degrees']