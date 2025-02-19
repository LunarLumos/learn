# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load data (Replace with your own dataset path)
df = pd.read_csv('test.csv')  # Load your dataset

# Display first few rows of the dataset
print("Initial Data:")
print(df.head())

# 1. Handling Missing Data
# Check for missing values
print("\nMissing Data:")
print(df.isnull().sum())

# Impute missing values with mean for numerical columns
df.fillna(df.mean(), inplace=True)

# Alternatively, you can drop rows/columns with missing values if preferred
# df.dropna(inplace=True)

# 2. Removing Duplicates
df.drop_duplicates(inplace=True)
print("\nData after removing duplicates:")
print(df.head())

# 3. Handling Outliers (Detecting using IQR method)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))
print("\nOutlier Detection (First 5 Rows):")
print(outliers.head())

# Remove outliers (you can choose to drop outliers)
df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

# 4. Feature Engineering
# Create new feature (example: extracting year from a date column)
df['year'] = pd.to_datetime(df['date_column']).dt.year  # Modify this according to your column

# Encode categorical columns using Label Encoding (for ordinal data)
le = LabelEncoder()
df['category_column'] = le.fit_transform(df['category_column'])

# Alternatively, you can use One-Hot Encoding for nominal categorical data
# df = pd.get_dummies(df, columns=['category_column'])

# 5. Data Normalization/Standardization
# Normalization (Scaling between 0 and 1)
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df[['numeric_column1', 'numeric_column2']])  # Modify with actual numeric columns
df[['numeric_column1', 'numeric_column2']] = df_scaled

# Standardization (Zero mean, unit variance)
scaler = StandardScaler()
df_standardized = scaler.fit_transform(df[['numeric_column1', 'numeric_column2']])
df[['numeric_column1', 'numeric_column2']] = df_standardized

# 6. Train-Test Split
# Split the data into features (X) and target (y)
X = df.drop('target_column', axis=1)  # Replace 'target_column' with your actual target variable
y = df['target_column']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Model Training (Random Forest Classifier Example)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 8. Model Evaluation
# Predict on test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

# Cross-validation to validate the model
cross_val_scores = cross_val_score(model, X, y, cv=5)  # 5-fold cross-validation
print(f"\nCross-validation scores: {cross_val_scores}")
print(f"Average cross-validation score: {cross_val_scores.mean():.2f}")
