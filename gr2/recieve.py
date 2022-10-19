import pika,sys,os
import socket


HOST = 'localhost'
PORT = 64000

def main():
    #Establish connection with RabbitMQ server in case it doesen't already exist.
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='winner')

    #Get data from game server
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        send_to_socket(body)

    channel.basic_consume(queue='winner',
                      auto_ack=True,
                      on_message_callback=callback)

    print('********************RABBITMQ SERVER STARTED******************')
    channel.start_consuming()

    

    


def send_to_socket(data):
    
    try:
        #Send queue data to socket server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(data)
            data = sock.recv(512)
    except:
        print("Error")




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)






