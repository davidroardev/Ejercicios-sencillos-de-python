function palabraMasLarga (texto){
    let palabrasTexto = texto.split(' ');
    let palabraMasLarga ='';

    for (let palabras of palabrasTexto){
        if (palabras.length > palabraMasLarga.length){
            palabraMasLarga = palabras;
        }
    }
    return 'la palabra mas larga es: '+palabraMasLarga;
}

console.log(palabraMasLarga('Hola como estas'));

