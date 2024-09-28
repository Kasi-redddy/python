num1 = int(input("give 1st number: "))
num2 = int(input("give 2nd number: "))

operator = input("give operator")

if operator == "+":
    print(f"addition of 2 numbers is{num1+num2}")
elif operator ==  "-":
    print(f"subtraction of 2 numbers{num1-num2}")
elif operator ==  "*":
    print(f"multipication of 2 numbers{num1*num2}")
elif operator == "/":
    print(f"division of 2 numbers{num1/num2}")
else:
    print("Invalid operator")  
      
        