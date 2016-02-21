'''
Created on 21 Feb 2016

@author: David
'''
import lxml
import urllib2
import re

rssURL = "http://backfeed.strangecode.com/url/http://feeds.reuters.com/reuters/financialsNews"
content = urllib2.urlopen(rssURL).read()
print content

with open("Output.txt", "w") as text_file:
    text_file.write(content)


def getSentiments2(inputURL):
    base = "https://loudelement-free-natural-language-processing-service.p.mashape.com/nlp-text/?text="
    apikey = "mA332QeYvfmsh19cAuqEGx67OBuAp16FrZujsnNzRV8946Wge9"
    sendURL = base + "?apikey=" + apikey + "&url=" + inputURL 

    


def getSentiments(inputURL):
    base = "http://gateway-a.watsonplatform.net/calls/url/URLGetTextSentiment"
    apikey = "3aa994664428058396bb0b21c94b776f8c577da7"
    sendURL = base + "?apikey=" + apikey + "&url=" + inputURL 
    content = urllib2.urlopen(sendURL).read()
    print content
    for line in content.split("\n"):
        #print "line: " + line
        if not line or not re.match(r"\s*<score", line):
            continue
        matchRes = line.split(">")[1].split("<")[0]
        return float(matchRes)
    
    
inputURL1 = "http://money.cnn.com/2016/01/12/investing/markets-sell-everything-cataclysmic-year-rbs/"
inputURL2 = "http://www.profitconfidential.com/stock/google-stock-is-this-alphabet-inc-s-next-big-thing/"
#print getSentiments(inputURL2)
