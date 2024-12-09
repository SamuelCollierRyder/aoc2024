with open("example_input.txt") as f:
    text = f.read()
    text = text.strip()

new_text = []
file = True
file_count = 0
for c in text:
    if file:
        if c != "0":
            new_text.append(str(file_count) * int(c))
        file_count += 1
        file = False

    else:
        if c != "0":
            new_text.append("." * int(c))
        file = True

lp = 0
up = len(new_text) - 1

while lp < up:
    if "." not in new_text[lp]:
        lp += 1

    elif "." not in new_text[up]:
        up -= 1

    else:
        if len(new_text[lp]) >= len(new_text[up]):
            dot_len = len(new_text[lp])
            new_text[lp] = new_text[up]
            new_text[up] = "." * len(new_text[up])
            if len(new_text[up]) < dot_len:
                new_text.insert(lp+1, "." * (dot_len - len(new_text[up])))

            up -= 1
            lp += 1

            print(new_text)
            quit()

