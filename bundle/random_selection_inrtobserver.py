from random import random

a = 0
b = 0

while True:
    x = 0
    t = 0
    while x < 1:
        x += random()
        t += 1
    a += t
    b += 1
    print(a / b)
