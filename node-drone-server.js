var arDrone = require('ar-drone');
var client  = arDrone.createClient();
var express = require('express');
var app = express();

console.log("I think I am ready...");

// routes
app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.get('/liftoff', function(req, res){
  console.log("Recieved liftoff command");
  client.takeoff();
  
  client
    .after(5000, function() {
      this.clockwise(0.5);
    })
    .after(3000, function() {
      this.stop();
      this.land();
    });
  res.send("LIFTING!");
});

var server = app.listen(8866, '192.168.3.112', function () {

  var host = '192.168.3.112';
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);

});

