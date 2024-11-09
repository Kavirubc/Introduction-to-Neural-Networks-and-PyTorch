import torch

u = torch.tensor([1.0,0.0])
v = torch.tensor([0.0,1.0])
w = torch.tensor([0.0,1.0])

z = u+v

print(z)
# print("Type of Z is "+ str(z.dtype))
# print("Type of Z is "+ str(z.type))
# print("Type of Z is "+ str(z.size()))


#vectors and scalars

m = 2*z

print(m)

#Product of 2 tensors

result = torch.dot(w,v)

print(result.mean())

