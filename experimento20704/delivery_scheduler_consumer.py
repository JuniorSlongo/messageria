import pika
import json

def callback(ch, method, properties, body):
    order = json.loads(body)
    print(f"Pedido pronto para entrega: {order}")
    # Comunicação com o sistema de envio/logística
    # ...
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='delivery_queue')
channel.basic_consume(queue='delivery_queue', on_message_callback=callback, auto_ack=False)
channel.start_consuming()
