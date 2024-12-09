with open("input.txt") as f:
    text = f.read()
    text = text.strip()

new_text = []
file = True
file_count = 0
for c in text:
    if file:
        new_text += [str(file_count)] * int(c)
        file_count += 1
        file = False

    else:
        new_text += ["."] * int(c)
        file = True

lp = 0
up = len(new_text) - 1
while lp < up:
    while new_text[up] == ".":
        up -= 1

    if new_text[lp] == ".":
        new_text[lp] = new_text[up]
        new_text[up] = "."
        lp += 1

    else:
        lp += 1

# For some reason I get an off by one error if I don't do 
# a second pass
lp = 0
up = len(new_text) - 1
while lp < up:
    while new_text[up] == ".":
        up -= 1

    if new_text[lp] == ".":
        new_text[lp] = new_text[up]
        new_text[up] = "."
        lp += 1

    else:
        lp += 1

with open("output.txt", "w") as f:
    f.write("".join(new_text))

check_sum = 0
found_dot = False
for i in range(len(new_text)):
    if new_text[i] != ".":
        check_sum += int(new_text[i]) * (i)
        assert not found_dot
    else:
        found_dot = True

print(check_sum)