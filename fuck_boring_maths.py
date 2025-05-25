import torch 
m = torch.tensor(
    [
     [1., 1.],
     [2., 2.],
     [3., 3.],
     [4., 4.]
    ]
)

import pprint
pp = pprint.PrettyPrinter(); pp.pprint("Mean: {}".format(m.mean())); 

## concating in dimension 0 and 1
a = torch.ones((4,3)) * 6
a_cat0 = torch.cat([a, a, a], dim=0)
a_cat1 = torch.cat([a, a, a], dim=1)

print("Initial shape: {}".format(a.shape))
print("Shape after concatenation in dimension 0: {}".format(a_cat0.shape))
print("Shape after concatenation in dimension 1: {}".format(a_cat1.shape))

# a.add() means a + b but it copy and creates a new but add_() in_place
