def BubbleSort(elements, list2, list3):
    n = len(elements)
    for i in range(n):
        for j in range(n-i-1):
            if elements[j]>elements[j+1]:
                elements[j],elements[j+1] = elements[j+1],elements[j]
                list2[j],list2[j+1] = list2[j+1],list2[j]
                list3[j],list3[j+1] = list3[j+1],list3[j]




inputFile = open("F:\\GHC_previousYears\\b_lovely_landscapes.txt","r")
outputFile = open("F:\\GHC_previousYears\\sol.txt","w")
outputFile2 = open("F:\\GHC_previousYears\\sol2.txt","w")

lines = int(inputFile.readline())
keys = []
numOfTags = []
tags = []
for i in range(lines):
    myList = (inputFile.readline()).split()
    numOfTags.append(int(myList[1]))
    tags.append(myList[2:])
    keys.append(i)

BubbleSort(numOfTags,tags,keys)

#for i in range(lines):
   # outputFile.write(str(dic1[i]) + " " + str(i) + "\n")
    #outputFile2.write(str(dic2[i]) + "\n")
