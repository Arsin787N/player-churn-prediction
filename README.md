# Player Churn Prediction in Online Games

## Project Overview
Player churn (players leaving a game) is one of the major challenges in online games.
This project aims to predict player churn using machine learning techniques and
propose personalized recommendations to reduce player drop-off.

The project was developed as part of a Data Mining course and includes data analysis,
modeling, evaluation, and interpretation of results.

---

## Dataset
The dataset was obtained from Kaggle and contains behavioral information of online game players,
including features such as:
- Total playtime
- Player level
- Number of matches played
- Purchase history
- Last login activity

The target variable is **Churn**, which indicates whether a player leaves the game or not.

---

## Methodology

### Data Preprocessing
- Missing values were removed
- Categorical features were converted to numerical values
- Feature encoding was applied using one-hot encoding

### Models Used
Two machine learning models were implemented and compared:

1. **Logistic Regression**
   - Used as a baseline model
   - Simple, fast, and interpretable

2. **Random Forest Classifier**
   - Used as the main model
   - Capable of capturing non-linear relationships
   - Provided better overall performance

---

## Model Evaluation
The models were evaluated using the following metrics:
- Accuracy
- Precision
- Recall
- F1-score

Due to class imbalance in the dataset, Recall and F1-score were considered more important
than Accuracy alone. Random Forest achieved better performance, especially in identifying
players at risk of churn.

---

## Personalized Recommendation System
After predicting players who are likely to churn, a rule-based recommendation system was designed.
Based on player behavior, different actions are suggested, such as:
- Free rewards for inactive players
- Helper items for low-progress players
- Discounts or incentives for non-paying players

The goal of this system is to increase engagement and reduce churn.

---

## How to Run the Project
1. Open the notebook file in Google Colab
2. Upload the dataset CSV file
3. Run all cells sequentially
4. Review model evaluation results and recommendations

---

## Tools and Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Google Colab

---

## Notes
This project is designed in a step-by-step manner so that it can be easily extended
or continued by other students without major issues.
