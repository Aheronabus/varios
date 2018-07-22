#!/usr/bin/python
#-*- coding: utf-8 -*-

#Importacion de librerias

import os
import time
from random import randint, uniform, random

#Declaracion de Variables globales 

a = 0				  #Numero mas pequeño posible (INICIAL)
b = 9 				  #Numero mas grande posible (INICIAL)
lengthNum = 1		  #Cantidad cifras (INICIAL)
i = 1				  #Intentos (INICIAL)
maxI = 5              #Intentos maximos (INICIAL)
aumento_a = 10        #Aumento de a, al pasar de nivel (INICIAL)
aumento_b = 90        #Aumento de b, al pasar de nivel (INICIAL)

def arcade():

	num_al = randint(a,b) #Numero aleatorio	
	
	while(i<=maxI): #Mientras intentos, sea menor o igual que la cantidad maxima de intentos, haz esto:

		os.system("cls")
		print("Estoy pensando en un numero de "+repr(lengthNum)+" cifras. Puedes adivinarlo?")
		print("Tienes "+repr((maxI+1)-i)+" intentos")
		print("*_* El numero es: "+repr(num_al)+" *_*")
		numInput = input("---> ")
		if (numInput == num_al):
			print("Felicitaciones, has descubierto el numero en tan solo "+repr(i)+" intentos.")
			global a,b,i,maxI,aumento_a,aumento_b,lengthNum      #Importacion de variables globales para su modificacion
			a = a + aumento_a
			b = b + aumento_b
			i = 1
			maxI = maxI + 5 #Aumento progresivo de la dificultad
			aumento_a = aumento_a * 10
			aumento_b = aumento_b * 10
			lengthNum += 1
			num_al = randint(a,b)
			time.sleep(3)
		
		elif(numInput < num_al):
			print("El numero es mayor")
			i += 1
			time.sleep(1)
		elif(numInput > num_al):
			print("El numero es menor")
			i += 1
			time.sleep(1)

	os.system("cls")
	print("Lo siento, no has logrado adivinar el numero.")		
	print("El numero era: "+repr(num_al))

arcade()
