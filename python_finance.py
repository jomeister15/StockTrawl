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


style.use('ggplot')
yf.pdr_override()

start = dt.datetime(2018,6,3)
end = dt.datetime(2018,6,4)
data = yf.download("MU", start, end)


print(data.head())
