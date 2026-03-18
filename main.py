import os
import hashlib

files_hash = {}

folder = r"C:\Users\Sanjib Dey\OneDrive\Desktop\python\test_folder"

if os.path.exists(folder):
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        with open(path, "rb") as file:
            content = file.read()
            file_hash = hashlib.md5(content).hexdigest()

            if file_hash in files_hash:
                print("Duplicate found:", filename)
            else:
                files_hash[file_hash] = filename
else:
    print("Folder not found")