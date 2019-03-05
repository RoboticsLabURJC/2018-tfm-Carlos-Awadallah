

function hasGetUserMedia() {
  return !!(navigator.getUserMedia || navigator.webkitGetUserMedia ||
            navigator.mozGetUserMedia || navigator.msGetUserMedia);
}

var errorCallback = function(e) {
    console.log('Rejected!', e);
    errorElement = document.getElementById('error');
    error.display = 'block';
};

function saveNotebook() {
    console.log("click on iframe");
}

var myConfObj = {
    iframeMouseOver : false
}

/*function checkFocus() {
  if(document.activeElement == document.getElementById("ifr")) {
  	saveNotebook();
  	//document.activeElement.blur();
  }
}*/

function init() {

    // Normalize the various vendor prefixed versions of getUserMedia.
    navigator.getUserMedia = (navigator.getUserMedia ||
                            navigator.webkitGetUserMedia ||
                            navigator.mozGetUserMedia || 
                            navigator.msGetUserMedia);

    if (!hasGetUserMedia()) {
        alert('getUserMedia() is not supported in your browser');
    } else {
        videoElement = document.createElement('video');
        navigator.getUserMedia({video: true, audio: false}, function(localMediaStream) {
            videoElement.srcObject = localMediaStream;
            videoElement.muted = true;
            videoElement.play();
            document.getElementById("videodiv").appendChild(videoElement);  
        }, errorCallback);
    }

    window.addEventListener('blur',function(){
      if(myConfObj.iframeMouseOver){
        saveNotebook();
      }
    });

    document.getElementById('nb').addEventListener('mouseover',function(){
       myConfObj.iframeMouseOver = true;
    });
    document.getElementById('nb').addEventListener('mouseout',function(){
        myConfObj.iframeMouseOver = false;
    })

    //clickIframe = window.setInterval(checkFocus, 500);

}
