with open("input.txt") as file:
    rows = file.readlines()

def is_safe(nums):
    increasing = bool(nums[0] > nums[1])
    for i in range(len(nums)-1):
        diff = nums[i] - nums[i+1]

        if abs(diff) > 3 or abs(diff) == 0:
            break

        if increasing and diff < 0:
            break

        if not increasing and diff > 0:
            break

        if i == len(nums)-2:
            return True
    return False


safe = 0
for row in rows:
    nums = [int(n) for n in row.split(" ")]
    safe += is_safe(nums)

print(safe)

