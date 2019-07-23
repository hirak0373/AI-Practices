lst=[2,3,8,5,4,9,7,0]
new_list=[lst[2],lst[3],lst[4]]
print(new_list)
new_list2=[]
for i in range(2,6):
    new_list2.append(lst[i])
print(new_list2)
l1=[2,5,7]
l2=l1
l2.append(22)
print(l1)
print(l2)

a=10
b=a
b=20
list3=l1[:]
print(list3)
list3.append(45)
print(list3)
print(l1)
print(l1[3::-1])
print(lst[:2])


