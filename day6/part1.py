with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [list(line) for line in lines]


current_pos = (0, 0)
seen_positions = set()
seen_positions_dir = set()
current_direction = "up"
possible_directions = ["up", "right", "down", "left"]

for i in range(len(lines)):
    if "^" in lines[i]:
        current_pos = (i, lines[i].index("^"))
        break

while True:
    seen_positions.add(current_pos)
    seen_positions_dir.add((current_pos, current_direction))
    if current_direction == "up":
        next_pos = (current_pos[0] - 1, current_pos[1])

    elif current_direction == "right":
        next_pos = (current_pos[0], current_pos[1] + 1)

    elif current_direction == "down":
        next_pos = (current_pos[0] + 1, current_pos[1])

    elif current_direction == "left":
        next_pos = (current_pos[0], current_pos[1] - 1)

    if next_pos[0] >= len(lines) or next_pos[1] >= len(lines[0]):
        break

    if lines[next_pos[0]][next_pos[1]] == "#":
        current_direction = possible_directions[
            (possible_directions.index(current_direction) + 1) % 4
        ]
        continue
    current_pos = next_pos

print(len(seen_positions))
