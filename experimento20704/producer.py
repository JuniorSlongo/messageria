import pika
import json

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criação da fila de pedidos
channel.queue_declare(queue='order_queue')

# Simulação de envio de pedido
order = {'id': 123, 'produto': 'Livro de Python', 'quantidade': 1}
channel.basic_publish(exchange='',
                      routing_key='order_queue',
                      body=json.dumps(order))
print("Pedido enviado: %r" % order)

# Fechamento da conexão
connection.close()
