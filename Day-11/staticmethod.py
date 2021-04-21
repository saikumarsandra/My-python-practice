class mobile:
    #class variable
    charger='charger included'
    #constructor init()
    def __init__(self,name,ram):
        self.name=name#instance variables
        self.ram=ram

#instance method which uses one or more instance varianbles     
    def mobile_purchase(self):
        print("thanks for purchasing",self.name,"with",self.ram,mobile.charger)
    @classmethod #converts function to the class method
    def verification(cls):
        print(cls.charger)    

    @staticmethod #convert the function to the static method
    def add(a,b):
        return a+b

print(mobile.add(5,4))