import torch

c = torch.tensor([20,1,3,7,8])

c[0] = 100

print(c)

d = c[1:4]
c[3:5] = torch.tensor([200.1,21])

print(c.type(torch.FloatTensor))