import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create house dataset
np.random.seed(42)
n = 120

size = np.random.randint(500, 4000, n)
bedrooms = np.random.randint(1, 6, n)
bathrooms = np.random.randint(1, 4, n)
distance = np.random.randint(1, 30, n)

price = 3000*bedrooms + 5000*bathrooms + 200*size - 1500*distance

data = pd.DataFrame({
    "Size": size,
    "Bedrooms": bedrooms,
    "Bathrooms": bathrooms,
    "Distance": distance,
    "Price": price
})

print("House Dataset:")
print(data.head())

# Separate input and output
X = data[["Size", "Bedrooms", "Bathrooms", "Distance"]]
y = data["Price"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict house prices
y_pred = model.predict(X_test)

# Calculate model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nCoefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Regression equation
print("\nRegression Equation:")
print("Price =", model.intercept_,
      "+", model.coef_[0], "* Size",
      "+", model.coef_[1], "* Bedrooms",
      "+", model.coef_[2], "* Bathrooms",
      "+", model.coef_[3], "* Distance")

# Actual vs Predicted graph
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Price")
plt.grid()

# Residual graph
residuals = y_test - y_pred

plt.subplot(1, 2, 2)
plt.scatter(y_pred, residuals)
plt.axhline(0, color="red")
plt.xlabel("Predicted Price")
plt.ylabel("Residual")
plt.title("Residual Plot")
plt.grid()

plt.tight_layout()
plt.show()