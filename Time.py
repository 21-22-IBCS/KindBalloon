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
    listOfDifferences2 = []

    for e in range(len(n)):
        a = 1
         
        for i in range(10):

           

            test1 = []
            for i in range(n[e]):
                test1.append(random.randint(1,n[e]))
            
            start = time.time()
            mergeSort(test1)
            stop = time.time()
            difference = stop - start
            listOfDifferences.append(difference)

            test2 = []
            for i in range(n[e]):
                test2.append(random.randint(1,n[e]))
            
            start2 = time.time()
            selectionSort(test2)
            stop2 = time.time()
            difference2 = stop2 - start2
            listOfDifferences2.append(difference2)
       
        total = 0
        for dif in listOfDifferences:
            print("#" + str(a) + " of merge sort " + str(n[e]) + ": " + str(dif) + " seconds.")
            total = total + dif
            a = a + 1
        avgTime = total/10
        print("\nThe average time to sort the list of merge sort " + str(n[e]) + " was " + str(avgTime) + " seconds.\n")
        for p in range(len(listOfDifferences)):
            listOfDifferences.pop(0)

        total2 = 0
        a = 1
        for dif2 in listOfDifferences2:
            print("#" + str(a) + " of selection sort " + str(n[e]) + ": " + str(dif2) + " seconds.")
            total2 = total2 + dif2
            a = a + 1
        avgTime2 = total2/10
        print("\nThe average time to sort the list of selection sort " + str(n[e]) + " was " + str(avgTime2) + " seconds.\n")
        for p in range(len(listOfDifferences2)):
            listOfDifferences2.pop(0)


if __name__ == "__main__":
    main()
