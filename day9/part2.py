with open("input.txt") as f:
    text = f.read()
    text = text.strip()

new_text = []
data = []
data_index = []
file = True
file_count = 0
i = 0
for c in text:
    if file:
        s = [str(file_count)] * int(c)
        new_text += s
        data.append(s)
        data_index.append(i)
        file_count += 1
        file = False

    else:
        new_text += ["."] * int(c)
        file = True
    i += int(c)

new_text = list(new_text)
data = data[::-1]
data_index = data_index[::-1]
c = 0

for k, d in enumerate(data):
    done = False
    for i in range(data_index[k]):
        if new_text[i] == ".":
            size = 0
            while i + size < len(new_text) and new_text[i + size] == ".":
                size += 1

            if size >= len(d):
                new_text[i : i + len(d)] = d
                di = data_index[k]
                new_text[di : di + len(d)] = "." * len(d)
                c += 1
                done = True
        if done:
            break

check_sum = 0
for i in range(len(new_text)):
    if new_text[i] != ".":
        check_sum += int(new_text[i]) * i

print(check_sum)
