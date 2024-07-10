courses = []

with open("../CSV_Files/courses.csv", "r") as file:
    for line in file:
        language, category = line.strip().split(",")
        courses.append({"language": language, "category": category})

for course in courses:
    print(course)