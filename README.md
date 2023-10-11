@@ -1,135 +1,83 @@
# DNA Engineering ML Assignment
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
## Task 1 - Code Refactoring

The project contains by default:
- A baseline `naive bayes pipeline` trained on the aforementioned dataset
- An `API` that exposes an `inference endpoint` for predictions using the baseline pipeline
- A streamlit dashboard divided on three parts `(Exploratory Data Analysis, Training, Inference)`
I refactored the codebase following clean code guidelines. The main improvements are as follows:
