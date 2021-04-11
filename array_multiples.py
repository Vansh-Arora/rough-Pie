# Function to minimize array to 2 element
def reduce(A,var,j):
    if len(A) == 2:
        var['a'+ str(j)] = [A[0],A[1]]
        print(A)
        return var

    n = len(A)
    if n % 2 != 0:
        last = n-1 
    else:
        last = n
    temp = []
    for i in range(0,last,2):
        var['a'+ str(j)] = [A[i],A[i+1]]
        temp.append('a'+ str(j))

        j += 1
    if last < n:
        temp.append((A[last]))

    return reduce(temp,var,j)

def reduceArr(A):
    reduce(A,{},0)

# Function to print intermediate Variables
def print_var(var):
    print([key for key in var.keys()])

# Function to print intermediate pairs
def print_pairs(var):
    print([val for val in var.values()])


# calling functions
ans = reduceArr(['R_1','R_2','R_3','R_4','R_5','R_6','R_7'])
