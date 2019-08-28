import pandas as pd
from hdfs import InsecureClient
import os

client_hdfs = InsecureClient('http://' + "hadoop01.hadoop.com" + ':50070')

# # Creating a simple Pandas DataFrame
# liste_hello = ['hello1', 'hello2']
# liste_world = ['world1', 'world2']
# df = pd.DataFrame(data={'hello': liste_hello, 'world': liste_world})
# # print(df)


with client_hdfs.read('/tmp/helloworld.csv', encoding = 'utf-8') as reader:
    df = pd.read_csv(reader, index_col=0)
    print(df)

# import pymongo
# import pandas as pd
# from datetime import datetime
# conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@jiot.jiguem.com:27017/default_db?authSource=jiot_log')
# db = conn.get_database('jiot_log')
# collection = db.get_collection('ha_sensors_state')
#
# # convert your date string to datetime object
# start = datetime.now()
# df = pd.DataFrame(list(collection.find({})))
# print(df)
#
# # Writing Dataframe to hdfs
# with client_hdfs.write('/tmp/helloworld.csv', encoding='utf-8') as writer:
#     df.to_csv(writer)
#
# end = datetime.now()
# print(end - start)