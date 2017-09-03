import praw
import time
import sys
import random
import operator
from urllib.parse import quote_plus
from textblob import TextBlob, Word

r = praw.Reddit(user_agent="Testing Tutorial")
r.login("hozier_daddy", "metalslugs")
cache = []
def askBot():
	subreddit = reddit.subreddit('AskReddit')
	for submission in subreddit.stream.submissions():
		if len(submission.title.split()) < 10:
        	questions = ['what is', 'who is', 'what are']
			lower_title = submission.title.lower()
			for phrase in questions:
			    if phrase in lower_title:
			        reply_template = '[Let me google that for you](http://lmgtfy.com/?q={})
					url_title = quote_plus(submission.title)
					reply_text = reply_template.format(url_title)
					print('Replying to: {}'.format(submission.title))
					submission.reply(reply_text)
			        break
def summarybot():
	subreddit = r.get_subreddit("test")
	s = "This submission is about"
	cache = ()
	for submission in subreddit.stream.submissions():
		if submission.id not in cache:
			blob = TextBlob(submission.selftext)
			nouns = {}
			parts = ("NN", "PRP", "NNP")
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
			submission.add_comment(s)
			print s
			cache.append(submission.id)

def wordbot():
	cache = ()
	words_to_match = ['your', 'youre', "you're"]
	subreddit = r.get_subreddit("test")
	comments = subreddit.get_comments(limit=30)
	for comment in comments:
		comment_text = comment.body.lower()
		mis = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and mis:
			comment.reply('Your grammar sucks')
			cache.append(comment.id)
	time.sleep(10)
def happybot():
def disagree_bot():
def correct_bot():
	print("subreddit")
	cache = ()
	subreddit = r.get_subreddit("test")
	comments = subreddit.get_comments(limit=30)
	for comment in comments:
		comment_text = comment.body.lower()
		text = TextBlob(comment_text)
		words = text.words
		for word in words:
			info = word.spellcheck()
			if comment.id not in cache and info[0][0] != word and info[0][1] > 0.9:
				print("corrected")
				print(word + info[0][0])
				comment.reply('*' + info[0][0])
				cache.append(comment.id)
				time.sleep(5)
while True:
	correct_bot()
	time.sleep(10)