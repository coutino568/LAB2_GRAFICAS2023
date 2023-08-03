
import random
from gl import Renderer
import math
from obj import *
from mathcou import *
from shader import *
from collections import namedtuple

objetos =[]


V2 = namedtuple('Point2', ['x', 'y'])




windoWidth = 1920*1
windowHeight = 1080*1
scale= 1
viewportWidth= windoWidth*scale
viewportHeight= windowHeight *scale
viewportX=0
viewportY=0

M = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
Angulox=0
Anguloy=0
Anguloz=0

myRenderer = Renderer(windoWidth, windowHeight)
myRenderer.glViewPort(viewportX,viewportY,viewportWidth,viewportHeight)




# matrix1= [[1,2,3],[2,6,9],[5,0,4]]
# matrix2 = [[3,6,1],[8,0,7],[1,0,42]]


# resultadoMatrices= matrixVectorMultiplication(matrix1,matrix2)
objetito = Object("object.obj","texture.bmp")

objetos.append(objetito)


def transformarVertices():
    for objeto in objetos:
        for vert in objeto.vertices:
            # print(vert)
            vert= vertexShader(vert)
            # print(vert)
    



def renderizar():
    ## dibujara los objetos en el origen por el momento pero hay que hacer el pipeline de transformaciones.
    for objeto in objetos:
        for face in objeto.faces:
            print("HARE UN TRIANGULO CON ESTOS VERTICES :"+ str(face))
            vert1= objeto.vertices[face[0][0]-1]
            vert2= objeto.vertices[face[1][0]-1]
            vert3= objeto.vertices[face[2][0]-1]
            print(vert1)
            print(vert2)
            print(vert3)
            myRenderer.glTriangle3(vert1,vert2,vert3)

transformarVertices()
renderizar()


  
    


# A=[90,50]
# B=[1700,200]
# C=[150,1000]

# A=[random.randrange(0,windoWidth), random.randrange(0,windowHeight)]
# B=[random.randrange(0,windoWidth), random.randrange(0,windowHeight)]
# C=[random.randrange(0,windoWidth), random.randrange(0,windowHeight)]

# print(A,B,C)
# myRenderer.glTriangle3(A,B,C)
# myRenderer.glTriangle2(A,B,C)




myRenderer.glFinish("output.bmp")