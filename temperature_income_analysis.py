import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

temperature = pd.read_csv("/content/temperatures.csv")
salary = pd.read_csv("/content/salaries.csv")

temperature["City"] = temperature["City"].str.strip()
salary["City"] = salary["City"].str.strip()

temperature = temperature[["City", "Average Temperature"]]
salary = salary[["City", "Average Salary"]]

# Clean salary values
salary["Average Salary"] = (
    salary["Average Salary"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

salary["Average Salary"] = pd.to_numeric(
    salary["Average Salary"],
    errors="coerce"
)

# Combine the datasets
combined = pd.merge(temperature, salary, on="City", how="inner")

# Remove missing values
combined = combined.dropna(subset=["Average Temperature", "Average Salary"])

combined.to_csv("/content/city_salary_temperature.csv", index=False)

print(combined)

# Calculate Pearson correlation and p-value
correlation, p_value = stats.pearsonr(
    combined["Average Temperature"],
    combined["Average Salary"]
)

print("Correlation:", correlation)
print("P-value:", p_value)

X = combined["Average Temperature"]
y = combined["Average Salary"]

# Linear regression
X_linear = sm.add_constant(X)
linear_model = sm.OLS(y, X_linear).fit()

# Quadratic regression
combined["Temperature Squared"] = X ** 2
X_quadratic = sm.add_constant(
    combined[["Average Temperature", "Temperature Squared"]]
)
quadratic_model = sm.OLS(y, X_quadratic).fit()

print("Linear regression:")
print(linear_model.summary())

print("Quadratic regression:")
print(quadratic_model.summary())

# Compare the two models
print("Linear R-squared:", linear_model.rsquared)
print("Quadratic R-squared:", quadratic_model.rsquared)
print("Linear AIC:", linear_model.aic)
print("Quadratic AIC:", quadratic_model.aic)
