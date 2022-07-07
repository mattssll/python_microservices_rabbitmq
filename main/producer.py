import pika, json
from dotenv import load_dotenv
import os
load_dotenv()


params = pika.URLParameters(os.getenv('RABBIT_CLUSTER_URL'))


def publish(method, body):
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    properties = pika.BasicProperties(method)
    channel.close()
    connection.close()
        
