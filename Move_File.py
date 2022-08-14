from distutils import extension
import os
import shutil

from_dir="C:/Users/LENOVO/OneDrive/Desktop"
to_dir="C:/Users/LENOVO\OneDrive/DownloadedImages"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name,extension=os.path.splitext(file)
    
    #Project112
    if extension=="":
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1=from_dir+'/'+file
        path2=to_dir+'/'+"Document_Files"
        path3=to_dir+'/'+"Document_Files"+'/'+file

        #CHECK IF FOLDER/DIRECTORY PATH EXISTS BEFORE MOVING
        #ELSE MAKE A NEW FOLDER/DIRECTORY THEN MOVE

        if os.path.exists(path2):
            print("Moving" + file + ".....")

            # MOVE FROM PATH1 ---> PATH3
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving" + file + ".....")
            shutil.move(path1, path3)