# ain't having property on my name soon so let's teach tensor properties
import torch
x = torch.ones(3, 2)
print(x.dtype)
print(x.shape)

fuck_x = x = torch.Tensor([[1, 2], [3, 4], [5, 6]])

print(fuck_x.shape[0]) # number of elements # 0th is the row number 

# now size which means how many rows it holds in one axis/dimension
print(fuck_x.size(0))

# what's view
# we change the way tensor is shaped
# it is manipulating the actual tensor since both share same mem address
x_view = fuck_x.view(-1, 3)
print(f'Fucking changed the view dim {x_view.shape}. Previous was {fuck_x}')


# we can do auto infer of dim than calc
x_view = fuck_x.view(-1, 3)
print("printing auto infer dim............")
print(x_view)

x1 = torch.arange(10).reshape(5, 2) # 5x2 tensor
print(x1)

# 5 rows 2 columns

# adding a new dim of size 2
x2 = x1.unsqueeze(1)
print(x2.shape)
print(x2)

# getting rid of dim 1 from tensor x2
x3 = x2.squeeze()
print(x3.shape)

### Getting total number of elements in a tensor
x4 = x3.numel()
print(x4)

