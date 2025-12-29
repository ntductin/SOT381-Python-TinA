x=float(input('Nhap x: '))
n=int(input('Nhap n: '))
import math
s=0
for i in range(n+1):
    s+=math.sqrt(x+s)
print(f'Tong bang: {s} ')
