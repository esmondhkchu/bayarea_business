# Yelp
Analysis of Bay Area restaurants. <br>
Total restaurants collected: 19,223 <br>
Total reviews collected: 56,108

Data Source: <br>
Yelp Fusion: [API Link](https://www.yelp.com/fusion) <br>

## Exploratory Data Analysis

## Natural Language Processing Machine Learning Model
Recurrent Neural Network to learn customer's reviews and predict negative or positive.

## Directory Tree
Last Update: 1/3/2020
```bash
.
├── README.md
├── data
│   ├── all_businesses_info.csv
│   ├── all_reviews.csv
│   ├── bay_area_demography.csv
│   ├── cleaned_texts.csv
│   └── raw_businesses_data
│       ├── Alameda_CA_businesses_info.json
│       ├── Alameda_CA_reviews.json
│       │── ... all others CA cities businesses_info and reviews
├── data_analysis
│   └── NLP_model.ipynb
├── data_extraction
│   ├── bay_area_cities_data_extraction.ipynb
│   └── yelp_data_extraction.ipynb
├── data_wrangling
│   └── data_wrangling.ipynb
└── tools
    ├── data_tools.py
    └── yelp_fusion.py
```
