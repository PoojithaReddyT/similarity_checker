import nltk
nltk.download('punkt')
import numpy as np
import gensim
from nltk.tokenize import word_tokenize, sent_tokenize
from django.shortcuts import render
from users.views import getfile1, getfile2, deletion

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize,sent_tokenize 
from difflib import SequenceMatcher


def percent(request):
    getfile1()
    getfile2()
    with open('1.txt') as file_1,open('2.txt') as file_2:
        file1_data = file_1.read()
        file2_data = file_2.read()
        X_list = word_tokenize(file1_data)
        Y_list = word_tokenize(file2_data)

        # sw contains the list of stopwords
        sw = stopwords.words('english')
        l1 =[];l2 =[]

        # remove stop words from string
        X_set = {w for w in X_list if not w in sw}
        Y_set = {w for w in Y_list if not w in sw}

        # form a set containing keywords of both strings
        rvector = X_set.union(Y_set)
        for w in rvector:
            if w in X_set: l1.append(1) # create a vector
            else: l1.append(0)
            if w in Y_set: l2.append(1)
            else: l2.append(0)
            c = 0

        # cosine formula
        for i in range(len(rvector)):
            c+= l1[i]*l2[i]
        cosine = c / float((sum(l1)*sum(l2))**0.5)
    if((cosine*100)<65): s='Acceptable value of percentage'
    else: s='Unacceptable value of percentage'

    deletion()

    return render(request, 'page3.html', {'data': cosine*100,'data2': s})
