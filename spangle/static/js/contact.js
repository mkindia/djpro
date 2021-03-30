
function sayHi() {
    var enq='------ Contact Details ------' + '<br/>'            
    + 'Full Name : ' + document.getElementById("fname").value + '<br/>' 
    + '   E-mail : ' + document.getElementById("email").value + '<br/>'
    + '    Phone : ' + document.getElementById("phone").value + '<br/>'
    + '     City : ' + document.getElementById("city").value + '<br/>'
    + '    State : ' + document.getElementById("state").value + '<br/>'
    + '      Zip : ' + document.getElementById("zip").value + '<br/>' + '<br/>' 
    + '      ------ Message ------' + '<br/>'
    + '  Message : ' + document.getElementById("message").value + '<br/>'

   
    Email.send({
        SecureToken: '196b57c0-c730-404c-9326-a53fe2ebc1e0',
        To: 'info@spangle.in',
        From: 'mail@spangle.in',
        Subject: 'from site mail',
        Body: enq
    }).then(
        message => alert(message)
    );
    setTimeout(sayhello, 4000)

}
function sayhello() {

    window.location.reload()
}



