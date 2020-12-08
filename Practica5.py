# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:08:35 2020

@author: Angel y Fabiola Alejandra 
"""

#Algoritmo de inserción
import numpy as np

def algoritmo_Insercion(lista):
  for i in range(1, len(lista)):
    #Guardamos el valor para comparar se inicia con el segundo de la lista
    actual = lista[i]
    #indica la posicion en la lista
    pos = i

    while pos > 0 and lista[pos - 1] > actual:
      #vamos moviendo la lista 
      lista[pos] = lista[pos - 1]
      pos -= 1

    lista[pos] = actual
  #se regresa la lista ordenada 
  return lista



for i in range(3):
  #generamos 8 numeros aleatorios del 1 al 30 y lo guardamos
  print("prueba: {}".format(i + 1))
  test = np.random.randint(1, 30, 8)
  print("Lista desordenada --> ", test)
  ordenada = algoritmo_Insercion(test)
  print("lista ordenada -->    ", ordenada)
  print()
  
