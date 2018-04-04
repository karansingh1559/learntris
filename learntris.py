#!/usr/bin/python

from __future__ import print_function
WIDTH, HEIGHT = 10,22 
baseMatrix=[['.' for x in range(WIDTH)] for y in range(HEIGHT)]
matrix=[['.' for x in range(WIDTH)] for y in range(HEIGHT)]

def printMatrix():
    for y in range(HEIGHT):
        for x in range(WIDTH-1):
            print(matrix[y][x], end=' ')
        print(matrix[y][x+1], end='\n')

def saveMatrix():
    for y in range(HEIGHT):
        x_vec=raw_input()
        vec = (x_vec.split(' '))
        for i in range(len(vec)):
            matrix[y][i]=vec[i]

def clearMatrix():
    global matrix=[['.' for x in range(WIDTH)] for y in range(HEIGHT)]

while(True):
    inp = raw_input()
    if (inp=='q'):
        break
    elif inp=='p':
        printMatrix()
    elif inp=='g':
        saveMatrix()
    elif inp=='c':
        clearMatrix()
