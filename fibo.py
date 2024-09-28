def fib():
    a, b = 0, 1
    while True:
        yield a  # Use yield to return a value and pause the function
        a, b = b, a + b

# Using the generator in a for loop
for f in fib():
    if f > 100:
        break
    print(f)
