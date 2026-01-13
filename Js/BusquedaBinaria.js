function busquedaBinariaMejor(arr, objetivo){
    let izquierda = 0;
    let derecha = arr.length -1;
    let mitad;

    while (izquierda <= derecha){
        
        mitad = Math.floor((izquierda+derecha)/2);
        
        if (arr[mitad] === objetivo) return 'El numero onbjetivo '+arr[mitad]+'se encuentra en la pocision '+mitad;

        if (objetivo > arr[mitad]){
            izquierda = mitad +1; 
        }
        else{
            derecha = mitad -1;
        }
    }

    return 'no se encontro el numero'
}

console.log(busquedaBinariaMejor([3,45,56,59,60,67,72,74,78,86,89,94,96],100));