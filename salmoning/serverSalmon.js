var express = require('express')
var bodyParser = require('body-parser')
var app = express()
var fs = require('fs')
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({     
  extended: true
}));
app.listen(3000)
app.get('/',function(request,response) {
  response.end('I\'m up');
});
var content="";
app.post('/fished', function(request, response){
  fs.readFile('log', function read(err, data) {
      if (err) {
          throw err;
      }
      content = data;
  });
  content=content+"\n"+JSON.stringify(request.body)
  processFile();
  console.log(request.body);
  response.send(request.body);
});
function processFile() {
  fs.writeFile("log", content, function(err) {
    if(err) {
        return console.log(err);
    }
  });
}
