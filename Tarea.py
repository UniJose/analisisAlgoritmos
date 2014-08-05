
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
    for actualPosition in range( len(pList) ):
        minimumNumber = actualPosition
        for auxiliarPosition in range(actualPosition+1, len(pList) ):
            if list[auxiliarPosition] < list[minimumNumber]:
                minimumNumber = auxiliarPosition
        temporal = list[minimumNumber]
        list[minimumNumber] = list[actualPosition]
        list[actualPosition] = temporal

numberList = [10,9,8,7,6,5,4,3,2,1]

print ("Desordenada por BubbleSort:")
print (numberList)
#bubbleSort(numberList)
selectionSort(numberList)
print ("Ordenada por BubbleSort:")
print (numberList)




        
