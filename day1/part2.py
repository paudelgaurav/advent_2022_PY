with open("data.txt", "r") as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]

current_sum = 0
elf_sums = []
for calory in calories:
    if calory != "":
        current_sum += int(calory)
    else:
        elf_sums.append(current_sum)
        current_sum = 0
# for the last input
elf_sums.append(current_sum)
print(max(elf_sums))

sum_of_top_three = 0
for _ in range(3):
    sum_of_top_three += max(elf_sums)
    elf_sums.remove(max(elf_sums))

print(sum_of_top_three)
