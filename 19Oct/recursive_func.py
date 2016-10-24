# Python Exercises – Series 4
# Location: My Bedroom
# 13:28 19Oct2016
# version 1.0
# author Iris Yanfang Guo <yanfguo@outlook.com>


# q1.a: recursive functions
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


# q1.b
def gcd(a,b):
    if a>b:
        return gcd(b,a-b)
    elif a == b:
        return a
    else:
        return gcd(a,b-a)


# q2.f turn the function into a more readable function
def f(x,y,z,k=0):
    count = 0
    for i in range(k,k+y):
        if (x[i]%z==0 and x[i] !=0):
            count +=1
    return count
# k is the start index, and y is the number of elements inlvoled into this function
print(f([5,6,10,3,7,8,5,6],3,2))


# Nested Loops
def readfile(name):
    f = open(name, 'r')
    llist = []
    for line in f:
        llist.append(line.strip().split(' '))
    f.close()
    return llist

out=readfile('matrix1.txt')
print(out)


def writefile(name,out):
    with open(name,'w') as output_file:
        for i in out:
            for j in i:
                output_file.write(j)
                output_file.write(' ')
            output_file.write('\n')


writefile('test.txt',out)
mat1 = readfile('matrix1.txt')
mat2 = readfile('matrix2.txt')


def mul_matrix(matrix1,matrix2):
    result = []
    for i in range(len(matrix1)):
        a = []
        for j in range(len(matrix2[0])):

            mysum = 0
            for k in range(len(matrix2)):
                mysum += int(matrix1[i][k])*int(matrix2[k][j])
            a.append(mysum)
        result.append(a)
    return result
print(mul_matrix(mat1,mat2))


