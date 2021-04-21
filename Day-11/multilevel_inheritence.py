#base class
class Grand_parent:
    def house(self):
        print("i have house")
#child class get properties from base class
class parent(Grand_parent):
    def car(self):
          print("im a parent i have a car")
# sub child class aquires parent(child) properties, Base class properties along with its own properties           
class child(parent):
    def bike(self):
        print("i m a child  i have a bike")

obj=child()
obj.car()
obj.bike()     
obj.house()