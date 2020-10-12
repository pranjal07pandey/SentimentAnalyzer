import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


text = open('mark.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
tokenized_words = word_tokenize(cleaned_text, 'english')

#adding stop words
# stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
#               "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
#               "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
#               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
#               "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
#               "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
#               "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
#               "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
#               "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
#               "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


#final words ready to be analyzed

final_words = []

for words in tokenized_words:
    if words not in stopwords.words('english'):
        final_words.append(words)

#format the emotions.txt file

emotion_list = []

with open('emotions.txt', 'r') as file:
    for line in file:
        clean_lines = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        words, emotions = clean_lines.split(':')

        if words in final_words:
            emotion_list.append(emotions)

print(emotion_list)
count = Counter(emotion_list)
print(count)

def vibe_analyzer(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    print(score)

    neg = score['neg']
    pos = score['pos']

    if pos > neg:
        print('Positive Sentiment')
    elif neg > pos:
        print('Negative Sentiment')
    else:
        print('Neutral Sentiment')

vibe_analyzer(cleaned_text)

plt.bar(count.keys(), count.values())
plt.show()
