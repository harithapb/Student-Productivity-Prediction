# Student Productivity Prediction

## Project Overview

A Machine Learning project that predicts a student's productivity score based on study habits, sleep, phone usage, exercise, attendance, stress, focus, and other factors.

The project also includes an interactive Streamlit web application for making predictions.

## Models Used

* Linear Regression
* KNN Regressor
* Decision Tree Regressor
* Random Forest Regressor

## Model Results

| Model             |     MAE |    RMSE |   R² Score |
| ----------------- | ------: | ------: | ---------: |
| Linear Regression | 0.00248 | 0.00287 | 0.99999997 |
| KNN               |  4.9323 |  6.1820 |     0.8516 |
| Decision Tree     |  3.9745 |  4.9854 |     0.9035 |
| Random Forest     |  2.0018 |  2.5405 |    0.97494 |

Best performing model: Linear Regression

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

## Project Files

```text
app.py
productivity_model.sav
scaler.sav
Student_Productivity_Prediction.ipynb
requirements.txt
README.md
```

## Run the Application

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Key Features

* Student productivity prediction
* Machine Learning model comparison
* Interactive Streamlit interface
* Productivity categories and recommendations
