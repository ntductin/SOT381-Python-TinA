def doi_tien(usd):
    ket_qua=usd*26.331
    return ket_qua
usd=int(input('Nhap so tien USD: '))
print(f'{usd:,} USD = {doi_tien(usd):,} VND')