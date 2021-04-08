#pass,continue,break
num=[1,2,3,4,5,6,7,]

for v in num:
    if (v==7):
        break;
    print(v)

print ("##############")

for v in num:
    if (v==4):
        continue;#it skip the v==4 and move to the next values and print them
    print(v)

print ("##############")

for v in num:
    if (v==4):
        pass;
        print("it is passed") #it  make no changes  to the  values and print them
    print(v)


