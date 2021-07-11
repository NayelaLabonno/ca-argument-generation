## **Argument Generation**
The aim of our argument generation approach is to generate statements in natural language that can be used as a conclusion of an argument which is given in natural language.


### **Preprocessing of Text Data**
During our preprocessing, we convert all given argumentative texts to lower case forms. 
Afterwards, the texts are further processed into a formal writing style to ensure uniformity. 
This is done by replacing contractions with their formal equivalents. 
Namely, we transform contractions that contain forms of "be" and "not" to their corresponding equivalents, as well as some other contractions. 
We know that by deciding to replace contractions of the form "she's" or "he's" with "she is" resp. "he is", we might make mistakes since these contractions can also be used to mean "she has" resp. "he has". 
We tried both versions and saw that they had no influence on the resulting score, therefore we decided to accept this possible source of mistakes, because differentiating between both meanings is very hard. 
It not only relies on the sentence structure, but can also be amiguous in several cases, since the participles that would indicate that the contraction means "has" can often also be used as adjective or as an addition to a verb (e.g. "she's moved to tears", "he's grown up now"), thus, introducing other sources for errors.
Therefore, also backed up by our scoring results, we decided to always replace "she's" resp. "he's" with "she is" resp. "he is".  

After these preprocessing steps, we tokenize arguments into sentence level using the nltk library.  


### **Similarity Matrix**
In order to calculate the cosine similarity matrix, we do the following:  

In general, if we find non-ascii text in any given text (e.g., there is ´`λύνεται έτσι μια διοικητική, νομική` in the validation data set), we ignore these non-ascii parts of the text and only consider the (remaining) ascii-parts. 
This means, if a text consists of both, ascii and non-ascii parts, we do not discard it completely, but we only use the ascii-part of it in further steps. 
We decided this because otherwise, the function that calculates the cosine similarity cannot deal with these non-ascii characters.  

Then, each sentence of an argument is stripped off all its special characters.  
Stop words are removed using the nltk stopwords module. 
The PorterStemmer class is then used to retrieve the stemmed version of each sentence. 
Using sklearn library, the TFIDF matrix for each stemmed sentence of an argument is used as input to compute the cosine similarity of each sentence pair and the values are saved into a multidimensional array.  


### **Generate Conclusion**
Based on the reasoning given by Alshomary et al. 2020 [1], we decided to use a very similar, **extractive summarization** approach. 
Our approach is a graph-based and ranking-based approach. 
For this, we extract a graph based on the cosine similarity matrix and then calculate the PageRank of its nodes using `networkx.pagerank`. 
This is done to rank the sentences by their importance of representing the core of the arguments. 
Then, we use the top `n` sentences with the highest PageRank score and use these as a summary of the given argument (or, in case that `n` is larger than the number of sentences for the argument, we use the number of sentences of the argument).  

We tried different values for `n`, namely 1, 2 and 3. 
We decided against using the top 3 sentences as a summary for the argument because of the given arguments many do not contain many sentences (often: 2-4 sentences). 
This then often results in returning the complete argument as a summarization, which is obviously not the aim of our task. 
For the decision whether to use the top 2 sentences, as suggested in PAPER versus using only the 1 highest-ranking sentence, we compared the resulting BLEU scores. 
For top 2 we received the following scores: 
```
BLEU-1: 0.13244589770119441
BLEU-2: 0.6052621879897253
BLEU:   0.40231336204959456
```
In contrast to this, the results where better when using the top 1 sentence:
```
BLEU-1: 0.1385736124232639
BLEU-2: 0.6147962692497115
BLEU:   0.41094337139299003
```
Therefore, we decided to use only the one sentence with the highest ranking as a summary of the argument.  

**Please note** that one advantage of our approach is, that, since we are only extracting the most representative sentence of each argument, we do not need a pre-trained model or use a trained model at all. 
In fact, we are not using the training data. 
Therefore we are not submitting a trained model, since it does not exist and is not necessary for our approach. 
Our approach works directly on the data for which a conclusion is to be generated.

### **Validation and Evaluation**

To evaluate the performance of our argument generation approach, we are calculating BLEU-1, BLEU-2 and BLEU score:

```
BLEU-1: 0.1385736124232639
BLEU-2: 0.6147962692497115
BLEU:   0.41094337139299003
```

## **TODO - change EVERYTHING below s.t. it fits to this task**

### **Requirements**

Required libraries:

* nltk~=3.6.2
* pandas~=1.2.4
* numpy~=1.20.3
* tqdm~=4.61.1
* scikit-learn~=0.24.2
*  alt-profanity-check~=0.24.0
* json
* os
* re
* time
* datetime

Note that even though the installation of `alt-profanity-check`might state that it is not compatible with `scikit-learn 0.24.2` (this version is required by another of the used libraries), the program still runs using the libraries listed above. 


### **How to Run**

```bash 
python args-assessor.py
```

#### **Evaluation Script**
```bash
python eval.py --true val-data-prepared.json --predictions predictions.json
```

### **References**
[1] Alshomary et al. 2020, Extractive Snippet Generation for Arguments
