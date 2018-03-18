#retrieve_url_from_tweets

import pandas as pd
import json
import urllib
import csv



tweets_data_path = 'text_files/random_tweets/tweets_2202_1.txt'
tweets_csv_data_path = 'text_files/random_tweets/tweets_csv.csv'
finalList = []
with open(tweets_data_path, 'r') as file:
	myFields =  ['tweet_id','user_id', 'text', 'external_link', 'link', 'shares', 'likes', 'tweet_created_date']
	count = 0
	for line in file:
		try:
			tweet = json.loads(line)
			if tweet['place']['country_code'] == 'IN':
				if(tweet['extended_tweet']['entities']['urls']):
					for each_value in tweet['extended_tweet']['entities']['urls']:
						#for value1 in tweet['extended_tweet']['entities']['urls']:
						#for value2 in tweet['entities']['urls']:
						newList = [str(tweet['id_str']), str(tweet['user']['id_str']), tweet['extended_tweet']['full_text'].replace(';',''), each_value['expanded_url'] ,list(value['expanded_url'] for value in tweet['entities']['urls']) , tweet['retweet_count'], tweet['favorite_count'], tweet['created_at']]
						#list(value['expanded_url'] for value in tweet['extended_tweet']['entities']['urls']), list(value['expanded_url'] for value in tweet['entities']['urls'])
						finalList.append({myFields[i]:newList[i] for i in range(len(myFields))})
		except Exception as e:
			#print(e)
			continue

print(len(finalList))
df = pd.DataFrame(finalList)
df.index.name = 'row_id'
print(df)
print(count)
df.to_csv(tweets_csv_data_path)