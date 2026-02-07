import random
num=random.randint(1,10)
print("від 1 до 10")
trys=0

while True:
    if trys >= 3:
        break
    x=int(input("число "))

    if x>10 or x<1:
        print("не коректне число")
        continue

    if x<num:
        print("більше")
        trys=trys+1
        print(f"використано {trys} з 3 спроб")
    elif x==num:
        print("ви вгадали")
        break
    else:
        print("менше")
        print("спроба номер")
        trys=trys+1
        print(f"використано {trys} з 3 спроб")

print("кінець")