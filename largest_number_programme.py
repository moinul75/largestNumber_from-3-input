num1 = int(input("Enter the Number1: "))
num2 = int(input("Enter the Number2: "))
num3 = int(input("Enter the Number3: "))

if num1> num2 and num1 > num3:
    print("The largest Number is ", num1)
elif num2 > num1 and num2 > num3:
    print("The largest Number is: ", num2)
else:
    print("The largest Number is: ", num3)
