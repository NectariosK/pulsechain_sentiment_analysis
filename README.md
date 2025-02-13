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
4. Push to the branch## Machine Learning Models

### Notebooks Overview
- [pulsechain_sentiment_analysis.ipynb](cci:7://file:///Users/nectarioskisiigha/Documents/GitHub/pulsechain_sentiment_analysis/Notebooks/pulsechain_sentiment_analysis.ipynb:0:0-0:0): Main analysis notebook
- [pulsechain_sentiment_analysis_Data_Collection.ipynb](cci:7://file:///Users/nectarioskisiigha/Documents/GitHub/pulsechain_sentiment_analysis/Notebooks/pulsechain_sentiment_analysis_Data_Collection.ipynb:0:0-0:0): Data collection and preprocessing
- [pulsechain_sentiment_analysis_classic_ML_models.ipynb](cci:7://file:///Users/nectarioskisiigha/Documents/GitHub/pulsechain_sentiment_analysis/Notebooks/pulsechain_sentiment_analysis_classic_ML_models.ipynb:0:0-0:0): Traditional Machine Learning Models
- [pulsechain_sentiment_analysis_Neural_Model.ipynb](cci:7://file:///Users/nectarioskisiigha/Documents/GitHub/pulsechain_sentiment_analysis/Notebooks/pulsechain_sentiment_analysis_Neural_Model.ipynb:0:0-0:0): Deep Learning Sentiment Analysis

### Classic Machine Learning Models
Our classic machine learning approach includes:
- Logistic Regression
- Support Vector Machines (SVM)
- Random Forest Classifier
- Naive Bayes
- K-Nearest Neighbors (KNN)

#### Model Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

### Neural Network Model
Our deep learning approach includes:
- Recurrent Neural Networks (RNN)
- Long Short-Term Memory (LSTM) networks
- Word Embedding techniques
- Sentiment classification using neural architectures

#### Neural Model Features
- Pre-trained word embeddings
- Sequence padding
- Dropout for regularization
- Binary and multi-class sentiment classification

### Model Comparison
We compare traditional ML models with neural network approaches to:
- Understand model performance
- Assess computational efficiency
- Evaluate sentiment prediction accuracy

### Preprocessing Techniques
- Text tokenization
- Stop word removal
- Lemmatization
- Feature vectorization
- Handling class imbalance

## Model Usage
To explore and run the models:
1. Navigate to the `Notebooks/` directory
2. Open the respective Jupyter notebooks
3. Run cells sequentially to understand the model training process

**Note:** Ensure all dependencies are installed before running the notebooks
5. Create a Pull Request

## License
MIT

## Contact
Nectarios Kisiigha
Project Link: https://github.com/NectariosK/pulsechain_sentiment_analysis
