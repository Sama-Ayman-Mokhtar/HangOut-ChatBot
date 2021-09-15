
const messages = document.querySelector('.messages');
const form = document.querySelector('form');
const input = document.querySelector('input');

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
    location.href = '#edge';
}


