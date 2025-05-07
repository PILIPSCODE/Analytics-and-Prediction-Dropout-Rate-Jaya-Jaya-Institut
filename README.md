# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan Jaya Jaya 

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang baik. Akan tetapi terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alisan dropout.

Jumlah dropout yang tinggi ini tentunya juga menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya jaya institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
- Kurangnya alat analitik untuk membantu para guru/dosen memahami penyebab utama tingginya dropout rate.
- Tidak adanya sistem prediktif untuk mengidentifikasi siswa yang berpotensi akan di dropout.
- Kebanyakan siswa yang dropout berada dalam jurusan apa? 

### Solution
- Pembuatan Dashboard untuk membantu para guru/dosen memahami penyebab utama tingginya dropout rate.
- Membuat Model Predictive dengan machine learning untuk mengidentifikasi siswa yang berpotensi akan di dropout.
- Mengetahui Kebanyakan siswa dropout berdasarkan jurusan dengan Visualisasi 

### Cangkupan Proyek
Data source:  https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md 

## Business Dashboard
Dashboard ini dikembangkan menggunakan **Metabase** sebagai alat bantu visualisasi data untuk mendukung pengambilan keputusan terkait manajemen karyawan. Fokus utama dashboard ini adalah untuk memberikan gambaran menyeluruh mengenai **jumlah siswa**, **jumlah siswa yang keluar**, serta **analisis mendalam terhadap faktor-faktor yang memengaruhi siswa tersebut di keluarkan**.

### 🎯 Fitur Utama yang Ditampilkan
- **Total seluruh Siswa**
- **Jumlah siswa yang dikeluarkan**
- **Persentase siswa yang telah dikeluarkan**
- **Rata Rata Nilai Akhir berdasarkan Status** (`Average Performance Grade by Status`)
- **Analisis Status berdasarkan berbagai column**, meliputi:
  - **Beasiswa** (`Scholarship_holder`)
  - **Bayaran uang kuliah** (`Tuition_up_to_date`)
- **Analisi Dropout Rate berdasarkan berbagai column**
  - **Umur** (`Age_at_Enrollment`)
  - **Pekerjaan Orang Tua** (`Parrent Occupation`)
  - **Jurusan** (`Course`)


### Cara Menjalankan Dashboard
1. Pastikan Kamu sudah install Docker, setelah itu jalankan metabase.db.mv.db
2. Buka browsher di localhost:3000
3. Masukan Email:kunciropilihis@gmail.com Password:Kunciro123.

### Cara Menjalankan Model Prediksi
[Prediction-App]()

1. Clone repositori:
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
2. Install Package :
   ```bash
   pip install -r requirements.txt 
3. Cara menjalankan UI Prediction
   ```bash
   streamlit run app.py

## Conclusion
Berdasarkan Dasboard, Droput rate yang tinggi disebabkan oleh karena siswa tidak siap saat ujian bukti dari rata-rata nilai dropout pada 7 dan 5 di semester 1 dan 2, Selain itu ketidaksiapan orang tua juga berpengaruh karena pekerjaan orang tua yang tidak memadai bisa dilihat di *Dropout Rate by Parent Occupation* membuat keterlambatan dalam pembayaran uang kuliah hal bisa dilihat di *Dropout Rate by Tuition_fees_up_to_date*. Dan juga kesalahan mahasiswa dalam memilih jurusan juga sangat mempengaruhi dropout rate bisa dilihat di *Dropout Rate by Course*.

### Rekomendasi Action Items
- Orientasi Jurusan: Adakan sesi pengenalan jurusan & prospek karier.
- Pendampingan Akademik: Sediakan mentor untuk membantu belajar & adaptasi kuliah.
- Subsidi/Beasiswa: Perbanyak kuota Beasiwa untuk mahasiswa dengan kesulitan membayar kuliah.
- Pemetaan Risiko Dropout: Gunakan data untuk deteksi dini mahasiswa berisiko tinggi.
- Konseling Psikologis & Finansial: Dukung mahasiswa yang stres atau terbebani biaya.

