#same method name but different arguments is called method overloading
#not used in python as it is not requiered
#python will consider the last method from the other same name method 
#we can declare variable arguments and defauklt args on requirement
class test:
    def method(self):
        print("1st")

    def method(self,*a):
        print("2nd")    
    
    def method(self,a,b):
        print("3rd")    
obj=test()
obj.method(2,3)        