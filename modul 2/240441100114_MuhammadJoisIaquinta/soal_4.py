tahun = int(input("masukkan tahun: "))
if (tahun % 4 == 0 and tahun % 100!= 0) or (tahun % 400 == 0):
    print(f"{tahun}adalah tahun kebisat")
else:
    print(f"{tahun} bukan tahun kebisat")