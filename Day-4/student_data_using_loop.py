name=[]
marks=[]

for i in range(0,5):
    x=input("enter the student name :")
    y=eval(input("enter marks :"))
    name.append(x)
    marks.append(y)

print(name,marks)

student=dict(zip(name,marks)) 

print(student)   
