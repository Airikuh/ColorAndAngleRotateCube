import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL.shaders
import ctypes
import pygame
import numpy
import pyrr


pygame.init()


verticies = (
    (-1, -1, -1),
    (-1, -1, 1),
    (-1, 1, 1),
    (-1, 1, -1),
    (1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (1, 1, -1)
    )

edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (4,5),
    (5,6),
    (6,7),
    (7,4),
    (0,4),
    (1,5),
    (2,6),
    (3,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)


    glTranslatef(0,0, -5)

    #glRotatef(25, 2, 1, 0)

#Setting initial to the color red
    glColor3f(1,0,0)


  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)

                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)
                if event.key == pygame.K_x:
                    glRotatef(90,1,0,0)
                if event.key == pygame.K_y:
                    glRotatef(90,0,1,0)
                if event.key == pygame.K_z:
                    glRotatef(90,0,0,1)

                if event.key == pygame.K_r:
                    glColor3f(1,0,0)
                if event.key == pygame.K_g:
                    glColor3f(0,1,0)
                if event.key == pygame.K_b:
                    glColor3f(0,0,1)




            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
