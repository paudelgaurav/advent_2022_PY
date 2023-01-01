import string

with open("data.txt", "r") as f:
    lines = f.readlines()
    items = [entry.strip() for entry in lines]

alphabets = string.ascii_lowercase + string.ascii_uppercase

# assigning priority to alphabets
priority_map = {item: index for index, item in enumerate(alphabets, start=1)}

total_sum = 0
for count, item in enumerate(items, start=1):
    half = len(item) // 2
    f_half = set(item[:half])
    l_half = set(item[half:])
    common_item = f_half.intersection(l_half)
    total_sum += priority_map[list(common_item)[0]]

print(total_sum)
