import tkinter as tk
from tkinter import messagebox
import json
import os

# File untuk menyimpan data
DATA_FILE = "soal.json"
USER_FILE = "pengguna.json"

# Fungsi untuk memuat data dari file
def muat_data(file):
    try:
        if os.path.exists(file):
            with open(file, 'r') as f:
                return json.load(f)
        return {}
    except:
        return {}

# Fungsi untuk menyimpan data ke file
def simpan_data(file, data):
    try:
        with open(file, 'w') as f:
            json.dump(data, f)
        return True
    except:
        return False

# Inisialisasi data
soal_data = muat_data(DATA_FILE)
pengguna_data = muat_data(USER_FILE)

class AplikasiKuis:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kuis")
        self.root.geometry("500x500")

        # Variabel untuk melacak
        self.pengguna_saat_ini = None
        self.indeks_soal = 0
        self.skor = 0

        # Frame-frame utama
        self.login_frame = tk.Frame(root)
        self.daftar_frame = tk.Frame(root)
        self.menu_utama_frame = tk.Frame(root)
        self.kelola_soal_frame = tk.Frame(root)
        self.edit_soal_frame = tk.Frame(root)
        self.kuis_frame = tk.Frame(root)

        self.setup_login_frame()
        self.setup_daftar_frame()
        self.setup_menu_utama_frame()
        self.setup_kelola_soal_frame()
        self.setup_edit_soal_frame()
        self.setup_kuis_frame()

        # Tampilkan frame login pertama kali
        self.login_frame.pack()

    def setup_login_frame(self):
        tk.Label(self.login_frame, text="Login", font=('Arial', 14, 'bold')).pack(pady=10)

        tk.Label(self.login_frame, text="Nama Pengguna").pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        tk.Label(self.login_frame, text="Kata Sandi").pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        tk.Button(self.login_frame, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.login_frame, text="Daftar", command=self.tampilkan_daftar_frame).pack()
    
    def setup_daftar_frame(self):
        tk.Label(self.daftar_frame, text="Daftar", font=('Arial', 14, 'bold')).pack(pady=10)

        tk.Label(self.daftar_frame, text="Nama Pengguna (min. 5 karakter)").pack()
        self.reg_username_entry = tk.Entry(self.daftar_frame)
        self.reg_username_entry.pack()

        tk.Label(self.daftar_frame, text="Kata Sandi").pack()
        self.reg_password_entry = tk.Entry(self.daftar_frame, show="*")
        self.reg_password_entry.pack()

        tk.Label(self.daftar_frame, text="Konfirmasi Kata Sandi").pack()
        self.reg_confirm_entry = tk.Entry(self.daftar_frame, show="*")
        self.reg_confirm_entry.pack()

        tk.Button(self.daftar_frame, text="Daftar", command=self.daftar).pack(pady=5)
        tk.Button(self.daftar_frame, text="Kembali ke Login", 
                 command=lambda: self.tampilkan_frame(self.login_frame)).pack()

    def setup_menu_utama_frame(self):
        tk.Label(self.menu_utama_frame, text="Menu Utama", font=('Arial', 14, 'bold')).pack(pady=10)

        tk.Button(self.menu_utama_frame, text="Kelola Soal", 
                 command=lambda: self.tampilkan_frame(self.kelola_soal_frame)).pack(pady=5)
        tk.Button(self.menu_utama_frame, text="Mulai Kuis", 
                 command=self.mulai_kuis).pack(pady=5)
        tk.Button(self.menu_utama_frame, text="Logout", 
                 command=self.logout).pack(pady=5)

    def setup_kelola_soal_frame(self):
        tk.Label(self.kelola_soal_frame, text="Kelola Soal", font=('Arial', 14, 'bold')).pack(pady=10)

        tk.Label(self.kelola_soal_frame, text="Soal").pack()
        self.soal_text = tk.Text(self.kelola_soal_frame, height=3)
        self.soal_text.pack()

        self.opsi_entries = []
        opsi_labels = ['A', 'B', 'C', 'D']
        for label in opsi_labels:
            tk.Label(self.kelola_soal_frame, text=f"Opsi {label}").pack()
            entry = tk.Entry(self.kelola_soal_frame)
            entry.pack()
            self.opsi_entries.append(entry)

        tk.Label(self.kelola_soal_frame, text="Jawaban Benar (A/B/C/D)").pack()
        self.jawaban_entry = tk.Entry(self.kelola_soal_frame)
        self.jawaban_entry.pack()

        tk.Button(self.kelola_soal_frame, text="Simpan Soal", 
                 command=self.tambah_soal).pack(pady=5)
        tk.Button(self.kelola_soal_frame, text="Edit Soal", 
                 command=self.tampilkan_edit_soal_frame).pack(pady=5)
        tk.Button(self.kelola_soal_frame, text="Kembali", 
                 command=lambda: self.tampilkan_frame(self.menu_utama_frame)).pack()

    def setup_edit_soal_frame(self):
        tk.Label(self.edit_soal_frame, text="Edit/Hapus Soal", font=('Arial', 14, 'bold')).pack(pady=10)

        self.soal_listbox = tk.Listbox(self.edit_soal_frame, width=50, height=10)
        self.soal_listbox.pack(pady=5)

        tk.Button(self.edit_soal_frame, text="Hapus Soal", 
                 command=self.hapus_soal).pack(pady=5)
        tk.Button(self.edit_soal_frame, text="Kembali", 
                 command=lambda: self.tampilkan_frame(self.kelola_soal_frame)).pack()

    def setup_kuis_frame(self):
        tk.Label(self.kuis_frame, text="Kuis", font=('Arial', 14, 'bold')).pack(pady=10)

        self.soal_label = tk.Label(self.kuis_frame, wraplength=400)
        self.soal_label.pack(pady=10)

        self.opsi_frame = tk.Frame(self.kuis_frame)
        self.opsi_frame.pack()

        self.opsi_buttons = []
        for i in range(4):
            btn = tk.Button(self.opsi_frame, width=30)
            btn.pack(pady=2)
            self.opsi_buttons.append(btn)
