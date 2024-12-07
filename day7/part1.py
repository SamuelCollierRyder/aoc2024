def evaluate(numbers, operators):
    running_total = 0
    if operators[0] == "0":
        running_total = numbers[0] + numbers[1]

    else:
        running_total = numbers[0] * numbers[1]

    for i in range(2, len(numbers)):
        if operators[i-1] == "0":
            running_total += numbers[i]

        else:
            running_total *= numbers[i]

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
    for i in range(2**len(numbers)):
        binary_str = bin(i) 
        binary_str = binary_str[2:]
        
        if len(binary_str) <= len(numbers):
            binary_str = "0" * (len(numbers) - len(binary_str)-1) + binary_str

        if evaluate(numbers, list(binary_str)) == target:
            s += target
            break

    



print(s)

