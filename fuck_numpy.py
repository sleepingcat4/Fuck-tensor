import numpy as np 

# copied it from other place
data = [
        [0, 1], 
        [2, 3],
        [4, 5]
       ]

ndarray = np.array(data)
import torch 
x_numpy = torch.from_numpy(ndarray)
print(x_numpy)

# torch.rand_like() grabs random from uniform distrib
# torhc.randn_like() grabs randome from normal distrib
shape = (2, 3, 2)
x_zeros = torch.zeros(shape)
# print(x_zeros)
# print(x_zeros.shape) 


x = torch.arange(10)
print(x) # vector
