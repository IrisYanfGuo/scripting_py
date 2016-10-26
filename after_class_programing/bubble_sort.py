# this is a program buuuble sort
# input a list , output a sorted list
# do not need to have a new space to store
# two ways of bubble_sort
def bubble_sort(mylist):
    for i in range(len(mylist)-1,0,-1):
        for j in range(i):
            if mylist[j]<mylist[j+1]:
                temp = mylist[j]
                mylist[j]=mylist[j+1]
                mylist[j+1]=temp
    return mylist

def bubble_sort1(mylist1):
    for i in range(len(mylist1)-1):
        for j in range(len(mylist1)-1,i,-1):
            if mylist1[j]>mylist1[j-1]:
                mylist1[j-1],mylist1[j] = mylist1[j],mylist1[j-1]
    return mylist1


list1=[2,10,7,6,8,9]
print(bubble_sort(list1))
print(bubble_sort1(list1))