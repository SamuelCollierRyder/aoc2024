def int_to_base3(n):
    if n == 0:
        return '0'
    
    digits = []
    while n:
        n, remainder = divmod(n, 3)
        digits.append(str(remainder))
    
    return ''.join(digits[::-1])

def evaluate(numbers, operators):
    running_total = 0
    if operators[0] == "0":
        running_total = numbers[0] + numbers[1]

    elif operators[0] == "1":
        running_total = numbers[0] * numbers[1]

    else:
        running_total = int(str(numbers[0]) + str(numbers[1]))

    for i in range(2, len(numbers)):
        if operators[i-1] == "0":
            running_total += numbers[i]

        elif operators[i-1] == "1":
            running_total *= numbers[i]

        else:
            running_total = int(str(running_total) + str(numbers[i]))

    return running_total

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

s = 0
for line in lines:
    target = int(line.split(":")[0])
    numbers = line.split(":")[1]
    numbers = numbers.strip().split(" ")
    numbers = [int(number) for number in numbers]
    for i in range(3**len(numbers)):
        base_three_str = int_to_base3(i)
        
        if len(base_three_str) <= len(numbers):
            base_three_str = "0" * (len(numbers) - len(base_three_str)-1) + base_three_str

        if evaluate(numbers, list(base_three_str)) == target:
            s += target
            break

print(s)
