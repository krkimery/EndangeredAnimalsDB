import time
import json
import tweepy
from db_connection import *

API_KEY = 'KBXxG1cTxAPcDaUzvWZWoU1RM'
API_SECRET = 'jj3fdRkmyeZcxj6SCO0T3kYLaaMqqje0LUi0W5W6ylfqYKCnJE'
TOKEN_KEY = '244809142-A0YbyfuNrEZr5qxFzL8zvtosTkEm2A404dxK3eb3'
TOKEN_SECRET = 'iF5dVca8MiiffQaKR8Jci2Z4OQU61PA6V8KnTMIG1s5cw'

def get_api_instance():
  auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
  api_inst = tweepy.API(auth)
  return api_inst



def do_data_pull(api_inst):

  sql_query = "select continent_name from Continent"

  try: 
    conn = create_connection()
    db_cursor = conn.cursor()
    query_status = True
    try:
      db_cursor.execute(sql_query)  
    except pymysql.Error as error:
      print "execute error: ", error
    resultset = db_cursor.fetchall()

    for record in resultset:
      continent_name = record[0]
      #scientific_name = record[1]

      endangered_query = "(#endangered OR #endangeredspecies OR #extinct OR @endangered) AND "
      twitter_query = endangered_query + "'" + continent_name + "'"
      print "twitter_query: " + twitter_query
      twitter_cursor = tweepy.Cursor(api_inst.search, q=twitter_query, lang="en")

      for page in twitter_cursor.pages():
        for item in page:
          json_str = json.dumps(item._json)
          print "found a " + continent_name + " tweet"
          insert_stmt = "insert into Tweet(tweet_doc, continent_name) values(%s, %s)"
          run_prepared_stmt(db_cursor, insert_stmt, (json_str, continent_name))
          try:
            conn.commit()  
          except pymysql.Error as error:
            print "commit error: ", error

  except pymysql.Error as e:
    print "pymysql error"
  
  except tweepy.TweepError as twe:
    print "got a TweepError: " + twe.message
    if twe.message.endswith("429"):
      print "Rate limit error, stopping for 15 minutes"
      time.sleep(60*15)
      print "Finished waiting. Re-attempting do_data_pull"
      do_data_pull(api_inst)

api_inst = get_api_instance()
do_data_pull(api_inst)