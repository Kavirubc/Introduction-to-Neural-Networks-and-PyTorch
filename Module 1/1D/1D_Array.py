import torch

a = torch.tensor([1,2,3,4,5])
b = torch.tensor([0.1,2.3],dtype=torch.int32)

# print(b.dtype)

c = torch.FloatTensor([0,1,2,3,4])

a=a.type(torch.FloatTensor)
print(a.dtype)
print(a.size)

print("Size of the tensor is "+ str(a.size()))
print("Dimention is "+ str(a.ndimension()))

a_col =a.view(-1,1)
print(a_col)

#Can convert pandas and numpy in to tensors using specific methods as well



