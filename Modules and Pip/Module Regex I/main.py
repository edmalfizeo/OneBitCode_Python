import re

text = "The rain in Spain"
# Initial Index and Final Index of the string
print("-" * 20)
print("Initial Index and Final Index of the string")
match = re.search(r'Spain', text)
print(match.start(), match.end())

# Find the index of the point
print("-" * 20)
print("Find the index of the point")
website = 'https://www.google.com'
match = re.search(r'\.', website)
print(match)

# Find a list of characters in the string
print("-" * 20)
print("Find a list of characters in the string")
pattern = "[a-m]"
result = re.findall(pattern, text)
print(text)
print(result)

# Verify the beginning of the string
print("-" * 20)
print("Verify Beginning of the string")
rule = "^A"
phrases = ["Apple", "Banana", "Orange"]
for phrase in phrases:
    if re.findall(rule, phrase):
        print(f"Matche: {phrase}")
    else:
        print(f"No Match: {phrase}")

# Verify the end of the string
print("-" * 20)
print("Verify End of the string")
rule = "e$"
phrases = ["Apple", "Banana", "Orange"]
for phrase in phrases:
    if re.findall(rule, phrase):
        print(f"Matche: {phrase}")
    else:
        print(f"No Match: {phrase}")
