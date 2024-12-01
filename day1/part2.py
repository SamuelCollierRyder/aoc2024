with open("input.txt") as file:
    data = file.readlines()

col1 = []
col2 = []
for row in data:
    row = row.split(" ")
    col1.append(int(row[0]))
    col2.append(int(row[-1].rstrip("\n")))

num_count = {}
for num in col2:
    num_count[num] = num_count.get(num, 0) + 1

similarity = 0
for num in col1:
    similarity += num * num_count.get(num, 0)

print(similarity)
