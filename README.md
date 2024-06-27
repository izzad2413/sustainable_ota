# Predicting Sustainable Tourism in Malaysia's Accommodation Sector: A Machine Learning Approach

[![Static Badge](https://img.shields.io/badge/Back_to_Portfolio_Page-red?style=for-the-badge&logo=github&labelColor=black)](https://izzad2413.github.io/nazmirulizzadnassir.github.io/)

![Malaysia Sustainable Accommodation as of October 2023](https://github.com/izzad2413/sustainable_ota/assets/88135216/730a5322-90a8-455d-8eff-443df3b6348d)

## Table of Contents 

- [About Project](#about-project)
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Objective](#objective)
- [Built With](#built-with)
- [Data Source](#data-source)
- [Methodology](#methodology)
- [Result and Impact](#result-and-impact)
- [Challenges and Solutions](#challenges-and-solutions)
- [How to Use](#how-to-use)
- [License](#license)
- [Acknowledgement](#acknowledgement)

## About Project

This project simplifies and extends my master's thesis by deploying a machine learning model to predict sustainable practices in Malaysia's accommodation sector, enhancing tourism sustainability through data-driven insights.

## Overview

Tourism, a trillion-dollar industry, significantly impacts global Gross Domestic Product (GDP) and comprises about 7% of all exports, driving socio-economic development. However, it also contributes over 8% of global Green House Gases (GHG) emissions, with emissions rising annually (WTTC, 2023). Malaysia, a key tourist destination, leverages tourism as a vital economic driver, contributing RM 102 billion to GDP and creating 3.562 million jobs in 2019 (MOTAC, 2020). Emphasizing sustainable tourism, Malaysia's National Tourism Policy (NTP) aligns with the United Nation (UN) Sustainable Development Goals (SDGs), promoting ecotourism and responsible practices.

## Problem Statement

Rising environmental concerns in tourism emphasize the need for sustainable practices in accommodations, requiring a solid understanding of metrics and effective data-driven decision-making. The lack of precise data in Malaysia's accommodations sector is hindering the progress of sustainable tourism. This data gap hampers tourists' ability to make environmentally responsible choices and deprives providers and policymakers of crucial insights needed to promote sustainable practices.

## Objective

This project aims to develop and evaluate predictive models using machine learning techniques on data from an Online Travel Agent (OTA) platform to accurately classify tourist accommodations as sustainable, as indicated by the presence of a sustainability label. The objective encompasses:

- Identifying relevant features from the platform's data.
- Selecting appropriate machine learning algorithms.
- Assessing the models' performance in terms of accuracy, precision, recall, and other relevant metrics.

By leveraging OTA data, this project seeks to address current data collection challenges, enhance the reliability of sustainability indicators, and support informed decision-making for tourists, accommodation providers, and policymakers.

## Built With

- ![Python](https://img.shields.io/badge/Python-%233776AB?style=for-the-badge&logo=python&logoColor=3776AB&labelColor=black)
- ![Playwright](https://img.shields.io/badge/playwright-2EAD33?style=for-the-badge&logo=playwright&labelColor=black)
- ![Scikitlearn](https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&labelColor=black)
- ![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&labelColor=black)

## Data Source

- Data was meticulously gathered from the OTA platform, Booking.com.

## Methodology

- **Data Collection:** Using Python and Playwright as the main tools, the data was scraped from specified URLs for various locations. The algorithm extracted data from 25 accommodations per page, capturing 40 features each, over 40 pages, totaling 1000 accommodations per location. Covering 16 states and the federal territory of Malaysia, this yielded 17,866 raw samples. The data was stored in a CSV file for analysis and modeling.
- **Preprocessing:** 
- **Model Development:** 
- **Model Evaluation:**
- **Deployment:**

## Result and Impact

-
-
-

## Challenges and Solutions

- **Challenges in Web Scraping:** Enhance the robustness of web scraping tools by leveraging AI technologies such as ChatGPT to handle dynamic content and site structures effectively.
- **Complexity in Data Preprocessing:** Utilize AI, including tools like ChatGPT, to streamline and optimize the entire data preprocessing workflow, ensuring clean and well-structured datasets.
- **Handling Imbalanced Classes:** Implement SMOTE and employ suitable evaluation metrics to address and evaluate class imbalances effectively.
- **Managing a Large Number of Features:** Apply feature selection techniques to reduce dimensionality and select the most relevant features, improving model training efficiency and performance.

## How to Use

**1. Clone the Repository:**
```bash
git clone https://github.com/yourusername/sustainable_ota.git
```
**2. Navigate to the Project Directory:**
```bash
cd sustainable_ota
```
**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```
**4. Run the Model:**
```bash
python app.py
```

## License

-


## Acknowledgement

- [Hoffmann, F. J., Braesemann, F., & Teubner, T. (2022). Measuring sustainable tourism with online platform data. _EPJ Data Science 2022 11:1_, _11_(1), 1–21. https://doi.org/10.1140/EPJDS/S13688-022-00354-6](https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-022-00354-6)
- [Ministry Of Tourism, Arts & Culture (MOTAC)](https://www.motac.gov.my/)
- [Tourism Malaysia](https://www.tourism.gov.my/)
