import pika



def rabbitConnect(message: str):
    
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    
    channel.queue_declare(queue = "RequestQueue")
    channel.basic_publish(exchange="", routing_key="RequestQueue", body=message)
    print(f"sent request: {message}")
    
    connection.close()
    
    
if __name__ == "__main__":   
  message = "messages"
rabbitConnect(message)
