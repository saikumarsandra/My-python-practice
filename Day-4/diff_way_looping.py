myList=[1,2,3,4,5,6,]
for i in range (len(myList)):
    print(myList)

print("################################")
myNeList=[9,8,7,6,5,4,3,2,1]

for i in myNeList:
    print (myNeList)

print("################################")
myNeList=[i for i in range (10)]

print(myNeList)

print("################################")
myNeList=[0 for i in range (10)]

print(myNeList)

print("################################")
mlt=[i*i for i in range (-10,10,2)]

print(mlt)