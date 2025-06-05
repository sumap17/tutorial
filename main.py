import aritmatika
import konversi
import ubah_bilangan

def menu_utama():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Aritmatika")
        print("2. Konversi")
        print("3. Ubah Bilangan")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            menu_aritmatika()
        elif pilihan == "2":
            menu_konversi()
        elif pilihan == "3":
            menu_ubah_bilangan()
        elif pilihan == "4":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

def menu_aritmatika():
    print("\n--- Aritmatika ---")
    print("1. Penjumlahan")
    print("2. Perpangkatan")
    print("3. Perkalian")
    pilih = input("Pilih operasi: ")
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))

    if pilih == "1":
        print("Hasil:", aritmatika.penjumlahan(a, b))
    elif pilih == "2":
        print("Hasil:", aritmatika.perpangkatan(a, b))
    elif pilih == "3":
        print("Hasil:", aritmatika.perkalian(a, b))
    else:
        print("Pilihan tidak valid.")

def menu_konversi():
    print("\n--- Konversi ---")
    print("1. CM ke M")
    print("2. M ke CM")
    pilih = input("Pilih konversi: ")
    nilai = float(input("Masukkan nilai: "))

    if pilih == "1":
        print("Hasil:", konversi.cm_to_m(nilai), "meter")
    elif pilih == "2":
        print("Hasil:", konversi.m_to_cm(nilai), "cm")
    else:
        print("Pilihan tidak valid.")

def menu_ubah_bilangan():
    print("\n--- Ubah Bilangan ---")
    print("1. Desimal ke Biner")
    print("2. Desimal ke Oktal")
    print("3. Desimal ke Hexadesimal")
    pilih = input("Pilih konversi: ")
    nilai = int(input("Masukkan bilangan desimal: "))

    if pilih == "1":
        print("Biner:", ubah_bilangan.desimal_ke_biner(nilai))
    elif pilih == "2":
        print("Oktal:", ubah_bilangan.desimal_ke_oktal(nilai))
    elif pilih == "3":
        print("Hexadesimal:", ubah_bilangan.desimal_ke_hexa(nilai))
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu_utama()