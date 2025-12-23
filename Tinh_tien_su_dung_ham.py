def tinh_tien(tong,nguoi):
    return int(tong/nguoi)
tong=int(input('Nhap tong tien: '))
nguoi=int(input('Nhap so nguoi: '))
print(f'{tinh_tien(tong,nguoi):,}VND/nguoi')