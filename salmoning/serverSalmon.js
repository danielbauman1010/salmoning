var express = require('express')
var bodyParser = require('body-parser')
var app = express()
var fs = require('fs')
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
  extended: true
}));
var log = {};

var content="";
app.listen(3000)
app.get('/',function(request,response) {
  var neatResponse=""
  for(user in log){
    neatResponse= neatResponse + "\n"+user+":\n"+log[user]
  }
  response.end(neatResponse);
});
currentContent="";
app.post('/fished', function(request, response){
  fs.readFile('log', function read(err, data) {
      if (err) {
          throw err;
      }
      content = data;
  });
  currentContent = JSON.stringify(request.body)
  content=content+"\n"+ currentContent
  processFile(request.body);
  console.log(request.body);
  response.send(request.body);
});
function processFile(req) {
  fs.writeFile("log", content, function(err) {
    if(err) {
        return console.log(err);
    }
  });
  for(u in req) {
    if(u in log) {
      log[u] = log[u] + req[u]
    } else {
      log[u]=req[u]
    }
  }
}
