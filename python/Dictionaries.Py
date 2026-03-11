
# 1. SIMPLE DICTIONARY
print("=== SIMPLE DICTIONARY ===")

mahasiswa = {
    "nama": "Andi",
    "umur": 20,
    "jurusan": "Informatika"
}

print("Data Mahasiswa:", mahasiswa)
print("Nama:", mahasiswa["nama"])
print()


# 2. MENAMBAH DAN MENGUBAH DATA
print("=== TAMBAH DAN UBAH DATA ===")

mahasiswa["kota"] = "Bandung"
mahasiswa["umur"] = 21

print("Data setelah update:", mahasiswa)
print()


# 3. DICTIONARY DENGAN LIST
print("=== DICTIONARY DENGAN LIST ===")

siswa = {
    "nama": "Budi",
    "hobi": ["Gaming", "Musik", "Sepak Bola"],
    "nilai": [80, 85, 90]
}

print("Nama:", siswa["nama"])
print("Hobi:", siswa["hobi"])
print("Nilai:", siswa["nilai"])
print()


# 4. DICTIONARY DENGAN TUPLE
print("=== DICTIONARY DENGAN TUPLE ===")

lokasi = {
    "kota": "Jakarta",
    "koordinat": (6.2, 106.8)
}

print("Kota:", lokasi["kota"])
print("Koordinat:", lokasi["koordinat"])
print()


# 5. NESTED DICTIONARY
print("=== NESTED DICTIONARY ===")

data_sekolah = {
    "siswa1": {
        "nama": "Citra",
        "kelas": "XI IPA",
        "nilai": {
            "matematika": 90,
            "fisika": 88
        }
    },
    "siswa2": {
        "nama": "Dina",
        "kelas": "XI IPS",
        "nilai": {
            "ekonomi": 85,
            "geografi": 87
        }
    }
}

print("Nama siswa1:", data_sekolah["siswa1"]["nama"])
print("Nilai matematika:", data_sekolah["siswa1"]["nilai"]["matematika"])
print()


# 6. LOOPING DICTIONARY
print("=== LOOPING DICTIONARY ===")

for key, value in mahasiswa.items():
    print(key, ":", value)

print()


# 7. DICTIONARY COMPREHENSION
print("=== DICTIONARY COMPREHENSION ===")

kuadrat = {x: x*x for x in range(1,6)}

print("Dictionary Kuadrat:", kuadrat)
print()


# 8. DICTIONARY DARI LIST
print("=== DICTIONARY DARI LIST ===")

keys = ["nama", "umur", "kota"]
values = ["Eka", 22, "Surabaya"]

data = dict(zip(keys, values))

print("Dictionary hasil zip:", data)
print()


# 9. METHOD DICTIONARY
print("=== METHOD DICTIONARY ===")

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())
print()


# 10. CONTOH DATA PRODUK (DICTIONARY BESAR)
print("=== DATA PRODUK TOKO ===")

produk = {
    "P001": {
        "nama": "Laptop",
        "harga": 8000000,
        "stok": 10
    },
    "P002": {
        "nama": "Mouse",
        "harga": 150000,
        "stok": 50
    },
    "P003": {
        "nama": "Keyboard",
        "harga": 300000,
        "stok": 30
    }
}

for kode, item in produk.items():
    print("Kode:", kode)
    print("Nama:", item["nama"])
    print("Harga:", item["harga"])
    print("Stok:", item["stok"])
    print()


# 11. MENGHAPUS DATA
print("=== HAPUS DATA ===")

del mahasiswa["kota"]

print("Data mahasiswa setelah dihapus:", mahasiswa)

print("\n=== PROGRAM SELESAI ===")