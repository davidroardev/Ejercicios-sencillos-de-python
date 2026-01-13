function contarvocales(texto){
    let vocales = 'aeiouAEIOU';
    let contador = 0;

    for(let char of texto){
        if(vocales.includes(char)){
            contador++;
        }
    }
    return contador;
}

console.log(contarvocales('El pepe junto con el tilin bailan para salvarr la grasa'));