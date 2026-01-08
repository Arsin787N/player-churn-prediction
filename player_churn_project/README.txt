Project Title:
Player Churn Prediction using Machine Learning

Description:
This project aims to predict user churn using machine learning techniques.
The dataset is based on a public churn dataset and is treated as player behavior data
for an online game scenario.

Tools and Technologies:
- Python
- pandas
- numpy
- scikit-learn
- VS Code

Project Structure:
player_churn_project/
│
├── data/
│   └── players.csv        (Dataset file)
│
├── src/
│   └── main.py            (Main source code)
│
└── README.txt             (Project description)

How to Run the Project:
1. Install required libraries:
   pip install pandas numpy scikit-learn matplotlib

2. Run the main file:
   python src/main.py

Steps Performed in the Project:
1. Loading and cleaning the dataset
2. Handling missing values
3. Encoding categorical variables
4. Splitting data into train and test sets
5. Training Logistic Regression model
6. Training Random Forest model
7. Evaluating models using classification metrics
8. Identifying users at risk of churn

Common Issues and Fixes:
- ModuleNotFoundError:
  Fixed by installing required libraries using pip

Notes:
This project is designed so that other students can continue development
by modifying the models or adding new features.
