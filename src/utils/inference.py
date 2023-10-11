import streamlit as st
import pandas as pd
import json
import requests
from src.constants import LABELS_MAP, SAMPLES_PATH

def render_inference_section():
    st.header("Resume Inference")
    st.info("This section simplifies the inference process. Choose a test resume and observe the label that your trained pipeline will predict.")

    sample = st.selectbox(
        "Resume samples for inference",
        tuple(LABELS_MAP.values()),
        index=None,
        placeholder="Select a resume sample",
    )
    infer = st.button('Run Inference')

    if infer:
        with st.spinner('Running inference...'):
            try:
                sample_file = "_".join(sample.upper().split()) + ".txt"
                with open(SAMPLES_PATH / sample_file, encoding="utf-8") as file:
                    sample_text = file.read()

                result = requests.post(
                    'http://localhost:9000/api/inference',
                    json={'text': sample_text}
                )
                st.success('Done!')
                label = LABELS_MAP.get(int(float(result.text)))

                save_result = requests.post(
                    f'http://localhost:9000/api/save?prediction={label}',
                    json={'text': sample_text}
                )
                all_resume = json.loads(save_result.text)
                all_resume_df = pd.DataFrame(all_resume).drop("id", axis=1)
                st.metric(label="Status", value=f"Resume label: {label}")
                st.write(all_resume_df)
            except Exception as e:
                st.error('Failed to call Inference API!')
                st.exception(e)
