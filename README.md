# DNA Engineering - ML Assignment

## Requirements
- Python 3.9 or higher.
This repository contains the code and documentation for the Streamlit dashboard assignment. In this project, I was tasked with refactoring and enhancing a Streamlit dashboard that includes Exploratory Data Analysis, Training a machine learning model, and Inference (prediction).

#### - Install pipenv on your global python setup
```Python
    pip install pipenv 
```
Or follow [documentation](https://pipenv.pypa.io/en/latest/install/) to install it properly on your system
#### - Install requirements
```sh
    cd data-ml-assignment
```
```Python
    pipenv install
```
```Python
    pipenv shell
```
#### - Start the application
```sh
    sh run.sh
```
- API : http://localhost:8000
- Streamlit Dashboard : http://localhost:9000
## Project Setup

P.S You can check the log files for any improbable issues with your execution.
## Before we begin
- In this assignement, you will be asked to write, refactor, and test code. 
- Make sure you respect clean code guidelines.
- Some parts of the already existing code are bad. Your job is to refactor them.
- Read the assignement carefully.
- Read the code thoroughly before you begin coding.
Before starting the tasks, I encountered an issue with the backend where the `main.py` file was not in the correct place. I resolved this problem by moving `main.py` to the project's root directory.

## Description
This mini project is a data app that revolves around resume text classification.
Before run my project, ensure you have the following packages installed:

You are given a `dataset` that contains a number of resumes with their labels.
- [WordCloud](https://pypi.org/project/wordcloud/)
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)

Each row of the dataset contains:
- Label 1, 2, ..., 13 You will find the resume labels map under src/constants
- Resume text
## Task 1 :  Code Refactoring
As mentioned, the existing Streamlit dashboard is divided into three main sections:

Exploratory Data Analysis
Training
Inference
The current code for the dashboard is written as a single, lengthy Python script (dashboard.py), making it difficult to maintain and extend.

Streamlit is a component-based data app creator that empowers you to develop interactive Python dashboards. In this task, we aim to enhance the code structure for improved clarity and maintainability.

The monolithic dashboard.py script will be refactored into three separate files, each dedicated to one of the primary sections: EDA, Training, and Inference. These distinct components are now organized within the components directory.

The code will be reformatted to enhance readability, making it more accessible for future maintenance.

While Streamlit is designed to be user-friendly for non-frontend developers, complex code structures can still arise. Additionally, we have thoroughly reviewed the entire project codebase to identify and address any existing code irregularities, further elevating its quality.

As previously outlined, the Streamlit dashboard you are working with is segmented into three essential sections:

Exploratory Data Analysis
Training
Inference
For example, we have corrected an issue related to the static title in the confusion matrix display. Previously, it remained fixed as 'Naive Bayes,' and now it dynamically adjusts based on the selected model.

The existing code is currently consolidated within a single extensive Python script (dashboard.py). This consolidation makes it challenging to manage, optimize, read, maintain, and upgrade.

## Task 2 - Exploratory Data Analysis
Your main objectives are as follows:

Revise the code while adhering to "clean code" principles.
Break down the script into separate components.
Establish the necessary abstractions to facilitate future component additions.
As part of this task, I conducted Exploratory Data Analysis and incorporated it into the initial section of the Streamlit dashboard. The EDA encompassed the following steps:

Bonus points: You can earn extra credit if you identify and rectify any code irregularities throughout the entire project.

Displayed a random sample of the dataset.
Provided label counts for both raw and processed data.
Presented summary statistics for the data.
Implemented a user-friendly interface for selecting labels and specifying the number of words to visualize word clouds.

## Task 3 - Training

P.S: If required, data processing can be included in this section.
My primary objective was to outperform the baseline pipeline. Here's a summary of the key actions I took:

Preprocessed the data by removing unnecessary characters and stop words.
Balanced the dataset using RandomOverSampler.
Incorporated a selection box in the Streamlit web app, enabling users to choose their desired training model.
I trained multiple models, and here are the results:

## Task 4 - Inference

The goal is to outperform the baseline pipeline, with a higher F1 score indicating better performance.

In the Inference section of the dashboard, I made the following improvements:

You can trigger the baseline pipeline's training in the second section of the dashboard.
1. Saving Predictions:
I introduced an "api/save" endpoint accessible through the dashboard to save prediction results into an SQLite table, including the resume and prediction.

Choose the pipeline name and select whether to serialize it.
2. Displaying Predictions:
After each inference, I added a feature to display the prediction results, allowing users to conveniently review previous predictions.

## Task 5 - Unit Testing
As part of this project, I ensured that the code was thoroughly tested using unit tests.

Specifically, I wrote two unit tests for the following API endpoints:

1. api/inference:
This test assesses the functionality of the inference endpoint.

P.S: If you selected the "save" option at the beginning of training, you will be able to view the serialized pipeline under "models/pipeline_name."

Feel free to explore the code and interact with the Streamlit dashboard to understand the components and view the results of each task.
