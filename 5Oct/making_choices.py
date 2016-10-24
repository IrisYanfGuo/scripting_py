# yanfangguo@vub.ac.be
# scripting language courses 2nd WPO 14:49 5OCT2016
# the general structure of an if…elif…else structure

TYPE1 = "Not a leap year: not divisible by 4"
TYPE2 = "Leap year: divisible by 4 but not by a 100"
TYPE3 = "Not a leap year: divisible by a 100 but not by 400"
TYPE4 = "Leap year: divisible by 400"


def what_type_year(year):
    if year%400==0:
        return TYPE4
    elif year%100==0:
        return TYPE3
    elif year%100==0:
        return TYPE2
    else:
        return TYPE1
print(what_type_year(1900))
