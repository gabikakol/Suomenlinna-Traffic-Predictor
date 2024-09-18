# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Assuming your merged ferry traffic and weather dataset is in 'data'
# 'data' is a DataFrame with the columns 'temperature', 'wind_speed', 'precipitation', 'ferry_traffic', etc.

# Select the independent variables (weather features)
X = data[['temperature', 'wind_speed', 'precipitation', 'humidity', 'day_of_week', 'is_holiday']]  # Replace with actual column names

# Select the dependent variable (ferry traffic)
y = data['ferry_traffic']  # Replace with actual column name for ferry traffic

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")


#TO TEST MODEL 

import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel('Actual Ferry Traffic')
plt.ylabel('Predicted Ferry Traffic')
plt.title('Actual vs Predicted Ferry Traffic')
plt.show()

