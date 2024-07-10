import csv

courses = []
with open("../CSV_Files/courses.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        courses.append({"language": row["Language"], "category": row["Category"]})

for course in sorted(courses, key=lambda x: x["language"]):
    print(f"{course['language']} - {course['category']}")