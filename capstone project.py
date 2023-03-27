
index_karyawan = {'Nomor Karyawan': [101,102,103],
                    'Nama Depan':['Andhika','Abi','Edward'], 
                    'Nama Belakang':['Maesa', 'Rizq', 'Nathan'],
                    'Domisili':['Tangerang', 'Tangerang', 'Singapore'],
                    'Gaji/Bulan': [10000000, 20000000,10000000]
}

index_ID = index_karyawan['Nomor Karyawan']
index_namdep = index_karyawan['Nama Depan']
index_nambel = index_karyawan['Nama Belakang']
index_domisili = index_karyawan['Domisili']
index_gaji = index_karyawan['Gaji/Bulan']

def list_menu1():
    global index_karyawan
    global inputan_menu_utama
    for key_karyawan in range(len(index_karyawan)):
        print(list(index_karyawan.keys())[key_karyawan], end ='\t|')
    print()
    print('=================================================================================')

    for i in range(len(list(index_karyawan.values())[0])):
        for j in range(len(list(index_karyawan.keys()))):
            if len(str(list(index_karyawan.values())[j][i])) >= 7:
                print(list(index_karyawan.values())[j][i], end = '\t|')
            else:
                print(list(index_karyawan.values())[j][i], end = '\t\t|')
        print()

def indexing_data_karyawan(x): 
    global inputan_karyawan_pilihan
    global variable_kosong
    for i in range(len(list(index_karyawan[x]))):
        angka_user_input = index_karyawan[x][i]
        if inputan_karyawan_pilihan == angka_user_input:
            variable_kosong.append(inputan_karyawan_pilihan)
            # break

def indexing_ubah_karyawan(): 
    global nomor_karyawan_ubah
    global variable_kosong1
    for i in range(len(list(index_karyawan['Nomor Karyawan']))):
        angka_user_input = index_karyawan['Nomor Karyawan'][i]
        if nomor_karyawan_ubah == angka_user_input:
            variable_kosong1.append(nomor_karyawan_ubah)
            break

def indexing_hapus_karyawan(): 
    global nomor_karyawan_hapus
    global variable_kosong2
    for i in range(len(list(index_karyawan['Nomor Karyawan']))):
        angka_user_input = index_karyawan['Nomor Karyawan'][i]
        if nomor_karyawan_hapus == angka_user_input:
            variable_kosong2.append(nomor_karyawan_hapus)
            break

def menu_utama():
    global inputan_menu_utama
    print('''
Selamat datang di Data Karyawan Purwadhika!

\tList Menu:
\t1. Menampilkan data karyawan
\t2. Menambah data karyawan
\t3. Mengubah data karyawan
\t4. Menghapus data karyawan 
\t5. Exit program
      ''')
    inputan_menu_utama = input('Masukkan nomor dari list menu: ')

while True:
    menu_utama()

    if inputan_menu_utama.isnumeric():
        pass
    else:
        print('\nNomor yang dimasukkan bukan dalam bentuk angka\n')
        continue
    inputan_menu_utama = int(inputan_menu_utama)

    if inputan_menu_utama == 1:
        while True:
            print('''
Menu Tampilan Data Karyawan

\tList Menu:
\t1. Menampilkan seluruh data karyawan
\t2. Menampilkan data karyawan pilihan
\t3. Kembali ke Menu Utama
            ''')
            inputan_tampilan1 = input('Masukkan nomor dari list menu:')
            if inputan_tampilan1.isnumeric():
                pass
            else:    
                print('Nomor yang dimasukkan bukan dalam bentuk angka')
                continue 

            inputan_tampilan1 = int(inputan_tampilan1)
            if inputan_tampilan1 > 3:
                print('Nomor yang dimasukkan salah')
                continue
            elif inputan_tampilan1 == 1:
                if len(index_karyawan['Nomor Karyawan']) > 0:
                    print()
                    list_menu1()
                    input('\nMasukkan huruf atau angka apapun untuk kembali ke menu tampilan:\n')
                    continue
                else:
                    print('\nMohon maaf, data tidak tersedia\n')
            elif inputan_tampilan1 == 2:
                if len(index_ID) < 1:
                    print('\nMohon maaf, data tidak tersedia\n')
                    continue

                while True:
                    print('''
\tPilihan kolom ada:
\t- Nomor Karyawan
\t- Nama Depan
\t- Nama Belakang
''')
                    inputan_kolom_pilihan = (input('Masukkan nama kolom yang ingin dipakai:\n'))
                    inputan_kolom_pilihan = inputan_kolom_pilihan.title()

                    if inputan_kolom_pilihan == 'Nomor Karyawan':
                        inputan_karyawan_pilihan = int(input('\nMasukkan Data Karyawan:'))
                    elif inputan_kolom_pilihan == 'Nama Depan' or inputan_kolom_pilihan == 'Nama Belakang':
                        inputan_karyawan_pilihan = (input('\nMasukkan Data Karyawan:'))
                        inputan_karyawan_pilihan = inputan_karyawan_pilihan.title()
                    elif inputan_kolom_pilihan == 'Domisili' or inputan_kolom_pilihan == 'Gaji/Bulan':
                        print('Kolom yang dimasukkan tidak dapat digunakan')
                        continue
                    else:
                        print('Kata yang dimasukkan tidak ada pada kolom data')
                        continue

                    variable_kosong = []
#                     index_variable_kosong = []
                    indexing_data_karyawan(inputan_kolom_pilihan)
                    
                    if inputan_karyawan_pilihan in variable_kosong:
                        for key_karyawan in range(len(index_karyawan)):
                            print(list(index_karyawan.keys())[key_karyawan], end ='\t|')
                        print()
                        print('=================================================================================')

                        indexan = index_karyawan[inputan_kolom_pilihan].index(inputan_karyawan_pilihan)
                        for i in range(len(list(index_karyawan.keys()))):
                            if len(str(list(index_karyawan.values())[i][indexan])) >= 7:
                                print(list(index_karyawan.values())[i][indexan], end = '\t|')
                            else:
                                print(list(index_karyawan.values())[i][indexan], end = '\t\t|')
                        print()
                        input('\nMasukkan huruf atau angka apapun untuk kembali ke menu tampilan:\n')
                        variable_kosong = []
                        break

                    else:
                        print('\nData tidak tersedia')
                        variable_kosong = []

                continue

            elif inputan_tampilan1 == 3:
                break
    
    elif inputan_menu_utama == 2:
        while True:
            print('''
Menu Menambah Data Karyawan

\tList Menu:
\t1. Menambah data karyawan
\t2. Kembali ke Menu Utama
            ''')

            inputan_tampilan2 = (input('Masukkan nomor dari list menu: '))
            if inputan_tampilan2.isnumeric():
                pass
            else:
                print('\nNomor yang dimasukkan bukan dalam bentuk angka\n')
                continue

            if int(inputan_tampilan2) > 2:
                print('Nomor yang dimasukkan salah')
                continue
            elif int(inputan_tampilan2) == 1:
                print('\n-Masukkan nomor karyawan dengan angka sebanyak 3 karakter-')
                while True:
                    nomor_karyawan_baru = input('Masukkan Nomor Karyawan Baru: ')
                    if len(nomor_karyawan_baru) != 3:
                        print('Nomor yang dimasukkan tidak sebanyak 3 karakter')
                    elif nomor_karyawan_baru.isnumeric() == False:
                        print('Nomor yang dimasukkan bukan dalam bentuk angka')
                    elif int(nomor_karyawan_baru) in index_ID:
                        print('Nomor ID yang dimasukkan sudah terdaftar')
                    else:
                        break
                list_kosyong = []
                list_kosyong.append(int(nomor_karyawan_baru))
                namdep_karyawan_baru = input('\nMasukkan Nama Depan Karyawan Baru: ')
                list_kosyong.append(namdep_karyawan_baru.title())
                nambel_karyawan_baru = input('\nMasukkan Nama Belakang Karyawan Baru: ')
                list_kosyong.append(nambel_karyawan_baru.title())

                while True:
                    domisili_karyawan_baru = input('\nMasukkan Domisili Karyawan Baru: ')
                    if domisili_karyawan_baru.isalpha():
                        break
                    else:
                        print('Domisili yang dimasukkan bukan dalam bentuk huruf')
                        continue
                list_kosyong.append(domisili_karyawan_baru.title())

                while True:
                    gaji_karyawan_baru = input('\nMasukkan Gaji Karyawan Baru: ')
                    if len(gaji_karyawan_baru) < 5 and gaji_karyawan_baru.isnumeric():
                        print('Gaji yang di input kurang besar')
                    elif gaji_karyawan_baru.isnumeric():
                        break
                    else:
                        print('Gaji yang dimasukkan bukan dalam bentuk angka')
                        continue
                list_kosyong.append(int(gaji_karyawan_baru))

                for key_karyawan in range(len(index_karyawan)):
                    print(list(index_karyawan.keys())[key_karyawan], end ='\t|')
                print()
                print('=================================================================================')

                for i in range(len(list_kosyong)):
                    if len(str(list_kosyong[i])) >= 7:
                        print(list_kosyong[i], end = '\t|')
                    else:
                        print(list_kosyong[i], end = '\t\t|')
                        
                betulkah1 = input('\nApakah data karyawan diatas sudah sesuai dan anda ingin lanjut menambah?(y/n)\n')
                if betulkah1 == 'y':
                    index_ID.append(int(nomor_karyawan_baru))
                    index_namdep.append(namdep_karyawan_baru.title())
                    index_nambel.append(nambel_karyawan_baru.title())
                    index_domisili.append(domisili_karyawan_baru.title())
                    index_gaji.append(int(gaji_karyawan_baru))
                    pass
                elif betulkah1 == 'n':
                    print('\nData karyawan baru gagal tersimpan\n')
                    continue
                else:
                    print('Anda salah memasukkan karakter. Halaman akan kembali pada menu menambah data karyawan ')
                    continue
                print('\nData karyawan baru berhasil tersimpan\n')
                input('Masukkan huruf atau angka apapun untuk kembali ke menu tambahan:\n')
                continue

            elif int(inputan_tampilan2) == 2: 
                break

    elif inputan_menu_utama == 3:
        while True:
            print('''
Menu Mengubah Data Karyawan

\tList Menu:
\t1. Mengubah data karyawan
\t2. Kembali ke Menu Utama
            ''')
            inputan_tampilan3 = input('Masukkan nomor dari list menu: ')
            if inputan_tampilan3.isnumeric():
                pass
            else:
                print('\nNomor yang dimasukkan bukan dalam bentuk angka\n')
                continue

            if int(inputan_tampilan3) > 2:
                print('\nNomor yang dimasukkan salah\n')
                continue
            elif int(inputan_tampilan3) == 1:
                if len(index_ID) < 1:
                    print('\nMohon maaf, data tidak tersedia\n')
                    continue

                while True:
                    nomor_karyawan_ubah = input('\nMasukkan Nomor Karyawan Yang Ingin Di Ubah: ')
                    if len(nomor_karyawan_ubah) > 3:
                        print('Nomor yang dimasukkan terlalu panjang')
                        continue
                    elif nomor_karyawan_ubah.isalpha():
                        print('Nomor yang dimasukkan bukan dalam bentuk angka')
                        continue
                    elif int(nomor_karyawan_ubah) not in index_ID:
                        print('Nomor Karyawan yang dimasukkan tidak terdaftar')
                        continue
                    nomor_karyawan_ubah = int(nomor_karyawan_ubah)
                    variable_kosong1 = []
                    indexing_ubah_karyawan()

                    if variable_kosong1 == [nomor_karyawan_ubah]:
                        for key_karyawan3 in range(len(index_karyawan)):
                            print(list(index_karyawan.keys())[key_karyawan3], end ='\t|')
                        print()
                        print('=================================================================================')

                        index_ID2 = index_ID.index(nomor_karyawan_ubah)
                        for i in range(len(list(index_karyawan.keys()))):
                            if len(str(list(index_karyawan.values())[i][index_ID2])) >= 7:
                                print(list(index_karyawan.values())[i][index_ID2], end = '\t|')
                            else:
                                print(list(index_karyawan.values())[i][index_ID2], end = '\t\t|')
                            
                        print()
                        variable_kosong1 = []
                    break

                betulkah = input('Apakah data karyawan diatas sudah sesuai dan anda ingin lanjut mengubah?(y/n)\n')
                if betulkah == 'y':
                    while True:
                        print('''
\tPilihan kolom ada:
\t- Nama Depan
\t- Nama Belakang
\t- Domisili
\t- Gaji/Bulan
                        ''')
                        kolom_edit = input('Input nama kolom yang ingin di ubah pada data karyawan: \n')
                        kolom_edit = kolom_edit.title()
                        songkosong = 0
                        if kolom_edit == 'Gaji':
                            kolom_edit = 'Gaji/Bulan'

                        for karyawan_key in list(index_karyawan.keys()):
                            if karyawan_key == kolom_edit:
                                value_baru_edit = input('Input value baru pada data karyawan:\n')
                                yakin = input('Apakah anda yakin ingin mengubah? (y/n)\n')
                                if yakin == 'y':
                                    pass
                                elif yakin == 'n':
                                    songkosong += 1
                                    break
                                else:
                                    print('Anda salah memasukkan karakter')
                                    continue

                                if kolom_edit == 'Gaji/Bulan':
                                    if value_baru_edit.isnumeric():
                                        value_baru_edit=int(value_baru_edit)
                                        pass
                                    else:
                                        print('Input value yang dimasukkan salah')
                                        continue

                                else:
                                    value_baru_edit = value_baru_edit.title()
                                index_karyawan[kolom_edit][index_ID2] = value_baru_edit
                                print('\nData baru karyawan sudah tersimpan\n')
                                songkosong +=1
                                input('Masukkan huruf atau angka apapun untuk kembali ke menu mengubah karyawan:\n')
                                break

                        if songkosong > 0:
                            songkosong = 0
                            break
                        else:
                            print('Nama kolom yang dimasukkan salah\n')
                            continue

                elif betulkah == 'n':
                    continue
                else:
                    print('Anda salah memasukkan karakter. Halaman akan kembali pada menu mengubah data karyawan ')
                    continue

            elif int(inputan_tampilan3) == 2:
                break

    elif inputan_menu_utama == 4:
        while True:
            print('''
Menu Menghapus Data Karyawan

\tList Menu:
\t1. Menghapus data karyawan
\t2. Kembali ke Menu Utama
            ''')
            inputan_tampilan4 = input('Masukkan nomor dari list menu:')
            if inputan_tampilan4.isnumeric():
                pass
            else:
                print('\nNomor yang dimasukkan bukan dalam bentuk angka\n')
                continue

            if int(inputan_tampilan4) > 2:
                print('Nomor yang dimasukkan salah')
                continue
            elif int(inputan_tampilan4) == 1:
                if len(index_ID) < 1:
                    print('\nMohon maaf, data tidak tersedia\n')
                    continue

                while True:
                    nomor_karyawan_hapus = input('\nMasukkan Nomor Karyawan Yang Ingin Di Hapus: ')
                    print()
                    if len(nomor_karyawan_hapus) > 3:
                        print('\nNomor yang dimasukkan terlalu panjang')
                    elif nomor_karyawan_hapus.isalpha():
                        print('\nNomor yang dimasukkan bukan dalam bentuk angka')
                    elif int(nomor_karyawan_hapus) not in index_ID:
                        print('\nNomor Karyawan yang dimasukkan tidak terdaftar')
                    else:
                        nomor_karyawan_hapus = int(nomor_karyawan_hapus)
                        variable_kosong2 = []
                        indexing_hapus_karyawan()
                        if variable_kosong2 == [nomor_karyawan_hapus]:
                            for key_karyawan4 in range(len(index_karyawan)):
                                print(list(index_karyawan.keys())[key_karyawan4], end ='\t|')
                            print()
                            print('=================================================================================')

                            index_ID3 = index_ID.index(nomor_karyawan_hapus)
                            for i in range(len(list(index_karyawan.keys()))):
                                if len(str(list(index_karyawan.values())[i][index_ID3])) >= 7:
                                    print(list(index_karyawan.values())[i][index_ID3], end = '\t|')
                                else:
                                    print(list(index_karyawan.values())[i][index_ID3], end = '\t\t|')
                                
                            print()
                            variable_kosong2 = []
                        break

                betulkah1 = input('\nApakah data karyawan diatas sudah sesuai dan anda ingin lanjut menghapus?(y/n)\n')
                if betulkah1 == 'y':
                    index_ID3 = index_ID.index(nomor_karyawan_hapus)
                    for i in range(len(list(index_karyawan.keys()))):
                        del list(index_karyawan.values())[i][index_ID3]
                    print('\nData karyawan berhasil terhapus')
                    input('\nMasukkan huruf atau angka apapun untuk kembali ke menu menghapus:\n')
                elif betulkah1 == 'n':
                    continue
                else:
                    print('\nAnda salah memasukkan karakter. Halaman akan kembali pada menu menghapus data karyawan ')
                    continue

            elif int(inputan_tampilan4) == 2:
                break

    elif inputan_menu_utama == 5:
        print('\nTerima kasih\n')
        break

    else :
        print('\nAnda salah memasukkan angka')

                
