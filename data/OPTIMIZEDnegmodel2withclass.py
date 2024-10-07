import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class DataModel:
    def __init__(self, root, year, month, day, hour, avg_temp, wind_speed, precipitation, stop):
        self._root = root

        # Input data attributes
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.avg_temp = avg_temp
        self.wind_speed = wind_speed
        self.precipitation = precipitation
        self.stop = stop

        # Load the data and prepare it only once
        self.df = None
        self.model = None
        self.scaler = None
        self.mse = None
        self.r2 = None

        # Load data and train model lazily
        self.load_and_train_model()

    def load_and_train_model(self):
        # Load data once and cache it
        if self.df is None:
            self.df = pd.read_csv('data/combined-data.csv')

        X = self.df[['Year', 'Month', 'Day', 'Hour', 'Average temperature', 'Wind speed', 'Precipitation', 'Stop']]
        y = self.df['Passengers']

        # Split and scale the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize scaler once
        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        # Initialize and train the model if not already done
        if self.model is None:
            self.model = RandomForestRegressor(n_estimators=50, n_jobs=-1, random_state=42)  # Reduced n_estimators to 50
            self.model.fit(X_train_scaled, y_train)

        # Predict and calculate metrics once
        y_pred = self.model.predict(X_test_scaled)
        y_pred = np.maximum(y_pred, 0)  # Ensure no negative predictions

        self.mse = mean_squared_error(y_test, y_pred)
        self.r2 = r2_score(y_test, y_pred)

    def predict_traffic(self):
        # Create input data frame
        input_data = pd.DataFrame([[self.year, self.month, self.day, self.hour, self.avg_temp, self.wind_speed, self.precipitation, self.stop]],
                                  columns=['Year', 'Month', 'Day', 'Hour', 'Average temperature', 'Wind speed', 'Precipitation', 'Stop'])

        # Scale the input data
        input_data_scaled = self.scaler.transform(input_data)

        # Make prediction
        prediction = self.model.predict(input_data_scaled)
        prediction = np.maximum(prediction, 0)  # Ensure no negative predictions

        return prediction[0]
