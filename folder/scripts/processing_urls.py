import pandas as pd
import newspaper
import time
from date_extractor import extractArticlePublishedDate


start = time.time()
tweets_csv_data_path = 'text_files/random_tweets/tweets_csv.csv'

titleList=[]
authorList=[]
dateList=[]
df = pd.read_csv(tweets_csv_data_path)
for x,y in zip(df['external_link'].values, df['row_id'].values):
	try:
		first_article = newspaper.Article(url=x)
		first_article.download()
		first_article.parse()
		title = first_article.title
		print("Title extracted")
		author = first_article.authors
		print("Author extracted")
		date = extractArticlePublishedDate(x)
		print("Date extracted")
		titleList.append(title)
		authorList.append(author)
		dateList.append(date)
		#print(df.loc[int(y), 'external_link'])
	except Exception as e:
		print("Exception" ,e)
		if(title):
			titleList.append(title)
		else:
			titleList.append(None)
		if(author):
			authorList.append(author)
		else:
			authorList.append(None)
		if(date):
			dateList.append(date)
		else:
			dateList.append(None)
		continue
df.set_index('row_id')
df.insert(loc=8, column='title', value=titleList)
df.insert(loc=8, column='author', value=authorList)
df.insert(loc=8, column='published_date', value=dateList)
print(df)

df.to_csv('text_files/random_tweets/tweets_csv.csv')
print(time.time() - start)