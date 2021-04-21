class Car:
    #def __init__(self,carname,carprice,rating):
        #self.carname=carname
        #self.carprice=carprice
        #self.rating=rating
        carname=input("enter your Car name:\t")
        carprice=eval(input("enter your Car Price:\t"))
        rating=input("enter your Car Rating:\t")
#class Customer(Car): #single inheritance
class Customer():
    #def __init__(self,carname, carprice, rating):
        
       # super().__init__(carname, carprice, rating) 
        Customername=input("enter your customer name:\t")
        print(f'{Customername}','car details')#,f'\n Carname:\t{carname}\n Carprice:\t{carprice}\nRating:\t{rating}')
#c=Customer("Honda",45000,4.5) single inhertence ends   
class Tax(Customer,Car):#multiple inheritance starts
    #def __init__(self, carname, carprice, rating):
      #  super().__init__(carname, carprice, rating)
      
        print(f'\nCarname :\t{Car.carname}\nCarprice:\t{Car.carprice}\nRating  :\t{Car.rating}')
        if Car.carprice>450000:
            tax=Car.carprice*0.25
            print("payed tax per year:\t",tax)
        elif Car.carprice<450000 and Car.carprice>150000:
            tax=Car.carprice*0.05
            print("payed tax per year:\t",tax)
        else:
            print("tax not applicable")
#t-Tax("honda",45000,4.5)multiple inheritanc ends         
t=Tax()              

