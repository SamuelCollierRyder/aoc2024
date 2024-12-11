max_depth = 75
seen_num_depth = {}
l = 0

def calculate_numbers(number, depth):
    global l
    p = 0

    if depth == max_depth:
        l += 1
        return 1

    if (number, depth) in seen_num_depth:
        l += seen_num_depth[(number, depth)]
        return seen_num_depth[(number,depth)]
    
    elif number == 0:
        p += calculate_numbers(1, depth+1)
        
    elif len(str(number)) % 2 == 0:
        mid = len(str(number)) // 2
        new_num1 = int(str(number)[0:mid])
        new_num2 = int(str(number)[mid:])
        p += calculate_numbers(new_num1, depth+1)
        p += calculate_numbers(new_num2, depth+1)

    else:
        p += calculate_numbers(number*2024, depth+1)
    
    seen_num_depth[(number,depth)] = p
    return p


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
        numbers = text.split(" ")
        numbers = [int(number) for number in numbers]
    return numbers

if __name__ == "__main__":
    numbers = read_input()
    for number in numbers:
        calculate_numbers(number, 0)

    print(l)
