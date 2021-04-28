class company():
    def __init__(self,company):
        self.company=company 

    def display(self) :
        print(f"company name {self.company}")    
      
class emp(company):

    def __init__(self, company,emp_name):
        super().__init__(company)      
        self.emp_name=emp_name

    def display(self):
       print("company name",self.company)
       print("company name",self.emp_name)
       super().display()#we can use the self method when  the method names are same in both parent and child class
ob=emp("cognizant","saikumar")

ob.display()