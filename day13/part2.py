import math
with open("example_input.txt") as file:
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
for a in range(len(x_goal)):
    print(a)
    x1 = x_step[2*a]
    x2 = x_step[2*a+1]


    y1 = y_step[2*a]
    y2 = y_step[2*a+1]

    x_g = x_goal[a] + 10000000000000
    y_g = y_goal[a] + 10000000000000

    matches = []
    m_x = min(x1, x2)
    m_y = min(y1, y2)
    b = min(x_g // m_x, y_g // m_y)

    found_val = False
    for i in range(b):
        nx_g = x_g - i * x1
        if nx_g % x2 == 0:
            x2_step = nx_g // x2
            if x2_step * y2 == y_g - i * y1:
                s += i*3+x2_step
                break
print(s)
