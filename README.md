# learn where i learn

---

### 1. **Linear Regression (Single-variable regression)**

#### When to Use: 
You should use **linear regression** when you have only **one independent variable** (feature) and you want to predict a continuous target (dependent variable).

#### Example Dataset:
Let’s predict the **price of a house** based only on the **square footage** of the house.

| Square Footage (X) | House Price (Y) |
|--------------------|-----------------|
| 800                | 150,000         |
| 1000               | 180,000         |
| 1200               | 210,000         |
| 1400               | 240,000         |
| 1600               | 270,000         |

- **X (Feature)**: Square Footage
- **Y (Target)**: House Price

#### Why Use Linear Regression?
- You have **one feature** (Square Footage) predicting the **house price**.
- The relationship between **X (Square Footage)** and **Y (House Price)** is likely **linear** (i.e., as square footage increases, the price increases in a linear way).

#### Model:
Using **Linear Regression**, you find the equation that best fits this data (e.g., `Y = mX + b`, where `m` is the slope and `b` is the intercept).

---

### 2. **Multiple Linear Regression (Multiple Variables)**

#### When to Use:
Use **multiple linear regression** when you have **more than one independent variable** and you want to predict a continuous target. In this case, we have **multiple features** influencing the target variable.

#### Example Dataset:
Let’s predict the **price of a house** using **multiple features** (e.g., **square footage**, **number of bedrooms**, and **location**).

| Square Footage (X1) | Bedrooms (X2) | Location (X3) | House Price (Y) |
|--------------------|---------------|---------------|-----------------|
| 800                | 2             | Suburb        | 150,000         |
| 1000               | 3             | Urban         | 180,000         |
| 1200               | 3             | Suburb        | 210,000         |
| 1400               | 4             | Urban         | 240,000         |
| 1600               | 4             | Suburb        | 270,000         |

- **X1 (Feature 1)**: Square Footage
- **X2 (Feature 2)**: Number of Bedrooms
- **X3 (Feature 3)**: Location (Suburb vs. Urban)
- **Y (Target)**: House Price

#### Why Use Multiple Linear Regression?
- You have **multiple features** (Square Footage, Bedrooms, and Location).
- The **house price** is influenced by all these factors, so you need a model that accounts for all the variables.

#### Model:
Using **Multiple Linear Regression**, the model will find a more complex relationship such as:

`Y = m1 * X1 + m2 * X2 + m3 * X3 + b`

Where:
- `m1`, `m2`, and `m3` are the coefficients for each feature.
- `b` is the intercept.

---

### 3. **Polynomial Regression (Non-linear relationship)**

#### When to Use:
Use **polynomial regression** when you have a **non-linear relationship** between the feature(s) and the target variable. You can extend **linear regression** to a higher degree polynomial to capture curves in the data.

#### Example Dataset:
Let’s predict **sales** based on **advertising spend**, but the relationship between the two is **non-linear**.

| Advertising Spend (X) | Sales (Y) |
|-----------------------|-----------|
| 100                   | 200       |
| 200                   | 400       |
| 300                   | 600       |
| 400                   | 800       |
| 500                   | 900       |

But the relationship is not perfectly linear. The sales increase at a decreasing rate as the advertising spend increases.

#### Why Use Polynomial Regression?
- The data shows a **curved** or **non-linear** relationship.
- A **linear model** would not fit this data well because the relationship between advertising spend and sales is not straight.

#### Model:
You would fit a polynomial equation (e.g., quadratic):

`Y = a * X^2 + b * X + c`

Where:
- `a`, `b`, and `c` are the coefficients.
- The model captures the **curved** relationship between the features and the target.

---

### 4. **Ridge and Lasso Regression (Regularization)**

#### When to Use:
Use **Ridge** or **Lasso regression** when you have **many features** and want to reduce overfitting. These methods add a penalty term to the cost function to **regularize** the model and avoid overfitting.

#### Example Dataset:
Let’s predict the **performance of students** based on a large number of features such as **hours of study**, **attendance**, **IQ**, **study material** used, and more.

| Hours of Study (X1) | Attendance (X2) | IQ (X3) | Performance (Y) |
|---------------------|-----------------|---------|-----------------|
| 5                   | 90              | 110     | 75              |
| 7                   | 80              | 120     | 85              |
| 6                   | 95              | 115     | 78              |
| 4                   | 70              | 100     | 65              |
| 8                   | 85              | 125     | 90              |

#### Why Use Ridge/Lasso Regression?
- **Many features**: If you have many features (like study material, extracurriculars, etc.), some may be irrelevant.
- **Overfitting risk**: A standard linear regression model might overfit the data and perform poorly on new, unseen data.

#### Model:
- **Ridge regression** adds an L2 penalty (sum of the squares of coefficients).
- **Lasso regression** adds an L1 penalty (absolute sum of coefficients) and can **zero out irrelevant features**.

---

### 5. **Logistic Regression (Classification)**

#### When to Use:
Use **logistic regression** when you need to predict **binary outcomes** (i.e., classification problems). It is used when the target variable is categorical with two possible outcomes.

#### Example Dataset:
Let’s predict if a **customer will churn** (leave the service) or **stay** based on their **age** and **account balance**.

| Age (X1) | Account Balance (X2) | Churn (Y) |
|----------|----------------------|-----------|
| 25       | 500                  | No        |
| 40       | 1500                 | Yes       |
| 30       | 700                  | No        |
| 60       | 1000                 | Yes       |
| 50       | 800                  | No        |

#### Why Use Logistic Regression?
- **Binary outcome**: The target variable is **binary** (Yes/No), representing churn (whether the customer will leave or stay).
- **Prediction**: Logistic regression predicts the **probability** that a customer will churn.

#### Model:
Using **logistic regression**, the model will estimate the probability of churn (output between 0 and 1) using a logistic function (sigmoid curve).

`P(Y=1) = 1 / (1 + exp(-(b0 + b1 * X1 + b2 * X2)))`

Where:
- `P(Y=1)` is the probability of churn.
- `X1`, `X2` are the input features (Age, Account Balance).

---

### Summary of When to Use Which:

| **Scenario** | **Regression Type** | **Why?** |
|--------------|---------------------|----------|
| One feature predicting a continuous target | Linear Regression | Simple linear relationship |
| Multiple features predicting a continuous target | Multiple Linear Regression | Complex relationships with multiple features |
| Non-linear relationship between feature and target | Polynomial Regression | Captures curved relationships |
| Many features with risk of overfitting | Ridge/Lasso Regression | Regularization to prevent overfitting |
| Binary classification problem | Logistic Regression | Predicting probabilities for a binary outcome |

---


