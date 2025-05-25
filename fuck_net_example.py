import torch.nn as nn; import torch 

class MultilayerPerceptron(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(MultilayerPerceptron, self).__init__()
        self.input_size = input_size 
        self.hidden_size = hidden_size 
        
        self.linear = nn.Linear(self.input_size, self.hidden_size)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(self.hidden_size, self.input_size)
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):
        linear = self.linear(x)
        relu = self.relu(linear)
        linear2 = self.linear2(relu)
        output = self.sigmoid(linear2)
        return output
    
# importing optimizer 
import torch.optim as optim 
y = torch.ones(10, 5)
x = y + torch.randn_like(y)

model = MultilayerPerceptron(5, 3)
adam = optim.Adam(model.parameters(), lr=1e-1)
loss_func = nn.BCELoss()

# prediction on how model doin to calc loss
y_pred = model(x)
loss_func(y_pred, y).item()

n_epochs = 2
for epoch in range(n_epochs):
    # setting the gradients to 0
    adam.zero_grad()
    y_pred = model(x)
    loss = loss_func(y_pred, y)
    print(f'Epoch {epoch}: and training loss: {loss}')
    # computing the gradients
    loss.backward()
    # take a step to optimize the weights
    adam.step()