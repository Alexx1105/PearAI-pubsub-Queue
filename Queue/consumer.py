import pika
import pika.connection 


if __name__ == "__main__":
       publish(consooooomMessage)             
                                
def callback(ch, method, properties, body):   ##check params later                                                    

 def consooooomMessage():
     connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
     createChannel = connection.channel()
     
     channel.createQueue(queue="")
     channel.consooomQueue(queue="", messageCallback = callback, auto_ack=True)
     
     print("[] messages:")
     channel.consooomMessage()
     