function tdclick(elem,row,col){ 
    console.log('td clicked');
    console.log(elem)
    console.log(row)
    console.log(col)
    console.log(elem.style.background)
    if (elem.style.background != 'lightsalmon')
        elem.style.background = 'lightsalmon';
    else
        elem.style.background = 'lightskyblue';

    // console.log(document.getElementsByClassName('cell').length);
    // var len = document.getElementsByClassName('cell').length;
    // var str = ""
    // console.log(len)
    // for (let index = 0; index < len; index++) {
    //     if(document.getElementsByClassName('cell')[index].style.background == 'lightsalmon' ){
    //         str += " " + index
    //     }  
    // }
    // console.log(str)


};  

function saveTodb(elem,row,col){ 
    
    console.log(document.getElementsByClassName('cell').length);
    var len = document.getElementsByClassName('cell').length;
    var str = ""
    //console.log(len)
    for (let index = 0; index < len; index++) {
        if(document.getElementsByClassName('cell')[index].style.background == 'lightsalmon' ){
            str += " " + index
        }  
    }
    //console.log(str)
    $.ajax({
        data: {
            mess: str
        },
        type : "POST",
        url : '/dataBase'
    })
    .done(function(data){
        history.back();
        if(data.reply){
            botDisplayReply("saved data");
        }
        else{
            botDisplayReply("failed to get reply");
        }
    });   
};  