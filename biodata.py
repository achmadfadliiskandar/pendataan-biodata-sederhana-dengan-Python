print("aplikasi biodata sederhana dengan python")

# biodata itu ada nah mungkin di aplikasi kita adanya ini aja dulu
# nama 
# email
# alamat
# umur

# membuat inputnya terlebih dahulu
# dan berikan try and except sebagai error handling
# dan berikan lower/upper agar inputan dapat di terima
# nah itu di laporan nya akan ada Tidak di isi itu artinya orangnya mengosongkan form/field pada aplikasi kita 
while True:
    try:
        nama = input("Masukan Nama Anda : ").lower()
        email = input("Masukan Email Anda : ").lower()
        alamat = input("Masukan Alamat Anda : ").lower()
        umur = int(input("Masukan umur Anda : ").lower())
    except:
        # mencetak input yang tadi dimasukan tetapi salah/false
        print('maaf,data tidak diterima')
        continue
    else:
        usia = umur 
        laporan = open("biodata.txt","a")
        if not nama:
            laporan.write('Nama: Tidak di isi\n')
        else:
            laporan.write("Nama:"+nama+'\n')
        if not alamat:
            laporan.write('Alamat: Tidak di isi\n')
        else:
            laporan.write("Alamat:"+alamat+'\n')
        if not email:
            laporan.write('Email: Tidak di isi\n')
        else:
            laporan.write("Email:"+email+'\n')
        if not umur:
            laporan.write('Umur: Tidak di isi\n')
        else:
            laporan.write("Umur:"+str(usia)+"\n\n")
        laporan.close()
        print("terima kasih sudah mengisi")
        break