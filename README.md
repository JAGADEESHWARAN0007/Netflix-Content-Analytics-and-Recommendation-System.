# Netflix Content Analytics and Recommendation System

## Project Overview

This project analyzes Netflix's content library using Data Analytics, Business Intelligence, and Machine Learning techniques. The goal is to uncover content trends, identify business insights, and build a recommendation system that suggests similar movies and TV shows based on user preferences.

The project combines Python, Power BI, Streamlit, and Machine Learning to demonstrate the complete data analytics workflow from data cleaning to interactive dashboard development and recommendation generation.

---

## Problem Statement

Netflix hosts thousands of movies and TV shows across multiple countries, genres, and categories. As the content library grows, users face difficulties discovering relevant content, while business teams need insights to support content acquisition and investment decisions.

This project addresses these challenges through:

* Exploratory Data Analysis (EDA)
* Business Intelligence Dashboards
* Content-Based Recommendation System
* Interactive Streamlit Application

---

## Objectives

* Clean and preprocess Netflix dataset
* Perform exploratory data analysis
* Identify key content trends and business insights
* Build interactive Power BI dashboards
* Develop a movie recommendation system using TF-IDF and Cosine Similarity
* Create a user-friendly Streamlit application

---

## Dataset

Dataset Source:

Netflix Movies and TV Shows Dataset (Kaggle)

Features include:

* Title
* Type (Movie / TV Show)
* Director
* Cast
* Country
* Date Added
* Release Year
* Rating
* Duration
* Genre
* Description

---

## Technology Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorization
* Cosine Similarity

### Business Intelligence

* Power BI

### Web Application

* Streamlit

---

## Project Workflow

1. Data Understanding
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis
4. Feature Engineering
5. Power BI Dashboard Development
6. Recommendation System Development
7. Streamlit Application Deployment

---

## Key Business Insights

### Movies vs TV Shows

* Movies: 6,126
* TV Shows: 2,664

Insight:
Movies account for approximately 70% of Netflix content.

Recommendation:
Continue expanding successful TV show investments while maintaining a strong movie catalog.

---

### Top Content Producing Countries

Top Contributors:

1. United States
2. India
3. United Kingdom

Insight:
The United States dominates Netflix's content production.

Recommendation:
Increase investments in emerging markets such as India, South Korea, and Japan.

---

### Genre Analysis

Top Genres:

* International Movies
* Dramas
* Comedies

Insight:
Netflix strongly focuses on international and drama-based content.

Recommendation:
Expand region-specific content to attract global audiences.

---

### Content Growth Analysis

Insight:
Netflix experienced rapid content growth between 2016 and 2019, peaking in 2019.

Recommendation:
Focus on content quality while maintaining strategic expansion.

---

## Power BI Dashboard Features

The dashboard includes:

* Total Titles KPI
* Movies KPI
* TV Shows KPI
* Movies vs TV Shows Analysis
* Top Content Producing Countries
* Top Netflix Genres
* Content Rating Distribution
* Content Added Over Time
* Interactive Country Filter
* Interactive Content Type Filter

---

## Recommendation System

### Approach

The recommendation system uses:

* Genre Information
* Description
* Director
* Cast

These features are combined and transformed using TF-IDF Vectorization.

Cosine Similarity is then used to identify similar content.

### Recommendation Methods

#### 1. Title-Based Recommendation

Example:

Input:
Stranger Things

Output:

* The OA
* Manifest
* Warrior Nun
* The Umbrella Academy
* Nightflyers

#### 2. Preference-Based Recommendation

Users can select:

* Content Type
* Genre
* Rating
* Release Year

The system then recommends matching content.

---

## Streamlit Application

Features:

* Modern User Interface
* Title-Based Recommendations
* Preference-Based Recommendations
* Interactive Search
* Real-Time Results

Run locally:

```bash
streamlit run app.py
```

---

## Project Structure

```text
Netflix-Content-Analytics-and-Recommendation-System

├── dashboard
│   └── Netflix_Analytics_Dashboard.pbix

├── dataset
│   ├── netflix_cleaned.csv
│   ├── netflix_powerbi.csv
│   └── netflix_with_tags.csv

├── notebooks
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_EDA.ipynb
│   ├── 04_PowerBI_Preparation.ipynb
│   └── 05_Movie_Recommendation_System.ipynb

├── reports
│   └── EDA_Insights.docx

├── screenshots

├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Screenshots

### Power BI Dashboard

Add dashboard screenshot here.

### Streamlit Home Page

Add homepage screenshot here.

### Title Recommendation

Add recommendation screenshot here.

### Preference-Based Recommendation

Add recommendation screenshot here.

---

## Future Enhancements

* Hybrid Recommendation System
* Collaborative Filtering
* User Authentication
* Cloud Deployment
* Real-Time Recommendation API
* Sentiment Analysis on Reviews

---

## Author

Jagadeeshwaran S.

B.Tech Information Technology

Kumaraguru College of Technology

Aspiring Data Analyst | Data Science Enthusiast

---

## License

This project is developed for educational and portfolio purposes.
