with open("data.txt", "r") as f:
    lines = f.readlines()
    items = [entry.strip() for entry in lines]

total = 0
for count, item in enumerate(items, start=1):
    data = item.split(",")
    f_item, s_item = data[0], data[1]
    f_item_nums, s_item_nums = f_item.split("-"), s_item.split("-")

    start1, end1 = int(f_item_nums[0]), int(f_item_nums[1])
    start2, end2 = int(s_item_nums[0]), int(s_item_nums[1])

    task1 = {start1} if start1 == end1 else set(range(start1, end1 + 1))
    task2 = {start2} if start2 == end2 else set(range(start2, end2 + 1))

    if task1.issubset(task2) or task2.issubset(task1):
        total += 1

print(total)
