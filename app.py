import streamlit as st
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix

# === Load pipeline dan encoder ===
pipeline = joblib.load('final_pipeline.pkl')
try:
    le = joblib.load('label_encoder.pkl')  
    label_mapping = dict(zip(le.classes_, le.transform(le.classes_)))  #{'Dropout': 0, 'Non-Dropout': 1}
except:
    le = None
    label_mapping = {'Dropout': 0, 'Non-Dropout': 1}

# === UI Streamlit ===
st.set_page_config(page_title="Prediksi Dropout Mahasiswa", layout="centered")
st.title("🎓 Prediksi Dropout Mahasiswa")
st.write("Unggah data mahasiswa dalam format `.csv` untuk mendapatkan prediksi dropout dan evaluasi (gunakan studentcleaned.csv sebagai contoh).")

uploaded_file = st.file_uploader("📤 Unggah file CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("🧾 Data yang Diunggah")
    st.dataframe(data.head())

    # Cek apakah kolom Status ada (label asli)
    has_target = 'Status' in data.columns

    if has_target:
        status_col = data['Status']
        # Tangani jika Status berupa string
        if status_col.dtype == 'O' or str(status_col.dtype).startswith("category"):
            status_clean = status_col.astype(str).str.strip().str.lower()
            true_labels = status_clean.map(lambda x: label_mapping.get('Dropout') if x == 'dropout' else label_mapping.get('Non-Dropout'))
        else:
            true_labels = status_col.astype(int)
        
        if true_labels.isnull().any():
            st.error("❌ Data label (Status) mengandung nilai kosong atau tidak valid. Mohon periksa ulang.")
            st.stop()

        data_input = data.drop(columns=['Status'])
    else:
        data_input = data.copy()
        true_labels = None

    # === Prediksi ===
    pred = pipeline.predict(data_input)
    proba = pipeline.predict_proba(data_input)[:, 1]  # Probabilitas kelas 'Non-Dropout'

    # Pastikan pred adalah integer
    pred = pred.astype(int)

    # === Hasil Prediksi ===
    hasil = data.copy()
    hasil['Predicted_Label'] = le.inverse_transform(pred)

    # Gunakan inverse transform jika LabelEncoder tersedia
    if le:
        try:
            hasil['Predicted_Label'] = le.inverse_transform(pred)
        except Exception as e:
            st.warning(f"Gagal inverse_transform label: {e}")
            inverse_label_map = {v: k for k, v in label_mapping.items()}
            hasil['Predicted_Label'] = [inverse_label_map.get(int(p), "Unknown") for p in pred]
    else:
        inverse_label_map = {v: k for k, v in label_mapping.items()}
        hasil['Predicted_Label'] = [inverse_label_map.get(int(p), "Unknown") for p in pred]

    # Tambahkan probabilitas
    hasil['Non_Dropout_Probability'] = proba

    # Jika kolom Status berupa angka, ubah ke label juga
    if has_target and pd.api.types.is_numeric_dtype(data['Status']):
        try:
            hasil['Status'] = le.inverse_transform(data['Status'].astype(int))
        except Exception as e:
            st.warning(f"Gagal inverse_transform status: {e}")


    st.subheader("📈 Hasil Prediksi")
    st.dataframe(hasil)

    # === Evaluasi (jika label tersedia) ===
    if has_target:
        st.subheader("📊 Classification Report")

        try:
            report_dict = classification_report(true_labels, pred, target_names=['Dropout', 'Non-Dropout'], output_dict=True)
            report_df = pd.DataFrame(report_dict).transpose()
            st.dataframe(report_df.style.format("{:.2f}"))
        except Exception as e:
            st.error(f"⚠️ Gagal membuat classification report: {e}")

        st.subheader("🧩 Confusion Matrix")
        cm = confusion_matrix(true_labels, pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
                    xticklabels=['Dropout', 'Non-Dropout'], 
                    yticklabels=['Dropout', 'Non-Dropout'], ax=ax)
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        st.pyplot(fig)

    # === Unduh hasil ===
    csv = hasil.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Unduh Hasil Prediksi", csv, file_name="hasil_prediksi.csv", mime='text/csv')
