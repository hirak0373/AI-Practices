a = [1 ,2, 3, 4, 5, 6, 7, 8, 9, ] 
'''
names = ["amna", "hira", "kiran"]

names.append("Arsalah")
names.insert(0,"ali")
names.insert(2,"basit")
print(names)
g = names[1:4]
print(g)
del names[2]
print(names)
g.remove("basit")
print(g)
dd=g.pop(1)
print(g)
names.append(dd)
print(names)
days = ("monday", "tuesday", "wednesday", "thursday", "friday")
print(days)
days = list(days)
days.append("saturday")
print(days)
'''
'''
full_names = []
for a1 in a:
    for b in a:
        c = a1 * b
        print(str(a1) + " X " + str(b) + " = " + str(c))

for a1 in range(2,3):
    for b in range(1,11):
        c = a1 * b
        print(str(a1) + " X " + str(b) + " = " + str(c))
'''
'''
a = "HiRa KhAn"
a = a.lower()
print(a)
a = a.title()
print(a)
a = a.upper()
print(a) 
a_b_c = ["HiRa KhAn","chk"]

print(a_b_c)
a_b_c[1]=22
print(a_b_c)

print(a_b_c)
print(a_b_c[3])
a_b_c["religion"] = "Muslim"
a_b_c[3]=4.99
print([a_b_c])
del a_b_c[3]
print(a_b_c)
for abc in a_b_c.values():
        print(abc)
for abc in a_b_c.keys():
        print(abc)
'''
a_b_c = {"Name" : "HiRa KhAn", "Age " : 19, 3 : 4.3 }
for abc,xyz in a_b_c.items():
        print(str(abc) + " is " + str(xyz))

'''
customer = [ {"Customer ID: " : 0,"Name: ": "Amna" }, {"Customer ID: " : 1 ,"Name: ": "Kiran"  }, {"Customer ID: " : 2,"Name: ": "Ayesha" }]
print(customer)
a = customer[1]
c_name = a["Name: "]
a["discount"]=["standard", "volume", "loyalty"]
customer[1]=a
print(customer)
print(c_name)
'''
'''
dis = {"Customer ID: " : 1 ,"Name: ": "Kiran", "discount" : ["standard", "volume", "loyalty"]  }
if "brother_in_law" in dis["discount"]:
        d=.30
elif "loyalty" in dis["discount"]:
        d=.15
elif "volume" in dis["discount"]:
        d=.10
elif "standard" in dis["discount"]:
        d=.5
print(d)
'''

dis = {0 : {"Customer ID: " : 0,"Name: ": "Amna" }, 1 : {"Customer ID: " : 1 ,"Name: ": "Kiran"  }, 2 : {"Customer ID: " : 2,"Name: ": "Ayesha" }}
print(dis[2]["Name: "])

#function
def add(a,b=2):
        c = a + b
        print(a)
        print(b)
        print(c)
add(33)
add(2,b=221)




