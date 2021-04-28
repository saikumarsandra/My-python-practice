#public "."
#protected "._"
#private ".__"
class employee:
    def __init__(self,name,age,marks):
        self.name = name#public
        self._age = age#protected
        self.__marks = marks#private

    def __verify(self):
        print("verified")
#getter and setter for accessing the private variables and to update the values 
    def get_marks(self):
        return self.__marks

    def set_marks(self,a):
        self.__marks = a   
    
ob = employee("sai",25,100)
print(ob.name)
print(ob._age)
print(ob.get_marks())   #raise error at this poit as it  is private
ob.set_marks(95)
print(ob.get_marks())