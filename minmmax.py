import random 
arr=[]
for i in range(1,10) :
    arr.append(random.randint(1,1000))
print(arr)
temp=arr[0] 
index=0
for i in range(len(arr)) :
    if temp>arr[i] :
        temp=arr[i]
        index=i
     
print("minimum number is ",str(temp)+" at index "+str(index))

for i in range(len(arr)) :
    if temp<arr[i]:
        temp=arr[i]
        index=i
        
print("maximum number is ",str(temp)+" at index "+str(index))        
sum=0
for i in range(len(arr)) :
    sum=sum+arr[i]
mean=sum/len(arr)
print("mean   is ",mean)

