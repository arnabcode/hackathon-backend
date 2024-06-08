import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor  # Replace with desired model

# Replace 'path/to/your/data.csv' with the actual path to your CSV file
data = pd.read_csv('MOCK_DATA.csv')

# Feature Engineering
data['date'] = pd.to_datetime(data['date'])  # Convert date to datetime format
data['day_of_week'] = data['date'].dt.weekday  # Extract day of week (0-6)
data['week_of_month'] = data['date'].dt.isocalendar().week  # Extract week of month (1-5)
data['monthly_recurring'] = (data.groupby('merchant_name')['date']
                             .transform('nunique') == 1)  # Flag monthly recurring transactions

# Feature Scaling (numerical features)
scaler = StandardScaler()
data['scaled_amount'] = scaler.fit_transform(data[['amount']])

# Separate target variable (optional, can be 'amount' or a categorical variable)
target_variable = 'monthly_recurring'  # Replace with desired target variable

# Split data into training, validation, and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop(target_variable, axis=1),
                                                  data[target_variable], test_size=0.2, random_state=42)

# Model Building (using Random Forest Regressor for this example)
model = RandomForestRegressor(n_estimators=100)  # Adjust hyperparameters as needed
model.fit(X_train, y_train)

# Model Evaluation (Mean Squared Error for regression)
from sklearn.metrics import mean_squared_error
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save the Model (replace with preferred serialization method)
import joblib
joblib.dump(model, 'pattern_matching_model.pkl')
