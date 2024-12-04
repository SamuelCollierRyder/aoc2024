with open("input.txt") as file:
    lines = file.readlines()

c = 0
for i in range(len(lines)):
    for k in range(len(lines[0])):
        row_str = ""
        for x in range(4):
            if x + k < len(lines[0]):
                row_str += lines[i][x + k]
        if row_str == "XMAS" or row_str == "SAMX":
            c += 1

        col_str = ""
        for x in range(4):
            if x + i < len(lines):
                col_str += lines[i + x][k]
        if col_str == "XMAS" or col_str == "SAMX":
            c += 1

        diag_str = ""
        for x in range(4):
            if x + i < len(lines) and x + k < len(lines[0]):
                diag_str += lines[i + x][k + x]
        if diag_str == "XMAS" or diag_str == "SAMX":
            c += 1

        diag_str = ""
        for x in range(4):
            if i - x >= 0 and x + k < len(lines[0]):
                diag_str += lines[i - x][k + x]
        if diag_str == "XMAS" or diag_str == "SAMX":
            c += 1
print(c)
