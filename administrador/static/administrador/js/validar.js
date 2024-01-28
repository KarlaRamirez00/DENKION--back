function caracterLogin() {
    event.preventDefault();
    var id_correo = document.getElementById("inputEmail1").value;
    var id_pass = document.getElementById("inputContra1").value;

    var resultado_correo = /^(?=.*[@]).*\.(com|cl)$/i;

    var resultado_final_correo = false;
    var resultado_final_pass = false;

    var pass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
    
    if(!id_correo.match(resultado_correo)) {
        alert("No ha ingresado correctamente su correo")
        resultado_final_correo = false;
    }else{
        resultado_final_correo = true;
    }

    if (id_pass.match(pass)) {
        resultado_final_pass = true;
    }

    if (resultado_final_correo && resultado_final_pass) {
        alert('Login exitoso.');
        document.getElementById("valido").innerHTML = "Válido";
        return true;
    } else {
        alert('Login incorrecto.');
        document.getElementById("valido").innerHTML = "Inválido";
        return false;
    }
}

function caracter_registrar() {
    event.preventDefault();

    // Variables de los input
    var inputNombre = document.getElementById("inputName1").value;
    var inputApellido = document.getElementById("inputLastName1").value;
    var inputRut = document.getElementById("inputRut1").value;
    var inputDv = document.getElementById("inputDv1").value;
    var inputDire = document.getElementById("inputDireccion1").value;
    var inputCiudad = document.getElementById("inputCiudad1").value;
    var inputRegion = document.getElementById("inputRegion1").value;
    var inputEmail = document.getElementById("inputEmail2").value;
    var inputTel = document.getElementById("inputTelefono1").value;
    var inputCon = document.getElementById("inputPassword1").value;
    var inpuCond = document.getElementById("inputPassword2").value;

    // Variables de validación
    var resultado_rut = false;
    var resultado_dv1 = /^(?=.*\d|[kK]).{1}$/;     // variables de formato siempre comienza con /^  y termna con $/
    var resultado_final_dv = false;
    var resultado_correo = /^(?=.*[@]).*\.(com|cl)$/i;  // .*\. indica que al final debe terminar en .cl o .com, i esta letra i indica que se apecta minuscula y Mayuscula.
    var resultado_final_correo = false;
    var resultado_tel = /^.{8}$/;
    var resultado_final_tel = false;
    var resultado_pass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/; // \d que tenga al menos un dígito, [^a-zA-Z0-9] que tenga un caracter especial, es decir que sea diferente a lo que se espicifica dentro de los corchetes [], \s que no tenga un espacio vacío, .{8,15} indica que debe tener mínim 8 caracteres, y máximo 15
    var resultado_final_pass = false;

    // Validaciones con for
    var todasLasCondicionesCumplidas = true;
    var condiciones = [
        [inputNombre == '', "El nombre no puede estar vacío"],
        [inputApellido == '', "El apellido no puede estar vacío"],
        [isNaN(inputRut), "Solo deben ingresarse números"],
        [!inputDv.match(resultado_dv1), "Ingrese sólo un número o una letra 'k'"],
        [inputDire == '', "La dirección no puede estar vacía"],
        [inputCiudad == '', "La ciudad no puede estar vacía"],
        [inputRegion == 'Seleccione...', "Debe seleccionar una de las opciones"],
        [!inputEmail.match(resultado_correo), "No ha ingresado correctamente su correo"],
        [!inputTel.match(resultado_tel), "Ingrese el número sin el +569"],
        [(inputCon == '' || inpuCond == ''), "Las contraseñas no pueden estar vacías"],
        [!inputCon.match(resultado_pass), "Las contraseñas deben cumplir con los requisitos de seguridad"]
    ];

    for (var i = 0; i < condiciones.length; i++) {
        if (condiciones[i][0]) {
            alert(condiciones[i][1]);
            todasLasCondicionesCumplidas = false;
            break;
        }
    }

    // Alert Resultado Final
    if (todasLasCondicionesCumplidas) {
        alert('Registro exitoso.');
        document.getElementById("validado").submit();
    } else {
        alert('Registro incorrecto.');
    }
}

function caracter_contacto(){
    event.preventDefault();
    //variables de los input
    var inputNombre = document.getElementById("inputNombre1").value;
    var inputEmail = document.getElementById("inputCorreo1").value;
    var inputTel = document.getElementById("inputTel1").value;
    var inputTipoCon = document.getElementById("inputCon").value;
    var inputConsu  = document.getElementById("inputArea1").value;

    //variables Validación
    var resultado_correo = /^(?=.*[@]).*\.(com|cl)$/i;
    var resultado_final_correo = false;
    var resultado_tel = /^.{8}$/;
    var resultado_final_tel = false;

    //Desarrollo de los If
    if(inputNombre == ''){
        alert("El nombre no puede estar vacío")
    }

    if(!inputEmail.match(resultado_correo)) {
        alert("No ha ingresado correctamente su correo")
        resultado_final_correo = false;
    }else{
        resultado_final_correo = true;
    }

    if(!inputTel.match(resultado_tel)){
        alert("Ingrese el número sin el +569")
        resultado_final_tel = false;
    }else{
        resultado_final_tel = true;
    }

    if(inputTipoCon == 'Seleccione...'){
        alert("Debe seleccionar una de las opciones")
    }else if (inputConsu == ''){
        alert("La consulta no puee estar vacía")
    }else{
        document.getElementById("ContactoForm").submit();
    }
}