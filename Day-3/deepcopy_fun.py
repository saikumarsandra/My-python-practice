#to over come the objects sharing the same reference in the nested list we use the "deepcopy()" from copy module
import copy
x=[1,2,3,4,5,6,[4,3]]
y=copy.deepcopy(x)
y[6][0]=0
print(x)
print(y)
print(id(x))
print(id(y))
print(id(x[6]))
print(id(y[6]))