a=float(input('Nhap a: '))
b=float(input('Nhap b: '))
if a==0 and b==0:
    print('Phuong trinh co vo so nghiem')
elif a==0 and b!=0:
    print('Phuong trinh vo nghiem')
elif a!=0:
    print(f'Phuon trinh co mot nghiem x={-b/2*a}')