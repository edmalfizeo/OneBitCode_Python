courses = []
with open("../CSV_Files/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.strip().split(",")
        courses.append({"language": language, "category": category})

for course in sorted(courses, key=lambda course: course["language"]):
    print(course)