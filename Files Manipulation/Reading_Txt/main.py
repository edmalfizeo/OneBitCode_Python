"""
1 - w for write
2 - a for append
3 - r for read
"""

with open("../Writing_Txt/names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"Name: {line.rstrip()}")