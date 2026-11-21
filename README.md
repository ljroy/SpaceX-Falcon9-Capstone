# SpaceX-Falcon9-Capstone
SpaceX Falcon 9 Data Science Capstone Project
### 1. Project Overview

This project is part of the IBM Data Science Professional Certificate Capstone. The objective is to analyze SpaceX Falcon 9 launch data and develop machine learning models to predict whether the Falcon 9 first stage will land successfully.

The project uses data collection, data wrangling, exploratory data analysis, interactive visualization, and machine learning techniques.

### 2. Project Objectives

- Collect Falcon 9 launch data from available sources.
- Perform data cleaning and preprocessing.
- Explore launch records and identify patterns.
- Analyze launch sites and landing outcomes.
- Build an interactive dashboard using Plotly Dash.
- Train machine learning models to predict first-stage landing success.

### 3. Project Workflow

The project is organized into the following stages:

1. Data Collection Using Web Scraping
2. Data Collection Using SpaceX REST API
3. Data Wrangling
4. Exploratory Data Analysis Using SQL
5. Exploratory Data Analysis Using Data Visualization
6. Interactive Visual Analytics Dashboard
7. Machine Learning Prediction

### 4. Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- BeautifulSoup
- Requests
- SQL
- SQLite
- Matplotlib
- Seaborn
- Plotly
- Dash
- Scikit-learn
- GitHub

### 5. Project Files

| File | Description |
|---|---|
| `jupyter-labs-webscraping.ipynb` | Collecting launch data through web scraping |
| `jupyter-labs-spacex-data-collection-api.ipynb` | Collecting data using the SpaceX API |
| `labs-jupyter-spacex-Data wrangling.ipynb` | Data cleaning and preparation |
| `lab_jupyter_launch_site_location.ipynb` | Launch site location analysis |
| `spacex-dash-app.py` | Interactive SpaceX launch dashboard |
| `SpaceX_Machine Learning Prediction_Part_5.ipynb` | Machine learning prediction |
| `spacex_launch_dash.csv` | Dataset used by the dashboard |

### 6. Interactive Dashboard

The dashboard is developed using Plotly Dash.

It provides interactive visualizations to explore:
- Launch success distribution by launch site.
- Launch outcomes for selected launch sites.
- Payload mass and landing outcomes.
- Booster version categories.

### 7. Machine Learning

Machine learning classification algorithms are used to predict the success of Falcon 9 first-stage landings.

The models explored include:
- Logistic Regression
- Support Vector Machine
- Decision Tree
- K-Nearest Neighbors

Model performance is evaluated using test data and classification accuracy.

### 8. How to Run the Dashboard

Install the required libraries:

```bash
pip install pandas dash plotly
```

Run the application:

```bash
python spacex-dash-app.py
```

Open the local address displayed in the terminal to access the dashboard.

Make sure `spacex_launch_dash.csv` is in the same directory as the Python application.

### 9. Conclusion

This capstone project demonstrates the application of data science techniques to real-world aerospace launch data. It combines data collection, data analysis, visualization, and machine learning to investigate the factors associated with Falcon 9 first-stage landing success.



