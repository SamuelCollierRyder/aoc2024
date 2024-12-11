def dfs(row_pos, col_pos, num, found_goal):
    global end_count

    if lines[row_pos][col_pos] == "9":
        found_goal.append([row_pos, col_pos])
        return found_goal

    next_num = num + 1
    if row_pos + 1 < len(lines) and lines[row_pos + 1][col_pos] == str(next_num):
        dfs(row_pos + 1, col_pos, next_num, found_goal)

    if row_pos - 1 >= 0 and lines[row_pos - 1][col_pos] == str(next_num):
        dfs(row_pos - 1, col_pos, next_num, found_goal)

    if col_pos + 1 < len(lines[0]) and lines[row_pos][col_pos + 1] == str(next_num):
        dfs(row_pos, col_pos + 1, next_num, found_goal)

    if col_pos - 1 >= 0 and lines[row_pos][col_pos - 1] == str(next_num):
        dfs(row_pos, col_pos - 1, next_num, found_goal)

    return found_goal

def readlines():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def get_start_pos(lines):
    starting_positions = []

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "0":
                starting_positions.append([row, col])

    return starting_positions


if __name__ == "__main__":
    lines = readlines()
    starting_positions = get_start_pos(lines)
    trail_len = 0
    for starting_pos in starting_positions:
        trail_len += len(dfs(starting_pos[0], starting_pos[1], 0, []))

    print(trail_len)
