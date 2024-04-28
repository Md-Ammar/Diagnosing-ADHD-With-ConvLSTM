import pandas as pd
import os, shutil

df = pd.read_csv(r'D:\All Projects\ML\ADHD\Diagnosing-ADHD-With-ConvLSTM-master\Data\training_peking.csv')

folder_path = 'D:\All Projects\ML\ADHD\Peking_1'
os.chdir(folder_path)

destination_path = "D:\All Projects\ML\ADHD\Peking_new"

l = len(df['Image'])

for i in range(l):
    print(f"{i}. Copying file {df['Image'][i]}...")
    
    shutil.copy(df["Image"][i], destination_path + "\\" + f"{df['Image'][i][:-7]}_" + str(df["DX"][i]) + ".nii.gz")