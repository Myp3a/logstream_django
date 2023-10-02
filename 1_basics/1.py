import random
l = [random.randint(230,240) for _ in range(10)]
for number in l:
    if number % 2 == 0:
        print(number)
    if number == 237:
        break
