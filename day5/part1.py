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
    a = True
    for i in range(len(nums)):
        if intersect(d[nums[i]], nums[i+1:]):
            break

        if i == len(nums) - 1: # If we reach the end of the list we know that it's correct
            sum += int(nums[len(nums)//2])

print(sum)
