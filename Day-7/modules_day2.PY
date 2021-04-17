#user defined module
def add (a,b):
    return a+b
def sub(a,b):
    return a-b
def power(a,b):
    return a**b    
def avg(*a):
    return sum(a)/len(a) 

print(add(2,3))
print(sub(2,3))
print(power(2,3))
print(avg(1,2,3,4))