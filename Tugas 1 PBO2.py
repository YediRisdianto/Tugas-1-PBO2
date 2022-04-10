import psycopg2
import os

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "Garahaji05"
DB_HOST = "localhost"
DB_PORT = 5432
try:
    db = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print("\nServer Telah Terkoneksi Di Database\n")
except:
    print("\nServer Belum Terkoneksi Di Database\n")
cur = db.cursor()

def create_tabel(db):
    cur.execute("""
      CREATE TABLE IF NOT EXISTS public.data_mahasiswa
      (
        nim character varying(10) COLLATE pg_catalog."default" NOT NULL,
        nama character varying(40) COLLATE pg_catalog."default",
        jk "char",
        prodi character varying(10) COLLATE pg_catalog."default",
        CONSTRAINT data_mahasiswa_pkey PRIMARY KEY (nim)
      )
               """)
    db.commit()
    print("Selamat Anda Telah Berhasil Membuat Tabel...")

def insert_data(db):
  nim = input("\nMasukkan NIM : ")
  nama = input("Nama : ")
  jk = input("Jenis Kelamin : ")
  prodi = input("Prodi : ")
  val = (nim, nama, jk, prodi)
  cursor = db.cursor()
  sql = "INSERT INTO data_mahasiswa (nim, nama, jk, prodi) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("Data Telah Tersimpan".format(cursor.rowcount))

def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM data_mahasiswa"
  cursor.execute(sql)
  results = cursor.fetchall()
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def update_data(db):
  cursor = db.cursor()
  nim = input("\nMasukkan NIM yang ingin di update : ")
  nama = input("Nama : ")
  jk = input("Jenis Kelamin : ")
  prodi = input("Prodi : ")
  sql = "UPDATE data_mahasiswa SET nama=%s, jk=%s, prodi=%s WHERE nim=%s"
  val = (nama, jk, prodi, nim)
  cursor.execute(sql, val)
  db.commit()
  print("Data Telah Ter Update".format(cursor.rowcount))

def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  nim = input("\nPilih nim : ")
  sql = "DELETE FROM data_mahasiswa WHERE nim=%s"
  val = (nim,)
  cursor.execute(sql, val)
  db.commit()
  print("Data Telah Terhapus".format(cursor.rowcount))

def search_data(db):
  cursor = db.cursor()
  keyword = input("Masukkan NIM yang akan dicari : ")
  sql = "SELECT * FROM data_mahasiswa WHERE nama LIKE %s OR nim LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def show_menu(db):
  print("\n=== APLIKASI DATABASE PYTHON ===")
  print("\n1. Membuat Tabel data mahasiswa")
  print("2. Insert Data")
  print("3. Tampilkan Data")
  print("4. Update Data")
  print("5. Hapus Data")
  print("6. Cari Data")
  print("0. Keluar")
  print("\n------------------")
  menu = input("\nPilih menu => ")
  os.system("cls")
  if menu == "1":
    create_tabel(db)
  elif menu == "2":
    insert_data(db)
  elif menu == "3":
    show_data(db)
  elif menu == "4":
    update_data(db)
  elif menu == "5":
    delete_data(db)
  elif menu == "6":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah, Harap ulangi!")

if __name__ == "__main__":
  while(True):
    show_menu(db)