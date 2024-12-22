def is_almost_integer(n):
    if n % 1 < 0.01 or n % 1 > 0.99:
        return True
    return False


with open("input.txt") as file:
    text = file.read()
    s = text.split("\n")

x_step = []
y_step = []
x_goal = []
y_goal = []

for i in range(len(s)):
    line = s[i]

    if i % 4 == 0:
        x_step.append(int(line.split("+")[1].split(",")[0]))
        y_step.append(int(line.split("+")[2]))

    if i % 4 == 1:
        x_step.append(int(line.split("+")[1].split(",")[0]))
        y_step.append(int(line.split("+")[2]))

    if i % 4 == 2:
        x_goal.append(int(line.split("=")[1].split(",")[0]))
        y_goal.append(int(line.split("=")[2]))


s = 0
qwe = 0
for a in range(len(x_goal)):
    x1 = x_step[2*a]
    x2 = x_step[2*a+1]

    y1 = y_step[2*a]
    y2 = y_step[2*a+1]

    X = x_goal[a] + 10000000000000
    Y = y_goal[a] + 10000000000000

    B = (X - Y*(x1/y1)) / (x2 - y2*(x1/y1))
    A = (X - B*x2) / x1

    if is_almost_integer(A) and is_almost_integer(B):
        print(a)
        s += A*3 + B

print(s)
