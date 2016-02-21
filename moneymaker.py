import json
import re
import urllib
import urllib2
from urllib import urlopen
import feedparser
keywords=['Yahoo', 'Japan', 'Clinton']
from urllib2 import urlopen
diffbot= 'http://api.diffbot.com/v3/article?token=b79f68d0e3a98c014cae87196036f80b&url='
words={'S&P'}
d = feedparser.parse('http://mf.feeds.reuters.com/reuters/UKBankingFinancial')
links=[]
from urlparse import urlparse


for x in d['entries']:
    itr= x['links'][0]['href']
    links.append(itr)
    itr=itr[:itr.rfind('?feedType')]
    s = diffbot +itr
    print s
    html = urllib2.urlopen(s)
    text =html.read()
    text=text[text.rfind('text')+6:len(text)-3]
    if any(k in text for k in keywords):
        print text
