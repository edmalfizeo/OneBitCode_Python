import os

# 1 - Get root directory
base_path = os.path.expanduser("~")

# 2 - Navigate to the Download directory
path = os.path.join(base_path, "Downloads")
work_dir = os.chdir(path)

# 3 - List all file in the directory
list_files = os.listdir(work_dir)
print(list_files)

# 4 - adding folders
type_files = ['exe', 'pdf', 'zip', 'jpg', 'png', 'docx', 'pptx', 'xlsx', 'mp4', 'mp3', 'txt', 'csv', 'json', 'xml', 'mov', 'msi', 'ipynb', 'jar', 'html', 'sql', 'torrent', 'pat']
for type in type_files:
    if not os.path.exists(type):
        os.mkdir(type)

# 5 - Move files to the respective folders
for file in list_files:
    file_extension = file.split('.')[-1].lower()
    if file_extension in type_files:
        old_path = os.path.join(path, file)
        new_path = os.path.join(path, file_extension, file)
        if os.path.exists(old_path) and not os.path.exists(new_path):
            try:
                os.replace(old_path, new_path)
                print(f"Moved {file} to {new_path}")
            except Exception as e:
                print(f"Error moving {file}: {e}")
        elif not os.path.exists(old_path):
            print(f"File not found: {old_path}")
        else:
            print(f"File {file} already moved to {new_path}")


