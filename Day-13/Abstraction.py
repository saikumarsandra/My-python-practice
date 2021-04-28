from abc import ABC, abstractmethod #abc - Abstract Base Class
#if one method is an abstract method then  the base class is a abstract class

class mobile_design(ABC):
     
     @abstractmethod
     def camera(self):
         pass
        
     @abstractmethod
     def ram(self):
         pass

class test(mobile_design):
    def ram(self):
         print("8 Gb")  

    def camera(self):
           print("48MP")   

ob = test()

ob.ram()
ob.camera()

          