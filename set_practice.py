inputFile = open("F:\\GHC_previousYears\\b_lovely_landscapes2.txt","r")
outputFile = open("F:\\GHC_previousYears\\sol.txt","w")
outputFile2 = open("F:\\GHC_previousYears\\sol2.txt","w")
score=0
lines = int(inputFile.readline())
dict1 = {}
dict2 = {}

def getScore(A, B):
    inter =  len(list(set(A) & set(B)))
    uniqueA =  len(A)-inter
    uniqueB = len(B) - inter
    return min(inter, uniqueA, uniqueB)

for i in range(lines):
    myList = (inputFile.readline()).split()
    #print(myList[1])
    temp=int(myList[1])
    if(temp in dict1.keys()):
        dict1[temp].append(i) 
        l=len(dict1[temp])-1
        for j in range(l):
            #print(getScore(dict2[dict1[temp][j]],myList[2:]))
            if(getScore(dict2[dict1[temp][j]],myList[2:])==temp/2):
                score=score+temp//2
                dict1[temp].pop(j)
    else:
        dict1[temp]=[i]           # key------->int(myList[1])  value------------>i
    dict2[i] = myList[2:]