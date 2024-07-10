def read_file(file_name, number_of_lines):
    with open(file_name, 'r') as file:
        for line in range(number_of_lines):
            print(file.readline().strip())


read_file("Text.txt", 3)
