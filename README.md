# TV Shows Analysis Portfolio

Comprehensive data analytics portfolio project analyzing 2,500+ TV shows using Python, pandas, and data visualization.

## Project Overview

This project analyzes a dataset of 2,565 television programs to uncover patterns in ratings, genres, networks, and content types. After cleaning (removing 46 duplicates), the final dataset contains 2,519 shows across 17 features.

### Business Questions

1. What are the highest-rated TV shows and what characteristics do they share?
2. How do different genres compare in terms of quantity and quality?
3. Which networks produce the most and best-rated content?
4. What is the relationship between show longevity and ratings?
5. How do different content types (scripted, reality, animation) perform?

## Key Findings

- **Average rating**: 7.34/10 (median 7.50); highest-rated show is Breaking Bad (9.2)
- **Genre breakdown**: Drama (40.3%, avg 7.54), Comedy (27.9%, avg 7.21), Action (16.9%, avg 7.46)
- **Top networks by volume**: ABC (204), NBC (173), CBS (133)
- **Top networks by quality**: Showtime (7.86 avg), BBC One (7.74), HBO (7.72)
- **Content types**: Scripted (59.8%, avg 7.48), Reality (18.7%, avg 6.39), Animation (8.3%, avg 7.29)
- **Quality vs. quantity**: Weak correlation between show length and ratings — quality beats quantity

## Dataset

- **Source**: [2500 TV Shows Dataset on Kaggle](https://www.kaggle.com/datasets)
- **Records**: 2,565 raw / 2,519 after cleaning
- **Features**: Name, Rating, Network, Genres, Runtime, Episodes, Total Seasons, Type, Language, Premiere Date, and more

> The raw CSV is not included in this repo due to size. Download it from the source above and place it in a `2500 tv shows dataset/` folder.

## Project Structure

```
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── clean_tv_shows.py              # Data cleaning & deduplication script
├── TV_Shows_Analysis_Portfolio.ipynb  # Full EDA notebook with visualizations
└── 2500 tv shows dataset/         # (not tracked) Place raw CSV here
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Jack-Fernandes781/tv-shows-analysis-portfolio.git
   cd tv-shows-analysis-portfolio
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the dataset and place the CSV in `2500 tv shows dataset/`.

4. Run the cleaning script:
   ```bash
   python clean_tv_shows.py
   ```

5. Open the notebook:
   ```bash
   jupyter notebook TV_Shows_Analysis_Portfolio.ipynb
   ```

## Sample Visualizations

The notebook includes charts covering:
- Rating distributions and top-rated shows
- Genre comparison (count and average rating)
- Network analysis (volume vs. quality)
- Content type performance
- Show longevity vs. ratings correlation

## Technologies Used

- **Python 3**
- **pandas** — data manipulation and analysis
- **NumPy** — numerical operations
- **Matplotlib** — static visualizations
- **Seaborn** — statistical plots
- **Jupyter Notebook** — interactive analysis environment

## Limitations & Future Work

- Dataset is a snapshot; no time-series tracking of rating changes
- Genre categories are broad; sub-genre analysis could reveal deeper patterns
- Streaming platform data (Netflix, Hulu, etc.) could be added for comparison
- Sentiment analysis of viewer reviews would complement numerical ratings
