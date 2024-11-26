#!/usr/bin/env python3

import pika,sys,os,time
from datetime import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
queue_result = channel.queue_declare(queue='',
                    exclusive=True)
queue_name = queue_result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    start_time = time.time()
    print(f'Time start: {start_time}')
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    print(f'Time elapsed: {time.time()-start_time}')

channel.basic_consume(queue=queue_name,
                    on_message_callback=callback,
                    auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()




