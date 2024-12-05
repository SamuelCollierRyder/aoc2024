def intersect(a, b):
    return bool(list(set(a) & set(b)))


with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]

input_split = lines.index("")
ordering_rules = lines[:input_split]
updates = lines[input_split+1:]
sum = 0
d = {}
incorrect_lines = []

for line in ordering_rules:
    split = line.split("|")
    d[split[1]] = d.get(split[1], []) + [split[0]]

for line in updates:
    nums = line.split(",")
    wrong = False
    for i in range(len(nums)):
        if nums[i] in d and intersect(d[nums[i]], nums[i+1:]):
            incorrect_lines.append(line)
            break

for line in incorrect_lines:
    nums = line.split(",")
    new_nums = []
    while len(nums) > 0:
        for num in nums:
            if num not in d or not intersect(d[num], nums):
                new_nums.append(num)
                nums.remove(num)
                break
    sum += int(new_nums[len(new_nums)//2])
    
print(sum)
