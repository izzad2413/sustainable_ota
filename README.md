# Predicting Sustainable Tourism in Malaysia's Accommodation Sector: A Machine Learning Approach

[![Static Badge](https://img.shields.io/badge/Back_to_Portfolio_Page-red?style=for-the-badge&logo=github&labelColor=black)](https://izzad2413.github.io/nazmirulizzadnassir.github.io/)

![malaysia_sustainable_ota-modified_v2](https://github.com/user-attachments/assets/e5c83fec-b504-4f09-8627-f9fb4c100cab)

## Table of Contents 

- [About Project](#about-project)
- [Background Overview](#background-overview)
- [Problem Statement](#problem-statement)
- [Objective](#objective)
- [Built With](#built-with)
- [Data Source](#data-source)
- [Methodology](#methodology)
- [Result and Impact](#result-and-impact)
- [Challenges and Solutions](#challenges-and-solutions)
- [How to Use](#how-to-use)
- [Acknowledgement](#acknowledgement)

## About Project

This project simplifies and extends my master's thesis by deploying a machine learning model to predict sustainable practices in Malaysia's accommodation sector, enhancing tourism sustainability through data-driven insights.

## Background Overview

Tourism is a trillion-dollar industry contributing significantly to the global GDP and accounting for about 7% of all exports, with over 1.2 billion people traveling abroad annually. Despite its economic benefits, tourism significantly impacts global carbon emissions, contributing over 8% of all GHG emissions. Sustainable tourism is crucial to balancing the economic, social, and environmental impacts of tourism. Malaysia, a major tourist destination, has integrated sustainable practices into its tourism strategies, emphasizing data-driven approaches for assessing sustainability. 

## Problem Statement

Rising environmental concerns in tourism emphasize the need for sustainable accommodations practices, which require a solid understanding of metrics and effective data-driven decision-making. The lack of precise data in Malaysia's accommodations sector is hindering the progress of sustainable tourism. This data gap hampers tourists' ability to make environmentally responsible choices and deprives providers and policymakers of crucial insights needed to promote sustainable practices.

## Objective

This project aims to develop and evaluate predictive models using machine learning techniques on data from an Online Travel Agent (OTA) platform to accurately classify tourist accommodations as sustainable, as indicated by the presence of a sustainability label. The objective encompasses:

- Identifying relevant features from the platform's data.
- Selecting appropriate machine learning algorithms.
- Assessing the models' performance based on unseen data.

By leveraging OTA data, this project seeks to address current data collection challenges, enhance the reliability of sustainability indicators, and support informed decision-making for tourists, accommodation providers, and policymakers.

## Built With

![My Skills](https://go-skill-icons.vercel.app/api/icons?i=vscode,python,playwright,scikitlearn,streamlit,tableau&titles=true)

## Data Source

- Data was meticulously gathered from the OTA platform, Booking.com from September til October 2023.

## Methodology

- **Data Collection:** Using Python and Playwright, data was scraped from specified URLs, capturing 40 features for 25 accommodations per page across 40 pages, resulting in 1000 accommodations per location. Covering 16 states and Malaysia's federal territory, a total of 17,866 raw samples were collected and stored in a CSV file.
- **Preprocessing:** First, conduct [exploratory data analysis (EDA)](https://github.com/izzad2413/sustainable_ota/blob/main/notebooks/1.0_exploratory-data-analysis.ipynb) to inspect the dataset. After inspection, proceed with [data transformation and feature engineering](https://github.com/izzad2413/sustainable_ota/blob/main/notebooks/2.0_preprocessing-dataset.ipynb) to prepare for model development. After processing, the dataset has 84 features, which may cause overfitting. Use [feature selection methods](https://github.com/izzad2413/sustainable_ota/blob/main/notebooks/3.0_feature_selection.ipynb) like filter methods and recursive feature elimination (RFE) to identify the most relevant features. The selected features will be used for modeling.
- **Model Development:** The dataset's complexity is challenging, so testing with non-linear classifiers such as Support Vector Machine (SVM), Decision Tree (DT), Random Forest (RF), K Nearest Neighbor (KNN), and Multi-layer Perceptron (MLP).
- **Model Evaluation:** Due to class imbalance, accuracy alone may be misleading. Therefore, precision, recall, F1-scores, and precision-recall area under the curve (PRAUC) will be used as evaluation metrics.
- **Deployment:** Use Streamlit framework for model deployment due to its simplicity and free availability.

## Result and Impact

- A quick [visual summary](https://public.tableau.com/views/MalaysiaTravelSustainableAccommodationTourism/Overview?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) of the current landscape of sustainable tourism in Malaysia's accommodation sector is provided using Tableau. As of the date data collected, there is around 79.12% of non-travel sustainable while only 20.88% travel sustainable accommodation in Malaysia.
- The RFE method indicates that the significant number of features ranges between 11 and 22, which can be extracted from OTA data.
- Among various models tested, the MLP model shows the best performance. Although its performance is acceptable, there is still room for improvement.
- The model has been deployed using Streamlit, creating a web application that is easy for the public to use and try out.

## Challenges and Solutions

- **Challenges in Web Scraping:** Enhance the robustness of web scraping tools by leveraging AI technologies such as ChatGPT to handle dynamic content and site structures effectively.
- **Complexity in Data Preprocessing:** Utilize AI, including tools like ChatGPT, to streamline and optimize the entire data preprocessing workflow, ensuring clean and well-structured datasets.
- **Handling Imbalanced Classes:** Implement SMOTE and employ suitable evaluation metrics to address and evaluate class imbalances effectively.
- **Managing a Large Number of Features:** Apply feature selection techniques to reduce dimensionality and select the most relevant features, improving model training efficiency and performance.

## How to Use

To test the application, click this link: [Malaysia Sustainable Tourism Accommodation Predictor](https://sustainableota-895nmbahjpzb8cimfmgkkt.streamlit.app/)

[webapp-demo](https://github.com/user-attachments/assets/3425572b-7129-49e9-b268-0ba3cccbf9ce)

## Acknowledgement
- Ministry of Tourism, Arts & Culture (MOTAC)
- Tourism Malaysia
- Hoffmann, F. J., Braesemann, F., & Teubner, T. (2022). Measuring sustainable tourism with online platform data. EPJ Data Science, 11, 41. [https://doi.org/10.1140/epjds/s13688-022-00354-6](https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-022-00354-6)
- Brownlee, J. (2020). How to use RFE for feature selection. In J. Brownlee (Ed.), Data preparation for machine learning (pp. 175–189). [https://machinelearningmastery.com/data-preparation-for-machine-learning/](https://machinelearningmastery.com/data-preparation-for-machine-learning/)
- Brownlee, J. (2020). Imbalanced Classification with Python. [https://machinelearningmastery.com/imbalanced-classification-with-python/](https://machinelearningmastery.com/imbalanced-classification-with-python/)

