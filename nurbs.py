import auxiliars.vectors as vectors
import ipdb
import cam


class Nurbs:

    def __init__(self, p, q, n, m, points, knotsP, knotsQ, weights):
        self.p = p
        self.q = q
        self.n = n
        self.m = m
        self.control_points = vectors.clone_m(points)
        self.knotsP = vectors.cloneV(knotsP)
        self.knotsQ = vectors.cloneV(knotsQ)
        self.weights = weights
        self.weights = self.clone_weights()
        self.iterations = 50
        #self.normalize_knots()
        #self.normalize_weight()

    def clone_weights(self):
        aux = []
        for i in range(len(self.weights)):
            aux.append(vectors.cloneV(self.weights[i]))
        return aux

    def normalize_knots(self):
        self.knotsP = vectors.normalize(self.knotsP)
        self.knotsQ = vectors.normalize(self.knotsQ)

    def normalize_weight(self):
        totalSum = 0
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                    totalSum = totalSum + self.weights[i][j]
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                    self.weights[i][j] = self.weights[i][j] / totalSum


    def __str__(self):
        p = "p: " + str(self.p)
        q = "q: " + str(self.q)
        n = "n: " + str(self.n)
        m = "m: " + str(self.m)
        control_points = "control points: " + str(self.control_points)
        knotsP = "knotsP: " + str(self.knotsP)
        knotsQ = "knotsQ: " + str(self.knotsP)
        weights = "weights: " + str(self.weights)
        return (p + "\n" + q + "\n" + n + "\n" + m +
             "\n" + control_points + "\n" + knotsP + "\n" + knotsQ +
                  "\n" + weights + "\n")

    def set_iterations(self, val):
        #set the total number of iterations
        self.iterations = val

    def checkSpan(self,u1,u2,u):
        # ui <= u < u1+1
        if u1<=u and u<u2:
            return 1
        else:
            return 0

    def bsplineBFunction(self, knots, u, i, p):
        #the B-spline basis function
        """
            knots: list of knots that has a interval that contais u
            u: position
            i: actual interval
            p: degree
        """
        if p==0:
            try:
                return self.checkSpan(knots[i], knots[i+1], u)
            except:
                print("deu erro", i)
                raise()
        N1 = self.bsplineBFunction(knots,u,i,p-1)
        aux1 = 0
        if N1!=0:
            aux1 = (N1*(u-knots[i])) / (knots[i+p]-knots[i])
        N2 = self.bsplineBFunction(knots,u,i+1,p-1)
        aux2 = 0
        if N2!=0:
            aux2 = (N2*(knots[i+p+1] - u)) / (knots[i+p+1] - knots[i+1])
        return aux1 + aux2

    def nurbs_surface(self, u, v):
        #computes a point on the surface
        """
            knotsP: list of knots that contains knots relative to p degree
            knotsQ: list of knots that contains knots relative to q degree
            p: first degree
            q: second degree
            control_points: matrix of control_points
            n: points degree(line)
            m: points degree(column)
            weights: matrix of weights
            u: first parameter
            v: second parameter
        """
        #initializing
        knotsP = self.knotsP
        knotsQ = self.knotsQ
        p = self.p
        q = self.q
        n = self.n
        m = self.m
        control_points = self.control_points
        weights = self.weights
        #
        downSum = 0
        upperPart = vectors.createEmptyVector(len(control_points[0][0]))
        for i in range(n+1):
            firstPart = self.bsplineBFunction(knotsP,u,i,p)
            if(firstPart!=0):
                secondPart = 0
                secondPart_with_point = vectors.createEmptyVector(len(control_points[0][0]))
                for j in range(m+1):
                    aux = self.bsplineBFunction(knotsQ,v,j,q)*weights[i][j]
                    if(aux!=0):
                        secondPart = secondPart + aux
                        secondPart_with_point = vectors.sumV(secondPart_with_point,vectors.constantMult(control_points[i][j], aux))
                downSum = downSum + (firstPart*secondPart)
                upperPart = vectors.sumV(upperPart, vectors.constantMult(secondPart_with_point, firstPart))
        #ipdb.set_trace()
        if(downSum!=0):
            return vectors.constantMult(upperPart, 1/downSum)
        else:
            return upperPart
    
    def find_surface(self, camera, width, height):
        #find every point of the surface and put it on the path
        #path is the var for drawing
        #cam is the camera
        plots =[]#this will be send to a function on draw.py to draw all points on it
        #we are using them equal to 0 because we are using mathplot lib
        for i in range(self.iterations):
            plots.append([])
            for j in range(self.iterations):
                p1 = 0
                if i == 0 and j == 0:
                    p1 = self.control_points[0][0]

                else:
                    p1 = self.nurbs_surface(i/self.iterations, j/self.iterations)
                print(p1)
                #we have the points, now we need to find the projection since they are already transformed them
                p1 = camera.organize_single_point(p1)
                #p1 = camera.find_position_p(p1,width,height)
                plots[i].append(p1)
        return plots
                

    def calculate_Q(self, knots, actual, degree):
        # reference: https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/B-spline/bspline-derv.html
        #ps: the deltaP will be calculated on tangent.
        return degree / (knots[actual+degree+1] - knots[actual+1])
        
    def tangent(self, u, v):
        #calculates the tangent of a nurbs curve
        #initializing
        control_points = self.control_points
        knotsQ = self.knotsQ
        knotsP = self.knotsP
        weights = self.weights
        n = self.n
        m = self.m
        p = self.p
        q = self.q
        #now calculating the parts without derivatives for the division rule of derivation
        downSum = 0
        upperPart = vectors.createEmptyVector(len(control_points[0][0]))
        for i in range(n+1):
            firstPart = self.bsplineBFunction(knotsP,u,i,p)
            secondPart = 0
            secondPart_with_point = vectors.createEmptyVector(len(control_points[0][0]))
            for j in range(m+1):
                aux = self.bsplineBFunction(knotsQ,v,j,q)*weights[i][j]
                secondPart = secondPart + aux
                secondPart_with_point = vectors.sumV(secondPart_with_point,vectors.constantMult(control_points[i][j], aux))
            downSum = downSum + (firstPart*secondPart)
            upperPart = vectors.sumV(upperPart, vectors.constantMult(secondPart_with_point, firstPart))
        #notice that downSum has the bottom part without being derivated and upperPart has the top vector without being derivated
        #calculating derivative based on u
        downSumU = 0
        upperPartU = vectors.createEmptyVector(len(control_points[0][0]))
        for i in range(n):
            firstPart = self.bsplineBFunction(knotsP,u,i+1,p-1)
            Q = self.calculate_Q(knotsP, i, p)
            secondPart = 0
            secondPart_with_point = vectors.createEmptyVector(len(control_points[0][0]))
            for j in range(m+1):
                aux = self.bsplineBFunction(knotsQ,v,j,q)#this is constant in the derivation
                secondPart = secondPart + aux*weights[i][j]
                deltaP = vectors.subV(vectors.constantMult(control_points[i+1][j], weights[i+1][j]), vectors.constantMult(control_points[i][j], weights[i][j]))
                secondPart_with_point = vectors.sumV(secondPart_with_point,vectors.constantMult(deltaP, aux))
            downSumU = downSumU + (firstPart*secondPart*Q)
            totalMult = firstPart * Q
            upperPartU = vectors.sumV(upperPartU, vectors.constantMult(secondPart_with_point, totalMult))
        # now we have the up derivative for U, the down derivative for U, the down common and the up common, and now we can use the derivative division rule
        partialU = vectors.constantMult(vectors.subV(vectors.constantMult(upperPartU, downSum), vectors.constantMult(upperPart, downSumU)), (1/(downSum**2)))
        #now lets calculate the partialV, since we already have the down and up common, we only need the derivative based on v
        downSumV = 0
        upperPartV = vectors.createEmptyVector(len(control_points[0][0]))
        for i in range(n+1):
            firstPart = self.bsplineBFunction(knotsP,u,i,p)
            secondPart = 0
            secondPart_with_point = vectors.createEmptyVector(len(control_points[0][0]))
            for j in range(m):
                aux = self.bsplineBFunction(knotsQ,v,j+1,q-1)#this is constant in the derivation
                Q = self.calculate_Q(knotsQ, j, q)
                secondPart = secondPart + (aux*weights[i][j]*Q)
                deltaP = vectors.subV(vectors.constantMult(control_points[i][j+1], weights[i][j+1]),vectors.constantMult(control_points[i][j], weights[i][j]))
                secondPart_with_point = vectors.sumV(secondPart_with_point,vectors.constantMult(deltaP, aux))
            downSumV = downSumV + (firstPart*secondPart)
            upperPartV = vectors.sumV(upperPartV, vectors.constantMult(secondPart_with_point, firstPart))
        #now to partialV
        partialV = vectors.constantMult(vectors.subV(vectors.constantMult(upperPartV, downSum), vectors.constantMult(upperPart, downSumV)), (1/(downSum**2)))
        return vectors.crossProduct(partialU, partialV)

    def bounding_Box(self):
        max_x = self.control_points[0][0][0]
        min_x = self.control_points[0][0][0]
        max_y = self.control_points[0][0][1]
        min_y = self.control_points[0][0][1]
        max_z = self.control_points[0][0][2]
        min_z = self.control_points[0][0][2]
        #now we have to find the real max/min
        for i in range(len(self.control_points)):
            for j in range(len(self.control_points[i])):
                aux = self.control_points[i][j]

                if(aux[0]>max_x):
                    max_x = aux[0]
                elif(aux[0]<min_x):
                    min_x = aux[0]

                if(aux[1]>max_y):
                    max_y = aux[1]
                elif(aux[1]<min_y):
                    min_y = aux[1]

                if(aux[2]>max_z):
                    max_z = aux[2]
                elif(aux[2]<min_z):
                    min_z = aux[2]

        points = []
        points.append([min_x,min_y,min_z])
        points.append([min_x,min_y,max_z])
        points.append([min_x,max_y,min_z])
        points.append([min_x,max_y,max_z])

        points.append([max_x,min_y,min_z])
        points.append([max_x,min_y,max_z])
        points.append([max_x,max_y,min_z])
        points.append([max_x,max_y,max_z])
        return points
