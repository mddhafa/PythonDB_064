import sqlite3
import tkinter as tk
from tkinter import messagebox
 
def simpan_data_ke_sqlite( nilai1,nilai2,nilai3, fakultas_terpilih):
    #memasukkan ke database
    con = sqlite3.connect("FakultasPilihanDB.db")
    cursor = con.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_Mhs TEXT, 
                nilai1 INTEGER, 
                nilai2 INTEGER,
                nilai3 INTEGER,
                fakultas_terpilih TEXT)''')

    # Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute('''INSERT INTO hasil_prediksi (nilai1, nilai2, nilai3, fakultas_terpilih) VALUES (?,?,?)''',
    ( nilai1, nilai2, nilai3, fakultas_terpilih))

    # Melakukan commit dan menutup koneksi
    con.commit()
    con.close()

# Buat Jendela Halaman
root = tk.Tk()
root.title("Fakultas Pilihan")
root.geometry("500x500")
root.resizable(False,False)

#fungsi menampilkan Prediksi Fakultas
def PrediksiFakultas(Biologi, Fisika, Inggris):
        if Biologi > Fisika and Biologi > Inggris:
            return "Kedokteran"
        elif Fisika > Biologi and Fisika > Inggris:
            return "Teknik"
        elif Inggris > Biologi and Inggris > Fisika:
            return "Bahasa"
        else:
            return

#fungsi untuk menampilkan dan menginput nilai
def show():
    namaMhs = entry_mhs.get()
    Biologi = entry_biologi.get()
    fisika = entry_fisika.get()
    inggris = entry_inggris.get()

    Fakultas = PrediksiFakultas(Biologi, fisika, inggris)

    hasilMhs = f"Nama Mahasiswa: {namaMhs}"
    hasil1 = f"Biologi: {Biologi}"
    hasil2 = f"Fisika: {fisika}"
    hasil3 = f"Inggris: {inggris}"
    HasilPrediksi =f"Prediksi: {Fakultas}"

    label_hasilMhs.config(text=hasilMhs)
    label_hasil1.config(text=hasil1)
    label_hasil2.config(text=hasil2)
    label_hasil3.config(text=hasil3)
    label_HasilPrediksi.config(text=HasilPrediksi)

    if not Biologi and not fisika and not inggris and not namaMhs:
        frame_hasil.pack_forget()
    else:
        frame_hasil.pack()
        simpan_data_ke_sqlite(Biologi,fisika,inggris,namaMhs)
        messagebox.showinfo("Info","Data Tersimpan")

# Label Judul
label_judul = tk.Label(root, text="Fakultas Pilihan", font=("Times",14,"bold"))
label_judul.pack(pady=20)

# Buat Frame inputan
frame_input = tk.LabelFrame(root, labelanchor="n",pady=10, padx=10)
frame_input.pack()

# Label Nama Mahasiswa
label_nama_mhs = tk.Label(frame_input, text="Nama Mahasiswa: ")
label_nama_mhs.grid(row=0, column=0, pady=10)
entry_mhs = tk.Entry(frame_input)
entry_mhs.grid(row=0,column=1)

# Label Nilai1
label_nama_Biologi = tk.Label(frame_input, text="Nilai Biologi: ")
label_nama_Biologi.grid(row=1, column=0, pady=10)
entry_biologi = tk.Entry(frame_input)
entry_biologi.grid(row=1,column=1)

# Label Nilai2
label_nama_Fisika= tk.Label(frame_input, text="Nilai Fiska: ")
label_nama_Fisika.grid(row=2, column=0, pady=10)
entry_fisika = tk.Entry(frame_input)
entry_fisika.grid(row=2,column=1)

# Label Nilai3
label_nama_Inggris = tk.Label(frame_input, text="Nilai Inggris: ")
label_nama_Inggris.grid(row=3, column=0, pady=10)
entry_inggris = tk.Entry(frame_input)
entry_inggris.grid(row=3,column=1)

# Tombol Hasil
btn_hasil = tk.Button(root, text="Submit", command=show)
btn_hasil.pack(pady=10)

frame_hasil = tk.LabelFrame(root,labelanchor="n", padx=10,pady=10)
frame_hasil.pack_forget()

# Label Hasil
label_hasilMhs = tk.Label(frame_hasil, text="")
label_hasilMhs.pack()

label_hasil1 =  tk.Label(frame_hasil,text="")
label_hasil1.pack()

label_hasil2 =  tk.Label(frame_hasil,text="")
label_hasil2.pack()

label_hasil3 =  tk.Label(frame_hasil,text="")
label_hasil3.pack()

label_HasilPrediksi = tk.Label(frame_hasil, text="", font=("Times", 9,"bold"))
label_HasilPrediksi.pack()

# Jalankan Aplikasi
root.mainloop()
