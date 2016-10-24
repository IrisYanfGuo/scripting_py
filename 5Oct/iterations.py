# yanfangguo@vub.ac.be
# scripting language courses 2nd WPO 15:00 5OCT2016
# training for learn to use for loop


def print_bla(n):
    s_bla = ""
    for i in range(n):
        s_bla = s_bla + "bla"
    print(s_bla)


print_bla(5)  # test the function


def print_arrow(nsize):
    s_arrow = ""
    for i in range(nsize):
        s_arrow += (i + 1) * "*" + '\n'
    for i in range(nsize - 1, 0, -1):
        s_arrow += (i) * '*' + '\n'
    print(s_arrow)


print_arrow(5)  # test the function


def print_bla_while(nsize):
    s_bla = ""
    while nsize:
        s_bla += "bla"
        nsize -= 1
    print(s_bla)


print_bla_while(5)


def my_division(dividend, divisor):
    reminder = dividend
    quotient = 0

    while (reminder) >= divisor:
        reminder -=divisor
        quotient +=1
    #print("the remingder is"+quotient) wrong expression
    return "the reminder is "+str(reminder)+", the quotient is "+str(quotient)

# spend a lot time write this function, and finally it works. the problem comes from Math part.
# so before program, think over the math and algorithm carefully


print(my_division(10,5))
