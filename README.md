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
