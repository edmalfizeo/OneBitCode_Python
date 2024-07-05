import re

def check_character(text):
    rule = re.compile(r'^[a-zA-Z0-9]+$')
    if rule.search(text):
        result = "The string contains only letters and numbers."
    else:
        result = "The string contains other characters."
    return result


def main():
    text = input("Enter a text: ")
    print(check_character(text))


main()
