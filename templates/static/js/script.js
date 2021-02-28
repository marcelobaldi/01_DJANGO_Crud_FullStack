function catchForm(){

    var name  = document.getElementById('name').value;
    var age   = document.getElementById('age').value;
    var email = document.getElementById('email').value;
    var passw = document.getElementById('passw').value;

    var msg = "Por Favor, Preencha:" + "\n";

    if (name  == "") { msg = msg + "- Nome"  + "\n"; }
    if (age == "")   { msg = msg + "- Idade" + "\n"; }
    if (email == "") { msg = msg + "- Email" + "\n"; }
    if (passw == "") { msg = msg + "- Senha" + "\n"; }

    if (msg != "Por Favor, Preencha:" + "\n") {
        alert(msg);
        return false;
    }

}


