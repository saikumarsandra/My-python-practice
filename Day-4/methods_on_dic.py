std={"name":"sai","maths":25,"english":58}
std['avg']=(std["maths"]+std["english"])/2
print(std)

#built in methods 
#len
print(std.__len__())
#copy()
stduent=std.copy()
print(stduent)

#fromkeys()
keys=('name','math','english','avg')
std=std.fromkeys(keys)
print("New Dictionary",std)

#####dict(zip(keys,value)) bind the keyu values 
keys=('name','math','english','avg')
value=('sai',25,58,40.0)
std=dict(zip(keys,value))
print(std)

#items() returns list of key and value as a tuple pair

print(std.items())

#values()
print(std.values())

#keys()
print(std.keys())

#setdefault("key","value") create new key and value pair
s=std.setdefault("physics",100)
print(std)
