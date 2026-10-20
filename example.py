import tkinter as tk

def prediksi_prodi():
    # Fungsi menuliskan 'Teknologi Informasi' apapun input yang diberikan
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi")

# 1. Membuat jendela utama GUI
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")

# 2. Label Judul
label_judul = tk.Label(
    root, 
    text="Aplikasi Prediksi Prodi Pilihan", 
    font=("Arial", 14, "bold")
)
label_judul.pack(pady=10)

# Frame untuk mengelompokkan 10 input mata pelajaran
frame_input = tk.Frame(root)
frame_input.pack(pady=10, padx=20)

# Daftar 10 Mata Pelajaran
matpel_list = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Sosiologi", "Geografi", "Informatika"
]

entries = []

# 3. Membuat 10 Label dan Entry nilai mata pelajaran menggunakan grid layout
for i, matpel in enumerate(matpel_list):
    lbl = tk.Label(frame_input, text=f"Nilai {matpel}:", anchor="w")
    lbl.grid(row=i, column=0, sticky="w", pady=2, padx=5)
    
    ent = tk.Entry(frame_input, width=10)
    ent.grid(row=i, column=1, pady=2, padx=5)
    entries.append(ent)

# 4. Button bertuliskan 'Hasil Prediksi'
btn_prediksi = tk.Button(
    root, 
    text="Hasil Prediksi", 
    command=prediksi_prodi,
    bg="#e1e1e1"
)
btn_prediksi.pack(pady=15)

# 5. Label luaran hasil prediksi
label_hasil = tk.Label(
    root, 
    text="Hasil Prediksi: -", 
    font=("Arial", 11, "bold")
)
label_hasil.pack(pady=5)

# Menjalankan loop event utama GUI
root.mainloop()