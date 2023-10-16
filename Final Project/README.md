# Brief Summary:

This report provides an analysis of the dataset "amazon_alexa.csv" containing customer reviews of Amazon Alexa products. The main objective is to perform sentiment analysis on the reviews using various machine learning algorithms and natural language processing techniques.

# Exploratory Data Analysis (EDA):

The dataset contains 3150 entries and 5 columns, consisting of features such as 'rating', 'date', 'variation', 'verified_reviews', and 'feedback'.

Initial data examination revealed 715 duplicate values and no missing values.

The 'rating' column indicates a range of 1 to 5, with the majority of reviews having a rating of 5.

The 'feedback' column indicates positive and negative feedback, with significantly more positive reviews than negative ones.

# Data Preprocessing:

Data cleaning steps involved removing null values and duplicates from the dataset.

Text data was preprocessed by removing punctuation and stop words using the NLTK library.

# Machine Learning Algorithms:

# Naive Bayes Classifier:

Achieved an accuracy of 93% with precision, recall, and F1-score indicating a good performance for positive feedback classification.
# Logistic Regression:

Demonstrated an accuracy of 92% with lower precision for negative feedback, indicating a slight bias in the model's performance.

# Sentiment Analysis:

Utilized the TextBlob library to conduct sentiment analysis on specific reviews.

Identified a negative sentiment for a review that contained the text "Not much features."

# Conclusion:

The analysis showcases the effectiveness of Naive Bayes and Logistic Regression models in classifying sentiment from customer reviews. However, further improvements could be made to handle negative feedback more accurately. Additionally, the sentiment analysis provides a quick understanding of the general tone of individual reviews.

These insights could be valuable for businesses to gauge customer satisfaction and make informed decisions to enhance their product and service offerings.




