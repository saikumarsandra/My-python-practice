class expenses:
    def __init__(self,exp):
        self.exp = exp

    def __add__(self, other):
        print(self.exp + other.exp)

s=expenses(1000)
k=expenses(1000)        

s+k
