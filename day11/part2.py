import time

with open("input.txt") as f:
    text = f.read().strip()
    numbers = text.split(" ")
    numbers = [int(number) for number in numbers]

d = {}
for i in range(75):
    t1 = time.time()
    print(i)
    new_numbers = []
    for number in numbers:
        if number in d:
            for a in d[number]:
                new_numbers.append(a)


        elif number == 0:
            new_numbers.append(1)
            d[number] = [1]
            
        elif len(str(number)) % 2 == 0:
            mid = len(str(number)) // 2
            new_num1 = int(str(number)[0:mid])
            new_num2 = int(str(number)[mid:])
            new_numbers.append(new_num1)
            new_numbers.append(new_num2)
            d[number] = [new_num1, new_num2]

        else:
            new_numbers.append(number*2024)
            d[number] = [number*2024]
    numbers = new_numbers
    print(time.time() - t1)

print(len(numbers))
