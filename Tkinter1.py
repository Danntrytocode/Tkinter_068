##Buatlah GUI dengan Tkinter yang berisi:
##1 label judul Aplikasi prediksi Prodi Pilihan
##10 input nilai mata pelajaran
##1 button bertuliskan Hasil Prediksi
##1 label luaran hasil prediksi
##Atur posisi GUI sebaik mungkin!
##Fungsi Hasil Prediksi menuliskan prodi TeknologiInformasi apapun input yang diberikan!


import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def prediksi_prodi(): ##Fungsi Hasil Prediksi menuliskan prodi Teknologi Informasi apapun input yang diberikan!
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi")

root = tk.Tk() ##GUI Dasar
root.title ("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x520")
root.configure(bg="#2A1B3D")

label_judul = tk.Label( ##Membuat label judul
    root, 
    text="Aplikasi Prediksi Prodi Pilihan", 
    font=("Arial", 14, "bold")
    bg="#2A1B3D"
    fg="#FFD700"
)
label_judul.pack(pady=10)

frame_input = tk.Frame(root, bg="#3B224C", padx=15, pady=10) ##membuat input frame
frame_input.pack(pady=10, padx=20)

matapelajaran_list = [ ##daftar mapel
    "Matematika", "Bahasa Indonesia", "English", "Fisika", "Kimia", "Biologi", "Ekonomi", "Sejarah", "Geografi", "Seni Budaya"
]
entries = []

for i, matpel in enumerate(matapelajaran_list):##Membuat 10 Label dan Entry nilai mata pelajaran menggunakan grid layout
    lbl = tk.Label(frame_input, text=f"Nilai {matpel}:", anchor="w")
    lbl.grid(row=i, column=0, sticky="w", pady=2, padx=5)
    
    ent = tk.Entry(frame_input, width=10)
    ent.grid(row=i, column=1, pady=2, padx=5)
    entries.append(ent)

