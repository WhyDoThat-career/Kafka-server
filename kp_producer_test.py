from kafka import KafkaProducer 
from json import dumps 
import time 
import logging
logging.basicConfig(level=logging.INFO)
producer = KafkaProducer(acks=0, 
#                          compression_type='gzip', 
                         api_version=(2,3,0),
                         bootstrap_servers=['52.78.62.228:9092'], 
                         value_serializer=lambda x: dumps(x).encode('utf-8'))
start = time.time() 
# for i in range(10): 
#     data = '{}'.format(i)
#     print(data)
producer.send('test_topic',{'data':1}) 

producer.flush()
# print("elapsed :", time.time() - start)