n=int(input('Nhap n: '))
ds=[]
for i in range(1,n+1):
    so=int(input(f'Nhap so thu {i}: '))
    ds.append(so)
kq=[]
for i in ds:
    if i%2==0 and i%3==0:
        kq.append(i)
print(f'Danh sach cac so chia het cho ca 2 va 3: {kq}')