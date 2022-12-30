import os
import shutil

from_dir = "C:/Users/DELL/Downloads"
to_dir = "C:/Users/DELL/Desktop"
list_of_files = os.listdir(from_dir)
print(list_of_files)

for fileName in list_of_files :
    name, ext = os.path.splitext(fileName)
    if ext == "" :
        continue
    if ext in [".gif", ".png", ".jpg", ".jpeg"] :
        path1 = from_dir + "/" + fileName
        path2 = to_dir + "/" + "ImageFiles"
        path3 = to_dir + "/" + "ImageFiles" + "/" + fileName
        if os.path.exists(path2) :
            print("Moving Files")
            shutil.move(path1, path3)
        else : 
            os.mkdir(path2)
            print("Moving Files")
            shutil.move(path1, path3)