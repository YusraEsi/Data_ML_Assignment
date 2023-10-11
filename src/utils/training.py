import streamlit as st
from PIL import Image
from src.training.train_pipeline import TrainingPipeline
from src.constants import CM_PLOT_PATH

def render_training_section():
    st.header("Pipeline Training")
    st.info("Before you proceed to training your pipeline. Make sure you have checked your training pipeline code and that it is set properly.")

    name = st.selectbox("Pipeline name", ["Random Forest", "XGBC", "Naive Bayes", "SVC", "Decision Tree", "KNN"])
    serialize = st.checkbox('Save pipeline')
    train = st.button('Train pipeline')

    if train:
        with st.spinner('Training pipeline, please wait...'):
            try:
                tp = TrainingPipeline()
                tp.train(serialize=serialize, model_name=name)
                tp.render_confusion_matrix(model_name=name)
                accuracy, f1 = tp.get_model_performance()
                col1, col2 = st.columns(2)

                col1.metric(label="Accuracy score", value=str(round(accuracy, 4)))
                col2.metric(label="F1 score", value=str(round(f1, 4)))

                st.image(Image.open(CM_PLOT_PATH), width=850)
            except Exception as e:
                st.error('Failed to train the pipeline!')
                st.exception(e)
