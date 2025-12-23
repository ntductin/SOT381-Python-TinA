def tien(loai_tv,hoa_don):
    tien=hoa_don
    if loai_tv=='vip':
        tien=hoa_don*0.9
    if hoa_don>1_000_000:
        tien-=50_000
    return int(tien)
loai_tv=input('Thanh vien loai vip hay thuong: ').lower()
hoa_don=int(input('Hoa don cua ban(VND): '))
print(f'So tien ban phai tra la: {tien(loai_tv,hoa_don):,} VND')