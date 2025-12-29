toan=float(input('Nhap diem mon Toan: '))
ly=float(input('Nhap diem mon Ly: '))
hoa=float(input('Nhap diem mon hoa: '))
tong= toan+ly+hoa
if tong>=15 and (toan>=4 and ly>=4 and hoa>=4):
    if toan>5 and ly>5 and hoa>5:
        print('Ket qua dau. Hoc deu cac mon.')
    else:
        print('Ket qua dau. Hoc chua deu cac mon.')
else:
    print('Thi hong')
