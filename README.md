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

3. Pekerjaan dan pendidikan orang Tua
   - Pekerjaan ibu dengan kode 191 (cleaning workers) memiliki kontribusi yang tinggi terhadap keberhasilan studi, dengan koefisien +2.00 dan kontribusi 9.13%. Meskipun berasal dari sektor informal, keberadaan ibu yang aktif bekerja dapat memberikan stabilitas sosial dan nilai ketekunan yang memotivasi anak untuk bertahan.
   - Pekerjaan ayah dengan kode 193 (unskilled workers in extractive/construction sectors) juga berkontribusi positif (+1.36 / 6.24%), serta kode 163 (skilled workers di industri) dengan kontribusi +1.28 / 5.86%. Artinya, meskipun berasal dari pekerjaan kasar atau teknis, selama keluarga mampu menjaga kestabilan finansial minimum, risiko dropout bisa ditekan.
   - Pekerjaan ayah kode 171 (skilled construction workers) juga berdampak positif (+1.11 / 5.05%) — menandakan bahwa keberadaan pekerjaan tetap dan keterampilan teknis orang tua bisa mendukung kelanjutan studi anak.
   - Di sisi lain, pendidikan ibu kode 4 (Master’s Degree) memiliki pengaruh positif yang tinggi terhadap kelulusan mahasiswa (+1.47 / 6.71%), menunjukkan bahwa semakin tinggi tingkat pendidikan orang tua, semakin tinggi kemungkinan anak menyelesaikan studi. Sebaliknya, kode 34 (pendidikan tidak diketahui) memiliki pengaruh negatif besar (−1.23 / 5.60%), menandakan bahwa ketidakjelasan latar belakang pendidikan di rumah dapat menambah risiko dropout.
  
4. Jalur Masuk Mahasiswa (Application Mode)
   - Kode 53 "Short Cycle Diploma Holders" menunjukkan pengaruh positif tertinggi dalam fitur ini (+1.66 / 7.57%). Mahasiswa yang masuk melalui jalur ini cenderung memiliki latar belakang vokasional atau diploma sebelumnya, yang memberi bekal praktis dan motivasi tinggi untuk menyelesaikan studi lanjutan. Ini menunjukkan bahwa pengalaman akademik atau keterampilan sebelumnya mendorong keberhasilan.
   - Kode 15 "International Student (Bachelor)" menunjukkan kontribusi positif (+1.35 / 6.15%). Mahasiswa internasional biasanya telah melalui proses seleksi yang lebih ketat dan memiliki kesiapan adaptasi yang lebih tinggi, baik secara mental maupun finansial. Hal ini mendukung keberlangsungan studi mereka.
   - Kode 7 "Holders of Other Higher Courses" memiliki kontribusi negatif signifikan (−0.71 / 3.23%), menunjukkan bahwa mahasiswa yang pindah dari program studi lain justru memiliki risiko dropout lebih tinggi. Kemungkinan besar mereka merasa tidak cocok dengan program sebelumnya, mengalami kelelahan akademik, atau kurang memiliki motivasi untuk menyelesaikan studi baru.
  
5. Kualifikasi Sebelumnya
   - Kode 2 "Higher Education: Bachelor's Degree" Fitur ini memiliki kontribusi negatif yang besar terhadap keberlangsungan studi (−1.35 / 6.17%), menunjukkan bahwa mahasiswa yang sebelumnya telah memiliki gelar sarjana justru cenderung lebih tinggi risikonya untuk dropout. Hal ini dapat disebabkan oleh kurangnya motivasi intrinsik, perubahan jalur karier, atau ketidakcocokan ekspektasi terhadap program baru yang diambil.
   - Kode 4 "Higher Education: Master's" Fitur ini juga memberikan pengaruh negatif (−1.17 / 5.32%), yang mungkin menunjukkan bahwa mahasiswa yang kembali ke perguruan tinggi setelah memiliki pendidikan lanjutan justru kesulitan untuk mempertahankan komitmennya, atau mereka menghadapi tantangan dalam menyesuaikan waktu antara studi dan pekerjaan profesional.


### Rekomendasi Action Items
- Identifikasi Mahasiswa Berisiko Tinggi Secara Berkala

  Gunakan sistem prediksi untuk mendeteksi mahasiswa dengan skor risiko tinggi, terutama berdasarkan ciri seperti belum membayar tuition fee
  
- Berikan Dukungan Keuangan dan Pendampingan Akademik

  Fokuskan bantuan kepada mahasiswa yang belum up-to-date dalam pembayaran biaya pendidikan, serta yang memiliki histori akademik lemah pada semester awal.

- Evaluasi kurikulum

  Melakukan evaluasi kurikulum pada course-course yang memiliki rasio dropout tinggi seperti management dan basic education

- Sistem Mentoring atau Buddy System
  
  Tunjuk mahasiswa senior sebagai mentor untuk setiap mahasiswa baru. Fokuskan pada semester 1 dan 2 yang kritis.

