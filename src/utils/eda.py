import streamlit as st
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from src.constants import RAW_DATASET_PATH, PROCESSED_DATASET_PATH
st.set_option('deprecation.showPyplotGlobalUse', False)

def data_preprocessing():
    df = pd.read_csv(RAW_DATASET_PATH)
    label_mapping = {
        0: '.Net Developer',
        1: 'Business Analyst',
        2: 'Business Intelligence',
        3: 'Help Desk and Support',
        4: 'Informatica Developer',
        5: 'Java Developer',
        6: 'Network and System Administrator',
        7: 'Oracle DBA',
        8: 'Project Manager',
        9: 'Quality Assurance',
        10: 'SAP',
        11: 'SQL Developer',
        12: 'Sharepoint Developer',
        13: 'Web Developer'
    }
    df['label'] = df['label'].map(label_mapping)
    return df

def processed_data():
    df = pd.read_csv(PROCESSED_DATASET_PATH)
    label_mapping = {
        0: '.Net Developer',
        1: 'Business Analyst',
        2: 'Business Intelligence',
        3: 'Help Desk and Support',
        4: 'Informatica Developer',
        5: 'Java Developer',
        6: 'Network and System Administrator',
        7: 'Oracle DBA',
        8: 'Project Manager',
        9: 'Quality Assurance',
        10: 'SAP',
        11: 'SQL Developer',
        12: 'Sharepoint Developer',
        13: 'Web Developer'
    }
    df['label'] = df['label'].map(label_mapping)
    df = df[["label", "resume"]]
    return df

def render_eda_section():
    st.header("Exploratory Data Analysis")  
    df = data_preprocessing()
    df_p = processed_data()

    # Display a random sample
    st.subheader("Random sample of resumes")
    random_sample = df.sample(n=10)
    st.write(random_sample.reset_index(drop=True))

    # Summary statistics (for RAW data)
    st.subheader("Summary Statistics (for RAW data)")
    st.write(df.describe())

    # Summary statistics (for processed data)
    st.subheader("Summary Statistics (for processed data)")
    st.write(df_p.describe())

    # Label counts (without balancing data)
    st.subheader("Label counts (without balancing data)")
    label_counts = df['label'].value_counts()
    st.bar_chart(label_counts)

    # Label counts (with balanced data)
    st.subheader("Label counts (with balanced data)")
    label_counts_p = df_p['label'].value_counts()
    st.bar_chart(label_counts_p)

    # Generate word clouds for the top words associated with each label
    st.subheader("Word Clouds for Top Words for any Label")
    labels = [
        '.Net Developer',
        'Business Analyst',
        'Business Intelligence',
        'Help Desk and Support',
        'Informatica Developer',
        'Java Developer',
        'Network and System Administrator',
        'Oracle DBA',
        'Project Manager',
        'Quality Assurance',
        'SAP',
        'SQL Developer',
        'Sharepoint Developer',
        'Web Developer'
    ]
    selected_label = st.selectbox("Choose a label", labels, index=None, placeholder="Select a job title...")
    if selected_label:
        num_of_words = st.slider("Choose a number of words", 100, 500)
        st.subheader(f"{selected_label}")
        resumes_of_label = ' '.join(df_p[df_p['label'] == selected_label]['resume'])
        wordcloud = WordCloud(width=800, height=400, max_words=num_of_words, stopwords=STOPWORDS, background_color='black').generate(resumes_of_label)
        plt.figure(figsize=(8, 6), facecolor='k')
        plt.imshow(wordcloud)
        plt.axis('off')
        st.pyplot()
