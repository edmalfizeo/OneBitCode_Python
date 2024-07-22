from pathlib import Path

p1 = Path('/Automation/files/data/teste.txt')
print(p1)
print(type(p1))
print(p1.name)
print(p1.suffix)
print(p1.stem)
if p1.exists():
    with open(p1, 'r', encoding='utf-8') as file:
        print(file.read())
else:
    print("O arquivo não existe.")


p2= Path('/Automation/files/data')
print(list(p2.iterdir()))
