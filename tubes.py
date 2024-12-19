import tkinter as tk
from tkinter import messagebox
import json 
import os

#file untuk mrnyimpan data 
DATA_FILE = "soal.json"
USER_FILE = "pengguna.json"

#Fungsi untuk memuat data dari file 
def muat_data(file):
  try:
    if os.path.exists(file):
      with open(file, 'r') as f:
        return json.load(f)
    return {}
  except:
    return {}

#fungsi untuk menyimpan data ke file 
def simpan_data(file, data):
  try:
    with open(file, 'w') as f:
      json.dump(data, f)
    return True
  except:
    return False

#inisialisasi data
soal_data = muat_data(DATA_FILE)
pengguna_data = muat_data(USER_FILE)

class AplikasiKuis:
  def__init__(self, root):
    self.root = root
    self.root.title("Aplikasi Kuis")
    self.root.geometry("500x500")

    #variabel untuk melacak 
    self.pengguna_saat_ini = None
    self.indeks_soal = 0
    self.skor =0

    #frame-frame utama
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

    #Tampilkan Frame login pertama kali 
    self.login_frame.pack()

  def setup_login_frame(self)
    tk.Label(self.login_frame, text="Login", font=('Arial', 14, 'bold')).pack(pady=10)

    tk.Label(self.login_frame, text="Nama Pengguna").pack()
    self.username_entry = tk.Entry(self.login_frame)
    self.username_entry.pack()

    tk.Label(self.login_frame, text="Kata Sandi").pack()
    self.password_entry = tk.Entry(self.login_frame, show="*")
    self.password_entry.pack()

    tk.Button(self.login_frame, text="Login", command= self.login). pack(pady=5)
    tk.button(self.login_frame, text="Daftar", command= self.tampilkan_daftar_frame). pack()

  
