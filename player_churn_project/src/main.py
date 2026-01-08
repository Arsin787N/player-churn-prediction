print("Player Churn Project Started")

import pandas as pd

# Load dataset
df = pd.read_csv("data/players.csv")

# Show first 5 rows
print(df.head())

# Show dataset shape
print("\nDataset shape:", df.shape)

# Separate features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Convert categorical columns to numeric
X = pd.get_dummies(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train size:", X_train.shape)
print("Test size:", X_test.shape)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model training completed.")

from sklearn.metrics import classification_report

y_pred = model.predict(X_test)

print("\nModel Evaluation:")
print(classification_report(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier

# Train Random Forest model
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

# Evaluate Random Forest
rf_pred = rf_model.predict(X_test)

print("\nRandom Forest Evaluation:")
print(classification_report(y_test, rf_pred))

df["Churn_Prediction"] = rf_model.predict(X)

at_risk_players = df[df["Churn_Prediction"] == 1]

print("\nAt-risk users sample:")
print(at_risk_players.head())

def recommend_offer(player):
    if player['TotalPlayTime'] < 5:
        return "Free Daily Reward + XP Boost"
    elif player['Level'] < 10 and player['MatchesPlayed'] > 20:
        return "Difficulty Reduction + Helper Item"
    elif player['DaysSinceLastLogin'] > 7:
        return "Exclusive Item + Personal Message"
    elif player['Purchases'] == 0:
        return "First Purchase Discount"
    else:
        return "Standard Engagement Reward"
