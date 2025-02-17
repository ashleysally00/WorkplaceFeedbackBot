
# Workplace Sentiment Analyzer Tool ![Bot Logo](https://raw.githubusercontent.com/ashleysally00/WorkplaceFeedbackBot/main/workplacebot300dpi.png)


*WorkplaceFeedbackBot:v1.0* </br>

The Workplace Sentiment Analyzer Tool uses the Reddit API to process discussions from work-related subreddits. It applies NLP and data analysis to track sentiment trends and career-related insights across industry discussions.

## Features

- **Fetches Reddit posts** from:  
  `r/jobs`, `r/careerguidance`, `r/humanresources`, `r/productivity`
- **Uses VADER Sentiment Analysis** to classify discussions as **positive, neutral, or negative**  
- **Visualizes sentiment trends** using **Matplotlib**  
- **Stores data in a CSV file** for further analysis

## Technical Overview
The methodology combines **web scraping** (via the Reddit API) and **text mining** (using NLP techniques) to analyze trends and sentiments related to work. For a more detailed explanation of this technical approach, check out [METHODOLOGY.md](./METHODOLOGY.md).

## Methodology

This project consists of two main phases:

1. **Data Collection (Web Scraping via API)**
   * Uses the **Reddit API (PRAW)** to fetch job-related posts and comments
   * Extracts structured text data, including **post titles, comments, upvotes, and timestamps**

2. **Text Analysis (Sentiment Mining)**
   * Performs **sentiment analysis** on the extracted text using **NLTK's VADER**
   * Classifies discussions as **positive, neutral, or negative**
   * Uses NLP techniques like **tokenization, lemmatization, and stopword removal** to refine the analysis

## Technologies Used
* **Web Scraping**: Reddit API (PRAW)
* **Text Mining & NLP**: NLTK, VADER Sentiment Analysis 
* **Data Processing**: pandas, NumPy
* **Visualization**: Matplotlib, Seaborn

## Reddit API Setup

### Reddit Developer Dashboard Screenshot

Here's a screenshot of the **Reddit Developer Dashboard** used to set up API credentials:

<img src="https://raw.githubusercontent.com/ashleysally00/WorkplaceFeedbackBot/main/red.png" width="580">

To use the Reddit API, you need to **create a Reddit Developer account** and generate API credentials.

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/ashleysally00/WorkplaceFeedbackBot.git
cd WorkplaceFeedbackBot
```

### 2. Create a Virtual Environment & Install Dependencies

```sh
python -m venv workbot_env
source workbot_env/bin/activate  # Mac/Linux
workbot_env\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3. Create a .env File & Add Reddit API Credentials

1. Create a .env file in the project folder.
2. Add the following, replacing with your own Reddit API credentials:

```sh
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
```

### 4. Run the Data Collection Script

```sh
python reddit_data_collector.py
```

This fetches Reddit posts and saves sentiment data to reddit_workplace_sentiment.csv.

### 5. Run Sentiment Analysis & Visualization

```sh
python reddit_sentiment_analysis.py
```

This analyzes sentiment trends and visualizes workplace discussions.

## Customizing Your Analysis

By default, WorkplaceFeedbackBot analyzes posts from the following subreddits:
```python
subreddits = ["careerguidance", "jobs", "humanresources", "productivity"]
```

### Change Subreddits
To analyze different communities, edit reddit_data_collector.py and update this list:

```python
subreddits = ["your_subreddit_here", "another_subreddit"]
```

### Adjust the Number of Posts
By default, the bot collects 20 posts per subreddit:

```python
for post in subreddit.hot(limit=20):  # Change 20 to a higher/lower number
```

To fetch more data, increase the limit (e.g., limit=50).
To get only recent discussions, change .hot to .new:

```python
for post in subreddit.new(limit=20)
```


## Example Output

| Subreddit       | Title                                        | Sentiment Score       |
|----------------|--------------------------------------------|----------------------|
| jobs          | "I just got promoted!"                      | **0.95** (Positive)  |
| jobs          | "I can't find a job 😞"                    | **-0.89** (Negative) |
| careerguidance | "How do I negotiate salary?"               | **0.45** (Neutral)   |

**Most Positive Post:** `"Struggling with motivation? Me too, but here’s what helped!"` (**0.9992**)  
**Most Negative Post:** `"I’m depressed because I can’t find a job."` (**-0.9786**)  

## Disclaimer
This repository provides guidance on how to build a tool using the official **Reddit API** for job sentiment analysis. It does not involve web scraping of HTML pages and fully complies with **Reddit’s Data API Terms**.  

Users are responsible for ensuring that their implementation follows Reddit’s **rate limits**, **terms of use**, and any applicable laws regarding data collection and analysis.  

For more information, refer to Reddit’s official [Data API Terms](https://www.redditinc.com/policies/data-api-terms).


