n = 2
s = n + ( n * n) + (n * n * n)
print(s)
print(4*5+5%8+4*5)
list1 = ['a',"dedd",1,1.3]
print(list1[1][1])
print(int(43.55+2/2))
r = ("hello","dd")
g = list("hell" "xx" "ssss")
print(g)
h = [2, 33, 222, 14, 25]
print(h[-1])
names = ['Amir', 'Bear', 'Charlton', 'Daman']
print(names[-1][-1])
names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names1.append("Hira")
names3 = names1[:]
names2[0] = "Alice"
names3[1] = "Bob"
sum = 0
print(names1)
print(names2)
print(names3)
for ls in (names1, names2, names3):
    if ls[0] == "Alice":
        sum += 1
    if ls[1] == "Bob":
        sum += 10
print(sum)
num = [1, 2, 3, 4]
num.append([2,4,6,7])
num.extend([33,22])
num.append(77)
print(num)
a=list((45,)*4) 
print((45)*4) 
print(a)
word1="Apple" 
word2="Apple" 
list1=[1,2,3] 
list2=[1,2,3] 
print(word1 is word2) 
print(list1 is list2)
A = 16
B =15
print(A % B // A)
f = [1, 2, 3, 4]
print(f[-2: ])
