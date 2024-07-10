names = []

with open('../Writing_Txt/names.txt', 'r', encoding="utf-8") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    with open('sorted_names.txt', 'a', encoding="utf-8") as file:
        file.write(name + '\n')
