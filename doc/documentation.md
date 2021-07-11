## **Argument generation**
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


## **Similarity matrix**
In order to calculate the cosine similarity matrix, we do the following:  

In general, if we find non-ascii text in the given text (e.g., there is 'λύνεται έτσι μια διοικητική, νομική' in the validation data set), we ignore this non-ascii text. 
We decided this because otherwise, the function that calculates the cosine similarity cannot deal with these none-ascii characters.  

Then, each sentence of an argument is stripped off all its special characters.  
Stop words are removed using the nltk stopwords module. 
The PorterStemmer class is then used to retrieve the stemmed version of each sentence. 
Using sklearn library, the TFIDF matrix for each stemmed sentence of an argument is used as input to compute the cosine similarity of each sentence pair and the values are saved into a multidimensional array.



### **Validation and Evaluation**

To evaluate the performance of our argument generation approach, we are calculating BLEU-1, BLEU-2 and BLEU score.

```
BLEU-1: 0.126078
BLEU-2: 0.553019
BLEU:   0.371241
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


### **How to run**

```bash 
python args-assessor.py
```

#### **Evaluation script**
```bash
python eval.py --true val-data-prepared.json --predictions predictions.json
```
