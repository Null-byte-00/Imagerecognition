import torch
import pandas as  pd
from model import Model

model = Model()
dataset_file = 'dataset.hdf'

frame = pd.read_hdf(dataset_file)
for _ in range(1):
    for i in frame.index:
        inp = torch.tensor(frame['image'][i], dtype=torch.float32).unsqueeze(0)
        labels = {
            "house": 0,
            "smilingface": 1,
            "fish": 2,
        }
        target_tensor = torch.tensor([0.,0.,0.])
        target_tensor[labels[frame['label'][i]]] = 1.
        print(target_tensor)
        model.trainn(inp, target_tensor)

model.save()