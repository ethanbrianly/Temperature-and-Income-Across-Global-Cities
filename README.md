# Temperature and Income Across Global Cities

## Project Overview

This project investigates whether there is a relationship between average temperature and economic prosperity across cities around the world. I combined two separate datasets—one containing temperature measurements and another containing average salary data—to create a single dataset that could be used to analyze the relationship between climate and salary.

## Research Question

Is a city's average temperature related to its economic prosperity?

## Datasets

### Temperature Dataset

* Daily temperature records from January 1, 2015, through December 31, 2019
* Cities were originally formatted together with their countries (e.g., Afghanistan-Farah)
* Values represent recorded daily average temperatures in °C

### Salary Dataset

* Contains city, region, and country information
* Contains annual average salary data for individual cities
* Salary values are reported by year

### Tools Used

* Python
* Pandas
* SciPy
* Statsmodels
* Microsoft Excel

## Data Cleaning & Preparation

Before analyzing the relationship between temperature and salary, I had to restructure and standardize both datasets so they could be combined.

### 1. Restructured the Temperature Dataset

The original temperature dataset was organized with dates as rows and cities as columns, while the salary dataset was organized with cities as rows and years as columns. Using **Excel**, I transposed the temperature dataset so that cities could be treated as individual observations and more easily compared with the salary data.

### 2. Separated and Standardized City Names

In the temperature dataset, the city and country were combined into a single column using a format such as `Afghanistan-Farah`. I used **Excel's delimiter tools** to split the combined values into separate city and country columns. I then cleaned and standardized the city names to address differences in formatting, spelling, and capitalization, making it easier to accurately match cities between the two datasets.

### 3. Calculated Yearly Average Temperatures

The temperature dataset contained daily observations, while the salary dataset contained one value per year. Using **Excel**, I grouped the temperature data by city and year and calculated the average temperature for each city for each year.

This converted daily temperature observations into a single yearly average for each city.

### 4. Matched the Years

I compared the years available in both datasets and kept only the years that appeared in both. This ensured that each temperature value was compared with the salary value from the same year, rather than comparing data from different time periods.

### 5. Joined the Datasets

After restructuring and cleaning the data, I used **Python and Pandas** to combine the temperature and salary datasets based on matching city information. This resulted in a final dataset containing **343 cities** with data available from both sources.

### 6. Removed Unusable Data

I used **Excel and Python** to identify and remove null values that could interfere with the analysis. Salary values containing missing or unusable entries were converted to missing values and excluded from the statistical analysis.

## Statistical Analysis

I used several statistical methods to examine the relationship between average temperature and average salary.

### Pearson Correlation

The Pearson correlation was used to measure the strength and direction of the linear relationship between average temperature and average salary.

* Correlation: -0.2603
* P-value: 1.02 × 10⁻⁶

The correlation indicates a weak negative relationship between average temperature and average salary. The small p-value indicates that the observed linear association is statistically significant in this dataset.

### Linear Regression

I fitted a linear regression model using average temperature to predict average salary.

* R²: 0.0677
* Temperature coefficient: -40.32
* 95% confidence interval: [-56.25, -24.39]

The temperature coefficient indicates that a 1°C increase in average temperature was associated with approximately $40.32 lower average salary in the dataset.

However, the R² value of approximately 0.068 means that average temperature explained only about 6.8% of the variation in salary across the cities.

### Quadratic Regression

I also tested whether the relationship between temperature and salary might be nonlinear by adding a squared temperature term to the regression model.

* R²: 0.0678
* Adjusted R²: 0.062
* Temperature coefficient: -34.50 (p = 0.364)
* Temperature² coefficient: -0.177 (p = 0.875)
* AIC: 5786.34

The quadratic model produced almost the same R² as the linear model and did not provide a meaningful improvement in model fit. The temperature-squared term was also not statistically significant.

The linear model had a slightly lower AIC (5784.37) than the quadratic model (5786.34), providing additional evidence that adding the quadratic term did not improve the model.

## Exploratory Analysis

I created a scatterplot comparing average temperature and average salary across the matched cities, along with a linear trendline.

* X-axis: Average Temperature (°C)
* Y-axis: Average Salary (USD)
* Trendline: y = -40.32x + 1858
* R²: 0.0677

The scatterplot and statistical analysis indicated a weak negative relationship between average temperature and average salary.

Although the relationship was statistically significant, the low R² value shows that temperature alone explains only a small portion of the differences in salary between cities.

## Conclusion

The analysis found a statistically significant but weak negative relationship between average temperature and average salary. Cities with higher average temperatures tended to have lower average salaries in this dataset.

However, the low R² value of 0.0677 indicates that temperature explained only about 6.8% of the variation in salary. The quadratic regression also provided virtually no improvement over the linear model, suggesting that there was no meaningful nonlinear relationship detected in this dataset.

These results show an association between temperature and salary, but they do not establish that temperature causes differences in salary. Other factors are likely to account for much more of the variation in salary between cities.

## Limitations

* The final dataset included only **343 matched cities**, which is a relatively small sample compared with the thousands of cities worldwide.
* Average salary does not fully represent economic well-being because **cost of living and purchasing power** can vary substantially between cities.
* The analysis only examined the relationship between temperature and salary and did not account for other factors that may influence salary, such as geography, industry, education, or local economic conditions.
* The datasets may not measure salary consistently across all cities, which can affect comparisons between locations.
* Because this is an observational analysis, the results show **association rather than causation**.
