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
try:
    print("ss")
#else:
 #   print("chk")
except:
    print("cc")
finally:
    print("take")
def ggf(r, f=22):
    d = r + f
    return d
t=ggf(4,5)
print(t)
if True:
    print("hahahah")
elif False:
    print("Noooo")
def num(first,second,*third):
    print(first,"\n",second,"\n",third)
num(100,200,300,400,500,600)
def num(first,second,**third):
    print(first,"\n",second)
    for k,v in third.items():
        print(k,":",v)
num(100,200,third=300,forth=400,fifth=500,sixth=600)