with open("input.txt") as file:
    data = file.readlines()

col1 = []
col2 = []
for row in data:
    row = row.split(" ")
    col1.append(int(row[0]))
    col2.append(int(row[-1].rstrip("\n")))

col1.sort()
col2.sort()

diff = 0
for i in range(len(col1)):
    diff += abs(col2[i] - col1[i])

print(diff)

