import snscrape.modules.twitter as sntwitter
import pandas as pd

query  = "python"
query1 = "(from:elonmusk) until:2020-01-01 since:2010-01-01"
tweets = []
limits = 100



for t in sntwitter.TwitterSearchScraper(query1).get_items():
    if(len(tweets)==limits):
        break
    else:
        tweets.append([t.date,t.user.username,t.content])

df = pd.DataFrame(tweets,columns=['Date','User','Tweet'])

print(df)
