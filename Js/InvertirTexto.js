function invertirTexto(texto){
    let textoInvertido = '';
    for(let letra of texto){
        textoInvertido = letra + textoInvertido; // textoInvertido = textoInvertido + letra;
    }
    return textoInvertido;
}

console.log(invertirTexto('Hola Mundo'));