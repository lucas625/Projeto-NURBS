class Draw:
    def __init__(self, our_svg, width, height):
        self.our_svg = our_svg
        self.width = width
        self.height = height
        self.write_start_svg()

    def write_start_svg(self):
        inicio = '<svg version="1.1" baseProfile="full" width="'+str(self.width)+'" height="'+str(self.height)+'" xmlns="http://www.w3.org/2000/svg">\n'
        self.our_svg.write(inicio)

    def order_draw(self):
        self.our_svg.write('</svg>')
        self.our_svg.close()

    def draw_single_p(self, point, color_p, tamanho):
        inicio = '<circle cx="'+str(point[0])+'" cy="'+str(point[1])+'" r="'+str(tamanho)+'" stroke="'+str(color_p)+'" fill="'+str(color_p)+'" stroke-width="1"/>\n'
        self.our_svg.write(inicio)

    def draw__line(self, point1, point2, color_p, tamanho):
        inicio = '<line x1="'+str(point1[0])+'" y1="'+str(point1[1])+'" x2="'+str(point2[0])+'" y2="'+str(point2[1])+'" style="stroke:'+str(color_p)+';stroke-width:'+str(tamanho)+'" />\n'
        self.our_svg.write(inicio)

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
                    self.draw_single_p([x[0],y[0]], color_p, 6)#ploting the 1st point
                    self.draw_single_p([x[1],y[1]], color_p, 6)#ploting the 2st point
                self.draw__line([x[0],y[0]], [x[1],y[1]], color_line, 1)
                
        for j in range(b):
            for i in range(a-1):
                #b00 -> b10
                x = [control_points[i][j][0], control_points[i+1][j][0]]
                y = [control_points[i][j][1], control_points[i+1][j][1]]
                self.draw__line([x[0],y[0]], [x[1],y[1]], color_line, 1)

    """def draw_bouding_box(self, bb, color_line, color_p):
        for i in range(len(bb)-1):
            x = [bb[i][0], bb[i+1][0]]
            y = [bb[i][1], bb[i+1][1]]
            plt.scatter(x, y, color=color_p, s=100)
            plt.plot(x, y, color_line, linewidth=3)
        for i in range(len(bb)-2):
            x = [bb[i][0], bb[i+2][0]]
            y = [bb[i][1], bb[i+2][1]]
            plt.plot(x, y, color_line, linewidth=3)
        for i in range(len(bb)-4):
            x = [bb[i][0], bb[i+4][0]]
            y = [bb[i][1], bb[i+4][1]]
            plt.plot(x, y, color_line, linewidth=3)"""
        
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