for (let i = 0 ; i<=100;i++){
    let output = '';
    
    if(i%3 == 0) output +='Fizz';
    if(i % 5 == 0) output += 'Buzz';
    if (i % 7 == 0) output += 'Bazz';

    console.log(output || i+ ' no es multiplo de 3 ni 5 ni 7');
}