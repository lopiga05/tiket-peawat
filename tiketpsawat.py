from os import system
from json import dump, load
from datetime import datetime
 
def print_menu():
    system("cls")
    print("""
    Penyimpanan Kontak Sederhana
    [1]. Pesan/Booking Tiket Pesawat
    [2]. Cari Tiket Pesawat 
    [3]. Edit Tiket Pesawat
    [4]. Batalkan/Hapus Tiket Pesawat
    [5]. Cetak PDF Tiket Pesawat
    [6]. Cetak QR Tiket Pesawat
    [Q]. Tentang
        """)
 
def print_header(msg):
    system("cls")
    print(msg)
 
def not_empty(container):
    if len(container) != 0:
        return True
    else:
        return False
 
def verify_ans(char):
    if char.upper() == "Y":
        return True
    else:
        return False
 
def print_data(id_pesanan=None, judul=True, jam=True, tanggal=True, studio=True, kursi=True,all_data=False):
    if id_pesanan != None and all_data == False:
        print(f"NOMOR TIKET : {id_pesanan}")
        print(f"NAMA PESANAN : {tickets[id_pesanan]['NAMA PESANAN']}")
        print(f"JAM : {tickets[id_pesanan]['jam']}")
        print(f"TANGGAL : {tickets[id_pesanan]['tanggal']}")
        print(f"GATE : {tickets[id_pesanan]['gate']}")
        print(f"KURSI : {tickets[id_pesanan]['kursi']}")
    elif kursi == False and all_data == False:
        print(f"NOMOR TIKET : {id_pesanan}")
        print(f"NAMA PESANAN : {tickets[id_pesanan]['nama pesanan']}")
        print(f"JAM : {tickets[id_pesanan]['jam']}")
        print(f"TANGGAL : {tickets[id_pesanan]['tanggal']}")
        print(f"GATE : {tickets[id_pesanan]['gate']}")
        print(f"KURSI : {tickets[id_pesanan]['kursi']}")
    elif all_data == True:
        for id_pesanan in tickets:
            judul = tickets[id_pesanan]["judul"]
            jam = tickets[id_pesanan]["jam"]
            tanggal = tickets[id_pesanan]["tanggal"]
            studio = tickets[id_pesanan]["studio"]
            kursi = tickets[id_pesanan]["kursi"]
            print(f"NOMOR PESANAN : {id_pesanan} - JUDUL : {judul} - JAM : {jam} - TANGGAL : {tanggal} - GATE : {gate} - NOMOR KURSI : {kursi}")
 
def view_ticket():
    print_header("DAFTAR TIKET TERSIMPAN")
    if not_empty(tickets):
        print_data(all_data=True)
    else:
        print("MAAF BELUM ADA TIKET TERSIMPAN")
    input("Tekan ENTER untuk kembali ke MENU")
 
def create_id_ticket(jam, tanggal, gate, kursi):
    hari_ini = datetime.now()
    tahun = hari_ini.year
    bulan = hari_ini.month
    hari = hari_ini.day
 
    counter = len(ticket) + 1
    first = name[0].upper()
    last_4 = phone[-4:]
    
    id_contact = ("%04d%02d%02d-C%03d%s%s" % (tahun, bulan, hari, counter, first, last_4))
    return id_ticket
 
def add_ticket():
    print_header("MENAMBAHKAN TIKET BARU")
    judul = input("JUDUL \t: ")
    jam = input("JAM \t: ")
    tanggal = input("TANGGAL \t: ")
    studio = input("GATE \t: ")
    kursi = input("NOMOR KURSI \t: ")
    respon = input(f"Apakah yakin ingin membuat tiket : {judul} ? (Y/N) ")
    if verify_ans(respon):
        id_pesanan = create_id_pesanan(judul=judul, jam=jam, tanggal=tanggal, studio=studio, kursi=kursi)
        tickets[id_pesanan] = {
            "judul" : judul,
            "jam" : jam,
            "tanggal" : tanggal,
            "gate" : gate,
            "kursi" : kursi
        }
        saved = save_data_tickets()
        if saved:
            print("Tiket telah dibuat.")
        else:
            print("Kesalahan saat membuat")
    else:
        print("TIKET Batal Dibuat")
    input("Tekan ENTER untuk kembali ke MENU")

def searching_by_id(ticket):
    if ticket in tickets:
        print('id_pesanan')
 
def find_ticket():
    print_header("MENCARI TIKET")
    nopes = input(" Nomor tiket yang Dicari : ")
    exists = searching_by_id(nopes)
    if exists:
        print("Tiket Ditemukan")
        print_data(id_pesanan=exists)
    else:
        print("Tiket Tidak Ada")
    input("Tekan ENTER untuk kembali ke MENU")

def delete_ticket():
    print_header("MENGHAPUS TIKET")
    nopes = input(" Nomor tiket yang akan Dihapus : ")
    exists = searching_by_id(nopes)
    if exists:
        print_data(contact=exists)
        respon = input(f"Yakin ingin menghapus {id_ticket} ? (Y/N) ")
        if verify_ans(respon):
            del tickets[id_pesanan]
            saved = save_data_tickets()
            if saved:
                print("Tiket Telah Dihapus")
            else:
                print("Kesalahan saat menghapus")
        else:
            print("Tiket Batal Dihapus")
    else:
        print("Tiket Tidak Ada")
    input("Tekan ENTER untuk kembali ke MENU")

def update_ticket_nama(id_ticket):
    print(f"Nama Lama : {contacts[id_contact]['nama']}")
    new_name = input("Masukkan Nama baru : ")
    respon = input("Apakah yakin data ingin diubah (Y/N) : ")
    result = verify_ans(respon)
    if result :
        contacts[id_contact]['nama'] = new_name
        print("Data Telah di simpan")
        print_data(id_contact)
    else:
        print("Data Batal diubah")
 
def update_ticket_jam(id_ticket):
    print(f"Ticket Jam Lama : {contacts[id_contact]['telp']}")
    new_telp = input("Masukkan Ticket Jam Baru : ")
    respon = input("Apakah yakin data ingin diubah (Y/N) : ")
    result = verify_ans(respon)
    if result :
        tickets[new_hour] = tickets[ticket]
        del tickets[ticket]
        print("Data Telah di simpan")
        print_data(new_hour)
    else:
        print("Data Batal diubah")
 
def update_ticket_tanggal(ticket):
    print(f"Tanggal Lama : {ticket}")
    new_date = input("Masukkan Tanggal baru : ")                  
    respon = input("Apakah yakin data ingin diubah (Y/N) : ")
    result = verify_ans(respon)
    if result :
        tickets[new_date] = tickets[ticket]
        del tickets[ticket]
        print("Data Telah di simpan")
        print_data(new_date)
    else:
        print("Data Batal diubah")

def update_ticket_gate():
    print_header("MENGUPDATE INFO KONTAK")
    print(f"Studio Lama : {ticket}")
    new_studio = input("Masukkan gate baru : ")
    respon = input("Apakah yakin data ingin diubah (Y/N) : ")
    result = verify_ans(respon)
    if result:
        tickets[new_studio] = tickets[ticket]
        del tickets[ticket]
        print("Data Telah di simpan")
        print_data(new_gste)
    else:
        print("Data Batal diubah")
        saved = save_data_contacts()
        if saved:
            print("Data Kontak Telah di-update.")
        else:
            print("Kesalahan saat menyimpan")

def update_ticket_nomor(ticket):
    print(f"Nomor Kursi Lama : {ticket}")
    new_chair = input("Masukkan Nomor Kursi baru : ")
    respon = input("Apakah yakin data ingin diubah (Y/N) : ")
    result = verify_ans(respon)
    if result :
        tickets[new_chair] = tickets[ticket]
        del tickets[ticket]
        print("Data Telah di simpan")
        print_data(new_chair)
    else:
        print("Data Batal diubah")

def update_ticket():
    print_header("MENGUPDATE INFO TIKET")
    nopes = input("Nomor Tiket yang akan di-update : ")
    exists = searching_by_id(nopes)
    if exists:
        print_data(id_pesanan)
        print("EDIT FIELD [1] JUDUL - [2] JAM - [3] TANGGAL - [4] GATE - [5] NOMOR KURSI")
        respon = input("MASUKAN PILIHAN (1/2/3) : ")
        if respon == "1":
            update_ticket_judul(nopes)
        elif respon == "2":
            update_ticket_jam(nopes)
        elif respon == "3":
            update_ticket_tanggal(nopes)
        elif respon == "4":
            update_ticket_studio(nopes)
        elif respon == "5":
            update_ticket_nomor(nopes)
        saved = save_data_tickets()
        if saved:
            print("Data Tiket Telah di-update.")
        else:
            print("Kesalahan saat mengupdate")
    else:
        print("Data Tidak Ada")
    input("Tekan ENTER untuk kembali ke MENU")

def about_application():
    print_header("TENTANG APLIKASI")
    print('''APLIKASI TIKET PESAWAT 
        Dibuat Oleh: Lopiga Parulian  
        ''')

def check_user_input(char):
    char = char.upper()
    if char == "Q":
        print("BYE!!!")
        return True 
    elif char == "1":
        view_()
    elif char == "2":
        add_contact()
    elif char == "3":
        find_contact()
    elif char == "4":
        delete_contact()
    elif char == "5":
        update_contact()
    elif char == "6":
        pass
 
def load_data_tickets():
    with open(file_path, 'r') as file:
        data = load(file)
    return data

def save_data_tickets():
    with open(file_path, 'w') as file:
        dump(tickets, file)
    return True

stop = False
file_path = "data/ticket_table.json"
tickets = load_data_tickets()
while not stop:
    print_menu()
    user_input = input("Pilihan : ")
    stop = check_user_input(user_input)