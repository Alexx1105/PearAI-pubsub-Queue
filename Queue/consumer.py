
##consumer file 
import pika
import pika.connection 

                  

def callback(ch, method, properties, body):  
       print(f" [] request: '{body.decode()}'")                                                   

def consooooomMessage():
     connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
     channel = connection.channel()
     
     channel.queue_declare(queue="RequestQueue")
     channel.basic_consume(queue="RequestQueue", messageCallback = callback, auto_ack=True)    ##consume messages
     
     print("[] messages:")
     channel.consooooomMessage()
     
     
     if __name__ == "__main__":
        consooooomMessage()