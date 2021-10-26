import time
import random

def mergeSort(li2):
    if len(li2) > 1:
        m = len(li2)//2
        left = li2[:m]
        right = li2[m:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li2[k] = left[i]
                i += 1
            else:
                li2[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            li2[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            li2[k] = right[j]
            j += 1
            k += 1

def selectionSort(li):
    sortedList = []
    while len(li) > 0:
        minE = li[0]
        for i in range(len(li)):
            if li[i] < minE:
                minE = li[i]
        li.pop(li.index(minE))
        sortedList.append(minE)

    return sortedList


def main():

    a = 1

    n = [100,500,1000,1500,2000]
    
    listOfDifferences = []

    for e in range(len(n)):
        a = 1
         
        for i in range(10):

           

            test1 = []
            for i in range(n[e]):
                test1.append(random.randint(1,n[e]))
            
            start = time.time()
            selectionSort(test1)
            stop = time.time()
            difference = stop - start
            listOfDifferences.append(difference)
       
        total = 0
        for dif in listOfDifferences:
            print("#" + str(a) + " of " + str(n[e]) + ": " + str(dif) + " seconds.")
            total = total + dif
            a = a + 1
        avgTime = total/10
        print("\nThe average time to sort the list of " + str(n[e]) + " was " + str(avgTime) + " seconds.\n")
        for p in range(len(listOfDifferences)):
            listOfDifferences.pop(0)

if __name__ == "__main__":
    main()
