with open("example_input.txt") as f:
    text = f.read()
    text = text.strip()

new_text = ""
file = True
file_count = 0
for c in text:
    if file:
        new_text += str(file_count) * int(c)
        file_count += 1
        file = False

    else:
        new_text += "." * int(c)
        file = True

print(new_text)
new_text = list(new_text)

lp = 0
up = len(new_text) - 1
while up >= lp:
    if new_text[lp] == ".":
        new_text[lp] = new_text[up]
        new_text[up] = "."
        lp += 1
        up -= 1

    else:
        lp += 1

check_sum = 0
for i in range(len(new_text)):
    if new_text[i] != ".":
        check_sum += int(new_text[i]) * (i)

print(check_sum)
