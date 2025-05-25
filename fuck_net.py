import torch.nn as nn
import torch 

block = nn.Sequential(
    nn.Linear(4, 2),
    nn.Sigmoid()
    
)

input = torch.ones(2, 3, 4)
output = block(input)
print(output)

## let's define a perceptron
class MultilayerPerceptron(nn.Module):
    def __ini__(self, input_size, hidden_size):
        super(MultilayerPerceptron, self).__init__()
        self.input_size = input_size 
        self.hidden_size = hidden_size 
        
        self.linear = nn.linear(self.input_size, self.hidden_size)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(self.hidden_size, self.input_size)
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):
        linear = self.linear()
        relu = self.relu(linear)
        linear2 = self.linear2(relu)
        output = self.sigmoid(linear2)
        return output