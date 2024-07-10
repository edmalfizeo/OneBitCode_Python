name = input("Write your name: ")

"""
1 - w for write
2 - a for append
3 - r for read
"""

# Alternative 1
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# Alternative 2
with open("names.txt", "a") as file:
    file.write(f"{name}\n")