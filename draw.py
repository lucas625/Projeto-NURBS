import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

class Draw:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.Path = mpath.Path
        self.path_data = path_data = []

    def order_draw(self):
        plt.show()

    

    def drawPoints(self, control_points, color_line, color_p, with_p):
        #send a matrix and draw it, basically we will be using this for the control points
        a = len(control_points)
        b = len(control_points[0])
        for i in range(a):
            for j in range(b-1):
                #b00 -> b01
                x = [control_points[i][j][0], control_points[i][j+1][0]]
                y = [control_points[i][j][1], control_points[i][j+1][1]]
                if with_p:
                    plt.scatter(x, y, color=color_p, s=100)#ploting the 1st point
                    plt.scatter(x, y, color=color_p, s=100)#ploting the 1st point
                plt.plot(x, y, color_line, linewidth=3)
                
        for j in range(b):
            for i in range(a-1):
                if with_p:
                    x = [control_points[i][j][0], control_points[i+1][j][0]]
                    y = [control_points[i][j][1], control_points[i+1][j][1]]
                plt.plot(x, y, color_line, linewidth=3)


        
"""d = Draw()
pontos = [
    [
        [1,1], [1,3], [2,5]
    ],
    [
        [5,5], [2,7], [3,3]
    ]
]
d.drawPoints(pontos)
pontos1 = [
    [
        [0,0], [1,6], [12,22]
    ],
    [
        [4,1], [21,26], [77,46]
    ],
    [
        [13,32], [38,50], [24,47] 
    ]
]
#d.drawPoints(pontos1)
d.order_draw()"""