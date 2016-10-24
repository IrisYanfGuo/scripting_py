# 19 OCT 2016 tuples in scrioting language class
# author iris yanfang guo  yanfguo@outlook.com

tup1 = (12,34,56) #tuples are immutable

print(tup1[1])

#sets

x = set([3,1,2,1])
# wrong  print (x[0]) set does not support indexing
print(x)

lows = {0,1,2,3,4}
odds ={1,3,5,7,9}

lows.add(9)
print(lows.difference(odds))
print(lows.intersection(odds))

# dictionary is a collection of values.

states = {
    'oregon' : 'OR',
    'florida' :'FL',
    'New York':'NY'
}

print( states['florida'])
print(states.get('florida'))
print(states.keys())

x = abs(-1)