import pika


if __name__ == "__main__":   
    publish(rabbitConnect)

def rabbitConnect(message: str):
    
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    createChannel = connection.channel()
    
    channel.createQueue(queue = "")
    channel.publishQueue(exchange="", routing="", body=message)
    print("sent request: {message}")
    
    connection.close()
    
    
    