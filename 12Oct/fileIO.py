from pylab import *
# 1. read the file


# function 1 read the file and return content in a list
def readfile(name):
    f = open(name, 'r')
    llist = []
    for line in f:
        llist.append(line.split(';'))
    f.close()
    return llist


# function Write a function that looks up the grades of a student in the list
#  created in question 1 and returns it.

def grade(student, name, firstname):
    for i in range(len(student)):
        if (name == student[i][1] and firstname == student[i][0]):
            return student[i][3]
    return "not found"


student = readfile('data.csv')
print(grade(student, 'Aurelien', 'ADRIAENSSENS'))


def findbygrade(student, grade):
    result = []
    for i in range(len(student)):
        if (grade == student[i][3]):
            result.append(student[i])
    return result


print(findbygrade(student, '11.0\n'))


def writeinfo(fileName, list):
    f = open(fileName, 'w')
    for i in range(len(list)):
        str = list[i][0] + ';' + list[i][1] + ';' + list[i][2] + ';' + list[i][3]
        f.write(str)
    f.close()


writeinfo('test.csv', findbygrade(student, '11.0\n'))


def findByGrade(list, grade):
    result = []
    for i in range(len(student)):
        if (grade == student[i][2]):
            result.append(student[i])
    return result


def sortByGrade():
    return findByGrade(student, 'IA-A')
    findByGrade(student, 'IA-B')
    findByGrade(student, 'IR-A')
    findByGrade(student, 'IR-B')
    findByGrade(student, 'IR-C')
    findByGrade(student, 'IA-D'),


print(sortByGrade())


def convert2float(list):
    mylist = []
    for i in range(len(list)):
        temp = list[i][3]
        temp = temp[0: 2]
        temp = float(temp)
        mylist.append(temp)
    return mylist


def count(list,grade):
    count = 0
    for i in list :
        if (i==grade):
            count += 1
    return count

mylist = [count(convert2float(student),i) for i in range(21)]
print(mylist)

figure()
n, bins, patches = hist(convert2float(student), 20, range=(0,21), normed=0,histtype='stepfilled')
title('Group x')
show()
