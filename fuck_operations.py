import torch; x = torch.ones(3, 2, 2); print(x) # creating an example tensor 
# use sub, add, multi and div 
x += 2; print(x); x -= 2; print(x); x *= 2; print(x); x /= 2; print(x)

# applying the operations in tensors
a = torch.ones((4, 3)) * 6; print(a); b = torch.ones(3) * 2; print(b); a /= b; print(a)

# in tensor matrix multi, you have transpose second matrix to match inner dim. 
# a @ b.T or use a.matmul(b)
a = torch.ones((4, 3)) * 6; print(a); b = torch.ones(3) * 2; ans = a.matmul(b); print(ans)