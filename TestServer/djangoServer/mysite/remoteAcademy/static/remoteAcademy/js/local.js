
var http = require('http');
var fs = require('fs');

function post() {
    var token = document.getElementById('tokenvalue');
    console.log(token);
    var options = {
      hostname: '127.0.0.1',
      port: 8888,
      path: '/api/contents/color_filter.ipynb',
      method: 'PUT',
      headers: {
          'Content-Type': 'application/json',
          //'X-CSRFToken':cookies['_xsrf'],
          'Authorization': 'token ' + token,
      }
    };
    var req = http.request(options, function(res) {
      // logging response
      console.log('Status: ' + res.statusCode);
      console.log('Headers: ' + JSON.stringify(res.headers));
      res.setEncoding('utf8');
      res.on('data', function (body) {
        console.log('Body: ' + body);
      });
    });

    req.on('error', function(e) {
      console.log('problem with request: ' + e.message);
    });

    // write data to request body
    //req.write('{"copy_from": "color_filter.ipynb"}');
    req.write(' {"type": "notebook","format": "json","content": ' + nbcontent + '} ');
    req.end();
}

var nbcontent = fs.readFileSync(__dirname + '/color_filter.ipynb','utf8');
