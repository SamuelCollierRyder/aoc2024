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
print(new_text)
