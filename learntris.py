#!/usr/bin/python

from __future__ import print_function
WIDTH, HEIGHT = 10,22 
baseMatrix=[['.' for x in range(WIDTH)] for y in range(HEIGHT)]
matrix=[['.' for x in range(WIDTH)] for y in range(HEIGHT)]
score=0
ncl=0       #number of cleared lines
emptyRow= ['.' for x in range(WIDTH)]
tetraminoList=['I']
baseTetraminoMatrix=[['.' for x in range(4)] for y in range(4)]
tetramino=[['.' for x in range(4)] for y in range(4)]
#tetraminoIndex={ 'I':1}

def printMatrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])-1):
            print(matrix[y][x], end=' ')
        print(matrix[y][x+1], end='\n')

def saveMatrix():
    global matrix
    for y in range(HEIGHT):
        x_vec=raw_input()
        vec = (x_vec.split(' '))
        for i in range(len(vec)):
            matrix[y][i]=vec[i]

def clearMatrix():
    global matrix
    matrix=[['.' for x in range(WIDTH)] for y in range(HEIGHT)]

def step():
    global score, ncl, matrix
    for row in matrix:
        if not '.' in row:
            row[:] = emptyRow
            ncl=ncl+1
            score=score+100

def generateTetramino(tetraminoIndex):
    global tetramino
    if tetraminoIndex==1:
        tetramino[1] = ['c' for elem in tetramino[1]]

while(True):
    inp = raw_input()
    if (inp=='q'):
        break
    elif inp=='p':
        printMatrix(matrix)
    elif inp=='g':
        saveMatrix()
    elif inp=='c':
        clearMatrix()
    elif inp=='?s':
        print(score)
    elif inp=='?n':
        print(ncl)
    elif inp=='s':
        step()
    elif inp=='t':
        printMatrix(tetramino)
    elif inp=='I':
        generateTetramino(1)
