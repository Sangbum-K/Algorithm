n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

class p():
    def __init__(self,n,a,r):
        self.n = n
        self.a = a
        self.r = r

pp = []

for i in range(n):
    pp.append(p(name[i],street_address[i],region[i]))

pp.sort(key = lambda x:x.n,reverse = True)

print('name',pp[0].n)
print('addr',pp[0].a)
print('city',pp[0].r)