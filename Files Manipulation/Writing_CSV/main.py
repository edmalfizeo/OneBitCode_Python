import csv

# Writing CSV file
language_name = input("Enter the name of the language: ")
category = input("Enter the category where the language fits: ")

with open("languages.csv", mode="a", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow([language_name, category])