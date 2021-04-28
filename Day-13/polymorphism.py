#operater overoading on '+'

a=1
b=2
print(a+b)

print(int.__add__(a, b))
print("##########################")

a = 'sai' 
b = 'kumar'

print(a+b)
print(str.__add__(a,b))
print("##########################")

a = (1,2,3,)
b = (4,5,6)

print(a+b)
print(tuple.__add__(a,b))

