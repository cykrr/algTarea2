#!/bin/python
import random
a=[]
for cont in range(0,100):
    a.append((int(random.randint(1,6))))

    if a[cont-1] == a[cont]:
        print ( ">>",  a[cont], " ", a[cont-1], end = " " ) 

    if a[cont] == 1:
        print("Has perdido")
        break

print(a)





