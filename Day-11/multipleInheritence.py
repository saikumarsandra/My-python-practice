#base class1
class Father:
    def house(self):
        print("i have house")
#another base class get properties from base class1
class mother:
    def car(self):
          print("im a Mother i have a car")
#child1 class aquires father and mother properties along with its own properties           
class child1(Father,mother):
    def bike(self):
        print("i m a child i have a bike")

obj1=child1()
obj1.car()     
obj1.house()
obj1.bike()