#!/usr/bin/env python3

import pika,sys

sev = sys.argv[1] if len(sys.argv) > 1 else "info"
message = ' '.join(sys.argv[2:]) or "Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',
                        exchange_type='direct')

channel.basic_publish(exchange='direct_logs',
                        routing_key=sev,
                        body=message)
print(" [x] Sent %r:%r" % (sev,message))
connection.close()

