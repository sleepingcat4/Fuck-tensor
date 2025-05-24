import torch 
import torch.nn as nn
import pprint 
pp = pprint.PrettyPrinter()

# explaining tensor
# it's matrix with an extra dose of dimension
# 3x256x256

# making a tensor from python list
data = [
    [0, 1],
    [2, 3],
    [4, 5]
]

x_python = torch.tensor(data)
# print(x_python)

# we can specify the datatype as well
bool_python = x_python.bool()
# print(bool_python)