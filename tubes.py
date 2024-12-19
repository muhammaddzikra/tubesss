def tampilkan_frame(self, frame):
        for f in [self.login_frame, self.daftar_frame, self.menu_utama_frame, 
                  self.kelola_soal_frame, self.edit_soal_frame, self.kuis_frame]:
            f.pack_forget()
        frame.pack()

    def login(self):
        nama_pengguna = self.username_entry.get()
        kata_sandi = self.password_entry.get()

        if nama_pengguna in pengguna_data and pengguna_data[nama_pengguna] == kata_sandi:
            self.pengguna_saat_ini = nama_pengguna
            messagebox.showinfo("Sukses", "Login berhasil!")
            self.tampilkan_frame(self.menu_utama_frame)
        else:
            messagebox.showerror("Error", "Nama pengguna atau kata sandi salah!")

    def tampilkan_daftar_frame(self):
        self.tampilkan_frame(self.daftar_frame)

    def daftar(self):
        nama_pengguna = self.reg_username_entry.get()
        kata_sandi = self.reg_password_entry.get()
        konfirmasi = self.reg_confirm_entry.get()

        if len(nama_pengguna) < 5:
            messagebox.showerror("Error", "Nama pengguna minimal 5 karakter!")
            return

        if nama_pengguna in pengguna_data:
            messagebox.showerror("Error", "Nama pengguna sudah digunakan!")
            return

        if kata_sandi != konfirmasi:
            messagebox.showerror("Error", "Kata sandi tidak cocok!")
            return

        pengguna_data[nama_pengguna] = kata_sandi
        if simpan_data(USER_FILE, pengguna_data):
            messagebox.showinfo("Sukses", "Registrasi berhasil!")
            self.tampilkan_frame(self.login_frame)
        else:
            messagebox.showerror("Error", "Gagal menyimpan data!")

    def tambah_soal(self):
        soal = self.soal_text.get("1.0", "end-1c")
        opsi = [entry.get() for entry in self.opsi_entries]
        jawaban = self.jawaban_entry.get().upper()

        if not all([soal, all(opsi), jawaban]):
            messagebox.showerror("Error", "Semua field harus diisi!")
            return

        if jawaban not in ['A', 'B', 'C', 'D']:
            messagebox.showerror("Error", "Jawaban harus A/B/C/D!")
            return

        soal_baru = {
            "soal": soal,
            "opsi": opsi,
            "jawaban": jawaban
        }

        soal_data.setdefault("default", []).append(soal_baru)
        if simpan_data(DATA_FILE, soal_data):
            messagebox.showinfo("Sukses", "Soal berhasil ditambahkan!")
            self.bersihkan_form_tambah()
        else:
            messagebox.showerror("Error", "Gagal menyimpan soal!")

    def bersihkan_form_tambah(self):
        self.soal_text.delete("1.0", tk.END)
        for entry in self.opsi_entries:
            entry.delete(0, tk.END)
        self.jawaban_entry.delete(0, tk.END)

  
