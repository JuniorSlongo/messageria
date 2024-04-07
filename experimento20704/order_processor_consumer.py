import pika
import json

def callback(ch, method, properties, body):
    order = json.loads(body)
    print(f"Pedido recebido: {order}")
    # Processamento do pedido e registro no banco de dados
    # ...
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='order_queue')
channel.basic_consume(queue='order_queue', on_message_callback=callback, auto_ack=False)
channel.start_consuming()
