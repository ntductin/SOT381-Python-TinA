def is_armstrong(n):
    if n<0:
        return Fasle
    str_n=str(n)
    k=len(str_n)
    total=0
    for digit in str_n:
        total+=int(digit)**k
    return total==n
n=int(input('Nhap n: '))
ds=[]
for i in range(1,n+1):
    so=int(input(f'Nhap so thu {i}: '))
    ds.append(so)
ds_armstrong=[]
for so in ds:
    if is_armstrong(so):
        ds_armstrong.append(so)
print(f'Danh sach cac so armstrong la: {ds_armstrong}')
print(f'So luong so armstrong la: {len(ds_armstrong)}')
    
        