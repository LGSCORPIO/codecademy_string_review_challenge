#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:17:25 2021

@author: lilygoodyersait
"""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here == return number od unique english characters in a word:
def unique_english_letters(word):
    a1=[]
    for i in letters:
        if i in word:
            a1.append(i)
    return len(a1)
     
unique_english_letters("word")

###ways to count number of times a character'x' occurs in 'word'

def count_char_x(word,x):
  b1=word.count(x)
  return b1
count_char_x("word", "w")

def count_char_x(word,x):
  b1=[i for i in word if i == x]
  return len(b1)


def count_char_x(word,x):
  b1=[]
  for i in word:
      if i == x:
          b1.append(i)
  return len(b1)


### ways to count number of times multiple character string (x) occurs within another string (word)
def count_multi_char_x(word,x):
  c1=word.count(x)
  return c1

count_multi_char_x("wooordor", "or")

def count_multi_char_x(word,x):
  c1=word.split(x)
  return len(c1)-1

def multi_char_x(word,x):
 b1=[i for i in word if i == x]
 return len(b1)

### return substring between start and end, just reteurning the whole word if neither start or end are in word

def substring_between_letters(word, start, end):
    
    if start in word and end in word:
        start_index=word.find(start)
        end_index=word.find(end)
        return word[start_index +1: end_index]
    if start not in word and end in word:
        end_index=word.find(end)
        return word[:end_index]
    if start in word  and end not in word:
        start_index=word.find(start)
        return word[start_index +1:]
    else:
        return word

substring_between_letters("word", "w","d")
substring_between_letters("word", "p","k")


### Check every word in sentence == longer than integer x
def x_length_words(sentence,x):
  words=sentence.split()
  for i in words:
    if len(i) < x:
      return False
    else:
      return True


### check if name is in sentence
def check_for_name(sentence, name):
  lc=sentence.lower()
  lcname=name.lower()
  if lcname in lc:
    return True
  else:
    return False


def every_other_letter(word):
    new=word[::2]
    return new
            
every_other_letter("pink")

##reverse word
  
def reverse_string(word):
    return x[::-1]
    

### create spoonerism (swap first letters) with word1 and word2

def make_spoonerism(word1, word2):
  spooner1=word2[0] +word1[1:]
  spooner2 = word1[0] + word2[1:]
  spoonerfinal=spooner1 + " "+spooner2
  return spoonerfinal

###add exclamation until len == 20 (if already 20 == just return word)

def add_exclamation(word):
    word_length=len(word)
    exc_no=(20-word_length)
    exclamations= "!"  * exc_no
    new_word=word+exclamations
    return(new_word)
    
add_exclamation("cat")





