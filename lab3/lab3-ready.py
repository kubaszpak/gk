#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

# Constants
N = 50


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


# def spin(angle):
#     glRotatef(angle, 1.0, 0.0, 0.0)
#     glRotatef(angle, 0.0, 1.0, 0.0)
#     glRotatef(angle, 0.0, 0.0, 1.0)

def spin(time):
    angle = time * 180 / math.pi
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


def render_egg():
    tab = np.zeros((N, N, 3))
    u = [None] * N
    v = [None] * N
    last_val = 0
    for i in range(N):
        u[i] = last_val
        v[i] = last_val
        last_val += 1/(N-1)
    # print(u)
    for i in range(N):
        for j in range(N):
            tab[i][j][0] = (-90 * (u[i]**5) + 225 * (u[i]**4) - 270 * (u[i]
                            ** 3) + 180 * (u[i]**2) - 45 * u[i]) * math.cos(math.pi * v[j])
            tab[i][j][1] = 160 * (u[i]**4) - 320 * \
                (u[i]**3) + 160 * (u[i]**2) - 5
            tab[i][j][2] = (-90 * (u[i]**5) + 225 * (u[i]**4) - 270 * (u[i]
                            ** 3) + 180 * (u[i]**2) - 45 * u[i]) * math.sin(math.pi * v[j])

    # print(tab)

    # glBegin(GL_POINTS)
    # glColor3f(1.0, 1.0, 1.0)

    # for i in range(N):
    #     for j in range(N):
    #         glVertex(tab[i][j])
    # glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)

    for i in range(N - 1):
        for j in range(N - 1):
            glVertex(tab[i][j])
            glVertex(tab[i + 1][j])
            glVertex(tab[i][j])
            glVertex(tab[i][j + 1])
    glEnd()


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()

    render_egg()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(1/2 * time)

    axes()

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
