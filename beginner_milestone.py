#1 An App That Says "Hi"
print("Hi")

#2 An App That Creates A Random List Of Numbers, Unsorted
import random 

list = []

for i in range(8):
    n = random.randint(1, 25)
    list.append(n)

print(list)
