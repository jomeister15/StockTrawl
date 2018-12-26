import praw
import numpy
import re
from psaw import PushshiftAPI
import sys
import pandas as pd
import datetime as dt
from datetime import datetime, timedelta
from collections import Counter
import csv
import praw
import numpy
import re
import sys
import yahoo_finance
from yahoo_finance import Share
from collections import Counter
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import datetime as dt
from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib import style




def get_data_from_date(date4):

	style.use('ggplot')
	yf.pdr_override()

	dateholder = dt.datetime(2000, 1, 1)


	class Post:
		def __init__(self):
			self.ticker = "yo"
			self.comment = "ok"
			self.score = 0
			self.date = dateholder
			self.sentiment = "oof"
			self.weight = 0
			self.mentions = 0
			self.Open = 0
			self.High = 0
			self.Low = 0
			self.Close = 0
			self.AdjClose = 0
			self.Volume = 0
	##'Open': self.Open, 'High': self.High, 'Low': self.Low, 'Close': self.Close, 'AdjClose': self.AdjClose, 'Volume': self.Volume, 
		def as_dict(self):
	   		return {'Ticker': self.ticker, 'score': self.score, 'Bull/Bear': self.sentiment, 'date': self.date, 'weight': self.weight, 'mentions': self.mentions}

	reddit = praw.Reddit(client_id='GCjpdb-78ljIQg',
		             client_secret='VZJL5_pkHuFIKcZE7gC_5r7iRhk',
			     password='solaris15',
		             user_agent='testguyman',
			     username='opsanun')

	api = PushshiftAPI(reddit)

	time_begin = date4
	time_end = time_begin + timedelta(days=1)

	start_epoch = time_begin

	end_epoch = time_end

	List1 = list(api.search_submissions(q='Daily Discussion Thread', after=start_epoch, before=end_epoch, subreddit='wallstreetbets', limit=10))
	List2 = list(api.search_submissions(q='DD', after=start_epoch, before=end_epoch, subreddit='wallstreetbets', limit=5))

	print (List1)
	print (List2)

	for y in List2:
		List1.append(y)

	callarray = List1

	print ("done")
	m = 0
	for submission in callarray:
		
			print (submission.title)


	i = 0
	print ("searching")
	keywords = ["call", "moon", "bullish", "calls", "bull", "long","ride"]
	keyword = ["put", "crash", "tumble", "bearish", "puts", "bear", "short"]
	##general_keywords = []

	##with open('list1.csv', 'r') as f:
	##	reader = csv.reader(f)
	##	for row in reader:
	##		general_keywords.append(row[0])

	##print (general_keywords)


	bullish = [0]*0
	bearish = [0]*0
	test = [0]*0
	test1 = [0]*0
	test2 = [0]*0
	test3 = [0]*0
	newbearish = [0]*0
	commentlist = [0]*0

	nogos = ["If I", "DD", "LEAPs", "ATH", "I", "Gj", "So I", "OTM", "ITM", "My", "A", "So", "TF", "WHY", "LOL", "No", "Leap", "Leaps", "Go", "Up", "It", "WSB", "WSB DD", "YOLOS", "YOLO", "FD", "If", "LMAO", "RIP", "IV", "Or", "Is", "ER", "REWARDS", "Ok", "FOMO", "DOJ", "NYC", "FDs", "Of", "OTM FDs", "We", "Yo", "Im", "At", "Do", "Su", "My", "To", "ETF", "IPAD", "BAC"]

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
						if x in nogos or len(x) > 5:
							print ("l")
						else:
							a.ticker = x
							a.comment = j.selftext
							a.score = j.score
							a.date = start_epoch
							a.sentiment = "bull"

							





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
								a.date = start_epoch
								a.sentiment = "bull"

								




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
							a.date = start_epoch
							a.sentiment = "bear"

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
							a.date = start_epoch
							a.sentiment = "bear"
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
		commentlist.append(newbearish1[z].comment)
		z = z + 1

	z = 0
	while z < len(newbullish1):
		newbullish.append(newbullish1[z].ticker)
		commentlist.append(newbullish1[z].comment)
		z = z + 1

	headers = ['date', 'time', 'somethingelse']


	if (len(newbearish1) == 0):
		return


	try:
		bearish_pd = pd.DataFrame([x.as_dict() for x in newbearish1])
		
	except:
		raise Exception("oh crap")

	bullish_pd = pd.DataFrame([x.as_dict() for x in newbullish1])

	##newbearish1 is data, newbearish is ticker names
	print (newbearish1[0].date)
	print (newbearish)
	print (test1)

	print ("")
	print ("---------")
	print (newbullish)
	print (test)
	print (bearish_pd.dtypes)
	print (bearish_pd)
	print (bullish_pd)

	final_array = [0]*0

	for x in newbullish1:
		for y in range(len(newbullish1)):
			if x.ticker == newbullish1[y].ticker:
				x.weight = newbullish1[y].score + x.weight
				x.mentions = x.mentions + 1

	for x in newbearish1:
		for y in range(len(newbearish1)):
			if x.ticker == newbearish1[y].ticker:
				x.weight = newbearish1[y].score + x.weight
				x.mentions = x.mentions + 1

	for x in newbullish1:
		for y in newbearish1:
			if x.ticker != y.ticker:
				if x not in final_array:
					final_array.append(x)
				else: 
					print ("l")
				if y not in final_array:
					final_array.append(y)
				else:
					print ("l")
			else:
				a = Post()
				a.ticker = x.ticker
				a.date = start_epoch
				a.weight = x.weight - y.weight
				a.mentions = x.mentions + y.mentions
				a.sentiment = "mixed"
				if a not in final_array:
					final_array.append(a)
	##for x in newbearish1:
	##	for y in range(len(newbearish1 - 1):
	##		if x.ticker == newbearish1[y].ticker:
	##			x.weight == newbearish1[y].score + x.weight




	start = start_epoch
	end = start_epoch
	ah = 0
	##make this final array
	list_of_tickers = [0]*0
	for x in final_array:
		if x.ticker not in list_of_tickers:
			try:
				ah = yf.download(x.ticker, start, end)
				x.Open = ah.iloc[0]['Open']
				x.Close = ah.iloc[0]['Close']
				x.AdjClose = ah.iloc[0]['Adj Close']
				x.High = ah.iloc[0]['High']
				x.Low = ah.iloc[0]['Low']
				x.Volume = ah.iloc[0]['Volume']
				list_of_tickers.append(x.ticker)
			except:
				print ("oh!")
				final_array.remove(x) 


	bearish_pd1 = pd.DataFrame([x.as_dict() for x in newbearish1])

	bullish_pd1 = pd.DataFrame([x.as_dict() for x in newbullish1])

	bullish_pd2 = bullish_pd1.drop_duplicates(subset=['Ticker'], keep="last")
	bearish_pd2 = bearish_pd1.drop_duplicates(subset=['Ticker'], keep="last")



	print (bullish_pd2)
	print (bearish_pd2)

	final_pd = pd.DataFrame([x.as_dict() for x in final_array])
	final_pd1 = final_pd.drop_duplicates(subset=['Ticker'], keep='last')
	print (final_pd1)
	final_pd1.to_csv(a, encoding='utf-8', index=False)


	##could be used as beginnings of sentiment analysis
	##wtr = csv.writer(open ('out.csv', 'w'), delimiter=',', lineterminator='\n')
	##for x in commentlist : wtr.writerow ([x])

	##where to pick up
	##EASY: combine stock financial info with this info
		##generate csv of comment data first then iterate through and update individually for each ticker? for loop based on date
	##HARD: sentiment analysis of comments for better bear/bull assignment
	##EASY: improve algorithms so many for loops
	##MEDIUM: better algorithm to determine importance of comment

y = 2018
m = 1

for d in range(1,30):
	date2 = dt.datetime(y, m, d)
	get_data_from_date(date2)