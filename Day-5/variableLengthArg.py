# when * is added before any argument then t act as  the variable length argument
#it act as a parameter that accepts N number of values to one argument act as a tuple
def myFun(a,*b):
    print (a,b)
   
myFun("sai",2.0)    

#type 2

myFun("this is 'a'",2.0,1,2,3,4,5,6,[1,2,3],(1,2,3),{9,8,10})   

def avg(*vals):
    Average= sum(vals)/len(vals)
    print("avarage of  the values",Average)
avg(1,2,3,4,5,6,9,8,7,)