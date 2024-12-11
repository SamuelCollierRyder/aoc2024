with open("input.txt") as f:
    text = f.read().strip()
    numbers = text.split(" ")

for i in range(25):
    new_numbers = []
    for number in numbers:
        if number == "0":
            new_numbers.append("1")
            
        elif len(number) % 2 == 0:
            mid = len(number) // 2
            new_numbers.append(str(int(number[0:mid])))
            new_numbers.append(str(int(number[mid:])))

        else:
            new_numbers.append(str(int(number)*2024))
    numbers = new_numbers

print(len(numbers))
