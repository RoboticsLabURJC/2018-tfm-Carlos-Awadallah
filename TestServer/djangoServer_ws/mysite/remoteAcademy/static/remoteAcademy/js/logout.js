
function del_code(ip,port,token,src) {
    // Eliminar un fichero
    src_del='http://'+ip+':'+port+'/api/contents/'+src
    const message = {
            headers:{
                     'Authorization': 'token ' + token,
                    },
            method:"DELETE"
    };
    fetch(src_del,message)
        .then(data=>{return data.json()})
        .then(res=>{console.log(res)})
        .catch(error=>console.log(error))
}

function deleteKernel() {
    var _ip = document.getElementById("jupyter").getAttribute("_ip");
    var _port = document.getElementById("jupyter").getAttribute("_port");
    var _token = document.getElementById("jupyter").getAttribute("_token");
    var _session = document.getElementById("jupyter").getAttribute("_session");
    // Eliminar Session y KernelL
    const src_session='http://'+_ip+':'+_port+'/api/sessions/'+_session
    const message = {
            headers:{
                     'Authorization': 'token ' + _token,
                    },
            method:"DELETE"
    };
    fetch(src_session,message)
        .then(data=>{return data.json()})
        .then(res=>{console.log(res)})
        .catch(error=>console.log(error))

    code_files = ['color_filter.py','color_filter.ipynb', 'color_filter_conf.yml', 'color_filter.pyc']
    for (var f in code_files) {
        del_code(_ip,_port,_token,code_files[f]);
        console.log("DELETED "+code_files[f]);
    }
      
}

deleteKernel();
