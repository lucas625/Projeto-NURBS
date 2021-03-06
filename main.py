from auxiliars.helpers import getJson 
import auxiliars.vectors as vectors
import cam
import nurbs
import draw

entrada = getJson('entrada.json')#get the input

camIn = entrada['cam']
pointsIn = entrada['control_points']
weightsIn = entrada['weights']
knotsIn = entrada['knots']
degreesIn = entrada['degrees']

width = 1000
height = 1000
drawp = draw.Draw(width, height)#our class draw

nurbsVar = nurbs.Nurbs(#create the surface class
    degreesIn['Pdegree'], degreesIn['Qdegree'],
    len(pointsIn)-1, len(pointsIn[0])-1,
    pointsIn, knotsIn['P'], knotsIn['Q'], weightsIn
)

workingCam = cam.Cam(camIn)#prepare the cam
pointsIn = workingCam.organizePoints(pointsIn)#the control points after all camera transformation
nurbs_with_cam = nurbs.Nurbs(#create the surface class but with points already transformed
    degreesIn['Pdegree'], degreesIn['Qdegree'],
    len(pointsIn)-1, len(pointsIn[0])-1,
    pointsIn, knotsIn['P'], knotsIn['Q'], weightsIn
)
#control_screen = workingCam.find_control_screen(nurbs_with_cam.control_points, drawp.width, drawp.height)

bb = nurbsVar.bounding_Box()#our bounding box


def go_draw():
    p = []
    for i in range(len(nurbsVar.control_points)):
        p.append([])
        for j in range(len(nurbsVar.control_points[i])):
            aux = workingCam.organize_single_point(nurbsVar.control_points[i][j])
            p[i].append(workingCam.find_position_p(aux,drawp.width,drawp.height))
    print(p)
    drawp.drawPoints(p, 'go-', 'r', True)#control polygon
    drawp.order_draw()
    
def create_comands():
    #creates the string of commands
    c_all = []
    c_all.append('Commands: ')
    c_all.append('See the commands.')#0
    c_all.append('Change iterations')#1
    c_all.append('Load surface.')#2
    c_all.append('Find specific point.')#3
    c_all.append('Find tangent.')#4
    c_all.append('Find bounding box.')#5
    c_all.append('Draw.')#7
    c_all.append('Quit Program.')#7
    commands = ''
    for i in range(len(c_all)):
        if i>0:
            commands = commands + str(i-1) + ' - ' + c_all[i] + '\n'
        else:
            commands = commands + c_all[i] + '\n'
    return commands

def get_uv():
    #gets user input for parameters u and v
    print('Type 2 numbers.')
    inp1 = input()
    inp2 = input()
    ok = False
    while not ok:
        try:
            inp1 = float(inp1)
            inp2 = float(inp2)
            ok = True
        except:
            print("Sorry, invalid input.\nType two numbers again, please.")
            inp1 = input()
            inp2 = input()
    return [inp1, inp2]

def checkIn(inp, commands):
    #gets and takes care of user input
    if inp == '0':
        print(commands)
    elif inp == '1':
        print('Number of iterations: ')
        new_iterations = input()
        ok = False
        while not ok:
            try:
                new_iterations = int(new_iterations)
                if new_iterations > 0:
                    ok = True
                elif new_iteration == 0:
                    return True
                else:
                    raise Exception
            except:
                print("Sorry, invalid input.\nType the new number of iterations again, please.\nOr use 0 to cancel.")
                new_iterations = input()
        nurbsVar.set_iterations(new_iterations)
        nurbs_with_cam.set_iterations(new_iterations)

    elif inp == '2':
        #here we will draw the surface
        point_Screen = nurbsVar.find_surface(workingCam, drawp.width, drawp.height)#now we have the points on screen
        drawp.drawPoints(point_Screen, 'c-', '', False)

    elif inp == '3':
        #here we will find a specific point on the surface
        inp = get_uv()
        p = nurbsVar.nurbs_surface(inp[0],inp[1])
        p = workingCam.organize_single_point(p)
        p = workingCam.find_position_p(p,drawp.width,drawp.height)
        drawp.draw_single_p(p,'k')


    elif inp == '4':
        #here we will find a tangent
        inp = get_uv()
        p = nurbsVar.tangent(inp[0],inp[1])
        print("The tangent is: ")
        print(p)

    elif inp == '5':
        #here we will find the bounding box
        for i in range(len(bb)):
            aux = workingCam.organize_single_point(bb[i])
            bb[i] = workingCam.find_position_p(aux,drawp.width,drawp.height)
            drawp.draw_single_p(bb[i], 'y')

        drawp.draw_line(bb[0], bb[1], 'y-')
        drawp.draw_line(bb[0], bb[2], 'y-')
        drawp.draw_line(bb[0], bb[4], 'y-')
        drawp.draw_line(bb[1], bb[3], 'y-')
        drawp.draw_line(bb[1], bb[5], 'y-')
        drawp.draw_line(bb[2], bb[3], 'y-')
        drawp.draw_line(bb[2], bb[6], 'y-')
        drawp.draw_line(bb[3], bb[7], 'y-')
        drawp.draw_line(bb[4], bb[5], 'y-')
        drawp.draw_line(bb[4], bb[6], 'y-')
        drawp.draw_line(bb[5], bb[7], 'y-')
        drawp.draw_line(bb[6], bb[7], 'y-')
        

    elif inp == '6':
        go_draw()
        return False

    elif inp == '7':
        return False
    else: 
        print('invalid command, type again please.')
        return True
    return True
        

def keepExecuting():
    executing = True
    inp = 0
    commands = create_comands()
    print(commands)
    while(executing):
        print("Please use a command.")
        inp = input()
        executing = checkIn(inp, commands)

keepExecuting()
