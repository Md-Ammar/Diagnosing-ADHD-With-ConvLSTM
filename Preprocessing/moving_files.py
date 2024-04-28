import os
import re
import shutil

data_dir = r"D:\Peking_1_preproc\Peking_1" # Downloaded files directory

os.chdir(data_dir)
files = os.listdir()

dest_dir = r"D:\Peking_1"

for file in files:
    cur_dir = data_dir+f"\\{file}" # accessing each folder
    os.chdir(cur_dir)

    for f in os.listdir(cur_dir):
        m = re.match("(snwmrda|sfnwmrda).+(nii.gz)", str(f)) # getting required file
        if m:
            print(m.group())
            shutil.copy(cur_dir+"\\"+str(m.group()), dest_dir) # copying files at dest_dir
