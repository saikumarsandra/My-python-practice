#constructeroverloading is not possible in python 
#if we define N no of  the constructers with same name the python will consider the last constructer
#we can declare variable arguments and defauklt args on requirement
class Test:
    def __init__(self):
       print("1st")
    def __init__(self,a):
      print("2nd")
    
    def __init__(self,*a):
         print("3rd")
    
    def __init__(self,a,b):
        print("4th")
    
obj=Test()
