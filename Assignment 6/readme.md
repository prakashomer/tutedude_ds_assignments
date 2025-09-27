## Methodology

### Data Loading & Inspection
- The Austin weather CSV data is loaded and explored using pandas Python library.
- Key observations: Some columns are objects (strings), and symbols like "T" and "-" are used for trace or missing values.

### Data Cleaning & Preprocessing
- Irrelevant columns (Date, Events) are removed.
- Special symbols ("T" for trace, "-" for missing) are handled:
  - "T" replaced with `0.0` (no measurable rain).
  - "-" and other non-numeric entries converted to NaN, then dropped for model simplicity.
- All features are converted to float type for numerical modeling.

### Feature Selection
- Model predictors: All available weather features except precipitation.
- Target variable: Precipitation (inches).

### Modeling
- Linear Regression (scikit-learn) predicts precipitation using weather features.
- Data is split into train/test sets.
- Model performance is evaluated using Mean Squared Error (MSE) and R^2 (explained variance).

### Analysis & Visualization
- Precipitation trends are visualized over time using matplotlib.
- Correlations between precipitation and weather features are analyzed using a heatmap.
- Relationships between precipitation and key attributes (Temperature, Humidity, Wind Speed) are displayed as scatter plots.

## Analysis Process
1. Load and inspect raw data.
2. Clean and preprocess for machine learning tasks.
3. Engineer features for regression modeling.
4. Train and evaluate linear regression.
5. Visualize results and correlations for insight.

## Key Findings
- Some weather features (average humidity, temperature, wind speed) show moderate-to-strong correlation with precipitation.
- Visualizations reveal seasonal and event-driven rainfall patterns.
- Linear regression can approximate rainfall levels, though non-linear models may improve accuracy.
