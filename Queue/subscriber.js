const amqp = require("ampqlib/callback_api");
const { error } = require("console");
const { channel } = require("diagnostics_channel");
const { connect } = require("http2");

amqp.connect("amqp://localhost", (connectionError2, connection) => {
  if(connectionError2) {
      return(connectionError2);
  }

   connection.createChannel((connectionError2, channel) => {
    if(connectionError2) {
        return(connectionError2)
    }
      
       var exchangeType = '';

       channel.assertExchange(exchangeType, 'fanout', {
         durable: false
        
       });

       channel.assertQueue(" ", {
        exclusive: false
       }, (error, q) => {

        if(error) {
            return(error)
        }
     
         console.log("requests:",q.makeQueue); 
    
         channel.bindQueue(q.exchangeType, '');
       
           channel.consume(q.queue, (message) => {
            if(message.content) {
                console.log("requests:", message.connect.toString());
            }
               noAck: true 
           });
        });
    
    });

});