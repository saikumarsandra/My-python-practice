#base class
class Father:
    def house(self):
        print("i have house")
#child class get properties from base class
class child1(Father):
    def car(self):
          print("im a child1 i have a car")
# sub child class aquires parent(child) properties, Base class properties along with its own properties           
class child2(Father):
    def bike(self):
        print("i m a child2 i have a bike")

obj1=child1()
obj1.car()     
obj1.house()
obj2=child2()
obj2.bike()
obj2.house()