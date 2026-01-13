function busquedaLineal (arr, objetivo){
    for (let num of arr){
        if (num === objetivo){
            return 'el numero obejtivo: ' +num +' se encuentra en la posicion: ' + arr.indexOf(num);
        }
    }
    return 'el numero no se encuentra en el array';
}



function busquedaLinealFor (arr, objetivo){
    for (let i = 0 ; i<arr.length; i++){
        if (arr[i] === objetivo){
            return 'el numero objetivo: ' +arr[i] +' se encuentra en la posicion: ' + i;
        }
    }
    return 'el numero no se encuentra en el array';
}

console.log(busquedaLinealFor([25,45,768,21,65,87,32,87,21,9,], 87));