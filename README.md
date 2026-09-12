# Temperature and Income Across Global Cities
## Project Overview
This project investigates whether there is a relationship between average temperature and economic prosperity across cities around the world. I combined two separate datasets—one containing daily temperature measurements and another containing yearly average income—to create a single dataset that could be used to analyze the relationship between climate and income.

## Research Question
Is a city's average temperature related to its economic prosperity?

## Datasets
### Temperature Dataset
Daily temperature records from January 1, 2015, through December 31, 2019
Cities were originally formatted together with their countries (e.g., Afghanistan-Farah)
Values represent recorded daily average temperatures in °C
### Income Dataset
Contains city, region, and country information
Contains annual average income data for individual cities
Income values are reported by year
Tools Used
Python
Pandas
Microsoft Excel

## Data Cleaning & Preparation
Before analyzing the relationship between temperature and income, I had to restructure and standardize both datasets so they could be combined.

### 1. Restructured the Temperature Dataset

The original temperature dataset was organized with **dates as rows and cities as columns**, while the income dataset was organized with **cities as rows and years as columns**. Using **Excel**, I transposed the temperature dataset so that cities could be treated as individual observations and more easily compared with the income data.

### 2. Separated and Standardized City Names

In the temperature dataset, the city and country were combined into a single column using a format such as `Afghanistan-Farah`. I used **Excel's delimiter tools** to split the combined values into separate city and country columns. I then cleaned and standardized the city names to address differences in formatting, spelling, and capitalization, making it easier to accurately match cities between the two datasets.

### 3. Calculated Yearly Average Temperatures

The temperature dataset contained **daily observations**, while the income dataset contained **one value per year**. Using **Excel**, I grouped the temperature data by city and year and calculated the **average temperature for each city for each year**.

This converted hundreds of daily temperature observations into a single yearly average for each city.

### 4. Matched the Years

I compared the years available in both datasets and kept only the years that appeared in both. This ensured that each temperature value was compared with the **income value from the same year**, rather than comparing data from different time periods.

### 5. Joined the Datasets

After restructuring and cleaning the data, I used **Python and Pandas** to combine the temperature and income datasets based on matching city information. This resulted in a final dataset containing **343 cities** with data available from both sources.

### 6. Removed Unusable Data

I used **Excel and Python** to identify and remove null values that could interfere with the analysis. I also excluded observations that did not contain the necessary temperature and income information.

## Exploratory Analysis
To examine the relationship between climate and economic prosperity, I created a scatterplot comparing average temperature and average income across the matched cities.

X-axis: Average Temperature (°C)
Y-axis: Average Income (USD)
Trendline: y = -40.32x + 1858
R²: 0.0677
The trendline indicated a slight negative relationship, meaning that higher average temperatures were generally associated with lower average income in the dataset. However, the relationship was weak.

The R² value of 0.0677 indicates that average temperature explained only about 6.8% of the variation in income. This suggests that temperature alone is not a strong predictor of economic prosperity.

## Conclusion
The analysis found a slight negative relationship between average temperature and income, but the relationship was not strong enough to conclude that temperature is a meaningful predictor of economic prosperity. The low R² value suggests that most differences in income between cities are explained by factors other than temperature.

Overall, temperature may play some role in economic conditions, but other factors are likely to have a much greater influence on a city's economic prosperity.

## Limitations
The final dataset only included 343 matched cities, which is a small sample compared to the thousands of cities worldwide. Additionally, income may not fully represent economic well-being because cost of living and purchasing power vary between cities. Finally, the analysis only examined temperature and income without accounting for other factors that may have a greater impact on economic prosperity.
