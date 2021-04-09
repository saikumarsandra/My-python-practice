myFun = lambda arg1,arg2:arg1+arg2
print(myFun(2,3))

#type2

def fu(n):
    return lambda a :a*n
mul=fu(5)
tmul=fu(3)
print(mul(10))

print(tmul(11))
