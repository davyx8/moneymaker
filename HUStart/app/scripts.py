import urllib
import feedparser
import re

TAG_RE = re.compile(r'<[^>]+>')
		
def remove_tags(text):
    return TAG_RE.sub('', text)


def extractLinksTitles(keywords):
    diffbot= 'http://api.diffbot.com/v3/article?token=b79f68d0e3a98c014cae87196036f80b&url='
    d = feedparser.parse('http://mf.feeds.reuters.com/reuters/UKBankingFinancial')
    links=[]

    linkslist = []
    titlelist = []
    for x in d['entries']:
        itr= x['links'][0]['href']
        links.append(itr)
        itr=itr[:itr.rfind('?feedType')]
        s = diffbot +itr
        html = urllib.urlopen(s)
        text =html.read()
        text = text[text.rfind('text')+6:len(text)-3]
        if any(k in text for k in keywords):
            linkslist.append(itr)
            sum = remove_tags( x['summary'])
            # print sum
            titlelist.append(sum)

    return [linkslist,titlelist]