
function upgrade2Ws() {

    // NO SE PUEDEN TOCAR ESAS CABECRAAAAAAAAAAAAAAAAAAAAAAS!! PROBAR A ENVIAR UN SOCKET DIRECTAMENTE
    var _ip = document.getElementById("jupyter").getAttribute("_ip");
    var _port = document.getElementById("jupyter").getAttribute("_port");
    var nbcontent = document.getElementById("jupyter").getAttribute("nbcontent");
    var _token = document.getElementById("jupyter").getAttribute("_token");

    const url = 'ws://'+_ip+':'+_port+'/http_over_websocket?min_version=0.0.1a3';

    var connection = new WebSocket(url);

    // When the connection is open, send some data to the server
    connection.onopen = function () {
      connection.send('Ping'); // Send the message 'Ping' to the server
    };

    // Log errors
    connection.onerror = function (error) {
      console.log('WebSocket Error ' + error);
    };

    // Log messages from the server
    connection.onmessage = function (e) {
      console.log('Server: ' + e.data);
    };
}

function postNotebook() {
    
    var _ip = document.getElementById("jupyter").getAttribute("_ip");
    var _port = document.getElementById("jupyter").getAttribute("_port");
    var nbcontent = document.getElementById("jupyter").getAttribute("nbcontent");
    var _token = document.getElementById("jupyter").getAttribute("_token");

    const url = 'http://'+_ip+':'+_port+'/api/contents/color_filter.ipynb';
    const data_put = ' {"type": "notebook","format": "json","content": ' + nbcontent + '} ';
    const message = {
            headers:{'Content-Type':'application/json',
                     'Authorization': 'token ' + _token,
                    },
            body:data_put,
            method:"PUT"
    };
    fetch(url,message)
        .then(data=>{return data.json()})
        .then(res=>{console.log(res)})
        .catch(error=>console.log(error))

}

function sendCode() {

    var codefile = document.getElementById("jupyter").getAttribute("codefile");
    var configfile = document.getElementById("jupyter").getAttribute("configfile");
    var _ip = document.getElementById("jupyter").getAttribute("_ip");
    var _port = document.getElementById("jupyter").getAttribute("_port");
    var _token = document.getElementById("jupyter").getAttribute("_token");

    var files = [['color_filter.py',codefile], ['color_filter_conf.yml',configfile]];

    for (var f in files) {
        var src = files[f][0];
        url = 'http://'+_ip+':'+_port+'/api/contents/'+src
        data_put = ' {"type": "file","format": "text","content": ' + files[f][1] + '} '
        const message = {
                headers:{'Content-Type':'application/json',
                         'Authorization': 'token ' + _token,
                        },
                body:data_put,
                method:"PUT"
        };
        fetch(url,message)
            .then(data=>{return data.json()})
            .then(res=>{console.log(res)})
            .catch(error=>console.log(error))

    }

}

upgrade2Ws();
console.log("upgrades to wensockets");
postNotebook();
console.log("NOTEBOOK COPIED");
sendCode();
console.log("CODE FILES SENT");
