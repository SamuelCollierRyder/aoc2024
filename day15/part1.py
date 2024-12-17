def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        s = lines.index("")
        map = lines[0:s]
        map = [list(line) for line in map]
        move_lists = lines[s+1:]
        moves = ""
        for move_list in move_lists:
            moves += move_list
        return map, moves

def get_start(map):
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == "@":
                return (row, col)

def pretty_print(map):
    for row in map:
        print("".join(row))

def move_piece(map, pos, direction, piece):
    row, col = pos
    dr,dc = (0,0)
    if direction == "v": dr, dc = (1,0)
    elif direction == "^": dr, dc = (-1,0)
    elif direction == ">": dr, dc = (0,1)
    elif direction == "<": dr, dc = (0,-1)

    if map[row+dr][col+dc] == "#":
        return False, pos

    elif map[row+dr][col+dc] == "O":
        success = move_piece(map, (row+dr, col+dc), direction, "O")[0]
        if not success:
            return False, pos

    map[row][col] = "."
    map[row+dr][col+dc] = piece
    return True, (row+dr, col+dc)

def calculate_distance(map):
    s = 0
    for i in range(len(map)):
        for k in range(len(map[i])):
            if map[i][k] == "O":
                s += (i) * 100 + k
    return s



if __name__ == "__main__":
    map, moves = read_input()
    pos = get_start(map)

    for direction in moves:
        pos = move_piece(map, pos, direction, "@")[1]
    pretty_print(map)
    print(calculate_distance(map))
            
    

