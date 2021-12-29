#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render_rectangle_from_middle(x, y, a, b):
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(x - 0.5 * a, y - 0.5 * b)
    glVertex2f(x - 0.5 * a, y + 0.5 * b)
    glVertex2f(x + 0.5 * a, y - 0.5 * b)
    glVertex2f(x + 0.5 * a, y + 0.5 * b)
    glEnd()


def render_rectangle(x, y, a, b, d=0.0):

    deform = 1 + d

    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(x, y)
    glVertex2f(x, y + b * deform)
    glVertex2f(x + a * deform, y)
    glVertex2f(x + a * deform, y + b * deform)
    glEnd()


def sierpinski_iteration(x, y, w, h, iteration):

    if(iteration >= 3):
        return
    else:
        iteration += 1

    new_w = w / 3
    new_h = h / 3

    render_rectangle_from_middle(x - w, y + h, new_w, new_h)
    sierpinski_iteration(x - w, y + h, new_w, new_h, iteration)
    render_rectangle_from_middle(x, y + h, new_w, new_h)
    sierpinski_iteration(x, y + h, new_w, new_h, iteration)
    render_rectangle_from_middle(x + w, y + h, new_w, new_h)
    sierpinski_iteration(x + w, y + h, new_w, new_h, iteration)
    render_rectangle_from_middle(x + w, y, new_w, new_h)
    sierpinski_iteration(x + w, y, new_w, new_h, iteration)
    render_rectangle_from_middle(x + w, y - h, new_w, new_h)
    sierpinski_iteration(x + w, y - h, new_w, new_h, iteration)
    render_rectangle_from_middle(x, y - h, new_w, new_h)
    sierpinski_iteration(x, y - h, new_w, new_h, iteration)
    render_rectangle_from_middle(x - w, y - h, new_w, new_h)
    sierpinski_iteration(x - w, y - h, new_w, new_h, iteration)
    render_rectangle_from_middle(x - w, y, new_w, new_h)
    sierpinski_iteration(x - w, y, new_w, new_h, iteration)


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    # glColor3f(0.0, 1.0, 0.0)
    # glBegin(GL_TRIANGLES)
    # glVertex2f(0.0, 0.0)
    # glVertex2f(0.0, 50.0)
    # glVertex2f(50.0, 0.0)
    # glEnd()

    # glColor3f(1.0, 0.0, 0.0)
    # glBegin(GL_TRIANGLES)
    # glVertex2f(0.0, 0.0)
    # glVertex2f(0.0, 50.0)
    # glVertex2f(-50.0, 0.0)
    # glEnd()

    # glColor3f(1.0, 0.4, 0.2)
    # random.seed(10)
    # render_rectangle(-25, -25, 50, 50, random.uniform(0, 1))

    def sierpinski():
        glClear(GL_COLOR_BUFFER_BIT)

        x = 0
        y = 0

        height = 80
        width = 120

        glColor3f(0.0, 0.5, 1.0)
        render_rectangle_from_middle(x, y, width, height)

        h = height / 3
        w = width / 3

        glColor3f(1.0, 1.0, 1.0)
        render_rectangle_from_middle(x, y, w, h)

        sierpinski_iteration(x, y, w, h, 0)

    sierpinski()

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
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

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
