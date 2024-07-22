from pathlib import Path
from datetime import datetime

path = Path('C:/Users/dudum/OneDrive/Documents/OneBitCode_Python/Automation/files/data2/teste.txt')

stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)

date_created_str = date_created.strftime('%d/%m/%Y %H:%M:%S')
print(date_created_str)