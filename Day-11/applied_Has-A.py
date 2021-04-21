class bank:
    bank_name="sbi"
    def __init__(self,name,balance=0.0) :
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("amount deposited in to  account:\t",self.balance)  

    def withdrwaw(self,amount):

        if amount >self.balance:
            print("insufficient funds")
        else:
            self.balance=self.balance-amount
            print("amount witdrawn from you account",self.balance)
            
print("welcome to",bank.bank_name)      
name= input("enetr your name:\t")
customer=bank(name)
print("helo",name)

while True:
    print("d-deposit\nw-withdraw\nc-cancel")
    opt=input("select banking option:\t")
    if opt.lower()=='d':
        dep=eval(input("enter amount for deposit:\t"))
        customer.deposit(dep)
    elif opt.lower()=='w':
        withd=eval(input("enter amount to withdraw:\t")) 
        customer.withdrwaw(withd)   
    elif opt.lower()=='c':
        print(" thanks for banking with us")
        break
    else:
        print("please select the right  option:\t")    