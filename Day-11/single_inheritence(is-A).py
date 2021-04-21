class parent:#parent class
    def car(self):
          print("im a parent i have a car")
# child class aquires parent properties along with its own properties           
class child(parent):
    def bike(self):
        print("i m a child  i have a bike")

obj=child()
obj.car()
obj.bike()     