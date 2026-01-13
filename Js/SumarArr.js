function sumArr (arr){
    let suma = 0;
    for (let i = 0 ; i < arr.length; i++){
        suma += arr[i];
    }
    return suma;
}

console.log(sumArr([1,5,8]));