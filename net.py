import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 6, 3)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv3 = nn.Conv2d(16, 64, 2)
        self.conv4 = nn.Conv2d(64, 75, 4)
        self.conv5 = nn.Conv2d(75, 120, 5)
        self.pool2 = nn.MaxPool2d(2, 2)


        self.fc1 =  nn.Linear(120*2*2, 350)
        self.fc2 = nn.Linear(350, 250)
        self.fc3 = nn.Linear(250, 175)
        self.fc4 = nn.Linear(175, 90)
        self.fc5 = nn.Linear(90, 50)
        self.fc6 = nn.Linear(50, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv2(F.relu(self.conv1(x)))))
        x = self.pool2(F.relu(self.conv5(F.relu(self.conv4(F.relu(self.conv3(x)))))))
        x = x.view(-1, 120*2*2)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = F.relu(self.fc5(x))
        x = self.fc6(x)
        return x