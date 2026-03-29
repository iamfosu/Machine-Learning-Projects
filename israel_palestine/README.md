# 📊 Israel-Palestine Conflict Data Analysis

This project focuses on Exploratory Data Analysis (EDA) of datasets related to the Israel-Palestine conflict. Using Python, I have analyzed casualty records and news data to visualize trends, demographic impacts, and historical patterns.

## 📋 Project Overview
The goal of this analysis is to provide a data-driven perspective on the conflict by processing raw CSV data into meaningful visualizations. It covers:
* Trend analysis over time.
* Demographic distribution of fatalities.
* Correlation between events and news reporting.

## 📁 Dataset Description
The analysis utilizes two primary data sources:
* **`fatalities.csv`**: Detailed records of individuals, including dates, locations, and demographic information.
* **`news_data.csv`**: A collection of news headlines or reports related to specific dates and events to correlate data with media coverage.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** * `Pandas` (Data manipulation)
    * `Matplotlib` / `Seaborn` (Data visualization)
    * `NumPy` (Numerical processing)

## 🧠 Key Insights from `main.ipynb`
The Jupyter Notebook contains the following workflow:
1. **Data Cleaning:** Handling missing values and formatting dates for time-series analysis.
2. **Fatality Trends:** Visualizing the spike in incidents over specific years/months.
3. **Geographic Distribution:** Identifying regions with the highest conflict intensity.
4. **Demographic Analysis:** Breakdown of casualties by age, gender, and citizenship.

## 🚀 How to View the Analysis
1. Ensure you have the global requirements installed from the root directory.
2. Open the notebook locally:
   ```bash
   jupyter notebook main.ipynb
