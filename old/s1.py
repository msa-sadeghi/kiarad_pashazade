import os
import shutil

directory = 'robot'

files = os.listdir(directory)

for f in files:
    full_path = os.path.join(directory, f)

    if os.path.isdir(full_path):
        continue

    name, ext = os.path.splitext(f)
    prefix = name.split()[0]

    des_folder = os.path.join(directory, prefix)

    if not os.path.exists(des_folder):
        os.mkdir(des_folder)

    last_path = os.path.join(des_folder, f)

    shutil.move(full_path, last_path)

    print(last_path)
