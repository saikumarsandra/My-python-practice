class mobile:
    def __init__(self,name,cost,ram,cam):
        self.name = name
        self.cost = cost
        self.ram = ram
        self.cam = cam
    def info(self):
        print("mobile name : ",self.name)
        print("cost        : ",self.cost)
        print("Ram         : ",self.ram)
        print("cam         : ",self.cam)
list_of_mobile_sold =[]
while True:
    name= input("enter the mobile u want to purchse")
    ram = input ("ram requires")   
    cost = input("cost prefernce")
    cam = input("cam prefernce") 
    ob = mobile(name,cost,ram,cam) 
    list_of_mobile_sold.append(ob)
    print("thanks for purchasing")
    opt= input("look for another mobile Y/N?")
    if opt =="N":
        break
for mobile in list_of_mobile_sold:
    mobile.info()
    print()       
          

          


