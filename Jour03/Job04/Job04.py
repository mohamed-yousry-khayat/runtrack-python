def FizzBuzz():
    i = 0
    while i < 100:
        i = i + 1
        if i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        if i%5 == 0 and i%3 == 0:
            print("FizzBuzz")
        else:
            print(i)

FizzBuzz()