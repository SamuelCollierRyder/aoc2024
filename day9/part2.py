with open("example_input.txt") as f:
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

print("".join(new_text))
lp = 0
up = len(new_text) - 1
while lp < up:
    while new_text[up] == ".":
        up -= 1

    if new_text[lp] == ".":
        space_size = 1
        while new_text[lp + space_size] == ".":
            space_size += 1

        data_size = 0
        while new_text[up - data_size] == new_text[up]:
            print(new_text[up], data_size)
            data_size += 1

        if data_size <= space_size:
            new_text[lp: lp+data_size] = new_text[up-data_size+1:up+1]
            new_text[up-data_size+1:up+1] = "." * data_size

        up -= data_size

    else:
        lp += 1

print("".join(new_text))
check_sum = 0
found_dot = False
for i in range(len(new_text)):
    if new_text[i] != ".":
        check_sum += int(new_text[i]) * (i)
        # assert not found_dot
    else:
        found_dot = True

print(check_sum)
