candies = 10


for i in range(candies):
    if candies - i == 5:
        print("only 5 candies left.stop distribution")
        continue
    print("giving candy to a friend")