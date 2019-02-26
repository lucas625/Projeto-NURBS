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

    def surface(self, point1,point2,point3,point4):
        draw.path.append((Path.MOVETO, (p1[0],p1[1])))
        draw.path.append((Path.LINETO, (p2[0],p2[1])))
        draw.path.append((Path.LINETO, (p4[0],p4[1])))
        draw.path.append((Path.MOVETO, (p1[0],p1[1])))
        draw.path.append((Path.LINETO, (p3[0],p3[1])))
        codes, verts = zip(*self.path_data)
        path = mpath.Path(verts, codes)
        x,y = zip(*path.vertices)
        line,  = self.ax.plot(x,y,'c')

    def drawPoints(self, control_points):
        #send a matrix to the Path
        a = len(control_points)
        b = len(control_points[0])
        for i in range(a):
            for j in range(b-1):
                #b00 -> b01
                self.path_data.append((self.Path.MOVETO, (control_points[i][j][0],control_points[i][j][1])))
                self.path_data.append((self.Path.LINETO, (control_points[i][j][0],control_points[i][j+1][1])))
        for j in range(b):
            for i in range(a-1):
                self.path_data.append((self.Path.MOVETO, (control_points[i][j][0],control_points[i][j][1])))
                self.path_data.append((self.Path.LINETO, (control_points[i+1][j][0],control_points[i+1][j][1])))

        self.path_data.append((self.Path.MOVETO, (control_points[a-1][j-1][0],control_points[i-1][j-1][1])))
        self.path_data.append((self.Path.LINETO, (control_points[0][0][0],control_points[0][0][1])))
        codes, verts = zip(*self.path_data)
        path = mpath.Path(verts, codes)
        x,y = zip(*path.vertices)
        line,  = self.ax.plot(x,y,'go-')

        
d = Draw()
pontos = [
    [
        [1,1], [1,3], [2,5]
    ],
    [
        [1,5], [2,7], [3,3]
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
d.order_draw()