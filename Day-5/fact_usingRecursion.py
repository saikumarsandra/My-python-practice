def fact_recu(fact):
    if fact==1:
        return fact
    else:
         return fact*fact_recu(fact-1)

num=eval(input())

if num<0:
    print ("enter the valid number")

else:
     print("the factorial is :",fact_recu(num))   