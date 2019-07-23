num1 =input("Enter number 1: ")
num2 =input("Enter number 2: ")
op =input("Enter operator: ")
if op == "+":
    ans =int(num1)+int(num2)
    print("Answer is "+ str(ans))
elif op == "-":
    ans =int(num1)-int(num2)
    print("Answer is "+ str(ans))
elif op == "*":
    ans =int(num1)*int(num2)
    print("Answer is "+ str(ans))
elif op == "/":
    ans =int(num1)/int(num2)
    print("Answer is "+ str(ans))
else:
    print("Error")
