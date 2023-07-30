# Big-Data-Analysis

## **Social Media Big Data Analysis**
This repository contains a Python project for analyzing big data from social media sites like Twitter and YouTube. The analysis is carried out using Twitter API, Python, Airflow, Pandas, and Seaborn to gain insights from the collected data.

### **Twitter Data Analysis**
In the "twitter_analysis" directory, we use Twitter API, Python, and Airflow to read and process Twitter tweets. The data includes tweet details, user information, retweet count, favorite count, etc.

### **YouTube Data Analysis**
In the "youtube_analysis" directory, we utilize the YouTube Data API to scrape YouTube data. We load this data into a Python Pandas DataFrame and then analyze it. We also create simple visualizations using the Seaborn library.

### **Getting Started**
Obtain API keys and tokens from the Twitter Developer portal and YouTube Data API Key from the Google Developer Console.

Install required dependencies mentioned in the "requirements.txt" file.

Set up necessary configurations in "config.py" for both Twitter and YouTube data analysis.

### **Usage**
For Twitter Analysis: Create tasks as Airflow DAGs in the "twitter_analysis/dags" directory, then schedule and trigger them using the Airflow UI or CLI.

For YouTube Analysis: Write Python code to interact with the YouTube API, retrieve data, process it, and load it into a Pandas DataFrame. Perform data analysis and create visualizations using Seaborn.

### **Contributing**
Contributions are welcome! Feel free to submit pull requests for enhancements, bug fixes, or new features.

