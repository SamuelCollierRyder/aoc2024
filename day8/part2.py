with open("example_input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

pos_dict = {}
for i in range(len(lines)):
    for k in range(len(lines[i])):
        c = lines[i][k]
        if c != ".":
            pos_dict[c] = pos_dict.get(c, []) + [(i,k)]

possitions = set()
seen_positions = []
c = 0

for key in pos_dict:
    positions = pos_dict[key]
    for i in range(len(positions)):
        for k in range(len(positions)):
            if i == k:
                continue
                
            i_x = positions[i][0]
            i_y = positions[i][1]

            k_x = positions[k][0]
            k_y = positions[k][1]

            delta_x = i_x - k_x
            delta_y = i_y - k_y

            m = 0
            while True:
                new_x = i_x + m * delta_x
                new_y = i_y + m * delta_y
            
                if new_x >= 0 and new_x < len(lines[0]) and new_y >= 0 and new_y < len(lines):
                    if (new_x, new_y) not in seen_positions:
                        c += 1
                        seen_positions.append((new_x, new_y))

                else:
                    break
                m += 1
            
print(c)