import time
import random
#Tarea 1 Análisis de algoritmos
#Jose Enrique Alvarado Chaves 201129079

def listRandomGenerator(largo):
   numberList = []
   if(largo>1):
       for i in range(1,largo):
           number = int(random.uniform(0,500))
           numberList.append(number)
   return numberList

def listGeneratorDec(largo):
   numberList = []
   if(largo>1):
       cont=largo
       while(cont>0):
           numberList.append(cont)
           cont=cont-1
   return numberList

def listGeneratorAc(largo):
   numberList = []
   if(largo>1):
       cont=1
       while(cont<largo+1):
           numberList.append(cont)
           cont=cont+1
   return numberList

#Esta función fue tomada de internet, para medir el tiempo de un algoritmo.
#URL: http://elviajedelnavegante.blogspot.com/2010/06/calcular-tiempos-de-ejecucion-en-python.html
def cronometro(funcion):
   def funcion_a_ejecutar(*argumentos):
       # Tiempo de inicio de ejecución.
       inicio = time.time()
       # Lanzamos función a ejecutar.
       ret = funcion(*argumentos)
       # Tiempo de fin de ejecución.
       fin = time.time()
       # Tiempo de ejecución.
       tiempo_total = fin - inicio
       # Devolvemos el tiempo de ejecución.
       return tiempo_total
   # Devolvemos la función que se ejecuta.
   return funcion_a_ejecutar

def bubbleSort(pList):
    num = len(pList)
    lenCounter= 0
    while (lenCounter < num):
        Counter = lenCounter
        while (Counter < num):
            if(pList[lenCounter] > pList[Counter]):
                temp = pList[lenCounter]
                pList[lenCounter] = pList[Counter]
                pList[Counter] = temp
            Counter= Counter+1
        lenCounter=lenCounter+1

def selectionSort(pList):
     for actualPosition in range(0, len(pList)):
         minimum = actualPosition
         for auxiliarPosition in range(actualPosition+1, len(pList)):
             if pList[auxiliarPosition] < pList[minimum]:
                 minimum = auxiliarPosition
         temp = pList[actualPosition]
         pList[actualPosition] = pList[minimum]
         pList[minimum] = temp

#Esta funcción se encarga de dar un conjunto de tiempos conforme la lista crece en tamaño
def getTimerOfSort():
    counter=5000
    print("Calculo Bubble Sort con :")
    while(counter<35000):
        numberList=listRandomGenerator(counter)
        print(counter)
        print(cronometro(bubbleSort)(numberList))
        counter=counter+5000
    counter=5000    
    print("Calculo Selection Sort con :")
    while(counter<35000):
        numberList=listRandomGenerator(counter)
        print(counter)
        print(cronometro(selectionSort)(numberList))
        counter=counter+5000
    counter=5000  
    print("Calculo Bubble Sort con lista ordenada ascendentemente:")
    while(counter<35000):
        numberList=listGeneratorAc(counter)
        print(counter)
        print(cronometro(bubbleSort)(numberList))
        counter=counter+5000
    counter=5000    
    print("Calculo Selection Sort con lista ordenada ascendentemente:")
    while(counter<35000):
        numberList=listGeneratorAc(counter)
        print(counter)
        print(cronometro(selectionSort)(numberList))
        counter=counter+5000
    counter=5000       
    print("Calculo Bubble Sort con lista ordenada descendente:")
    while(counter<35000):
        numberList=listGeneratorDec(counter)
        print(counter)
        print(cronometro(bubbleSort)(numberList))
        counter=counter+5000
    counter=5000       
    print("Calculo Selection Sort con lista ordenada descendente:")
    while(counter<35000):
        numberList=listGeneratorDec(counter)
        print(counter)
        print(cronometro(selectionSort)(numberList))
        counter=counter+5000


getTimerOfSort()
print("Programa finalizado...")


        
