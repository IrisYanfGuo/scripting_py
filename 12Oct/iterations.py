# by Iris Yanfang Guo  yanfguo@vub.ac.be
# this is the third python exercise class, 12 Oct

# write the for loop below with a while loop
for k in range(9, 0, -1):
    print('k=', k)


# write a function that returns the smallest and largest element in a list
def small_and_big_list(nlist):
    small = nlist[0]
    big = nlist[0]
    for i in nlist:
        if (small > i):
            small = i
        else:
            if (big < i):
                big = i
    return small, big


# test for the funtion small_and_big_list
mylist = [1, 2, 3, 4, 5, 8, 0]
print(small_and_big_list(mylist))


# write a function that return the length of the longest list
def longest_length_lists(llist):
    longest_length = 0
    for i in llist:
        longest_length = longest_length if longest_length > len(i) else len(i)
    return longest_length


mylist = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
print('the longest lenth of the element in list is ', longest_length_lists(mylist))


def extend_list(mylist):
    for i in range(len(mylist)):
        if (len(mylist[i]) < longest_length_lists(mylist)):
            for j in range(len(mylist[i]), longest_length_lists(mylist)):
                mylist[i].append(0)


def averages_lists(mlist):
    result = []
    for j in range(longest_length_lists(mlist)):
        nsum = 0
        count = 0
        for i in range(len(mlist)): # for el in mylist  l.append(el[i])
            if (j < len(mlist[i])):
                nsum += mlist[i][j]
                count += 1

        result.append(nsum / count)
    return result


mylist1 = [[1, 2, 1, 4], [5, 6, 2, 5], [54, 8, 7]]
print(averages_lists(mylist))
