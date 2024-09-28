a = input("Enter three numbers separated by commas: ")

# Split the input string and strip any extra spaces
x, y, z = [num.strip() for num in a.split(",")]

# Convert the strings to integers
num1 = int(x)
num2 = int(y)
num3 = int(z)

# Find the greatest number
great = num1
if num2 > great:
    great = num2
if num3 > great:
    great = num3

print(great)