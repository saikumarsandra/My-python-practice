#Arthimetic operators
n=eval(input())
if (n==1):
    print("Arthimetic  operators")
    sum=2+3
    sub=2-3
    mul=2*3
    div=2/3
    mod=2%3
    exponent=2**3
    floordivision=2//3
    print("sum is:",sum,"\nsub is:",sub,"\nmul is:",mul,"\ndiv is:",div,"\nmod is:",mod,"\nexpo is:",exponent,"\nfloordiv is:",floordivision)
#assignment opperators
if(n==2):
  print("Assignment operators")
  equal1=5
  addEqual=1
  addEqual+=2
  diff=3
  diff-=2
  multi=5
  multi*=2
  divi=9
  divi/=3
  modulos=4
  modulos%=2
  floordivi=8
  floordivi//=4
  expo=2
  expo**=2
  andop=5
  andop&=2
  orOp=4
  orOp|=2
  xorOP=2
  xorOP^=2
  rightshift=5
  rightshift>>=2
  leftshift=4
  leftshift<<=3
  print("\n =    :",equal1,
      "\n +=   :",addEqual,
      "\n diff :",diff,
      "\n multi:" ,multi,
      "\n mod  :",modulos,
      "\n floor:",floordivi,
      "\n expo :",expo,
      "\n andop:",andop,
      "\n orOP :",orOp,
      "\n right:",rightshift,
      "\n left :",leftshift)
#comparision operator
if(n==3):
    print("Comparision operators")
    cop1=2
    cop2=5
    print(cop1==cop2)
    print(cop1!=cop2)
    print(cop1>cop2)
    print(cop1<cop2)
    print(cop1>=cop2)
    print(cop1<=cop2)
if(n==4):
   print("logical operators")
   nd=eval(input("enter the number :    "))
   print("and   :",nd<5 and nd<10)
   print("or    :",nd<2 or nd>1)
   print("not   :",not(nd<5 and nd<10))
#identity operators
if(n==5):
    x=eval(input("enter the x vlaue:    "))
    y=eval(input("enter the y vlaue:    "))
    print("is",x is y)
    print("is not",x is not y)
#membership operators    
if(n==6):
    x=2
    y=[1,2,3,4,5]
    print(" x in y",x in y)
    print(" x not in y",x not in y)
#bitwise operators
else:
    print("bitwise operators")
    print("And :",1&2)
    print("OR  :",1|2)
    print("XOR :",1^2)
    print("NOT :",~2)
    print("ZLS :",1<<2)
    print("siR :",1>>2)

