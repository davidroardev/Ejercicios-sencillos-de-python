function esPalindromo (texto){
    let textoLimpio = texto.replace(/\s+/g, '').toLowerCase();
    let totalIndice = textoLimpio.length - 1;
    let textoInvertido = '';
    
    for(let i = totalIndice; i>=0;i--){
        textoInvertido += textoLimpio[i];
    }

    let esPalindromo = (textoInvertido === textoLimpio) ? 'Es un palindromo' : 'No es un palindromo';
    
    return esPalindromo;
}



function palindromo2 (texto){
    let textoLimpio = texto.replace(/\s+/g,'').toLowerCase();
    let indiceTexto = textoLimpio.length -1;
    let textoInvertido = '';

    for (let i = indiceTexto; i>=0; i--){
        textoInvertido += textoLimpio[i];
    }

    return (textoInvertido === textoLimpio) ? texto + ' Es palindromo' : texto + ' No es Palindromo';
}

console.log(palindromo2('olo'));