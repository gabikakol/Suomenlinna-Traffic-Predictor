import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class DataModel:

    def __init__(self, root, year, month, day, hour, avg_temp, wind_speed, precipitation, stop):

        self._root = root

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.avg_temp = avg_temp
        self.wind_speed = wind_speed
        self.precipitation = precipitation
        self.stop = stop

        df = pd.read_csv('combined-data.csv')

        X = df[['Year', 'Month', 'Day', 'Hour', 'Average temperature', 'Wind speed', 'Precipitation', 'Stop']] 
        y = df['Passengers']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

        self.model.fit(X_train_scaled, y_train)

        y_pred = self.model.predict(X_test_scaled)
        y_pred = np.maximum(y_pred, 0)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

    def predict_traffic(self):
        input_data = pd.DataFrame([[self.year, self.month, self.day, self.hour, self.avg_temp, self.wind_speed, self.precipitation, self.stop]], 
                                columns=['Year', 'Month', 'Day', 'Hour', 'Average temperature', 'Wind speed', 'Precipitation', 'Stop'])
        input_data_scaled = self.scaler.transform(input_data)
        prediction = self.model.predict(input_data_scaled)
        prediction = np.maximum(prediction, 0)
        return prediction[0]



    """
    year = 2025
    month = 7
    day = 25
    hour = 15  # Example hour
    avg_temp = 22.0  # Example temperature
    wind_speed = 2.0  # Example wind speed
    precipitation = 18.0  # Example precipitation
    stop = 99  
    """
