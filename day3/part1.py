import re

with open("input.txt") as file:
    lines = file.readlines()

sum = 0
for line in lines:
    regex_result = re.findall(r"mul\(\d+,\d+\)", line)
    for m in regex_result:
        s = m.split(",")
        prod = int(s[0].split("(")[1]) * int(s[1].split(")")[0])
        sum += prod

print(sum)
