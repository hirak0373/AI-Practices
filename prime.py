num = int(input("Enter nbr: "))
#if num >1 :
 #   for i in range(2,num):
  #      if num%i==0:
   #         print("Nbr is not prime")
    #else:
     #   print(" prime")
# prime with flag
if num==1 or num ==0 :
    print(num , "is not prime")
elif  num ==2:
    print(num , "is  prime")
else:
    is_prime = True
    for i in range(2,num):
        if num % i ==0:
            is_prime = False
            break #for removing unnecisary iterations
    if is_prime:
        print("Is prime")
    else:
        print("Not Prime")