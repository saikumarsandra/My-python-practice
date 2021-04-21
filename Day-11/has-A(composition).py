class laptop:
    def __init__(self,brand,color,inch,cost,rating) :
        self.brand=brand
        self.color=color
        self.inch=inch
        self.cost=cost
        self.rating=rating
    def lap_data(self):
            print(f'laptop brand:{self.brand}\nColor:{self.color}\ninches:{self.inch}\ncost:{self.cost}\nrating:{self.rating}')

class user:
    def __init__(self,username,userlaptop) :
       self.username=username
       self.userlaptop=userlaptop

    def userInfo(self):
        print(f'username :{self.username}')   
        self.userlaptop.lap_data()
lapy=laptop('hp','black',15,45000,4.5)   
Udata=user('sai',lapy)    
Udata.userInfo()