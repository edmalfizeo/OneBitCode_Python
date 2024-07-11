import glob, os, zipfile

# 1 - Current working directory
os.getcwd()

# 2 - List .txt files in a directory
for file in glob.glob("../Sorting_File/*.txt"):
    print(file)

# 3 - List .csv files in a directory
for file in glob.glob("../CSV_Sort/*.csv"):
    print(file)

# 4 - Compact files .txt
with zipfile.ZipFile('files.zip', 'w') as myzip:
    for file in glob.glob("../Sorting_File/*.txt"):
        myzip.write(file)

# 5 - Compact All files
with zipfile.ZipFile('all_files.zip', 'w') as myzip:
    for file in glob.glob("*"):
        myzip.write(file)