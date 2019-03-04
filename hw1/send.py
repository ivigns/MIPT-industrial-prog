#!/usr/bin/env python
import pika
import time
import random

print('Starting producer')
conn_params = pika.ConnectionParameters('rabbit', 5672, socket_timeout=10)
while True:
    try:
        connection = pika.BlockingConnection(conn_params)
        break
    except pika.exceptions.AMQPConnectionError:
        print('Cannot connect yet, sleeping 3 seconds')
        time.sleep(3)
channel = connection.channel()
print('Connection successful')

channel.queue_declare(queue='main_queue', durable=True)

while True:
    number = random.randint(0, 1000000)
    channel.basic_publish(exchange='',
                          routing_key='main_queue',
                          body=str(number),
                          properties=pika.BasicProperties(delivery_mode=2)
    )
    print('Sent number\t', number)
    time.sleep(random.randint(1, 15))

connection.close()
