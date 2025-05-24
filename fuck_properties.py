# ain't having property on my name soon so let's teach tensor properties
import torch
x = torch.ones(3, 2)
print(x.dtype)
print(x.shape)

fuck_x = x = torch.Tensor([[1, 2], [3, 4], [5, 6]])

print(fuck_x.shape[0]) # number of elements # 0th is the row number 

# now size which means how many rows it holds in one axis/dimension
print(fuck_x.size(0))

