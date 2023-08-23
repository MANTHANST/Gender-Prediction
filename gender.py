import pandas as pd
import pickle
import streamlit as st
import sklearn

data = pd.read_csv("gender_classification_v7.csv")
rf = pickle.load(open("rf.pkl", "rb"))

st.title("Gender Prediction")

r1col1, r1col2, r1col3, r1col4 = st.columns(4)
with r1col1:
    lh = st.selectbox("Has Long Hair?", ["None", "Yes", "No"])
with r1col2:
    fw = st.number_input("Forehead Width", min_value = 0)
with r1col3:
    fh = st.number_input("Forehead Height", min_value = 0)
with r1col4:
    nw = st.selectbox("Is Nose Wide?", ["None", "Yes", "No"])

r2col1, r2col2, r2col3 = st.columns(3)
with r2col1:
    nl = st.selectbox("Is Nose Long?", ["None", "Yes", "No"])
with r2col2:
    lt = st.selectbox("Are Lips Thin?", ["None", "Yes", "No"])
with r2col3:
    dist = st.selectbox("Is Nose to Lip Distance Long?", ["None", "Yes", "No"])

if st.button("Predict", use_container_width = True):

    if lh == "Yes":
        lh = 1
    elif lh == "No":
        lh = 0

    if nw == "Yes":
        nw = 1
    elif nw == "No":
        nw = 0

    if nl == "Yes":
        nl = 1
    elif nl == "No":
        nl = 0

    if lt == "Yes":
        lt = 1
    elif lt == "No":
        lt = 0

    if dist == "Yes":
        dist = 1
    elif dist == "No":
        dist = 0

    try:
        prediction = rf.predict(pd.DataFrame([[lh, fw, fh, nw, nl, lt, dist]],
                                columns=["long_hair", "forehead_width_cm", "forehead_height_cm", "nose_wide", "nose_long",
                                         "lips_thin", "distance_nose_to_lip_long"]))

        if prediction[0] > 0.5:
            prediction = "Male"
        else:
            prediction = "Female"

        label = "Prediction :  " + prediction
        centered_bold_label = f"<h3 style='text-align: center;'><b>{label}</b></h3>"
        st.write(centered_bold_label, unsafe_allow_html=True)
    except:
        st.error("Select From Every Option")