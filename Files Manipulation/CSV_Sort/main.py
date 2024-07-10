with open('../CSV_Files/courses.csv', 'r', encoding="utf-8") as file:
    for line in sorted(file):
        language, category = line.rstrip().split(',')
        with open("sorted_courses.csv", "a", encoding="utf-8") as sorted_file:
            sorted_file.write(f'{language},{category}\n')
