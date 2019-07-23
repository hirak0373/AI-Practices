import random
age=[]
for i in range(10):
    age.append(random.randint(10,22))
print(age)
for age1 in range(0,len(age)):
    for age2 in range(0,len(age)):
        if age[age1] < age[age2]:
            temp = age[age1]
            age[age1]=age[age2]
            age[age2]=temp
print(age)