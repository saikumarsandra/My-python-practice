
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from textblob import TextBlob


#dataset
amazonDataset=pd.read_csv(r"E:\My-python-practice\Day-13\AmazonData.csv")

# analysis review
amazonDataset['reviews.text']= amazonDataset['reviews.text'].astype(str)
#set polarity
polValue = lambda x: TextBlob(x).sentiment.polarity
amazonDataset['polarity'] = amazonDataset['reviews.text'].apply(polValue) 
#set bin
binValue = 50
#plot 
n, Numbins, patchValue = plt.hist(amazonDataset.polarity, binValue, facecolor='blue', alpha=0.5)
# title
plt.title('Polarity Score')
#x label
plt.xlabel('Polarity')
# y label
plt.ylabel('Number of Reviews')

plt.show();
# view
amazonDataset

# plot polarity
sns.boxenplot(x='reviews.good', y='polarity', data=amazonDataset)
plt.show();

# subjectivity
subValue = lambda x: TextBlob(x).sentiment.subjectivity
# apply subjectivity
amazonDataset['subjectivity'] = amazonDataset['reviews.text'].apply(subValue)
amazonDataset.sample(10)

# plot subjectivity vs polarity
sns.scatterplot(x='polarity', y='subjectivity', hue="reviews.good", data=amazonDataset)
#y label
plt.ylabel('Subjectivity')
#x label
plt.xlabel('Polarity')
#title
plt.title(' Subjectivity vs Polarity', fontsize=15)
plt.show();