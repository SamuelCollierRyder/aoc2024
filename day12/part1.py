def dfs(row, col, region, crop):
    if row < 0 or row >= len(lines):
        return
    if col < 0 or col >= len(lines[row]):
        return
    if (row, col) in region:
        return
    if lines[row][col] != crop:
        return

    region.append((row, col))
    dfs(row-1, col, region, crop)
    dfs(row+1, col, region, crop)
    dfs(row, col-1, region, crop)
    dfs(row, col+1, region, crop)

def get_neighbors(row, col):
    return [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

def place_fence(row, col, region):
    new_parimeter = 0
    for neighbor in get_neighbors(row, col):
        if neighbor not in region:
            new_parimeter += 1
    return new_parimeter


def read_input():
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines


if __name__ == "__main__":
    lines = read_input()

    price = 0
    visited = set()

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if (row, col) in visited:
                continue

            region = []
            crop = lines[row][col]
            dfs(row, col, region, crop)
            area = len(region)
            perimeter = 0
            for plot in region:
                fence = place_fence(plot[0], plot[1], region)
                perimeter += fence
            price += area * perimeter

            for crop in region:
                visited.add(crop)

    print(price)

