# yanfangguo@vub.ac.be
# scripting language courses 2nd WPO 15:57 5OCT2016
# training for learn to use lists


def subsequent_power(n):
    my_list = [1]
    temp = 1
    for i in range(1, n):
        my_list.append(temp * -2)
        temp = temp * (-2)
    return my_list


# this is another form of power which contains more parameters
def powers(n, base):
    my_list = [1]
    base = -2
    for i in range(1, n):
        my_list.append(my_list[i - 1] * base)
    return my_list


print(subsequent_power(15))
print(powers(10, -2))


# Write a function that reverses a list (the last element be comes the first etc.). Implement this
# function by copying the values of the list to a new list. Do NOT use the list.reverse() method!


# it reverse the element by element in my list
def reverse(my_list):
    t_list = []
    for i in range(len(my_list)):
        t_list.append(my_list[len(my_list) - i - 1])
    return t_list


def is_palindrome(my_list):
    t_list = reverse(my_list)
    return t_list == my_list


print(is_palindrome(['c', 'l', 'i', 'l', 'c']))
print (is_palindrome([1,2,3,4,3,2]))



temp = 0
