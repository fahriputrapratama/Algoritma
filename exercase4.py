nama = input("Masukan Nama Karyawan : ").title()
jabatan = input ("Jabatan Karyawan (design / programmer / resource) : ")

design = 5000000
programmer = 10000000
resource = 5000000

jabatan_list = ["design","programmer","resource"]

if jabatan in ["design"]:
    status = input ("Status perkawinan ( Y / T ) : ")
    if status == "Y":

        print("="*15)
        print(f"Nama : {nama}")
        print(f"Jabatan : {jabatan}")
        print(f"Sudah Menikah : {status}")
        print("="*25)
        print("="*25)

        tunjangan = design * 20/100
        gaji_kotor = design + tunjangan

        print (f"Gaji Kotor = {gaji_kotor:,.0f}")
        print("Pajak 10 % ")
        pajak = gaji_kotor * 10/100
        total = gaji_kotor - pajak

        print(f"Total Gaji : Rp.{total:,.0f}")
        print("="*25)
    else:
        print("="*15)

        print(f"Nama : {nama}")
        print(f"Jabatan : {jabatan}")
        print(f"Sudah Menikah : {status}")
        print (f"Gaji Kotor : {design:,.0f}")
        print("Pajak 10 % ")

        print("="*25)
        print("="*25)
        pajak = design * 10/100
        total = design - pajak
        print(f"Total Gaji : Rp.{total:,.0f}")
        print("="*25)

elif jabatan in ["programmer"]:
    status = input ("Status perkawinan ( Y / T ) : ")
    if status == "Y":
        print("="*15)
        print(f"Nama : {nama}")
        print(f"Jabatan : {jabatan}")
        print(f"Sudah Menikah : {status}")
        print("="*25)
        print("="*25)

        tunjangan = programmer * 20/100
        gaji_kotor = programmer + tunjangan
        print (f"Gaji Kotor = {gaji_kotor:,.0f}")
        print("Pajak 10 % ")

        pajak = gaji_kotor * 10/100
        total = gaji_kotor - pajak
        print(f"Total Gaji : Rp.{total:,.0f}")
        print("="*25)
    else:
        print("="*15)
        print(f"Nama : {nama}")
        print(f"Jabatan : {jabatan}")
        print(f"Sudah Menikah : {status}")
        print (f"Gaji Kotor : {programmer:,.0f}")
        print("Pajak 10 % ")

        print("="*25)
        print("="*25)
        pajak = programmer * 10/100
        total = programmer - pajak
        print(f"Total Gaji : Rp.{total:,.0f}")

        print("="*25)

else:
    status = input ("Status perkawinan ( Y / T ) : ")
    if status == "Y":
        print("="*15)
        print(f"Nama : {nama}")
        print(f"Jabatan : {jabatan}")
        print(f"Sudah Menikah : {status}")

        print("="*15)
        print("="*15)
        tunjangan = resource * 20/100
        gaji_kotor = resource + tunjangan
        print (f"Gaji Kotor = {gaji_kotor:,.0f}")
        print("Pajak 10 % ")

        pajak = gaji_kotor * 10/100
        total = gaji_kotor - pajak
        print(f"Total Gaji : Rp.{total:,.0f}")
        print("="*15)
    else:

        print("="*15)
        print(f"Nama : {nama}")
        print(f"Jabatan : {jabatan}")
        print(f"Sudah Menikah : {status}")
        print("="*15)
        print("="*15)

        print (f"Gaji Kotor : {resource:,.0f}")
        print("Pajak 10 % ")
        pajak = resource * 10/100
        total = resource - pajak

        print(f"Total Gaji : Rp.{total:,.0f}")
        print("="*15)