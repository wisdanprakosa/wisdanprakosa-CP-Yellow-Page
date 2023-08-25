# Capstone Project Muhammad Zaki Wijdan Prakosa
# JCDSOL011
# Yellow Card


DaftarKontak = {
 'abimana' : {'No.id': '1001',
              'Nama' : 'Abi Mana',
              'Alamat' : 'Jln. Gasem no. 2',
              'Phone' : '087711112222' },

 'dutarama': {'No.id' : '1002',
              'Nama' : 'Duta Rama',
              'Alamat' : 'Jln. Wolter no. 4',
              'Phone' : '087722223333' },

 'akiokio': {'No.id' : '1003',
             'Nama' : 'Akio Kio',
             'Alamat' : 'Jln. Veteran no. 6',
             'Phone' : '087633334444' },

 'bagasnaga': {'No.id' : '1004',
               'Nama' : 'Bagas Naga',
               'Alamat' : 'Jln. Gondang no. 8',
               'Phone' : '082144445555'}
}   

def KontakUtama():
    if len(DaftarKontak) == 0:
        print('Kontak Tidak ditemukan')
    else:
        print('\n \t\t\tDaftar Kontak \n')
        print('|No.id\t |Nama\t\t\t |Alamat\t\t |Phone')
        for key in DaftarKontak.keys():
            print('|{}\t |{}\t\t |{}\t |{}\t'.format(DaftarKontak[key]['No.id'], DaftarKontak[key]['Nama'],DaftarKontak[key]['Alamat'],DaftarKontak[key]['Phone']))
   
# Fungsi Lihat Kontak
def LihatDaftarKontak():
    while len(DaftarKontak) == 0:
        print('Kontak tidak ditemukan')
        break
    else:
        while True:
            pilih_menu = int(input('\n \tMenu Daftar Kontak \n\n1. Lihat Kontak\n2. Cari Berdasarkan Nama\n3. Kembali ke Menu Utama\n\n Silakan Pilih Menu : '))
            if pilih_menu == 1:
                KontakUtama()
            elif pilih_menu == 2:
                Cari = input('Cari Berdasarkan Nama : ')
                print('|No.id\t |Nama\t\t\t |Alamat\t\t |Phone')
                for key in DaftarKontak.keys():
                    if Cari.lower() in DaftarKontak[key]['Nama'].lower():
                        print('|{}\t |{}\t\t |{}\t |{}\t'.format(DaftarKontak[key]['No.id'], DaftarKontak[key]['Nama'],DaftarKontak[key]['Alamat'],DaftarKontak[key]['Phone']))
                    else:
                        continue
            elif pilih_menu == 3:
                break
            else:
                print('Menu Tidak ditemukan')

# Fungsi Tambah Kontak
def TambahDaftarKontak():
    while True:
        KontakUtama()
        TambahKontak = input('Masukkan Nama : ')
        TambahKontakBaru = TambahKontak.replace(' ','')
        if TambahKontakBaru.lower() not in DaftarKontak.keys():
            print('Silakan Masukkan Kontak Baru')
            noid_kontak = int(input('Masukkan No.id Kontak Baru : '))
            nama_kontak = input('Masukkan Nama Kontak baru : ')
            alamat_kontak = input('Masukkan Alamat Kontak baru : ')
            while True:
                try:
                    phone_kontak = int(input('Masukkan Nomor Telepon Kontak Baru : '))
                    break
                except ValueError:
                    print("Masukkan Hanya Angka")
            cek1 = input('Apakah Anda Yakin ingin menambahkan daftar kontak baru? Ya/Tidak: ')
            while cek1 != 'ya':
                print('Kontak Tidak Jadi ditambahkan')
                break
            else:
                DaftarKontak[TambahKontakBaru.lower()] = {'No.id' : noid_kontak, 'Nama' : nama_kontak, 'Alamat' : alamat_kontak, 'Phone' : phone_kontak}
                KontakUtama()
                print('Kontak berhasil ditambahkan')
                break          
        else:
            print('Kontak Sudah Ada di Daftar Kontak')
            break

# Fungsi Edit Kontak
def EditDaftarKontak():
    EditDaftarKontak = int(input('Menu Edit Kontak \n1. Edit Berdasarkan Nama \n2. Kembali ke Menu Utama \n Silakan Pilih Menu : '))
    if EditDaftarKontak == 1:
        KontakUtama()
        Edit_kontak = input('Masukkan Nama yang ingin diedit : ')
        Edit_baru = Edit_kontak.replace(' ','')
        while Edit_baru.lower() in DaftarKontak.keys():
            pilih_edit = int(input('\nInformasi Menu Edit Kontak\n \n Apa yang ingin Anda Edit? \n1. Nama \n2. No.id \n3. Alamat \n4. Phone \n5. Kembali ke Menu Utama \n Silakan Pilih Menu : '))
            if pilih_edit == 1:
                Edit_nama = input('Masukkan Nama Baru : ')
                Edit_nama_baru = Edit_nama.replace(' ','')
                while Edit_nama_baru.lower in DaftarKontak.keys():
                    print('Nama Kontak Sudah Ada')
                    Edit_nama = input('Masukkan Nama Baru : ')
                    Edit_nama_baru = Edit_nama.replace(' ','')
                cek1 = input('Apakah Anda yakin ingin Mengganti Nama? Ya/Tidak : ')
                if cek1 != 'ya':
                    break
                else:
                    DaftarKontak[Edit_nama_baru] = DaftarKontak[Edit_baru.lower()]
                    del DaftarKontak[Edit_baru.lower()]
                    DaftarKontak[Edit_nama_baru]['Nama'] = Edit_nama
                    KontakUtama()
                    print('Nama telah diedit')
                    break
            elif pilih_edit == 2:
                Edit_noid = input('Masukkan No.id Baru : ')
                Edit_noid_baru = Edit_noid.replace(' ','')
                while Edit_noid_baru in DaftarKontak.keys():
                    print('No id Kontak Sudah Ada')
                    Edit_noid = input('Masukkan No.id Baru : ')
                    Edit_noid_baru = Edit_noid.replace(' ','')
                cek2 = input('Apakah Anda yakin ingin mengganti No.id? Ya/Tidak : ')
                if cek2 != 'ya':
                    break
                else:
                    DaftarKontak[Edit_baru.lower()]['No.id'] = Edit_noid_baru
                    KontakUtama()
                    print('No.id telah diedit')
                    break
            elif pilih_edit == 3:
                Edit_alamat_baru = input('Masukkan Alamat Baru : ')
                cek3 = input('Apakah Anda yakin ingin mengganti alamat? Ya/Tidak : ')
                if cek3 != "ya":
                    break
                else:
                    DaftarKontak[Edit_baru.lower()]['Alamat'] = Edit_alamat_baru
                    KontakUtama()
                    print('Alamat Sudah diedit')
                    break
            elif pilih_edit == 4:
                Edit_phone_baru = int(input('Masukkan Nomor Telepon Baru : '))
                cek4 = input('Apakah Anda Yakin ingin mengganti Nomor Telepon? Ya/Tidak : ')
                if cek4 != 'ya':
                    break
                else:
                    DaftarKontak[Edit_baru.lower()]['Phone'] = Edit_phone_baru
                    KontakUtama()
                    print('Nomor Telepon Sudah diedit')
                    break
            else:
                break
        else:
            print('Nama Kontak Tidak Ada')
           
# Fungsi Hapus Kontak
def HapusKontak():
    KontakUtama()
    hapus_kontak = input('Masukkan Nama Kontak yang ingin dihapus : ')
    hapus_kontak_baru = hapus_kontak.replace(' ','')
    while hapus_kontak_baru.lower() not in DaftarKontak.keys() :
        print('Kontak Tidak ditemukan')
        break
    else:
        cek5 = input('Apakah Anda Yakin ingin menghapus Kontak {} hapus? Ya/Tidak : '.format(hapus_kontak))
        while cek5 != 'ya':
            print('Kontak Tidak dihapus')
            break
        else:
            del DaftarKontak[hapus_kontak_baru.lower()]
            KontakUtama()
            print('Kontak Berhasil dihapus')

# Fungsi Daftar Kontak Utama
while True : 
     PilihanMenu = input('''
        Main Menu Kontak Telepon:  
        1. Daftar Kontak                 
        2. Tambah Kontak
        3. Edit Kontak
        4. Hapus Kontak
        5. Keluar Program
                      
        Pilih Menu yang Tersedia : ''')

     if(PilihanMenu == '1'):
        LihatDaftarKontak()
     elif(PilihanMenu == '2'):
        TambahDaftarKontak()
     elif(PilihanMenu == '3'):
        EditDaftarKontak()
     elif(PilihanMenu == '4'):
        HapusKontak()
     elif(PilihanMenu == '5'):
        break