class car:
     def __init__(self,name,model,cost):
         self.name=name
         self.model=model
         self.cost=cost
     def display(self):
         print("Name: ",self.name)
         print("Model: ",self.model)
         print("cost: ",self.cost)
class purchase(car):
    def __init__(self, name, model, cost,payment):
        super().__init__(name, model, cost)    
        self.payment=payment   
    def display(self):
       super().display()
       print("payement mode: ",self.payment) 
obj = purchase("audi","I8",45000000,"cash")
obj.display()
         