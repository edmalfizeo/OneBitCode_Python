from pathlib import Path

root_directory = Path('/Automation/files/data')
file_paths = list(root_directory.iterdir())
for path in file_paths:
    new_file_name = f'new_{path.stem}{path.suffix}'
    new_file_path = path.with_name(new_file_name)
    path.rename(new_file_path)
