# selection sort

def select_sort(mylist):
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if mylist[i]<mylist[j]:
                mylist[i],mylist[j] = mylist[j],mylist[i]
    return mylist
print(select_sort([1,2,5,4,2,8,2]))