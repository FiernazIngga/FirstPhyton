# Import library standar
import tkinter as tk              # Modul utama Tkinter
from tkinter import ttk           # Modul ttk untuk widget yang lebih modern

# Membuat window utama
window = tk.Tk()                  # Inisialisasi window
window.title("Sapa Dia!")         # Judul window
window.geometry("360x260")        # Ukuran window (lebar x tinggi)
window.resizable(False, False)    # Window tidak bisa di-resize
window.configure(bg="#f5f5f5")    # Warna background window

# Variabel Tkinter untuk menyimpan input user
NAMA_DEPAN = tk.StringVar()       # Menyimpan nama depan
NAMA_BELAKANG = tk.StringVar()    # Menyimpan nama belakang

# ================= FRAME UTAMA =================
main_frame = ttk.Frame(window)   # Membuat frame utama
main_frame.pack(
    padx=20,                      # Jarak horizontal dari tepi window
    pady=20,                      # Jarak vertikal dari tepi window
    fill="x",                     # Mengisi arah horizontal
    expand=True                   # Frame bisa melebar
)

# ================= JUDUL =================
judul = ttk.Label(
    main_frame,
    text="Aplikasi Penyapa 👋",
    font=("Segoe UI", 14, "bold")
)
judul.pack(pady=(0, 15))          # Padding atas 0, bawah 15

# ================= INPUT NAMA DEPAN =================
label_depan = ttk.Label(
    main_frame,
    text="Nama Depan"
)
label_depan.pack(fill="x")

entry_depan = ttk.Entry(
    main_frame,
    textvariable=NAMA_DEPAN
)
entry_depan.pack(fill="x", pady=5)

# ================= INPUT NAMA BELAKANG =================
label_belakang = ttk.Label(
    main_frame,
    text="Nama Belakang"
)
label_belakang.pack(fill="x")

entry_belakang = ttk.Entry(
    main_frame,
    textvariable=NAMA_BELAKANG
)
entry_belakang.pack(fill="x", pady=5)

# ================= LABEL HASIL =================
hasil_label = ttk.Label(
    main_frame,
    text="",
    foreground="green",
    font=("Segoe UI", 10, "bold")
)
hasil_label.pack(pady=10)

# ================= FUNGSI TOMBOL =================
def sapa():
    # Mengambil isi dari Entry
    depan = NAMA_DEPAN.get().strip()
    belakang = NAMA_BELAKANG.get().strip()

    # Validasi sederhana
    if depan == "":
        hasil_label.config(text="Nama depan tidak boleh kosong!")
    else:
        hasil_label.config(
            text=f"Halo, {depan} {belakang} 👋"
        )

# ================= TOMBOL SAPA =================
btn_sapa = ttk.Button(
    main_frame,
    text="Sapa",
    command=sapa                 # Saat diklik, fungsi sapa dijalankan
)
btn_sapa.pack(fill="x", pady=5)

# Fokus awal ke input nama depan
entry_depan.focus()

# Menjalankan aplikasi
window.mainloop()
