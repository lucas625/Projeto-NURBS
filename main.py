from auxiliars.helpers import getJson 
import auxiliars.vectors as vectors
import cam
import nurbs
import draw

entrada = getJson('example.json')#get the input

camIn = entrada['cam']
pointsIn = entrada['control_points']
weightsIn = entrada['weights']
knotsIn = entrada['knots']
degreesIn = entrada['degrees']


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
control_screen = workingCam.find_control_screen(nurbs_with_cam.control_points, 0, 0)
drawp = draw.Draw()#our class draw
point_Screen = []#our matrix with all points on the curve
p_s = [False]#if the point_Screen wasn't instancied yet
changed_iterations = [False]#if we changed the number of iterations
bb = nurbs_with_cam.bounding_Box()#our bounding box
go_bb = [False]
bb_screen = []


def go_draw():
    drawp.drawPoints(control_screen, 'go-', 'r', True)#control polygon
    drawp.order_draw()
    
def create_comands():
    #creates the string of commands
    c_all = []
    c_all.append('Commands: ')
    c_all.append('See the commands.')#0
    c_all.append('Change iterations')#1
    c_all.append('Draw surface.')#2
    c_all.append('Find specific point.')#3
    c_all.append('Find tangent.')#4
    c_all.append('Find bounding box.')#5
    c_all.append('Quit Program.')#6
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
                    changed_iterations[0] = True
                elif new_iteration == 0:
                    return True
                else:
                    raise Exception
            except:
                print("Sorry, invalid input.\nType the new number of iterations again, please.\nOr use 0 to cancel.")
                new_iterations = input()
        nurbsVar.set_iterations(new_iterations)

    elif inp == '2':
        #here we will draw the surface
        if changed_iterations[0] or (not p_s[0]):
            point_Screen = nurbs_with_cam.find_surface(workingCam)#now we have the points on screen
        changed_iterations[0] = False
        p_s[0] = True
        drawp.drawPoints(point_Screen, 'c-', '', False)
        go_draw()


    elif inp == '3':
        #here we will find a specific point on the surface
        inp = get_uv()
        p = nurbsVar.nurbs_surface(inp[0],inp[1])
        print("The point is: ")
        print(p)
            #still need to draw

    elif inp == '4':
        #here we will find a tangent
        inp = get_uv()
        p = nurbsVar.tangent(inp[0],inp[1])
        print("The tangent is: ")
        print(p)

    elif inp == '5':
        #here we will find the bounding box
        if not go_bb[0]:
            bb_p = workingCam.find_position_p(bb, 0, 0)
        for i in range(len(bb_p)):
            bb_screen.append([])
            for j in range(len(bb_p[0])):
                bb_screen.append(bb_p[i][j])

        drawp.drawPoints(bb, 'k-', 'y', True)#control polygon
        go_draw()

    elif inp == '6':
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
        executing = checkIn(inp, commands, )

keepExecuting()