'''
•Buatlah GUI dengan Tkinter yang berisi:
   1 label judul Aplikasi prediksi Prodi Pilihan
   10 input nilai mata pelajaran
   1 button bertuliskan Hasil Prediksi
   1 label luaran hasil prediksi
•Atur posisi GUI sebaik mungkin!
•Fungsi Hasil Prediksi menuliskan prodi TeknologiInformasi apapun input yang diberikan!
'''

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def prediksi_prodi(): ##Fungsi Hasil Prediksi menuliskan prodi Teknologi Informasi apapun input yang diberikan!
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi")

root = tk.Tk() ##GUI Dasar
root.title ("Aplikasi Prediksi Prodi Pilihan")
root.geometry("350x450")

label_judul = tk.Label( ##Membuat label judul
    root, 
    text="Aplikasi Prediksi Prodi Pilihan", 
    font=("Arial", 14, "bold")
)
label_judul.pack(pady=10)

frame_input = tk.Frame(root) ##membuat input frame
frame_input.pack(pady=10, padx=20)