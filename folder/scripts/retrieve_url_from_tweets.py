#retrieve_url_from_tweets

import pandas as pd
import json
import urllib
import csv



tweets_data_path = 'text_files/random_tweets/tweets_2202.txt'
tweets_csv_data_path = 'text_files/random_tweets/tweets_csv.csv'

with open(tweets_data_path, 'r') as file:
	myFields =  ['name', 'place', 'text', 'new_link', 'link']
	output = csv.DictWriter(open(tweets_csv_data_path, 'w'), fieldnames=myFields)
	output.writeheader()
	for line in file:
		try:
			tweet = json.loads(line)
			if tweet['place']['country_code'] == 'IN':
				if(tweet['extended_tweet']['entities']['urls']):
					for each_value in tweet['extended_tweet']['entities']['urls']:
						if each_value['url']:
							newList = [tweet['user']['name'], tweet['place']['country'] , tweet['extended_tweet']['full_text'], list(value['expanded_url'] for value in tweet['extended_tweet']['entities']['urls']), list(value['expanded_url'] for value in tweet['entities']['urls'])]
							output.writerow({myFields[i]:newList[i] for i in range(len(myFields))})
		except Exception as e:
			#print(e)
			continue


'''
tweets_data_path = 'text_files/random_tweets/tweets_2202.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
	try:
		tweet = json.loads(line)
		if(tweet['extended_tweet']['entities']['urls']):
			for each_vale in tweet['extended_tweet']['entities']['urls']:
				if each_vale['url']:
					tweets_data.append(tweet)
	except Exception as e:
		#print(e)
		continue
print(len(tweets_data))

tweets = pd.DataFrame()
tweets['user_name'] = list(map(lambda tweet: tweet['user']['name'], tweets_data))
tweets['text'] = list(map(lambda tweet: tweet['extended_tweet']['full_text'], tweets_data))
tweets['new_links'] = list(map(lambda tweet: list(value['expanded_url'] for value in tweet['extended_tweet']['entities']['urls']), tweets_data))
tweets['links'] = list(map(lambda tweet: list(value['expanded_url'] for value in tweet['entities']['urls']), tweets_data))

#print(tweets)

#for i in tweets['link']:
	#for j in i:
		#print(j)

tweets.to_csv('text_files/random_tweets/tweets_csv.csv', sep=',', encoding='utf-8')
'''
