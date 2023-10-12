import torch
from torch import nn 
from torch.optim import SGD
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.stack = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=4, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3),
            nn.Conv2d(in_channels=4, out_channels=4, kernel_size=3),
            nn.ReLU(),
            #nn.Dropout(0.25),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Flatten(start_dim=0),
            nn.Linear(26244, 3000),
            nn.ReLU(),
            #nn.Dropout(0.5),
            nn.Linear(3000, 3),
        )
        self.optimizer = SGD(self.parameters(), lr=0.001)
        self.criterion = nn.MSELoss()
    
    def forward(self, x):
        with torch.no_grad():
            print(self.stack(x))
        return F.softmax(self.stack(x), dim=-1)
    
    def trainn(self, inp, target, verbose=True):
        output = self.forward(inp)
        loss = self.criterion(output, target)
        loss.backward()
        self.optimizer.step()
        if verbose:
            print(loss)
    
    def save(self, file_name='models/model.pth'):
        torch.save(self.state_dict(), file_name)
    
    def load(self, file_name='models/model.pth'):
        self.load_state_dict(torch.load(file_name))



