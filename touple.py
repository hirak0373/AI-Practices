days=("Mon","tues","wednes","thurs","fri")
print(days)
print(days[0])
days=list(days)
print(days)
days[0]="sunday"
days=tuple(days)
print(days)
for day in range(0,len(days)):
    if days[day] =="sunday":
        print("Holiday")
    else:
        print("Work today")
a=(1,2,3)
for w in a:
    print(w)