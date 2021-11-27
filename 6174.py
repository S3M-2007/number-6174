import time as t

num = int(input('Enter a four-digit number with different digits ==>    '))
if num == 6174:
    t.sleep(0.2)
    print('Sorted from large to small ==>', 7641)
    t.sleep(0.2)
    print('Sorted from small to large ==>', 1467)
    t.sleep(0.2)
    print('result ==>', num) # becase it always comes here
while num != 6174:
    if num > 10000:
        t.sleep(0.2)
        print('<<<=== Wrong number! Try again ===>>>')
    else:
        yekan = num % 10
        dahgan = num // 10 % 10
        sadgan = num // 100 % 10
        hesaran = num // 1000 % 10
        number = [hesaran, sadgan, dahgan, yekan]
        number.sort()
        number.reverse()
        biggest = str(number[0])
        big = str(number[1])
        small = str(number[2])
        smallest = str(number[3])
        number = biggest + big + small + smallest
        number = int(number)
        t.sleep(0.2)
        print ('Sorted from large to small ==>', number)
    number2 = str(number)
    a = number2[::-1]
    a = int(a)
    t.sleep(0.2)
    print ('Sorted from small to large ==>', a)
    result = number-a
    t.sleep(0.2)
    print ('result ==>', result)
    num = result

print('\n\nMADE BY ::: SEYED MOHAMMAD MAHDI MIRJALILI\n\nImitation of this project is legally wrong.\n\n')
# Seyed Mohammad Mahdi Mirjalili