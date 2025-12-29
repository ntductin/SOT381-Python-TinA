def tinh_cuoc_taxi(km):
    if km>0 and km<=1:
        thanh_tien= 15_000
    elif km>=2 and km<=10:
        thanh_tien= 15_000 + 12_000*(km-1)
    else:
        thanh_tien= 15_000 + 12_000*9 + 10_000*(km-10)
    if km>100:
        thanh_tien*=0.9
    return thanh_tien
nhap_km=float(input('Nhap so km ban di: '))
ket_qua= tinh_cuoc_taxi(nhap_km)
print(f'So tien ban phai tra la {ket_qua:,} VND')

        