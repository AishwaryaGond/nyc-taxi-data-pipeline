from pathlib import Path

for file in Path('.').iterdir():
    print(file.name)
