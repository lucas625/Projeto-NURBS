import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

def drawPoints(control_points):
    fig, ax = plt.subplots()

    Path = mpath.Path

    path_data = []

    for i in range(len(control_points)-1):
        for j in range(len(control_points[i])-1):
            #b00 -> b01
            path_data.append((Path.MOVETO, (control_points[i][j][0],control_points[i][j][1])))
            path_data.append((Path.LINETO, (control_points[i][j+1][0],control_points[i][j+1][1])))

            #b00 -> b10
            path_data.append((Path.MOVETO, (control_points[i][j][0],control_points[i][j][1])))
            path_data.append((Path.LINETO, (control_points[i+1][j][0],control_points[i+1][j][1])))

    #path_data.append(Path.CLOSEPOLY, (control_points[], -2.57))
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)

    x,y = zip(*path.vertices)
    line,  = ax.plot(x,y,'go-')

    plt.show()

pontos = [
    [
        [1,1], [2,2], [4,6]
    ],
    [
        [2,3], [4,6], [7,6]
    ],
    [
        [1,3], [8,10], [4,7] 
    ]
]
drawPoints(pontos)