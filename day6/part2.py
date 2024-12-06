# Global variables
possible_directions = ["up", "right", "down", "left"]
starting_direction = "up"


def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [list(line) for line in lines]
    return lines


def find_starting_position(lines):
    for i in range(len(lines)):
        if "^" in lines[i]:
            return (i, lines[i].index("^"))


def calculate_next_position(current_pos, current_direction):
    if current_direction == "up":
        return (current_pos[0] - 1, current_pos[1])

    elif current_direction == "right":
        return (current_pos[0], current_pos[1] + 1)

    elif current_direction == "down":
        return (current_pos[0] + 1, current_pos[1])

    else:  # left
        return (current_pos[0], current_pos[1] - 1)


def get_visited_positions(starting_position, lines):
    current_direction = starting_direction
    current_pos = starting_position
    seen_positions = set()
    while True:
        seen_positions.add(current_pos)
        next_pos = calculate_next_position(current_pos, current_direction)
        if next_pos[0] >= len(lines) or next_pos[1] >= len(lines[0]):
            break

        if lines[next_pos[0]][next_pos[1]] == "#":
            current_direction = possible_directions[
                (possible_directions.index(current_direction) + 1) % 4
            ]
            continue
        current_pos = next_pos

    return seen_positions


def checkloop(starting_position, lines, forbidded_pos):
    current_direction = starting_direction
    current_pos = starting_position
    seen_positions_dir = set()
    while True:
        seen_positions_dir.add((current_pos, current_direction))
        next_pos = calculate_next_position(current_pos, current_direction)

        if (
            next_pos[0] >= len(lines)
            or next_pos[1] >= len(lines[0])
            or next_pos[0] < 0
            or next_pos[1] < 0
        ):
            return False

        if lines[next_pos[0]][next_pos[1]] == "#" or next_pos == forbidded_pos:
            current_direction = possible_directions[
                (possible_directions.index(current_direction) + 1) % 4
            ]
            continue

        if (next_pos, current_direction) in seen_positions_dir:
            return True

        current_pos = next_pos


if __name__ == "__main__":
    lines = read_input()
    starting_pos = find_starting_position(lines)
    visited_positions = get_visited_positions(starting_pos, lines)
    loop_count = 0
    for visited_pos in visited_positions:
        if checkloop(starting_pos, lines, visited_pos):
            loop_count += 1

    print(loop_count)
