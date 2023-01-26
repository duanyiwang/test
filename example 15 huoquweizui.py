import os
import shutil

dir = './example 15'

for file in os.listdir(dir):

    ext = os.path.splitext(file)[1][1:]

    pathfile = os.path.join(dir, ext)
    if not os.path.isdir(pathfile):
        os.mkdir(pathfile)
    print(pathfile)
    source_path = f"{dir}/{file}"
    target_path = f"{pathfile}/{file}"
    shutil.move(source_path, target_path)
