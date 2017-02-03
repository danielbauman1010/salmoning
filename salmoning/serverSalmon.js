var express = require('express')
var bodyParser = require('body-parser')
var app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));
app.listen(3000)
app.get('/',function(request,response) {
  response.end('I\'m up');
});
app.post('/fished', function(request, response){
  var json = request.body
  console.log(request.body);      // your JSON
  response.send(request.body);    // echo the result back
});
