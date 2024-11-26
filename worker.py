#!/usr/bin/env python3

import pika,sys,os,time
from datetime import datetime

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue',
                        durable=True)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        start_time = time.time()
        print(f'Time start: {start_time}')
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        print(f'Time elapsed: {time.time()-start_time}')
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_qos(prefetch_count=1)                      
    channel.basic_consume(queue='task_queue',
                        on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


