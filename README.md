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
Dalam proyek ini, model terbaik yang diperoleh adalah Logistic Regression, yang mencapai performa sangat baik dengan skor AUC sebesar 0.9006 setelah dilakukan balancing data menggunakan SMOTE dan pemilihan fitur menggunakan RFE (Recursive Feature Elimination).

Model ini mampu secara akurat membedakan antara mahasiswa yang berisiko dropout dan yang tidak, berdasarkan kombinasi faktor akademik, administratif, dan sosiodemografis.

Berdasarkan analisis koefisien model, berikut adalah beberapa faktor paling berpengaruh terhadap risiko dropout:
- Status pembayaran tuition fee yang up to date → sangat berkontribusi dalam mengurangi kemungkinan dropout.
- Pekerjaan ibu dan ayah, serta tingkat pendidikan orang tua, memberikan pengaruh signifikan terhadap kelanjutan studi mahasiswa.

### Rekomendasi Action Items
- Identifikasi Mahasiswa Berisiko Tinggi Secara Berkala

  Gunakan sistem prediksi untuk mendeteksi mahasiswa dengan skor risiko tinggi, terutama berdasarkan ciri seperti belum membayar tuition fee
  
- Berikan Dukungan Keuangan dan Pendampingan Akademik

  Fokuskan bantuan kepada mahasiswa yang belum up-to-date dalam pembayaran biaya pendidikan, serta yang memiliki histori akademik lemah pada semester awal.

- Evaluasi kurikulum

  Melakukan evaluasi kurikulum pada course-course yang memiliki rasio dropout tinggi seperti management dan basic education

- Sistem Mentoring atau Buddy System
  
  Tunjuk mahasiswa senior sebagai mentor untuk setiap mahasiswa baru. Fokuskan pada semester 1 dan 2 yang kritis.

