import pandas as pd
import numpy as np
dataset=pd.read_csv(r'C:\Users\saileo\Downloads\student_marks.csv').values#converted to numpy ARRAY
print(dataset[:,3:])
avg=np.mean(dataset[:,3:],axis=1)
avg=avg.reshape(-1,1)

print(avg)
def Grade(mark):
    grade=''
    if (mark>0 and mark<35):
        grade='F'
    elif(mark>=35 and mark<45):
        grade='S'
    elif(mark>=45 and mark<65):
        grade='c'
    elif(mark>=65 and mark<75):
        grade='B'
    elif(mark>=75 and mark<=100):
        grade='A'

    return grade    
mathsGrade = np.array([Grade(i)for i in dataset[:,3]])
mathsGrade= mathsGrade.reshape(-1,1).reshape(-1,1)
print(mathsGrade)  

PhysicsGrade = np.array([Grade(i)for i in dataset[:,4]])
PhysicsGrade= PhysicsGrade.reshape(-1,1)#coloumn vector (-1,1) row vector(1,-1) 1 d to 2d array
print(PhysicsGrade)

ChemistryGrade = np.array([Grade(i)for i in dataset[:,5]])
ChemistryGrade= ChemistryGrade.reshape(-1,1)
print(ChemistryGrade)    

EnglishGrade = np.array([Grade(i)for i in dataset[:,6]])
EnglishGrade= EnglishGrade.reshape(-1,1)
print(EnglishGrade)

BiologyGrade = np.array([Grade(i)for i in dataset[:,7]])
BiologyGrade= BiologyGrade.reshape(-1,1)
print(BiologyGrade)

EconomicGrade = np.array([Grade(i)for i in dataset[:,8]])
EconomicGrade= EconomicGrade.reshape(-1,1)
print(EconomicGrade)

HistoryGrade = np.array([Grade(i)for i in dataset[:,9]])
HistoryGrade= HistoryGrade.reshape(-1,1)
print(HistoryGrade)

CivicGrade = np.array([Grade(i)for i in dataset[:,10]])
CivicGrade= CivicGrade.reshape(-1,1)
print(CivicGrade)
dataset = np.append(dataset,mathsGrade,axis=1)
dataset = np.append(dataset,PhysicsGrade,axis=1)
dataset = np.append(dataset,ChemistryGrade,axis=1)
dataset = np.append(dataset,EnglishGrade,axis=1)
dataset = np.append(dataset,BiologyGrade,axis=1)
dataset = np.append(dataset,HistoryGrade,axis=1)
dataset = np.append(dataset,EconomicGrade,axis=1)
dataset = np.append(dataset,CivicGrade,axis=1)
dataset = np.append(dataset,avg,axis=1)
print(dataset)
datasetframe=pd.DataFrame(data=dataset,columns=["name","gender","dob","Maths",	"Physics","Chemistry","English","Biology","Economics","History"	,"Civics","Maths Grade"	,"Ps Grade","ChemGrade","Eng Grade","Bio Grade"	,"Economics Grade",	"History Grades","Civics Grades", "Avarage Of all subs"

])
datasetframe.to_csv('StudentGradesData.csv',index=False)
#print(datasetframe)

