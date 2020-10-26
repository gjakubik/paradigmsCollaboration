// JavaScript code for Daily 14
console.log('entered main.js');

var sendButton = document.getElementById('send-button');
sendButton.onmouseup = getFormInfo;

function getFormInfo(){
    console.log('entered getFormInfo');
    var index = '/movies/'
    var baseUrl = document.getElementById('select-server-address').value;
    var port = document.getElementById('input-port-number').value;
    var type = document.querySelector('input[name="bsr-radios"]:checked').value;
    var key = document.getElementById('input-key').value;
    var message = document.getElementById('text-message-body').value;
    console.log('URL:' + baseUrl);
    console.log('Port: ' + port);
    console.log('Request type: ' + type);
    console.log('Key: ' + key);
    console.log('Message: ' + message);

    var usekey = false;
    var usemessage = false;
    if (document.getElementById('checkbox-use-key').checked){
        usekey = true;
    }
    if (document.getElementById('checkbox-use-message').checked){
        usemessage = true;
    }
    console.log('Use key: ' + usekey)
    console.log('Use message: ' + usemessage)

    var uri = baseUrl + ':' + port + index;
    if(usekey){
        uri += key;
    }

    makeRequestToServer(uri, type, message, usemessage);
}

function makeRequestToServer(uri, type, message, usemessage){
    console.log('entered makeRequestToServer');
    console.log('Uri: ' + uri);

    // create new request
    var xhr = new XMLHttpRequest();
    

    xhr.open(type, uri, true);

    xhr.onload = function(e){
        console.log(xhr.responseText);
        // update location with response
        displayResponse(xhr.responseText);
    }
    // decide wether to send with body or not
    if(usemessage){
        xhr.send(message);
    }
    else{
        xhr.send(null);
    }
    
}

function displayResponse(response_text){
    console.log('Response: ' + response_text);
    var answerLabel = document.getElementById('answer-label');
    answerLabel.innerHTML = response_text;
}
