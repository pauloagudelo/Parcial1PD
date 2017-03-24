#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import random

class Matriz(object):

    def __init__(self, filas=None, columnas=None):
        if filas:
            self.filas=filas
        else:
            self.filas=int(raw_input("ingrese numero de filas: "))
        if columnas:
            self.columnas= columnas
        else:
            self.columnas = int(raw_input("ingrese numero de columnas: "))

    def crearMatrizA(self):
        self.matriz=[]
        for f in range(self.filas):
            self.matriz.append([0]*self.columnas)

    def llenarmatrizA(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = random.randint(1,20)
                #int(raw_input("ingrese %d, %d: " % (f, c)))
        return self.matriz

    def imprime_matriz(self):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(self.matriz[i][j]) + "\n"
                else:
                    cadena = cadena + str(self.matriz[i][j]) + "  "

        print "Matriz uno: "+'\n' + cadena

    def imprime_matrizC(self):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(self.matriz[i][j]) + "\n"
                else:
                    cadena = cadena + str(self.matriz[i][j]) + "  "

        print "Matriz dos: "+'\n' + cadena

    def imprime_matrizB(self,matrizB):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(matrizB[i][j]) + "\n"
                else:
                    cadena = cadena + str(matrizB[i][j]) + "  "
        return cadena

    def matriz_det(self,b):

        if (self.filas != self.columnas):
            print "la matriz no es cuadrada: "
            return True
        elif self.filas==2:
                a=1
                b=1
                for f in range(self.filas):
                    for c in range(self.columnas):
                        if f==c:
                            a*=self.matriz[f][c]
                        else:
                            b*=self.matriz[f][c]
                det=a-b

                print "la determinante es: "+str(det)
                return det
        else:
                m = self.matrizcopy(b)
                n = len(m)
                det = 1
                for i in range(n):
                    j = self.primeroNoNulo(m,i)
                    if j == n:
                        return 0
                    if i != j:
                        det = -1 * det
                        self.intercambiaFilas(m, i, j)
                    det = det * m[i][i]
                    self.multiplicaFila(m, i, 1. / m[i][i])
                    for k in range(i + 1, n):
                        self.combinacion(m, i, k, -m[k][i])

                print "La determinante es: " + str(det)
                return det

    def matrizcopy(self, matriz):
        self.result = []
        for f in matriz:
            self.result.append(f[:])
        return self.result

    def primeroNoNulo(self,m,i):
        result = i
        while result < len(m) and m[result][i] == 0:
            result = result + 1
        return result

    def intercambiaFilas(self, m,i,j):
        m[i], m[j] = m[j], m[i]

    def multiplicaFila(self, m, f, e):

        n = len(m)
        for c in range(n):
            m[f][c] = m[f][c] * e

    def transpuesta(self):
        if (self.filas != self.columnas):
            print "la matriz no es cuadrada: "
            return True
        self.matrizB = []
        for f in range(self.columnas):
            self.matrizB.append([0] * self.filas)

        for i in range(self.filas):
            for j in range(self.columnas):
                self.matrizB[j][i] = self.matriz[i][j]

        a=self.imprime_matrizB(self.matrizB)
        print "Matriz Transpuesta: " + '\n' + a
        return self.matrizB

    def matriz_numero(self):
            self.matrizB = []
            for f in range(self.columnas):
                self.matrizB.append([0] * self.filas)
            a = int(raw_input("ingrese el numero a multiplicar: "))

            if (self.filas != self.columnas):
                print "la matriz no es cuadrada: "
                return True

            for i in range(self.filas):
                for j in range(self.columnas):
                   self.matrizB[i][j]= self.matriz[i][j]*a
            b = self.imprime_matrizB(self.matrizB)
            print "el resultado es: " + '\n' + b


