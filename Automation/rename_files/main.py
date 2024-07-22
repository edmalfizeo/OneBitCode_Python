from pathlib import Path

root_directory = Path('C:/Users/dudum/OneDrive/Documents/OneBitCode_Python/Automation/files')
# file_paths = root_directory.iterdir()
# for path in file_paths:
#     print(path)
#     for file_path in path.iterdir():
#         print(file_path)
file_paths = root_directory.glob('**/*')
for path in file_paths:
    # print(path)
    if path.is_file():
        # print(path.parts)
        parent_directory = path.parts[-2]
        new_file_name = f'{parent_directory}_{path.name}'
        # print(new_file_name)
        new_filepath = path.with_name(new_file_name)
        path.rename(new_filepath)
