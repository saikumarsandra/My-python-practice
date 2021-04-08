billAmount=eval(input("enter the bill amount: "))
if billAmount>1000:
    discount=billAmount*0.10
    print("Discount recived",discount)
elif billAmount>600<900:
    discount=billAmount*0.5
    print("Discount recived",discount)    
else :
    discount=billAmount*0.2
    print("Discount recived",discount)
print("Net Aount",billAmount-discount)
    