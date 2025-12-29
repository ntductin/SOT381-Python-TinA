n=int(input('Nhap n: '))
ds=[]
for i in range(1,n+1):
    so=int(input(f'Nhap so thu {i}: '))
    ds.append(so)
kq=[]
s=0
for i in ds:
    if i%2==0 and i%3==0:
        s+=i
print(f'Tong cac so chia het cho ca 2 va 3: {s}')