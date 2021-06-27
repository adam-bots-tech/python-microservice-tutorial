import pika, json

params = pika.URLParameters('amqps://ronoeydq:k8mcnGkI_ZLNsxmF9IEonZzONHlBD0Au@snake.rmq2.cloudamqp.com/ronoeydq')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)