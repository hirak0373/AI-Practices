names1 = ['Amir', 'Bear', 'Charlton', 'Daman']

A= 16
B = 15
C = A % B
D = C //A
print(C)
print(D)
print(4+(3%5))
print(43.55+2/2)
print('{0:.2}'.format(1/3))
if (9 < 0) and (0 < -9):
   print("hello")
elif (9 > 0) or False: 
   print("good") 
else: 
   print("bad")
print(not(10<20) and not(10>30))

list1 = ['a',2,'d',"dd"]
#list1.shuffle()
#shuffle(list1)
#/random.shuffle(list1)
#random.shuffleList(list1)
list1 =[4, 2, 2, 4, 5, 2, 1, 0]
print(list1[-1])
print(list1[:2])
print(list1[:-2])
names2 = names1
names3 = names1[:]
#print(names3) 
___A_=22
print(___A_)
chosen_letter = "b"
letter_list = ["a", "b", "c", "d", "e", "f"]
for a_letter in letter_list:
  if a_letter == chosen_letter:
    print("It's a match.")
    break


for city in names1:
  city = city.lower()
  print(city)
print(names1)


__str__ = 1
print(__str__)
x = [i**+1 for i in range(3)]; print(x);
my_string="asdevggf"
print([i.lower() for i in "HELLO"])
#print([if i%2==0: i; else: i+1; for i in range(4)])
k = [print(i) for i in my_string if i not in "aeiou"]
print(k)
#k = [print(i) for i in my_string if i not in "aeiou"]

x = ["a", "c"]
y = []
for i in x:
    y.append(i.upper())
print(x)

d = {"john":40, "peter":45}
print(d)
d = {"john":40, "peter":45}
print(list(d.keys()))
if "john" in d:
    print("yes")
else:
    print("not")