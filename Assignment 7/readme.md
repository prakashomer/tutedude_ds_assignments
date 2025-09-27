## Methodology

### Data Loading and Cleaning

- Loaded the dataset from CSV
- Removed irrelevant columns, specifically `id`
- Verified that there were no missing values

### Exploratory Data Analysis (EDA)

- Visualized distribution of diagnosis labels
- Computed and visualized correlations between features using a heatmap

### Preprocessing

- Scaled feature values using `StandardScaler`
- Encoded diagnosis labels to binary format (0 for benign, 1 for malignant)
- Split data into training and testing sets

### Modeling

- Trained a `RandomForestClassifier` on training data
- Evaluated model performance on test data

### Results

- Model accuracy was approx. 96.5%
- Classification report showed high precision and recall on both classes
- Confusion matrix confirmed few misclassifications
