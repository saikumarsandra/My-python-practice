#hybrid inheritence is  the combination of the multilevel and multiple inheritence
#base class
#multilevel in heritence
class Grand_parent:
    def house(self):
        print("i am a Grandparent i  have a house")
class Father(Grand_parent):#level 1
    def owner(self):
        print("im a Father owner of the house")
#child class get properties from base class
class mother(Grand_parent):#level2
    def car(self):
          print("im a mother i have a car")
# sub child1 class aquires father,mother, Base class properties along with its own properties  
# multiple inheritence         
class child1(Father,mother):
    def bike(self):
        print("i m a child i have a bike")
       
obj1=child1()
obj1.house()
obj1.owner()
obj1.car()
obj1.bike()