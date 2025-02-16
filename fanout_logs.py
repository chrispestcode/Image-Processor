#!/usr/bin/env python3

import pika,sys

message = ' '.join(sys.argv[1:]) or "Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.exchange_declare(exchange='logs',
                        exchange_type='fanout')
queue_name = channel.queue_declare(queue='', exclusive=True)
channel.queue_bind(exchange='logs',
                    queue=queue_name.method.queue)
channel.basic_publish(exchange='logs',
                        routing_key='',
                        body=message)
print(" [x] Sent %r" % message)
connection.close()

