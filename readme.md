
---

# Linear Regression From Scratch

A simple implementation of **Linear Regression** from scratch in Python using **NumPy** and **Pandas**. This project demonstrates how a linear regression model learns the relationship between features and target variables using **gradient descent**, without relying on libraries like `scikit-learn` for model training .

---

## Features

* Linear regression implemented **from scratch**
* Computes **Mean Squared Error (MSE)** during training
* Calculates **R² (Coefficient of Determination)** to evaluate model performance
* Fully vectorized operations for efficient computation
* Easy to extend to multiple features

---

## Performance

* **R² Score:** 65%
* **Mean Squared Error (MSE):** 0.015

> The R² indicates a moderate fit, showing that the model explains a decent portion of the variance in the data.

---

## How It Works

1. Convert the dataset to NumPy arrays for efficient computation.
2. Initialize **weights** and **bias** randomly.
3. Train the model using **gradient descent**:

   * Compute predictions: `Ypred = X @ Weights + Bias`
   * Calculate gradients for weights and bias
   * Update weights and bias iteratively
4. Evaluate the model using **MSE** and **R² score**.

---
## Why This Project?

This project is perfect for learning the **mechanics behind linear regression**—understanding gradients, weight updates, and model evaluation—without relying on high-level libraries.


---

