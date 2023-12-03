import random

a=[1,2,3,4,5,6,7,8,9]
for i in a:
    print(i)
print()
a="RETURN"
for i in a:
    print(i)
print()
a=[1, 2, 3, 4, 5, 6, 7, 8 ,9]
while a:
    i = a.pop(0)
    print(i)
print(a)
print()
print("функция mult2(x,y)")
def mult2(x,y):
    result = x * y
    return result
v1=4
v2 = 6
b = mult2(v1,v2)
print("resuilt", b)
##################
import random
randomMy = random.randint(1,5)
print(randomMy)
