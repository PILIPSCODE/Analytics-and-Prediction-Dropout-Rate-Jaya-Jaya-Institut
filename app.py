import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load encoders dan model
encoder_Application_mode = joblib.load("./file_pkl/le_Application_mode.pkl")
encoder_Attendance = joblib.load("./file_pkl/le_Attendance.pkl")
encoder_Course = joblib.load("./file_pkl/le_Course.pkl")
encoder_Debtor = joblib.load("./file_pkl/le_Debtor.pkl")
encoder_Gender = joblib.load("./file_pkl/le_Gender.pkl")
encoder_Marital_Status = joblib.load("./file_pkl/le_Marital_status.pkl")
encoder_Scolarship_holder = joblib.load("./file_pkl/le_Scholarship_holder.pkl")
encoder_Tuition_fees_up_to_date = joblib.load(
    "./file_pkl/le_Tuition_fees_up_to_date.pkl"
)

PCA1_model = joblib.load("./file_pkl/pca1.pkl")
PCA2_model = joblib.load("./file_pkl/pca2.pkl")
PCA3_model = joblib.load("./file_pkl/pca3.pkl")

scaler = joblib.load("./file_pkl/scaler.pkl")
Random_Forest_Model = joblib.load("./file_pkl/Random_Forest_Clasification_model.pkl")

# Daftar fitur
PCA1_features = [
    "Curricular_units_2nd_sem_grade",
    "Curricular_units_2nd_sem_approved",
    "Curricular_units_1st_sem_approved",
    "Curricular_units_1st_sem_grade",
    "Curricular_units_2nd_sem_evaluations",
    "Curricular_units_2nd_sem_enrolled",
    "Curricular_units_1st_sem_enrolled",
    "Curricular_units_1st_sem_evaluations",
]

PCA2_features = [
    "Admission_grade",
    "Previous_qualification_grade",
]

PCA3_features = [
    "Unemployment_rate",
    "GDP",
]

numerical_others = ["Age_at_enrollment"]

categorical_features = {
    "Tuition_fees_up_to_date": encoder_Tuition_fees_up_to_date,
    "Course": encoder_Course,
    "Scholarship_holder": encoder_Scolarship_holder,
    "Application_mode": encoder_Application_mode,
    "Debtor": encoder_Debtor,
    "Gender": encoder_Gender,
    "Marital_status": encoder_Marital_Status,
    "Attendance": encoder_Attendance,
}

# UI
st.title("🎓 Student Status Prediction App")
st.write(
    "Masukkan data mahasiswa untuk memprediksi apakah akan **lulus** atau **drop out**."
)

with st.form("prediction_form"):
    inputs = {}

    # Kategorikal
    for feature, encoder in categorical_features.items():
        options = encoder.classes_.tolist()
        value = st.selectbox(feature.replace("_", " "), options)
        inputs[feature] = encoder.transform([value])[0]

    # Numerik input asli (yang akan dikonversi ke PCA)
    for feature in PCA1_features + PCA2_features + PCA3_features + numerical_others:
        inputs[feature] = st.number_input(feature.replace("_", " "), step=0.1)

    submitted = st.form_submit_button("Predict")

if submitted:
    # DataFrame input
    input_df = pd.DataFrame([inputs])

    # Transformasi PCA
    pca1 = PCA1_model.transform(input_df[PCA1_features])
    pca2 = PCA2_model.transform(input_df[PCA2_features])
    pca3 = PCA3_model.transform(input_df[PCA3_features])

    # Gabungkan hasil PCA dan fitur numerik lainnya
    pca_combined = np.hstack([pca1, pca2, pca3])
    final_numerical = np.hstack([pca_combined, input_df[numerical_others].values])

    # Scaling
    scaled_numerical = scaler.transform(final_numerical)

    # Gabungkan dengan fitur kategorikal
    categorical_values = input_df[list(categorical_features.keys())].values
    final_input = np.hstack([scaled_numerical, categorical_values])

    # Prediksi
    prediction = Random_Forest_Model.predict(final_input)[0]
    result = "🎓 Graduate" if prediction == 1 else "📉 Dropout"

    st.subheader("Prediction Result:")
    st.success(result)
