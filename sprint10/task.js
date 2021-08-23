// TASK 1


function modifyArray(array) {
  array[0] = 'Start'
  array[array.length - 1] = 'End'
  return array
}


// TASK 2


function combineArray(arr1, arr2) {
    // arr1 = arr1.filter(function(v){return v === +v});
    // arr2 = arr2.filter(function(v){return v === +v});
    // return arr1.concat(arr2);
    // const answer = [arr1, arr2].reduce(function(a, b) {
    //     return a.concat(b);
    // });
    // return answer

    arr1 = arr1.filter(item => typeof item === 'number');
    arr2 = arr2.filter(item => typeof item === 'number');
    const arr = arr1.concat(arr2);
    return arr;
}


// TASK 3


function longestLogin(loginList) {
    const longest = loginList.reduce(
    function (first_el, second_el) {
        return first_el.length > second_el.length ? first_el : second_el;
    }
);
    return longest;
}


// TASK 4


function factorial(n) {
    return (n === 0) ? 1 : n * factorial(n-1);
}

function processArray(arr, factorial) {
    return arr.map(factorial);
}


// TASK 5


function checkAdult(age){
    const complete = 'Age verification complete';
    if (!age) {
        let answer = 'Error Please, enter your age';
        console.log(answer);
    } else if (Math.sign(age) < 0) {
        let answer = 'Error Please, enter positive number';
        console.log(answer);
    } else if (typeof age != 'number') {
        let answer = 'Error Please, enter number';
        console.log(answer);
    } else if (Number(age) === age && age % 1 !== 0) {
        let answer = 'Error Please, enter Integer number';
        console.log(answer);
    } else if (age < 18) {
        let answer = 'Error Access denied - you are too young!';
        console.log(answer);
    } else if (age >= 18) {
        let answer = 'Access allowed';
        console.log(answer);
    }
    console.log(complete);
}
