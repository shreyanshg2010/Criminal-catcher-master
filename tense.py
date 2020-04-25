# -*- coding: utf-8 -*-
"""
@author: Shreyansh
"""
def getInfo(sent):
  from nltk import word_tokenize, pos_tag
  from nltk.tokenize import RegexpTokenizer
  tokenizer = RegexpTokenizer(r'\w+')
  text = tokenizer.tokenize(sent)
  tagged = pos_tag(text)
  future = [word for word in tagged if word[1] == "MD"]
  #print(future)
  #print(tagged)
  tense = {}
  tense["future"] = [word for word in tagged if word[1] == "MD"]
  tense["present"] = [word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]]
  tense["past"] = [word for word in tagged if word[1] in ["VBD", "VBN"]]
  tense["location"] = [word for word in tagged if word[1] in ["VB"]]
  #print(tense)
  time = {}
  time = [word for word in tagged if word[1] in ["NN"]]
  #print(time)
  return (tense,time)
