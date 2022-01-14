temp = ""
if i % 3 == 0 and i % 5 == 0:
    temp = "fizzbuzz"
elif i % 5 == 0:
    temp = "buzz"
elif i % 3 == 0:
    temp = "fizz"
else:
    temp = "no"
