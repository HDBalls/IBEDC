
// function connectToEventServer(){

//     var socket = io.connect('http://' + 'localhost' + ':' + '8000');
//     socket.on('connect', function() {
//             console.log('connected to event server');
//     });
//     socket.on('message', function(data) {
//             console.log(data);
//     });

// }

function connectToEventServer() {
            
    if ("WebSocket" in window) {
       console.log("WebSocket is supported by your Browser!");
       
       // Let us open a web socket
       var ws = new WebSocket("ws://localhost:8000");

       ws.onmessage = function (evt) { 
          var received_msg = evt.data;
          console.log("Message is received..."+received_msg);
       };
        
       ws.onclose = function() { 
          
          // websocket is closed.
          console.log("Connection is closed..."); 
       };
    } else {
      
       // The browser doesn't support WebSocket
       console.log("WebSocket NOT supported by your Browser!");
    }
 }