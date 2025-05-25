import torch 
x = torch.Tensor([
    [[1, 2], [3, 4]], 
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])

# print(x.shape)
# acccesing the 0th element which is the first row
# print(x[0]) # equivalent to x[0, :]

# getting top left using :
# print(x[:, 0, 0])

# creating new fucking tensor 
i = torch.tensor([0, 0, 1, 1])
# print(x[i]) # in pytorch it needs to be a tensor list to index another tensor
# i can be written as x[0], x[0], x[1], x[1]

i = torch.tensor([1, 2]) # targeting the dim
j = torch.tensor([0]) # targeting the row

# print(x[i, j])
# torch.tensor and torch.Tensor are same except torch.tensor is the newest one
# fuck another 
print(x[0, 0, 0]) # block 0, row 0, column 0
# change to python scalar value
# use item
print(x[0, 0, 0].item())