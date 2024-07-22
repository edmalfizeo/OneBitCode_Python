from pathlib import Path
from datetime import datetime

path = Path('C:/Users/dudum/OneDrive/Documents/OneBitCode_Python/Automation/files')
file_paths = path.glob('**/*')
for path in file_paths:
    if path.is_file():
        stats = path.stat()
        second_created = stats.st_ctime
        date_created = datetime.fromtimestamp(second_created)
        date_created_str = date_created.strftime('%d-%m-%Y_%H_%M_%S')
        new_file_name = f'{date_created_str}_{path.name}'
        new_file_path = path.with_name(new_file_name)
        path.rename(new_file_path)