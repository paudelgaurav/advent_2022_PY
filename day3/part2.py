import string

with open("data.txt", "r") as f:
    lines = f.readlines()
    items = [entry.strip() for entry in lines]

alphabets = string.ascii_lowercase + string.ascii_uppercase

# assigning priority to alphabets
priority_map = {item: index for index, item in enumerate(alphabets, start=1)}

total_sum = 0
counter = 1
for item in items:
    if counter == 1:
        first_item = set(item)
        counter += 1
    elif counter == 2:
        second_item = set(item)
        counter += 1
    elif counter == 3:
        third_item = set(item)
        common = first_item.intersection(second_item, third_item)
        total_sum += priority_map[list(common)[0]]
        counter = 1

print(total_sum)
