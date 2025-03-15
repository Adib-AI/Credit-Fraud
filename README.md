# Credit Card Fraud Detection

## Dataset
Dataset yang digunakan dalam proyek ini berasal dari Kaggle dan dapat diakses melalui tautan berikut:
[Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

## Proses yang Dilakukan
Proyek ini melibatkan beberapa tahap utama dalam pengolahan data dan pembuatan model:

### 1. Exploratory Data Analysis (EDA)
- Analisis skew pada fitur
- Distribusi kelas
- Korelasi antar fitur

### 2. Data Processing
- Handling skew pada fitur
- Normalisasi data
- Menangani ketidakseimbangan kelas
- Membagi data dengan proporsi 85:15 (train:test)

### 3. Modeling
Model yang digunakan dalam proyek ini adalah:
- **Random Forest**
- **Convolutional Long Short-Term Memory (C-LSTM)**

### 4. Evaluasi
Evaluasi model dilakukan menggunakan **Confusion Matrix** untuk mengukur performa model dalam mendeteksi transaksi penipuan.

## Tools yang Digunakan
- **Docker** untuk containerization
- **Railway** sebagai platform deployment
- **FastAPI** untuk membuat API

## Deployment
Proyek ini telah dideploy dan dapat diakses melalui tautan berikut:
[Credit Fraud Detection App](https://credit-fraud-production.up.railway.app/static/index.html)

## Pengujian Model
Untuk menguji model yang telah dideploy, Anda dapat menggunakan file **data_uji1.csv**.

---

Jika terdapat pertanyaan atau saran, silakan ajukan melalui issue atau hubungi pengembang proyek ini.
