

const amqp = require("ampqlib/callback_api");
const { channel } = require("diagnostics_channel");

amqp.connect("amqp://localhost",(connectionError0, connection) => {

   if(connectionError0)  {
     return(connectionError0);
 }
   
 
      connection.createChannel((connectionError1, channel) => {
             
        if(connectionError1)  {
            throw connectionError1;
         }
           
           var exchange = " ";  //exchange name of type "fanout"
           var message = " ";   


           channel.assertExchange(exchange, "fanout", {
               durable: true
           });

           channel.publish(exchange, '',Buffer.from(message));
           console.log("request traffic:", message);
   

        connection.close();
    
    });
});



