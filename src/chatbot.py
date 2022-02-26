import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer();

intents = json.loads(open("../intents.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))
model=load_model('newmodel.h5')

def preprocess_sentence(sentence):
    '''
    Tokenize the sentence entered by user into words, delete punctuation signs and lemmatize
    '''
    ignore_letters = ['?', '!', '.', ',']
    sent_words=nltk.word_tokenize(sentence)
    sent_words=[lemmatizer.lemmatize(word) for word in sent_words if word not in ignore_letters]
    return sent_words
def bag_words(sentence):
    '''
    Create the bag of words representation of a sentence.
    That is, identify which words from our intents file are present in the users' sentence
    '''
    sent_words=preprocess_sentence(sentence)
    bag=np.zeros(len(words))
    for sw in sent_words:
        for i, word in enumerate(words):
            if word==sw:
                bag[i]=1
    return bag
def predict_class(sentence):
    '''
    Predict the class (intent) of a users' sentence
    '''
    bow=bag_words(sentence)
    res=model.predict(np.reshape(bow, (1, len(bow))))[0]
    err_border=0.2
    results=[[i, r] for i, r in enumerate(res)if r>err_border]
    #Sort by probability in reverse order
    results.sort(key=lambda x: x[1], reverse=True)
    return_list=[]
    for r in results:
        return_list.append({'intent':classes[r[0]], 'probability':str(r[1])})
    print(return_list)
    return return_list
def get_response(intents_list, intents_json):
    '''
    Generate a response of the bot, given the probable intents of a users and the list of all intents
    '''
    tag=intents_list[0]['intent']
    list_of_intents=intents_json['intents']
    for i in list_of_intents:
        if i['tag']==tag:
            result=random.choice(i['responses'])
            break
    return result
print("You can start talking to the bot now. If you want to stop the bot, type `stop`")
while True:
    message= input("")
    if message.lower()=='stop':
        break
    ints=predict_class(message)
    res=get_response(ints, intents)
    print (res)