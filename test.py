import praw
import time
import sys
import random
import operator
from textblob import TextBlob, Word
def summarybot():

	text = "I am a fucking cunt. Dogs like to suck bones. I used to have a dog. Trees do not have dogs. Lebron James has a dog. I have a dog. You used to call me on my cellphone. Late night when you needed my love. Dogs should be number one. Trees and I sohuld be on there too. Trees and I have fun. "
#	subreddit = r.get_subreddit("test")
	s = "This submission is about"
	blob = TextBlob(text)
	print(text)
	parts = ("NN", "PRP", "NNP")
	nouns = {}
	for word, tag in blob.tags:
		if tag in parts:
			if word.lower() not in nouns:
				nouns[word.lemmatize().lower()] = 1
			else:
				nouns[word.lemmatize().lower()] += 1
		elif tag == "NNS":
			temp = word.singularize().lower()
			if temp in nouns:
				nouns[temp] += 1
			else: 
				nouns[temp] = 1
		

	sorteddict = sorted(nouns.items(), key=operator.itemgetter(1), reverse=True)
	print(sorteddict)
	for i in range(3):
		word = Word(sorteddict[i][0])
		if word == 'i':
			word = "the author"
		else:
			word = word.pluralize()
		print(word)
		s += " " + word
		
	print(s)

def wordbot():
	cache = ()
	words_to_match = ['your', 'youre', "you're"]
	subreddit = r.get_subreddit("test")
	comments = subreddit.get_comments(limit=30)
	for comment in comments:
		comment_text = comment.body.lower()
		words = comment_text.split()
	#	mis = any(string in comment_text for string in words_to_match)
	#	if comment.id not in cache and mis:
	#		comment.reply('Your grammar sucks')
	#	cache.append(comment.id)
		
def my():
	text = "Your a cunt. You're dog. You're a dog. You're house. You're gay. You're fat. You're extremely strong. you're the man"
	blob = TextBlob(text)
	for sentence in blob.sentences:
		for word, tag in sentence.tags:
			print(word, tag)
my()