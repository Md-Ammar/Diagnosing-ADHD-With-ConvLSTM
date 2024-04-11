#creating a training_peking file for the Peking dataset
#The file contains the image name and the corresponding diagnosis
#The diagnosis is extracted from the phenotypic.csv file

import pandas as pd
import os
import re

phenotypic = r"phenotypic.csv"
data_dir = r"D:\Peking_1"

data = pd.read_csv(phenotypic)

result = {"Image": [],
          "DX": []}

os.chdir(data_dir)

for file in os.listdir(data_dir):
    f = re.search(re.compile(r"(\d+)_"), file)
    name = f.group(1)

    result['Image'].append(file)
    result['DX'].append(list(data[data['ScanDir ID'] == int(name)]['DX'])[0])

result = pd.DataFrame(result)
result.to_csv(r"training_peking.csv", index=False)
