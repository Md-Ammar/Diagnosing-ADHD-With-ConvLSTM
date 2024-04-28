import pandas as pd
import shutil

dataset_dir = r"D:\All Projects\ML\ADHD\Peking_1"
data_dir = r"D:\All Projects\ML\ADHD\Diagnosing-ADHD-With-ConvLSTM-master\Data\training_peking.csv"
new_samples = r"D:\All Projects\ML\ADHD\Diagnosing-ADHD-With-ConvLSTM-master\Smaller_samples"

data = pd.read_csv(data_dir)

samples = data[data['DX'].isin([0, 1, 3])].groupby('DX').apply(lambda x: x.sample(n=10)).reset_index(drop=True)

for index, sample in samples.iterrows():
    file_path = dataset_dir + "\\" + sample["Image"]
    shutil.copy(file_path, new_samples)
    