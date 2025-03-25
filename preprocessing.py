import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from sklearn.model_selection import train_test_split

df = pd.read_csv('./Reviews.csv')
df = df[['Text', 'Score']]
df.rename(columns={'Text': 'review', 'Score': 'label'}, inplace=True)

df = df[df['label'] != 3]

df['label'] = df['label'].apply(lambda rating: 1 if rating > 3 else 0)

df.dropna(subset=['review'], inplace=True)
df.drop_duplicates(subset=['review', 'label'], keep='first', inplace=True)

pos_df = df[df.label == 1][:10000]
neg_df = df[df.label == 0][:10000]
df = pd.concat([pos_df, neg_df], ignore_index=True)
df = df.sample(frac=1).reset_index(drop=True)

plt.pie(df.label.value_counts(), labels=["1 (Positive)", "0 (Negative)"],
        colors=["yellowgreen", "lightskyblue"], startangle=90, autopct='%.1f%%')
plt.title("Sentiment Distribution")
plt.show()

df['review'] = df['review'].apply(lambda x: x.lower())
df['review'] = df['review'].apply(lambda x: re.sub(r'\d+', '', x))
df['review'] = df['review'].apply(lambda x: re.sub(r'[^\w\s]', ' ', x))
df['review'] = df['review'].apply(lambda x: x.strip())

x = df['review']
y = df['label']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(x_train)
x_train = tokenizer.texts_to_sequences(x_train)
x_test = tokenizer.texts_to_sequences(x_test)

max_review_length = 200
vocab_size = len(tokenizer.word_index) + 1

x_train = sequence.pad_sequences(x_train, maxlen=max_review_length)
x_test = sequence.pad_sequences(x_test, maxlen=max_review_length)

print("x_train shape:", x_train.shape)
print("x_test shape:", x_test.shape)
