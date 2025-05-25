import torch 
x = torch.Tensor([[1, 2], [3, 4]]) # example tensor
# print(x.device)

if torch.cuda.is_available():
    print("FUCK CUDA!")
else:
    print("Bloody CPU")
    x.to("cpu")