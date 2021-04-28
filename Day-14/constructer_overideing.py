class p:
    def __init__(self) :
        print("parent")

class child(p):# uses parent constructer if no constructer in child class
       print("case1 with no child constructer using parent constructer")
       pass

class child2(p):#  if child has a constructer parent constructer is overridden  by child class
       def __init__(self):
           print("child2")

obj= child()
obj=child2()