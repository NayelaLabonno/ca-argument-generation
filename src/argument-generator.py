import pandas as pd
import json
import numpy as np
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk import tokenize
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import networkx as nx

stop_words = stopwords.words('english')
summarize_text = []


def text_preprocess(text):
    text = re.sub('[^A-Za-z0-9?]', ' ', text)
    return text

def build_similarity_matrix(arg, stop_words):
    # Create an empty similarity matrix
    
    similarity_matrix = np.zeros((len(arg), len(arg)))
 
    for idx1 in range(len(arg)):
        for idx2 in range(len(arg)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(arg[idx1], arg[idx2], stop_words)
    return similarity_matrix


def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    #print(1 - cosine_distance(vector1, vector2))
    return 1 - cosine_distance(vector1, vector2)

#  ****Prepare Test and Train datasets****

argument_train=[]
text_train=[]
arg_train=[]
tokenized_train= []
dataset_train= pd.read_json('/argument-generation/train_data.json')
#print(dataset_train[:5])
argument_train=dataset_train['argument'][:5].to_list() ##index upto 5 for testing, change later
#print(argument_text[:5])

for a in argument_train:
    text_train.append(tokenize.sent_tokenize(a)) #splits argument into a list of sentences
for i in range(0, len(text_train)):
    for x in text_train[i]:
        arg = text_preprocess(x)
        arg_train.append(arg)
for arg in arg_train:    
    tokenized_train.append([word_tokenize(arg.lower())]) ##contains tokenized sentences

for arg in arg_train:  
    sentence_similarity_martix_train = build_similarity_matrix(arg, stop_words)
   

argument_test=[]
text_test=[]
arg_test=[]
tokenized_test= []
dataset_test = pd.read_json('/argument-generation/valid_data.json')
argument_test=dataset_train['argument'][:5].to_list() ##index upto 5 for testing, change later

for a in argument_test:
    text_test.append(tokenize.sent_tokenize(a)) #splits argument into a list of sentences
for i in range(0, len(text_test)):
    for x in text_test[i]:
        arg = text_preprocess(x)
        arg_test.append(arg)
for arg in arg_test:    
    tokenized_test.append([word_tokenize(arg.lower())]) ##contains tokenized sentences

for arg in arg_test:  
    sentence_similarity_martix_test = build_similarity_matrix(arg, stop_words)


# Rank sentences in similarity martix
#sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
#scores = nx.pagerank(sentence_similarity_graph)

# Sort the rank and pick top sentences
#ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(arg)), reverse=True)    
#print("Indexes of top ranked_sentence order are ", ranked_sentence)    

#for i in range(len(arg)):
##  summarize_text.append(" ".join(ranked_sentence[i][1]))

# Output the summarize text
#print("Summarize Text: \n", ". ".join(summarize_text))



