import praw
import numpy
import re
import sys
from collections import Counter

class Post:
	def __init__(self):
		self.ticker = "yo"
		self.comment = "ok"
		self.score = 0


reddit = praw.Reddit(client_id='GCjpdb-78ljIQg',
	             client_secret='VZJL5_pkHuFIKcZE7gC_5r7iRhk',
		     password='solaris15',
	             user_agent='testguyman',
		     username='opsanun')



callarray = [0]*0
print ("done")
m = 0
for submission in reddit.subreddit('wallstreetbets').search("Daily Discussion", sort='relevance', syntax='lucene', time_filter='day'):
	
	if submission not in callarray:
		callarray.append(submission)
		print (submission.title)

	
	
	if submission not in callarray:
		callarray.append(submission)
		print (submission.title)
	else:
		m = m + 1
for submission in reddit.subreddit('wallstreetbets').search("DD", sort='relevance', syntax='lucene', time_filter='day'):
	
	
	if submission not in callarray:
		callarray.append(submission)
		print (submission.title)
	else:
		m = m + 1


i = 0
print ("searching")
keywords = ["call", "moon", "bullish", "calls" "bull"]
keyword = ["put", "crash", "tumble", "bearish", "puts", "bear"]
bullish = [0]*0
bearish = [0]*0
test = [0]*0
test1 = [0]*0
test2 = [0]*0
test3 = [0]*0
newbearish = [0]*0

nogos = ["DD", "ATH", "I", "So I", "OTM", "ITM", "My", "A", "So", "TF", "WHY", "LOL", "No", "Leap", "Leaps", "Go", "Up", "It", "WSB", "WSB DD", "YOLOS", "If", "LMAO", "RIP", "IV", "Or", "Is", "ER", "REWARDS", "Ok", "FOMO", "DOJ", "NYC", "FDs", "Of", "OTM FDs", "We", "Yo", "Im", "At", "Do", "Su", "My", "To" ]

for j in callarray:
	j.comments.replace_more(limit=0)
	if j not in test2:
		for k in keywords:
			if k in j.selftext:
				print (j.selftext)
				print (k)
				matches = re.findall(r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)", comment.body)
				for x in matches:
					a = Post()
					if x in nogos:
						print ("l")
					else:
						a.ticker = x
						a.comment = j.selftext
						a.score = j.score
						bullish.append(a)
						test.append(x)
						test2.append(j)
				

	for comment in j.comments:
			for k in keywords:
				if k in comment.body:
					print (comment.body)
					print (k)
				
					matches = re.findall(r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)", comment.body)
					for x in matches:
						a = Post()
						if x in nogos:
							print ("l")
					
						else:
							a.ticker = x
							a.comment = comment.body
							a.score = comment.score
							bullish.append(a)
							test.append(x)
							test2.append(comment)
							



print ("searching for bears")				

for j in callarray:
	j.comments.replace_more(limit=0)
	for k in keyword:
			if k in j.selftext:
				print (j.selftext)
				print (k)
				
				matches = re.findall(r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)", comment.body)
				for x in matches:
					a = Post()
					if x in nogos:
						print ("nogo")
					else:
						a.ticker = x
						a.comment = j.selftext
						a.score = j.score
						bearish.append(a)
						test1.append(x)

	for comment in j.comments:
		for k in keyword:
			if k in comment.body:
				print (comment.body)
				print (k)

				matches = re.findall(r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)", comment.body)
				for x in matches:
					a = Post()
					if x in nogos:
						print ("nogo")
					else:
						a.ticker = x
						a.comment = comment.body
						a.score = comment.score
						bearish.append(a)
						test1.append(x)
print ("--------")
z = 0
b = 0
b = (len(bullish) - 1)
p = 0
v = 0

remove = Post()
remove.ticker = "AHH"
remove.score = 0
remove.comment = ""

while p < len(bullish):
	for x in range(1, b):
		v = 1
		if bullish[b].comment == bullish[b-x].comment and bullish[b].ticker == bullish[b-x].ticker:
			print ("deleting")
			bullish[b] = remove
	b = b - 1
	p = p + 1

newbullish1 = [0]*0

for x in range(1, len(bullish) - 1):
	if bullish[x].ticker != "AHH":
		newbullish1.append(bullish[x])



z = 0
b = 0
b = (len(bearish) - 1)
p = 0
v = 0


while p < len(bearish):
	for x in range(1, b):
		v = 1
		print(x)
		print(b)
		if bearish[b].comment == bearish[b-x].comment and bearish[b].ticker == bearish[b-x].ticker:
			print ("deleting")
			bearish[b] = remove
			
	b = b - 1		
	p = p + 1

newbearish1 = [0]*0

for x in range(1, len(bearish) - 1):
	print (x)
	if bearish[x].ticker != "AHH":
		newbearish1.append(bearish[x])



print ("bullish")
print (test)
print ("bearish")
print (test1)
print ("")

z = 0
##while z < len(bullish):
##	print (bullish[z].ticker)
##	print (bullish[z].comment)
##	print (bullish[z].score)
##	print ("")
##	print ("------------")
##	print ("")
##	z = z + 1

b = 0
newbullish = 0*[0]


while b < len(bearish):
	print (bearish[b].ticker)
	print (bearish[b].comment)
	print (bearish[b].score)
	print ("")
	print ("-----------")
	print ("")
	b = b + 1
##TODO: Machine Learning to determine sentiment of comment. Improve algorithm
z = 0
while z < len(newbearish1):
	newbearish.append(newbearish1[z].ticker)
	z = z + 1

z = 0
while z < len(newbullish1):
	newbullish.append(newbullish1[z].ticker)
	z = z + 1

##newbearish is data, newbearish1 is ticker names

print (newbearish)
print (test1)

print ("")
print ("---------")
print (newbullish)
print (test)