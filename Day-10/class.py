class mobile:
    def mobile_purchase(self,name,ram):
        print("thanks for purchasing",name,"with",ram)
#obj 1
m = mobile()
m.name= "samsung"
m.ram="8GB"
m.mobile_purchase(m.name,m.ram)       
#obj 2
s = mobile()
s.name= "samsung Note"
s.ram="12GB"
s.mobile_purchase(s.name,s.ram)       