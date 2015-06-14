var arDrone = require('ar-drone');
var client  = arDrone.createClient();

client.animateLeds('blinkRed', 5, 2);
