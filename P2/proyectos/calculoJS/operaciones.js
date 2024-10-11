function operacion() {
    // Obtener los valores ingresados
    const numero1 = parseFloat(document.getElementById('n1').value);
    const numero2 = parseFloat(document.getElementById('n2').value);
    const operacion = document.getElementById('tipo').value;
    let resultado; //se declara la variable

    // Verificar si los valores son válidos
    //el isNaN es una funcion que verifica si son numeros o no, mandando un boleano en caso de ser o no ser.
    if (isNaN(numero1) || isNaN(numero2)) {
        alert("Por favor ingresa números válidos.")
        // document.getElementById('tipo').innerHTML = "Por favor ingresa números válidos.";
        return;
    }
    
    // if (isNumber(n1) && isNumber(numero2))
    // {}
    // Realizar la operación
    //atravez de la seleccion en el html y el valor obtenido en la linea 5
    switch (operacion) {
        case "suma":
            resultado = numero1 + numero2;
            document.getElementById('resultado').innerHTML = `<h2> ${numero1} + ${numero2} = ${resultado}</h2>`;//este es para mostrarlo en la etiqueta con el id="resultado"
            break;
        case "resta":
            resultado = numero1 - numero2;
            document.getElementById('resultado').innerHTML = `<h2> ${numero1} - ${numero2} = ${resultado}</h2>`;
            break;
        case "multiplicar":
            resultado = numero1 * numero2;
            document.getElementById('resultado').innerHTML = `<h2> ${numero1} * ${numero2} = ${resultado}</h2>`;
            break;
        case "dividir":
            if (numero2 !== 0) {
                resultado = numero1 / numero2;
                document.getElementById('resultado').innerHTML = `<h2> ${numero1} / ${numero2} = ${resultado}</h2>`;
            } else {
                resultado = "No se puede dividir entre 0";
            }
            break;
        default:
            resultado = "Operación no válida";
            break;
    }

    // Mostrar el resultado en el div
    // document.getElementById('resultado').innerHTML = `<h2>resultado: ${resultado}</h2>`;

    // function isNumber(n)
    // {
    //     return !isNaN(parseInt(n) && isFinite(n))
    // }
}


