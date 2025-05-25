import torch 
x = torch.tensor([2,1], dtype=torch.float16, requires_grad=True)
# print(x)
y = (x *  x * 3).sum() # 3x^2
y.backward()
print(x.grad)
