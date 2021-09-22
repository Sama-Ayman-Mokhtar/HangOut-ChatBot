
const messages = document.querySelector('.messages');
const form = document.querySelector('form');
const input = document.querySelector('input');
var isLoggedin = false;

form.addEventListener('submit',
(e) =>{
    e.preventDefault();
    userDisplayReply(input.value);
    input.value = '';

});
function userDisplayReply(message){
    messages.innerHTML += `<div class="self">${message}</div>`
    location.href = '#edge';
    $.ajax({
        data: {
            mess: message
        },
        type : "POST",
        url : '/email_process'
    })
    .done(function(data){
        if(data.reply){
            botDisplayReply(data.reply);
        }
        else{
            botDisplayReply("failed to get reply");
        }
    });
}
function botDisplayReply(message){
    messages.innerHTML += `<div class="bot">${message}</div>`;
    //console.log(typeof message)
    //console.log(message.length)
    //console.log(typeof "you are logged in")
    //console.log("you are logged in".length)
    //console.log(message.includes("you are logged in"))
    if(message.includes("you are logged in")){
        isLoggedin = true;
        console.log("here")
    }
    if(isLoggedin){
        //https://stackoverflow.com/questions/19353331/getting-or-changing-css-class-property-with-javascript-using-dom-style
        messLen = document.getElementsByClassName('bot').length
        document.getElementsByClassName('bot')[messLen-1].style.background = 'lightsalmon';
    }
    location.href = '#edge';
}


