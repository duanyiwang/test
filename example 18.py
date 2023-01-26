import os

datadir = './data/example 18'
contents = []

for file in os.listdir(datadir):
    filepath = f"{datadir}/{file}"
    if os.path.isfile(filepath) and file.endswith(".txt"):
        with open(filepath, encoding="utf-8") as fin:
            contents.append(fin.read())
final_content = "\n".join(contents)
with open("./data/new.txt", mode="a", encoding="utf-8") as ffin:
    ffin.write(final_content)
