a = [1, 2, 3, 4]
b = a
c = a[ : ]
a.append(5)
c.append(6)
print(a , b , c)
h = {'a':'b','f':22,11.2:3}
print(h['a'])
print(h['f'])
print(h[11.2])
for f,l in h.items():
    print(f,l)
if 3 in h.values():
    print("good")