eng =input("Enter marks of English: ")
bio = input("Enter marks of Biology: ")
chem = input("Enter marks of Chemistry: ")
pak = input("Enter marks of Pakistan Sudies: ")
sin = input("Enter marks of Sindhi: " )
obtain =int(eng)+int(bio)+int(chem)+int(pak)+int(sin)
print (obtain)
per =int(obtain)/425
per1=per*100
print("your percentage is: "+str(per1))
if per1 >= 80 and per1 <= 100:
    print("Grade: A+")
elif per1 >= 70 and per1 <=79.99:
    print("Grade: A")
elif per1 >= 60 and per1 <=69.99:
    print("Grade: B")
elif per1 >= 50 and per1 <=59.99:
    print("Grade: C")
elif per1 >= 40 and per1 <=49.99:
    print("Grade: D")
elif obtain <40:
    print("Grade: fail")