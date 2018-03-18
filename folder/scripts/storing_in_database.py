import MySQLdb
import pandas as pd
import datetime
from dateutil.parser import parse


df = pd.read_csv('text_files/random_tweets/tweets_csv.csv')
df.index.name= 'row'
print(df)

 
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="mysql",     # password
                     db="trial")   # name of the database


create_query = "create table TWEET_DATA (article_id int PRIMARY KEY AUTO_INCREMENT, tweet_id varchar(20) NOT NULL, user_id varchar(20) NOT NULL, tweet_date datetime NOT NULL, tweet_text text NOT NULL, internal_link text, article_link varchar(255), title text,	author text,	published_date datetime, likes int, shares int, UNIQUE(tweet_id, article_link));"


cur = db.cursor()
db.set_character_set('utf8mb4')
#cur.execute("Drop table TWEET_DATA;")
#cur.execute(create_query)
cur.execute("Delete from TWEET_DATA;")
cur.execute("ALTER TABLE TWEET_DATA AUTO_INCREMENT = 1")
cur.execute("ALTER TABLE trial.TWEET_DATA MODIFY COLUMN tweet_text text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;")

tweet_dt = datetime.date(2018, 1, 1)
pub_dt = datetime.date(2018, 1, 1)
insert_query = ""


for row in df['row_id']:
	tweet_id = str(df.loc[row, 'tweet_id'])
	user_id = str(df.loc[row, 'user_id'])
	tweet_date = df.loc[row, 'tweet_created_date']
	tweet_text = df.loc[row, 'text'].encode("utf-8", 'ignore').decode('utf-8','ignore')
	internal_link = df.loc[row, 'link']#.strip('[\'').strip('\']')
	article_link = df.loc[row, 'external_link']
	title = df.loc[row, 'title'].encode("utf-8", 'ignore').decode('utf-8','ignore')
	author = df.loc[row, 'author']#.strip('[\'').strip('\']')
	published_date = str(df.loc[row, 'published_date'])
	likes = str(df.loc[row, 'likes'])
	shares = str(df.loc[row, 'shares'])

	try:
		print(tweet_date)
		dt = parse(tweet_date)
		tweet_dt = dt.strftime('%Y-%m-%d %H:%M:%S')

		if(published_date != 'nan'):
			print(published_date)
			pub_dt = datetime.datetime.strptime(published_date[:19], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

		#print(tweet_dt, pub_dt)
		#print(insert_query)

		insert_query = "insert into TWEET_DATA values(NULL,"+ str(tweet_id) + ", "+ str(user_id) +", \""+str(tweet_dt)+"\", \""+tweet_text+"\", \""+str(internal_link)+"\", \""+str(article_link)+"\", \""+str(title)+"\", \""+str(author)+"\", \""+str(pub_dt)+"\", "+likes+", "+shares+");"
		print("Query",insert_query)
		cur.execute(insert_query)
		db.commit()
		print("commit done\n\n")
	except Exception as e:
		print("Query",insert_query)
		print("Exception", e, "\n\n")
		continue


#cur.execute("Drop table TWEET_DATA;")
#cur.execute(query)
#cur.execute("Delete from TWEET_DATA;")
#cur.execute("ALTER TABLE TWEET_DATA AUTO_INCREMENT = 1")
#cur.execute("insert into TWEET_DATA values(NULL, '2', '2', '2012-01-03 12:50:59', 'first tweet', 'www.eee.com', 'qwertyui', 'asdfghj', 'asdfghjdfgh', '2012-01-03 12:50:59', '2', '2');")
#db.commit()
#ALTER TABLE trial.TWEET_DATA MODIFY COLUMN title varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL;
db.close()