from prettytable import PrettyTable
daftarbarang = [
    {"ID": 1, "Nama Barang":"Whiskas Kucing", "Harga Barang": 12000, "Stock Barang": 12 }
]

def listbarang():
    table = PrettyTable(["ID", "Nama Barang", "Harga Barang", "Stock Barang"])
    for produk in daftarbarang:
        table.add_row([produk["ID"], produk["Nama Barang"], produk["Harga Barang"], produk["Stock Barang"]])
        print(table)

def tambahbarang():
    global id_barang
    id_barang = int(input("Masukkan ID Barang"))
    nama_barang = str(input("Masukkan Nama Barang"))
    harga_barang = int(input("Masukkan Harga Barang"))
    stock_barang = int(input("Masukkan Stock Barang"))
    daftarbarang.append({"ID": id_barang, "Nama Barang": nama_barang, "Harga Barang": harga_barang, "Stock Barang": stock_barang})
    print("Barang Berhasil Ditambah")

def updatebarang():
    listbarang() 
    id_barang = int(input("Masukkan ID Barang Yang Ingin Anda Ubah(ID Harus Sesuai!): "))
    for produk in daftarbarang:
        if (produk['ID'] == id_barang):
            nama_barang = str(input("Ubah Nama Barang: "))
            harga_barang = float(input("Ubah Harga Barang: "))
            stock_barang = int(input("Ubah Stock Barang: "))
            produk["Nama Barang"] = nama_barang
            produk["Harga Barang"] = harga_barang
            produk["Jumlah Barang"] = stock_barang
            print("Barang Berhasil Berubah!") 
            return
        print("ID barang tidak ditemukan")

def hapusbarang():
    id_barang = int(input("Masukkan Barang Yang Ingin Di Hapus(Masukkan Sesuai ID): "))
    for produk in daftarbarang:
        if (produk['ID'] == id_barang):
            daftarbarang.remove(daftarbarang[produk])
        produk = produk + 1

def pembayaran():
    listbarang()
    id_barang = int(input("Masukkan ID Barang Yang ingin anda beli: "))
    for produk in daftarbarang:
        if (produk['ID'] == id_barang):
            daftarbarang.remove(daftarbarang[produk]['Stock Barang'])
        produk = produk - 1

        
def login():
    while True:
        print("================================")
        print("=     ----Pilih Login----      =")
        print("=           1.Admin            =")
        print("=           2.Pembeli          =")
        print("================================")
     
        login = input("Ingin Login Sebagai Apa? (1/2):")
    
        if login == '1':
            user = str(input("Masukkan Username :"))
            pw = str(input("Masukkan Password :"))

            print("===== Selamat Datang Admin =====")
            print(f"\nHallo Admin {user}, Selamat Datang")
            print(f"\nPassword Anda {pw}\n")
            break
        elif login == '2':
            user = str(input("Masukkan Username :"))
            pw = str(input("Masukkan Password :"))
            print("==========================================")
            print(f"Selamat Datang {user} password anda {pw}")
            print("==========================================")
            break
        else:
            print("Pilihan Anda Tidak ada")

login()
while True:
    print("===================")
    print("Menu Admin")
    print("1.Tampilkan Barang")
    print("2.Tambah Barang")
    print("3.Edit Barang")
    print("4.Hapus Barang")
    print("5.Kembali")
    print("===================")

    menuadmin = input("Pilih Menu (1,2,3,4,5): ")
    if menuadmin == '1':
        listbarang()
    elif menuadmin == '2':
        tambahbarang()
    elif menuadmin == '3':
        updatebarang()
    elif menuadmin == '4':
        hapusbarang()
    elif menuadmin == '5':
        break
    else:
        print("Menu Tidak Tersedia.")

login()
while True:
    print("===================")
    print("Menu User")
    print("1.Beli Barang")
    print("2.List Barang")
    print("3.Checkout Barang")
    print("4.Keluar")
    print("===================")

    menuuser = input("Pilih Menu (1,2,3),4: ")      
    if menuuser == '1':
        pembayaran()
    elif menuuser == '2':
        listbarang()
    elif menuuser == '3':
        tambahbarang()
    elif menuuser == '4':
        break
    else:
        print("Menu tidak ada")

if __name__ == "__main__":
        while True:
            login()


