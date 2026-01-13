function ordenarBurbuja(arr){
    let indice = arr.length -1;

    for (let i = 0 ; i <= indice; i++){
        for (let j = 0 ; j <= indice -i;j++){
            if (arr[j] > arr[j+1]){
                let temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    return arr;
}

///console.log(ordenarBurbuja([7,100,68,82,1,5]));



function OrdenarBurbuja2(arr){
    for(let i = 0 ; i<arr.length;i++){
        for(let j = 0 ; j<arr.length - i ;j++){
            if(arr[j] > arr[j+1]){
                let temp = arr[j];
                arr[j]= arr[j+1];
                arr[j+1] = temp
            }
        }
    }
    return arr
}

console.log(OrdenarBurbuja2([66,77,21,98,132,654,68,156,35,17883,85]))