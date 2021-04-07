x=[1,2,3,4,5,6,[4,3]]
y=x.copy()
y[6][0]=0
print(x)
print(y)
print(id(x))
print(id(y))

