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
#obj 1
m = mobile("samsung","8gb")
m.mobile_purchase()       
#obj 2
s = mobile("samsung note","12gb")
s.mobile_purchase()       