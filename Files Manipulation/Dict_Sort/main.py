courses = []
with open("../CSV_Files/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.strip().split(",")
        courses.append({"language": language, "category": category})


def get_language(course):
    return course["language"]


def get_category(course):
    return course["category"]


for course in sorted(courses, key=get_language):
    print(course)
