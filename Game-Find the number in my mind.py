import random

print("----------------Welcome----------------")
print("------Find the number in my mind!------")
print()
number = random.randrange(1,100)
t = 0
list = [1,100]
#print(number)
while True:
    n = int(input("Enter a number: "))
    t += 1
    if n == number:
        print("*************Conguratulation*************")
        print(f'************You find it {t}.try************')
        break
    elif number < n :
        if n < list[1]:
            list[1] = n
        print(f'----------------[{list[0]} - {list[1]}]---------------')
        print("----------------smaller----------------")
    else:
        if n > list[0]:
            list[0] = n
        print(f'----------------[{list[0]} - {list[1]}]---------------')
        print("----------------bigger----------------")