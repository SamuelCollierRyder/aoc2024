with open("input.txt") as file:
    lines = file.readlines()

c = 0
for i in range(len(lines)-2):
    for k in range(len(lines[0])-2):
        mini_matrix = []
        for x in range(i, i+3):
            for y in range(k, k+3):
                mini_matrix.append(lines[x][y])
        diag1 = [lines[i][k], lines[i+1][k+1], lines[i+2][k+2]]
        diag2 = [lines[i][k+2], lines[i+1][k+1], lines[i+2][k]]
        diag1 = "".join(diag1)
        diag2 = "".join(diag2)

        if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
            c += 1
        


print(c)
