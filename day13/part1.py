import math

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
for a in range(len(x_goal)):
    x1 = x_step[2*a]
    x2 = x_step[2*a+1]

    y1 = y_step[2*a]
    y2 = y_step[2*a+1]

    x_g = x_goal[a]
    y_g = y_goal[a]

    gcd_x = math.gcd(x1, x2)
    gcd_y = math.gcd(y1, y2)

    if x_g % gcd_x != 0 or y_g % gcd_y != 0:
        continue

    for i in range(100):
        nx_g = x_g - i * x1
        if nx_g % x2 == 0:
            x2_step = nx_g // x2
            if x2_step * y2 == y_g - i * y1:
                s += i*3+x2_step
                break
print(s)
