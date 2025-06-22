# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi baik dalam menghasilkan lulusan berkualitas. Namun, salah satu tantangan besar yang dihadapi adalah tingginya angka **mahasiswa yang mengalami dropout** atau tidak menyelesaikan pendidikannya.

Maka dari itu, institusi ini ingin **memprediksi kemungkinan dropout mahasiswa sejak dini** agar dapat mengambil tindakan pencegahan, seperti pemberian bimbingan khusus.

### Permasalahan Bisnis
- Tingginya jumlah mahasiswa yang mengalami dropout di Jaya Jaya Institut.
- Dampak negatif terhadap reputasi institusi dan nilai akreditasi.
- Tidak adanya sistem deteksi dini untuk mengidentifikasi mahasiswa yang berisiko tinggi melakukan dropout.
- Kurangnya informasi berbasis data yang dapat digunakan untuk mendukung intervensi dan pengambilan keputusan yang cepat dan tepat.

### Cakupan Proyek
1. **Analisis data historis mahasiswa**
2. **Membangun model machine learning untuk klasifikasi dropout**
3. **Mengevaluasi performa model**
4. **Membuat prototype sistem prediksi berbasis UI menggunakan streamlit**
5. **Membuat business dashboard (Looker Studio)** sebagai alat bantu pengambilan keputusan


### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv
1. **Buka terminal atau PowerShell.**

2. **Clone repositori GitHub kamu:**

   ```
   git clone https://github.com/apriadichio/Penerapan_data_science_student_droput.git
   ```

3. **Masuk ke folder proyek:**

   ```bash
   cd Penerapan_data_science_student_droput
   ```

4. **Buat virtual environment:**

   ```bash
   python -m venv venv
   ```

5. **Aktifkan virtual environment:**

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

6. **Instal semua dependensi dari **``**:**

   ```bash
   pip install -r requirements.txt
   ```

7. **Jalankan Notebook (opsional):**

   ```bash
   jupyter-notebook
   ```


## Business Dashboard
Untuk mendukung analisis visual, telah dibuat dashboard interaktif menggunakan Looker Studio. Dashboard ini menyajikan visualisasi dropout, distribusi variabel penting, dan insight lainnya yang dapat digunakan oleh pihak institusi.

Beberapa insight utama dari dashboard:
- Mahasiswa usia muda (18–19 tahun) memiliki tingkat dropout lebih tinggi.
- Mahasiswa yang tidak membayar biaya kuliah tepat waktu atau tidak menerima beasiswa lebih rentan dropout.
- Jurusan seperti Management menunjukkan tingkat dropout yang sangat tinggi.
- Status pernikahan seperti "divorced" atau "legally separated" juga menunjukkan kecenderungan dropout yang lebih tinggi, dengan statu single memiliki jumlah dropout tertinggi

Link Looker : https://lookerstudio.google.com/reporting/9bbf1365-7f78-4c4a-8716-300a45012777/page/gRmOF?s=mdSo8rm7J5w

## Menjalankan Sistem Machine Learning
Pastikan file ```final_pipeline.pkl``` dan ```label_encoder``` sudah ada dan tersimpan dengan benar 

**Jalankan aplikasi Streamlit :**
   ```bash
   streamlit run app.py
   ```

   Atau akses link berikut :https://penerapandatasciencestudentdroput-yu8paenfvajcevz5rmn4vz.streamlit.app/

## Conclusion
Model terbaik yang dihasilkan dalam proyek ini adalah Logistic Regression, dengan performa sangat baik ditunjukkan oleh skor AUC sebesar 0.9006 setelah melalui tahapan SMOTE dan RFE.Analisis terhadap 15 fitur teratas menunjukkan bahwa faktor-faktor akademik, administrasi keuangan, serta kondisi sosial keluarga memiliki pengaruh besar terhadap kemungkinan mahasiswa mengalami dropout. Berikut adalah ringkasan faktor utama dan pengaruhnya:

1. Jumlah Mata Kuliah Disetujui di Semester 2 (coef = +2.52, 11.5%)
   - Mahasiswa yang menyelesaikan lebih banyak mata kuliah cenderung tidak dropout
   - Hal ini menunjukkan tingkat adaptasi dan kinerja akademik yang baik.
     
2. Status Pembayaran Tuition Fee Up-to-Date (Koefisien: +2.41 (11.00%)
   - Mahasiswa yang membayar tepat waktu memiliki peluang jauh lebih rendah untuk dropout.
   - Artinya dukungan finansial stabil sangat penting dalam keberlangsungan studi.

3. Pekerjaan Ibu (Kode 191,kode 4), Pekerjaan Ayah(Kode 193, Kode 163)
      Analisis terhadap pekerjaan orang tua menunjukkan bahwa meskipun berasal dari sektor pekerjaan informal atau berisiko rendah, seperti pekerja kebersihan (kode 191), buruh konstruksi (171), atau pekerja kasar industri (193), mahasiswa tetap memiliki peluang besar untuk menyelesaikan studi. Hal ini menunjukkan bahwa bukan semata status pekerjaan yang memengaruhi keberlanjutan studi, melainkan stabilitas pendapatan dan dukungan sosial yang diberikan orang tua. Ketekunan dan nilai pendidikan dalam keluarga memiliki peran signifikan dalam mendorong mahasiswa untuk bertahan di perguruan tinggi.

5. Pendidikan Ibu

Kategori pekerjaan profesional dari ibu mendukung kelanjutan studi.

Jalur Masuk (Application Mode 53) (+1.66 / 7.6%)

Jalur ini berkorelasi positif terhadap keberhasilan mahasiswa.



Pendidikan ibu tinggi (SMA/Universitas) mendukung keberhasilan studi.

Pekerjaan Ayah (Kode 193) (+1.37 / 6.2%)

Pekerjaan formal dari ayah memberi dampak positif.

Kualifikasi Sebelumnya (Kode 2) (−1.35 / 6.2%)

Pendidikan sebelumnya yang kurang memadai meningkatkan risiko dropout.

Jalur Masuk (Kode 15) (+1.35 / 6.1%)

Jalur ini juga memberikan hasil positif.

Pekerjaan Ayah (Kode 163) (+1.29 / 5.9%)

Jumlah SKS Semester 2 Diambil tapi Tidak Disetujui (−1.24 / 5.6%)

Pendidikan Ibu (Kode 34) (−1.23 / 5.6%)

Kualifikasi Sebelumnya (Kode 4) (−1.17 / 5.3%)

Pekerjaan Ayah (Kode 171) (+1.11 / 5.0%)

Kewarganegaraan (Kode 26) (+1.06 / 4.8%)

Jalur Masuk (Application Mode 7) (−0.71 / 3.2%)


   

### Rekomendasi Action Items
- Identifikasi Mahasiswa Berisiko Tinggi Secara Berkala

  Gunakan sistem prediksi untuk mendeteksi mahasiswa dengan skor risiko tinggi, terutama berdasarkan ciri seperti belum membayar tuition fee
  
- Berikan Dukungan Keuangan dan Pendampingan Akademik

  Fokuskan bantuan kepada mahasiswa yang belum up-to-date dalam pembayaran biaya pendidikan, serta yang memiliki histori akademik lemah pada semester awal.

- Evaluasi kurikulum

  Melakukan evaluasi kurikulum pada course-course yang memiliki rasio dropout tinggi seperti management dan basic education

- Sistem Mentoring atau Buddy System
  
  Tunjuk mahasiswa senior sebagai mentor untuk setiap mahasiswa baru. Fokuskan pada semester 1 dan 2 yang kritis.

