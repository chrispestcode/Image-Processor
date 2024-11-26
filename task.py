#!/usr/bin/env python3
import pika, sys

message = ' '.join(sys.argv[1:]) or "Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue='task_queue',
                    durable=True)
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                      ))
print(" [x] Sent %r" % message)

# sudo rabbitmqctl list_queues
# rabbitmqctl add_user lawson L497!
connection.close()