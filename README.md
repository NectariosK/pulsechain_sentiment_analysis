# Pulsechain Sentiment Analysis

## Project Overview
A comprehensive sentiment analysis project focused on the Pulsechain cryptocurrency, leveraging social media data from Reddit and Twitter to understand community perception and trends.

### Key Features
- Web scraping from multiple social media platforms
- Advanced text preprocessing and cleaning
- Sentiment analysis using Natural Language Processing (NLP)
- Machine learning-based clustering of sentiments
- Visualization of sentiment trends

## Project Structure
- `Notebooks/`: Jupyter notebooks for data analysis and visualization
- `webscrapping.py`: Web scraping script for Reddit and Twitter
- `requirements.txt`: Project dependencies
- `reddit_data.csv`: Scraped Reddit comments
- `twitter_data.csv`: Scraped Twitter posts

## Technology Stack
- Python
- NLTK for natural language processing
- Pandas for data manipulation
- Scikit-learn for machine learning
- Tweepy for Twitter API
- PRAW for Reddit API

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup
1. Clone the repository
```bash
git clone https://github.com/NectariosK/pulsechain_sentiment_analysis.git
cd pulsechain_sentiment_analysis
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage
1. Configure API credentials in JSON files
2. Run web scraping
```bash
python webscrapping.py
```
3. Open Jupyter notebooks for analysis
```bash
jupyter notebook Notebooks/pulsechain_sentiment_analysis.ipynb
```

## Methodology
1. Data Collection
   - Scrape comments from Reddit and Twitter
   - Filter and preprocess text data
2. Sentiment Analysis
   - Tokenization
   - Stop word removal
   - Text cleaning
3. Machine Learning
   - K-Means clustering
   - Sentiment classification

## Roadmap
- [ ] Expand data sources
- [ ] Improve sentiment scoring
- [ ] Add real-time sentiment tracking
- [ ] Create interactive dashboard

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
[Specify your license here]

## Contact
Nectarios Kisiigha - [Your Email/Contact Info]
Project Link: https://github.com/NectariosK/pulsechain_sentiment_analysis
